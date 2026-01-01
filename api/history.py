import logging
from fastapi import APIRouter, HTTPException
from typing import List
from bson import ObjectId
from orm.models import PayrollAnalysis

logger = logging.getLogger(__name__)
router = APIRouter()

@router.get("/history", response_model=List[PayrollAnalysis])
async def get_payroll_history():
    """
    Recupera todas las nóminas guardadas en la base de datos.
    Ordenadas por fecha de subida (la más nueva primero).
    """
    try:
        # 1. BUSCAR: .find_all()
        # 2. ORDENAR: .sort("-upload_date") -> El menos (-) significa descendente (nuevas primero)
        # 3. LISTAR: .to_list() -> Ejecuta la consulta y nos da una lista de Python
        history = await PayrollAnalysis.find_all().sort("-upload_date").to_list()
        
        return history
    
    except Exception as e:
        print(f"Error recuperando historial: {e}")
        raise HTTPException(status_code=500, detail="Error al leer la base de datos")
    
@router.delete("/history/{payroll_id}")
async def delete_payroll(payroll_id: str):
    """
    Elimina una nómina específica de la base de datos por su ID.
    """
    try:
        # A) Validar que el ID tiene formato correcto de MongoDB
        if not ObjectId.is_valid(payroll_id):
            logger.warning(f"Intento de borrar con ID inválido: {payroll_id}")
            raise HTTPException(status_code=400, detail="ID de nómina no válido")

        # B) Buscar el documento
        # Usamos PydanticObjectId internamente, Beanie lo maneja si pasamos el string
        payroll = await PayrollAnalysis.get(payroll_id)
        
        if not payroll:
            logger.warning(f"Intento de borrar nómina inexistente: {payroll_id}")
            raise HTTPException(status_code=404, detail="Nómina no encontrada")

        # C) Borrar
        await payroll.delete()
        logger.info(f"Nómina eliminada correctamente: {payroll_id}")
        
        return {"message": "Nómina eliminada con éxito"}

    except HTTPException as he:
        raise he # Relanzamos los errores HTTP controlados
    except Exception as e:
        logger.error(f"Error crítico intentando borrar nómina {payroll_id}: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail="Error interno del servidor")