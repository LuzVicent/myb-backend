import logging
import openai
import os
import json
import base64
from dotenv import load_dotenv
from services.prompts import PAYROLL_ANALYSIS_PROMPT, PAYROLL_VISION_PROMPT

logger = logging.getLogger(__name__)

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    logger.warning("No se encontró OPENAI_API_KEY en las variables de entorno.")

client = openai.OpenAI(api_key=api_key)

def analyze_payroll(text_anonymized):
    """Analiza texto extraído de un PDF usando GPT-4o-mini."""
    logger.info("Iniciando análisis de texto con OpenAI...")
    
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": PAYROLL_ANALYSIS_PROMPT},
                {"role": "user", "content": f"Analiza esto:\n\n{text_anonymized}"}
            ],
            response_format={"type": "json_object"},
            temperature=0.2
        )
        return json.loads(response.choices[0].message.content)
    except Exception as e:
        logger.error(f"Error OpenAI (Texto): {e}", exc_info=True)
        return _error_response()

def analyze_payroll_image(image_bytes):
    """Analiza una imagen de nómina usando GPT-4o Vision."""
    logger.info("Iniciando análisis de visión con OpenAI...")
    
    # Convertir imagen a Base64 para la API
    base64_image = base64.b64encode(image_bytes).decode('utf-8')

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": PAYROLL_VISION_PROMPT},
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": "Analiza esta imagen de nómina:"},
                        {
                            "type": "image_url",
                            "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"}
                        }
                    ]
                }
            ],
            response_format={"type": "json_object"},
            temperature=0.2
        )
        return json.loads(response.choices[0].message.content)

    except Exception as e:
        logger.error(f"Error OpenAI Vision: {e}", exc_info=True)
        return _error_response()

def _error_response():
    """Devuelve un JSON seguro en caso de fallo."""
    return {
        "resumen": "Error al procesar el documento.",
        "salario_bruto": 0,
        "salario_neto": 0,
        "consejos": ["Por favor, inténtalo de nuevo más tarde."]
    }