import logging # <--- IMPORTAR LOGGING
import spacy
import re # Liberia regex

# Configurar el logger para este archivo
logger = logging.getLogger(__name__)

# 1. Cargamos el cerebro en español de spaCy
logger.info("--- Cargando modelo de anonimización (spaCy)... ---")
try:
    nlp = spacy.load("es_core_news_sm")
except Exception as e:
    logger.error(f"Error cargando spaCy (es_core_news_sm): {e}. Asegúrate de haber ejecutado 'python -m spacy download es_core_news_sm'")
    raise e

def anonymize_text(text):
    """
    Recibe: Texto en bruto (con nombres, DNI, etc.)
    Devuelve: Texto censurado con etiquetas como [DNI], [PERSONA].
    """
    
    # --- FASE 1: REGEX (Patrones fijos) ---
    # Definimos los moldes. "r" significa raw string (para que Python entienda los símbolos raros)
    
    # Molde para DNI/NIE (aprox: números + letra o letra + números + letra)
    pattern_dni = r'[0-9]{8}[A-Z]|[XYZ][0-9]{7}[A-Z]'
    
    # Molde para Emails
    pattern_email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    
    # Molde para Teléfonos (formato español básico)
    pattern_phone = r'\b(\+34|0034|34)?[ -]*(6|7|8|9)[ -]*([0-9][ -]*){8}\b'
    
    # Molde para IBAN (Cuentas bancarias españolas ES + 22 dígitos)
    pattern_iban = r'ES[0-9]{2}[ ]?[0-9]{4}[ ]?[0-9]{4}[ ]?[0-9]{2}[ ]?[0-9]{10}'
    
    # Seguridad Social (NAF): Aprox 12 dígitos
    pattern_naf = r'\b[0-9]{12}\b'

    # APLICAMOS EL ROTULADOR NEGRO (Sustitución)
    # re.sub(patrón, sustituto, texto)
    text = re.sub(pattern_dni, '[DNI]', text)
    text = re.sub(pattern_email, '[EMAIL]', text)
    text = re.sub(pattern_phone, '[TLF]', text)
    text = re.sub(pattern_iban, '[IBAN]', text)
    text = re.sub(pattern_naf, '[SS_NUM]', text)

    # --- FASE 2: INTELIGENCIA ARTIFICIAL (spaCy) ---
    # Usamos spaCy para encontrar nombres de personas y lugares
    
    doc = nlp(text)
    
    new_text = text
    
    # Recorremos las entidades que ha encontrado la IA
    # ent.label_ nos dice qué es: PER (Persona), LOC (Lugar), ORG (Organización)
    for ent in doc.ents:
        if ent.label_ == "PER":
            # Reemplazamos el nombre específico por [PERSONA]
            new_text = new_text.replace(ent.text, "[PERSONA]")
        elif ent.label_ == "LOC":
             new_text = new_text.replace(ent.text, "[UBICACION]")
             
    return new_text