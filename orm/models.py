from typing import Optional,List
from beanie import Document 
from pydantic import Field
from datetime import datetime

"""
Modelo de Datos para MongoDB (usando Beanie).
MongoDB crea automáticamente un _id único para cada documento.
"""

class PayrollAnalysis(Document):
    # En MongoDB, no definimos "columnas", sino campos.
    # Beanie usa Pydantic para validar tipos.
    
    filename: str
    upload_date: datetime = Field(default_factory=datetime.now)
    
    # Datos extraídos
    resumen: Optional[str] = None
    salario_bruto: Optional[float] = None
    salario_neto: Optional[float] = None
    
    # En Mongo podríamos guardar la lista directamen, 
    # pero para mantener la lógica actual, seguiremos usando string por ahora.
    consejos: Optional[str] = None 

    class Settings:
        # Nombre de la colección (equivalente a nombre de tabla)
        name = "nominas"