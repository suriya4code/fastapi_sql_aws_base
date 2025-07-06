from fastapi import APIRouter, HTTPException
import httpx
import logging

microservice_router = APIRouter()

@microservice_router.get("/external-data")
async def get_external_data():
    url = "http://external-microservice/api/data"
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            response.raise_for_status()
            data = response.json()
            logging.info(f"Fetched data from external microservice: {data}")
            return data
    except Exception as e:
        logging.error(f"External microservice call failed: {e}")
        raise HTTPException(status_code=502, detail="External microservice call failed")
