import pytest
from fastapi.testclient import TestClient
from unittest.mock import patch, MagicMock, AsyncMock
from app.main import app

client = TestClient(app)

@patch("app.aws.s3_utils.upload_file_to_s3", new_callable=MagicMock)
def test_upload_file_to_s3(mock_upload):
    mock_upload.return_value = "https://bucket.s3.region.amazonaws.com/test.txt"
    with open("test.txt", "w") as f:
        f.write("test")
    with open("test.txt", "rb") as f:
        response = client.post("/s3/upload", files={"file": ("test.txt", f, "text/plain")})
    assert response.status_code == 200
    assert "url" in response.json()

@patch("app.db.crud_utils.create_item", new_callable=MagicMock)
def test_create_item(mock_create):
    mock_create.return_value = {"id": 1, "name": "item", "description": "desc"}
    response = client.post("/db/items", json={"name": "item", "description": "desc"})
    assert response.status_code == 200
    assert response.json()["name"] == "item"

@patch("httpx.AsyncClient.get", new_callable=MagicMock)
def test_external_microservice(mock_get):
    mock_response = MagicMock()
    mock_response.json.return_value = {"data": "value"}
    mock_response.status_code = 200
    mock_get.return_value.__aenter__.return_value = mock_response
    response = client.get("/microservice/external-data")
    assert response.status_code == 200
    assert "data" in response.json()
