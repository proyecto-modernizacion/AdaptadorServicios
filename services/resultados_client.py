import httpx
from fastapi import HTTPException
import config

EXTERNAL_URL = "http://35.232.91.2/cgi-bin/wsreport.cgi/getresultados" 
FIXED_TOKEN = "YXJzb2Z0d2FyZTBSczJGdFcwcjE="

async def call_resultados_service(data: dict) -> str:
    payload = {
        "data": {
            "tkn": FIXED_TOKEN,            
            "tipo": "RT",
            **data
        }
    }

    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(EXTERNAL_URL, json=payload)
            response.raise_for_status()
    except httpx.HTTPError as e:
        raise HTTPException(status_code=502, detail=f"Error al contactar servicio de resultados: {str(e)}")

    return response.text
