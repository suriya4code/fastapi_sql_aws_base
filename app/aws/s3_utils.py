import boto3
import aioboto3
import logging
from fastapi import UploadFile
import os

AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
AWS_REGION = os.getenv("AWS_REGION", "us-east-1")
S3_BUCKET = os.getenv("S3_BUCKET")

async def upload_file_to_s3(file: UploadFile) -> str:
    session = aioboto3.Session()
    async with session.client(
        "s3",
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        region_name=AWS_REGION,
    ) as s3_client:
        content = await file.read()
        await s3_client.put_object(Bucket=S3_BUCKET, Key=file.filename, Body=content)
        url = f"https://{S3_BUCKET}.s3.{AWS_REGION}.amazonaws.com/{file.filename}"
        return url
