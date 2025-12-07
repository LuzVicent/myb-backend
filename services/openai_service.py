import time
import json

# No necesitamos API Key para el simulador
def analyze_payroll(text_anonymized):
    """
    SIMULADOR (MOCK):
    Finge que piensa y devuelve siempre un análisis fijo.
    Útil para desarrollar el Frontend sin gastar dinero.
    """
    
    print(f"--- [SIMULADOR] Recibido texto de {len(text_anonymized)} caracteres ---")
    print("--- [SIMULADOR] 'Pensando' (Simulando retraso de la IA)... ---")
    
    # Hacemos que el programa se espere 2 segundos para dar realismo 
    # (la IA real tarda un poco)
    time.sleep(2)
    
    # Creamos una respuesta falsa pero realista
    # Esto es lo que devolvería GPT-4 idealmente
    respuesta_falsa = {
        "resumen": "Esta nómina corresponde a un mes estándar. Se observa un salario base acorde al convenio, pero la retención de IRPF es ligeramente baja (2%), lo que podría implicar un pago mayor en la declaración de la renta anual.",
        "salario_bruto": 1850.50,
        "salario_neto": 1540.20,
        "impuestos": "Te han retenido un 6.35% de Seguridad Social y un 2% de IRPF. Es una retención baja para este rango salarial.",
        "consejos": [
            "Revisa si tu contrato es temporal, ya que el IRPF del 2% suele aplicarse ahí.",
            "Tienes un complemento de 'Plus Transporte' que no cotiza igual, ¡ojo!",
            "Estás cotizando por la base máxima de tu categoría."
        ]
    }
    
    print("--- [SIMULADOR] Análisis completado ---")
    
    return respuesta_falsa