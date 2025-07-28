from fastapi import FastAPI
from schemas import RequestResultados, RequestGrafica
from services.resultados_client import call_resultados_service
from services.grafica_client import call_grafica_service

app = FastAPI()

@app.post("/resultados-paciente/")
async def obtener_resultados_paciente(request: RequestResultados):
    """
    Endpoint para obtener resultados del paciente
    """
    return await call_resultados_service(request.dict())

@app.post("/grafica-examen/")
async def obtener_grafica_examen(request: RequestGrafica):
    """
    Endpoint para obtener gráfica de un examen
    """
    return await call_grafica_service(request.dict())
