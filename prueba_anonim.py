from services.anonimizador import anonymize_text

# 1. Creamos un texto falso con datos "sensibles" para probar
texto_prueba = """
La trabajadora Luz Vicent con DNI 12345678Z vive en Valencia.
Su correo es luz.test@gmail.com y su teléfono 600123456.
La empresa paga en la cuenta ES1234567890123456789012.
El jefe se llama Juan Pérez.
"""

print("--- TEXTO ORIGINAL ---")
print(texto_prueba)

# 2. Pasamos el rotulador
texto_limpio = anonymize_text(texto_prueba)

print("\n" + "="*30)
print("--- TEXTO ANONIMIZADO ---")
print("="*30)
print(texto_limpio)