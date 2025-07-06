from fastapi import APIRouter, UploadFile, File, HTTPException
from app.aws.s3_utils import upload_file_to_s3
from fastapi.responses import JSONResponse
import logging

s3_router = APIRouter()

@s3_router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    try:
        url = await upload_file_to_s3(file)
        logging.info(f"File {file.filename} uploaded to S3: {url}")
        return {"url": url}
    except Exception as e:
        logging.error(f"S3 upload failed: {e}")
        raise HTTPException(status_code=500, detail="S3 upload failed")
