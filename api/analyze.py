from fastapi import APIRouter, UploadFile, File, HTTPException, Depends
from sqlmodel import Session
import shutil
import os

from services.ocr_service import extract_text 
from services.anonimizador import anonymize_text
# Importamos AMBAS funciones de análisis
from services.openai_service import analyze_payroll, analyze_payroll_image 
from orm.models import PayrollAnalysis


"""
Este archivo define el endpoint /analyze que recibe un archivo (PDF o Imagen),
procesa su contenido y devuelve el análisis en formato JSON.
Implementación de PERSISTENCIA DE DATOS.
Usamos INYECCIÓN DE DEPENDENCIAS (`Depends(get_session)`) para obtener
una sesión transaccional de base de datos.
Instanciamos el modelo `PayrollAnalysis` con los datos del DTO (Data Transfer Object)
y ejecutamos `session.add()` y `session.commit()` para confirmar la transacción ACID.
"""

router = APIRouter()
os.makedirs("tmp", exist_ok=True)

# ENDPOINT PRINCIPAL DE ANÁLISIS
@router.post("/analyze")
async def analyze_payroll_endpoint(file: UploadFile = File(...),):

    filename = file.filename.lower() 
    # 1. Guardar en disco temporalmente
    temp_filename = f"temp_{file.filename}"
    temp_path = os.path.join("tmp", temp_filename)
    
    result_json = {} # Variable para guardar el resultado antes de enviarlo
    try:
        with open(temp_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        
        # Leemos los bytes para procesar
        with open(temp_path, "rb") as f:
            file_content = f.read()

        # --- BIFURCACIÓN DEL CAMINO ---
        
        # CAMINO A: Es una IMAGEN (JPG/PNG) -> Usamos GPT-4 Vision
        if filename.endswith(('.jpg', '.jpeg', '.png')):
            print(f"Imagen detectada ({filename}). Usando GPT-4 Vision...")
            # Enviamos la imagen DIRECTA a OpenAI (sin pasar por EasyOCR local)
            result_json = analyze_payroll_image(file_content)
            

        # CAMINO B: Es un PDF -> Usamos el método clásico 
        elif filename.endswith('.pdf'):
            print(f"PDF detectado ({filename}). Usando OCR Local...")
            
            # 1. OCR Local
            text = extract_text(file_content, file.filename)
            if not text.strip():
                 raise HTTPException(status_code=400, detail="PDF vacío o ilegible.")
            
            # 2. Anonimizar texto
            clean_text = anonymize_text(text)
            
            # 3. Analizar texto
            result_json = analyze_payroll(clean_text)

        else:
             raise HTTPException(status_code=400, detail="Formato no soportado.")

        # --- PERSISTENCIA (GUARDAR EN DB) ---
        print("Guardando en MongoDB...")

        if not result_json: raise HTTPException(500, "Fallo análisis IA")
        
        # Preparar string de consejos
        consejos_lista = result_json.get("consejos", [])
        if not isinstance(consejos_lista, list): consejos_lista = []
        consejos_unidos = "|".join(consejos_lista)

        # 1. Crear el objeto (Documento)
        nuevo_analisis = PayrollAnalysis(
            filename=file.filename,
            resumen=result_json.get("resumen", "Sin resumen"),
            salario_bruto=result_json.get("salario_bruto", 0.0),
            salario_neto=result_json.get("salario_neto", 0.0),
            consejos=consejos_unidos
        )

        # 2. GUARDAR (Insertar en Mongo)
        # Usamos 'await' porque escribir en disco/red es lento
        await nuevo_analisis.insert() 
        
        print(f"Guardado en MongoDB con ID: {nuevo_analisis.id}")
        
        # Inyectamos el ID (convertido a string porque en Mongo el ID es un objeto especial)
        result_json["db_id"] = str(nuevo_analisis.id)
        
        return result_json

    except Exception as e:
        print(f"Error crítico: {e}")
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        if os.path.exists(temp_path): os.remove(temp_path)