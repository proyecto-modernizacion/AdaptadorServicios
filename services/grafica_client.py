import httpx
import config
from fastapi import HTTPException

EXTERNAL_URL = "http://35.232.91.2/cgi-bin/wsreport.cgi/getgraficahist"
FIXED_TOKEN = "YXJzb2Z0d2FyZTBSczJGdFcwcjE="

async def call_grafica_service(data: dict) -> str:
    payload = {
        "data": {
            "tkn": FIXED_TOKEN,
            **data
        }
    }

    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(EXTERNAL_URL, json=payload)
            response.raise_for_status()
    except httpx.HTTPError as e:
        raise HTTPException(status_code=502, detail=f"Error al contactar servicio de gráfica: {str(e)}")

    return response.text
