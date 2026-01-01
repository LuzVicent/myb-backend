from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from orm.models import PayrollAnalysis

"""
Configuración de MongoDB.
Usamos 'motor' como cliente asíncrono.
"""

# URL de conexión local por defecto de MongoDB
MONGO_URL = "mongodb://localhost:27017"
DB_NAME = "myb_database"

async def init_db():
    # 1. Crear el cliente de Motor (la conexión)
    client = AsyncIOMotorClient(MONGO_URL)
    
    # 2. Seleccionar la base de datos específica
    database = client[DB_NAME]
    
    # 3. Inicializar Beanie con los modelos que usaremos
    # Esto prepara a Beanie para traducir entre Python y Mongo
    await init_beanie(database=database, document_models=[PayrollAnalysis])
    
    print("--- Conexión a MongoDB Exitosa ---")