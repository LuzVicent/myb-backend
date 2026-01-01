import logging # <--- IMPORTAR
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from orm.models import PayrollAnalysis

"""
Configuración de MongoDB.
Usamos 'motor' como cliente asíncrono.
"""

# Configurar logger
logger = logging.getLogger(__name__)

# URL de conexión local por defecto de MongoDB
# (Si usas Docker, recuerda que el puerto mapeado es localhost:27017)
MONGO_URL = "mongodb://localhost:27017"
DB_NAME = "myb_database"

async def init_db():
    try:
        logger.info("🔌 Iniciando conexión con motor MongoDB (Beanie)...")
        
        # 1. Crear el cliente de Motor (la conexión)
        client = AsyncIOMotorClient(MONGO_URL)
        
        # 2. Seleccionar la base de datos específica
        database = client[DB_NAME]
        
        # 3. Inicializar Beanie
        await init_beanie(database=database, document_models=[PayrollAnalysis])
        
        logger.info(f"✅ Conexión a MongoDB Exitosa. Base de datos: '{DB_NAME}'")
        
    except Exception as e:
        logger.critical(f"🔥 ERROR FATAL conectando a base de datos: {e}", exc_info=True)
        # Aquí relanzamos la excepción porque si no hay DB, la app no debe arrancar
        raise e