from fastapi import APIRouter, HTTPException
from app.db.models import ItemCreate, ItemUpdate, ItemResponse
from app.db.crud_utils import (
    create_item,
    get_item,
    update_item,
    delete_item,
    list_items,
)
import logging

db_router = APIRouter()

@db_router.post("/items", response_model=ItemResponse)
async def create(item: ItemCreate):
    try:
        return await create_item(item)
    except Exception as e:
        logging.error(f"Create item failed: {e}")
        raise HTTPException(status_code=500, detail="Create item failed")

@db_router.get("/items/{item_id}", response_model=ItemResponse)
async def read(item_id: int):
    try:
        return await get_item(item_id)
    except Exception as e:
        logging.error(f"Get item failed: {e}")
        raise HTTPException(status_code=404, detail="Item not found")

@db_router.put("/items/{item_id}", response_model=ItemResponse)
async def update(item_id: int, item: ItemUpdate):
    try:
        return await update_item(item_id, item)
    except Exception as e:
        logging.error(f"Update item failed: {e}")
        raise HTTPException(status_code=500, detail="Update item failed")

@db_router.delete("/items/{item_id}")
async def delete(item_id: int):
    try:
        await delete_item(item_id)
        return {"status": "deleted"}
    except Exception as e:
        logging.error(f"Delete item failed: {e}")
        raise HTTPException(status_code=500, detail="Delete item failed")

@db_router.get("/items", response_model=list[ItemResponse])
async def list_all():
    try:
        return await list_items()
    except Exception as e:
        logging.error(f"List items failed: {e}")
        raise HTTPException(status_code=500, detail="List items failed")
