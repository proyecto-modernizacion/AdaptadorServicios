from pydantic import BaseModel
from typing import List

# Para listar exámenes de un paciente
class XMN(BaseModel):
    xmn: str
    pos: str

# Para obtener resultados del paciente
class RequestResultados(BaseModel):
    codpac: str
    fecha: str
    sede: str
    xmns: List[XMN]

    nitpac: str
    tipodopac: str
    examen: str
    codanalito: str

# Para obtener grafica de un examen
class RequestGrafica(BaseModel):
    nitpac: str
    tipodopac: str
    examen: str
    codanalito: str
