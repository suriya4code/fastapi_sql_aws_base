from app.db.db import SessionLocal, Item
from app.db.models import ItemCreate, ItemUpdate, ItemResponse
from sqlalchemy.future import select
from sqlalchemy.exc import NoResultFound

async def create_item(item: ItemCreate) -> ItemResponse:
    async with SessionLocal() as session:
        db_item = Item(name=item.name, description=item.description)
        session.add(db_item)
        await session.commit()
        await session.refresh(db_item)
        return ItemResponse(id=db_item.id, name=db_item.name, description=db_item.description)

async def get_item(item_id: int) -> ItemResponse:
    async with SessionLocal() as session:
        result = await session.execute(select(Item).where(Item.id == item_id))
        db_item = result.scalar_one_or_none()
        if not db_item:
            raise NoResultFound
        return ItemResponse(id=db_item.id, name=db_item.name, description=db_item.description)

async def update_item(item_id: int, item: ItemUpdate) -> ItemResponse:
    async with SessionLocal() as session:
        result = await session.execute(select(Item).where(Item.id == item_id))
        db_item = result.scalar_one_or_none()
        if not db_item:
            raise NoResultFound
        if item.name is not None:
            db_item.name = item.name
        if item.description is not None:
            db_item.description = item.description
        await session.commit()
        await session.refresh(db_item)
        return ItemResponse(id=db_item.id, name=db_item.name, description=db_item.description)

async def delete_item(item_id: int):
    async with SessionLocal() as session:
        result = await session.execute(select(Item).where(Item.id == item_id))
        db_item = result.scalar_one_or_none()
        if not db_item:
            raise NoResultFound
        await session.delete(db_item)
        await session.commit()

async def list_items() -> list[ItemResponse]:
    async with SessionLocal() as session:
        result = await session.execute(select(Item))
        items = result.scalars().all()
        return [ItemResponse(id=i.id, name=i.name, description=i.description) for i in items]
