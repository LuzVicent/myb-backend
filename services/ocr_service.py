import fitz #para abrir pdfs -> pymupdf
import easyocr #ia para leer img
import os

#inicializar ocr solo una vez al principio. Si se hace dentro de la función, el servidor se congelaría cada vez que subo un doc
print("cargarndo ocr...")
reader = easyocr.Reader(['es'], gpu=False) #buscan en español

#leer pdf
def pdf_to_text(file_path):
    """
    Recibe la ruta de un archivo pdf
    Devuelve un string gigante con todo el txt que ha encontrado
    """

    full_text = ""

    try:
        #1.Abrir pdf con fitz
        doc = fitz.open(file_path)

        #2. paginador
        for num_pag, page in enumerate(doc):
            #Intentar leer texto digital
            text = page.get_text()

            if text.strip():
                #si encuentra texto real, lo usamos
                print(f"Página {num_pag + 1}: Texto og.")
                full_text += text + "\n"
            
            else:
                #si es img usar ia
                print(f"Página {num_pag + 1}: No hay texto digital. Usando OCR ...")

                # Convertimos la página del PDF en una imagen (png)
                pix = page.get_pixmap()
                img_bytes = pix.tobytes("png")
                
                # Le pasamos la imagen a la IA
                # detail=0 hace que solo nos devuelva el texto, sin coordenadas ni confianza
                result = reader.readtext(img_bytes, detail=0) 
                
                # Unimos las palabras que encontró la IA
                page_text = " ".join(result)
                full_text += page_text + "\n"
        doc.close()
        return full_text

    except Exception as e:
        print(f"Error procesando el PDF: {e}")
        return None