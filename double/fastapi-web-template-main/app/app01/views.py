
from typing import Any, Optional
from app.app01.app01 import list_app01, create_app01, delete_app01
from app.app01.schema import App01CreateReq


async def list_app01_view(
    page: Optional[int] = 1,
    limit: Optional[int] = 10,
):
    return await list_app01(page, limit)

async def create_app01_view(item: App01CreateReq):
    await create_app01(item.name, item.description)
    return {"data": "success"}

async def delete_app01_view(record_id: str):
    await delete_app01(record_id)
    return {"data": "success"}

