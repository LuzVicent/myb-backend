from fastapi import APIRouter, UploadFile, File, HTTPException
import shutil
import os
from services.ocr_service import pdf_to_text
from services.anonimizador import anonymize_text
from services.openai_service import analyze_payroll # Importamos nuestro simulador

router = APIRouter()

@router.post("/analyze")
async def analyze_payroll_endpoint(file: UploadFile = File(...)):
    """
    Endpoint Maestro:
    1. Guarda el PDF.
    2. Lee el texto (OCR).
    3. Censura datos (Anonimización).
    4. Analiza (Simulador IA).
    5. Devuelve el resultado al usuario.
    """
    
    # 1. Guardar archivo temporalmente
    temp_filename = f"temp_{file.filename}"
    temp_path = os.path.join("tmp", temp_filename)
    
    try:
        with open(temp_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
            
        print(f"1. Archivo recibido: {temp_filename}")

        # 2. OCR (Leer)
        print("2. Procesando OCR...")
        text = pdf_to_text(temp_path)
        if not text:
            raise HTTPException(status_code=400, detail="No se pudo leer texto del PDF.")

        # 3. Anonimizar (Proteger)
        print("3. Anonimizando...")
        clean_text = anonymize_text(text)

        # 4. IA (Analizar - SIMULADO)
        print("4. Analizando con IA...")
        result_json = analyze_payroll(clean_text)
        
        # 5. Devolver resultado
        return result_json

    except Exception as e:
        print(f"Error crítico: {e}")
        raise HTTPException(status_code=500, detail=str(e))
        
    finally:
        # Limpieza: Borrar el archivo temporal para no llenar el disco
        if os.path.exists(temp_path):
            os.remove(temp_path)
            print("Limpieza: Archivo temporal eliminado.")