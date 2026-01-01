from fastapi import FastAPI
from contextlib import asynccontextmanager
#permisos para conexion
from fastapi.middleware.cors import CORSMiddleware

#orm
from orm.database import init_db

#routers
from api.health import router as health_router
from api.upload import router as upload_router
from api.analyze import router as analyze_router

#Ciclo de vida de la app
@asynccontextmanager
async def lifespan(app: FastAPI):
    #Al iniciar la app, crea las tablas si no existen
    await init_db() 
    yield
    #Aquí opcinalmente se puede poner código para cuando la app se cierra


app = FastAPI(title="MYB - Mind Your Business API", lifespan=lifespan)

#CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # <-- "*" permite entrar a cualquiera
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#conecta el router de healh a la app principal
app.include_router(health_router)

app.include_router(upload_router)

app.include_router(analyze_router)

#prueba de mensaje saludo
@app.get("/")
async def root():
    return {"message": "Bienvenido a la API de Mind Your Business"}

