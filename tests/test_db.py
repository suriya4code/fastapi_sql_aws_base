import pytest
from unittest.mock import AsyncMock, patch
from app.db.crud_utils import create_item, get_item, update_item, delete_item, list_items
from app.db.models import ItemCreate, ItemUpdate

@pytest.mark.asyncio
@patch("app.db.crud_utils.SessionLocal")
async def test_create_item_db(mock_session):
    mock_db = AsyncMock()
    mock_session.return_value.__aenter__.return_value = mock_db
    item = ItemCreate(name="test", description="desc")
    mock_db.add = AsyncMock()
    mock_db.commit = AsyncMock()
    mock_db.refresh = AsyncMock()
    result = await create_item(item)
    assert result.name == "test"

@pytest.mark.asyncio
@patch("app.db.crud_utils.SessionLocal")
async def test_list_items_db(mock_session):
    mock_db = AsyncMock()
    mock_session.return_value.__aenter__.return_value = mock_db
    mock_scalars = AsyncMock()
    mock_scalars.all.return_value = []
    mock_db.execute.return_value.scalars.return_value = mock_scalars
    result = await list_items()
    assert isinstance(result, list)
