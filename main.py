from fastapi import FastAPI, File, UploadFile
import shutil
import os
from uuid import uuid4

app = FastAPI()

#Comprobar que la API esta viva
@app.get("/health")
def health_check():
    return {"status": "ok", "message": "Backend MYB funcionando correctamente"}

#---------
#Endpoint para subir la nómina
#---------

"""@app.post("/upload")
async def upload_nomina(file: UploadFile = File(...)):
    #1. Comprobar extensión permitida
    ext_ok = ["png", "jpg", "jpeg", "pdf"]
    ext = file.filename.split(".")[-1].lower()

    if ext not in ext_ok:
        return{"error": "Formato incorrecto, por favor introduzca un archivo PNG, JPG, JPEG o PDF."}
    
    #2. Guardar temp
    temp_filename = f"{uuid4}.{ext}" #genera nombre aleatorio seguro
    temp_path = os.path.join("tmp", temp_filename)

    os.makedirs("tmp", exist_ok=True) #crea carpeta tmp si no existe

    with open(temp_path, "wb") as buffer:
        shutil.copyfileobj(file.file,buffer)

    #3. Por ahora, solo confirmamos subida
    #Mas tarde se pondrá aqui el ocr y todo el rollo

    return {
        "message" : "Archivo subido correctamente",
        "filename" : temp_filename,
        "temp_path" : temp_path
    }"""