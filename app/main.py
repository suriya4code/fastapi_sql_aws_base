from fastapi import FastAPI
import logging
from app.aws.s3 import s3_router
from app.db.crud import db_router
from app.services.microservice import microservice_router

app = FastAPI()

# Logging setup will be imported from a separate module
from app.logging_config import setup_logging
setup_logging()

app.include_router(s3_router, prefix="/s3", tags=["S3"])
app.include_router(db_router, prefix="/db", tags=["Database"])
app.include_router(microservice_router, prefix="/microservice", tags=["Microservice"])

@app.get("/health", tags=["Health"])
async def health_check():
    logging.info("Health check endpoint called")
    return {"status": "ok"}
