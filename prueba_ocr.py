from services.ocr_service import pdf_to_text
import os

# buscar pdf en tmp (subido)
files_in_tmp = os.listdir("tmp")

if files_in_tmp:
    # Cogemos el primero
    filename = files_in_tmp[0]
    path = os.path.join("tmp", filename)
    
    print(f"--- PROBANDO OCR CON: {filename} ---")
    
    # llamamos al metodo
    texto_extraido = pdf_to_text(path)
    
    print("\n" + "="*30)
    print("RESULTADO DEL ANÁLISIS")
    print("="*30)
    # Imprimimos solo los primeros 1000 c de prueba
    print(texto_extraido[:1000]) 
    print("\n... (texto cortado para visualizar)")

else:
    print("No hay archivos en la carpeta 'tmp'. Por favor sube uno o copia un PDF ahí.")