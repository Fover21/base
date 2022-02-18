# -*- coding: utf-8 -*-
import pickle

from typing import Any, Optional
from app.app01.app01 import list_app01, create_app01, delete_app01
from app.app01.schema import App01CreateReq
from core.middleware import g


async def list_app01_view(
    page: Optional[int] = 1,
    limit: Optional[int] = 10,
):
    # print(g, g.db)
    # print(g._vars)
    print("g.redis_session", g.redis_session)
    print("g.db", g.db)
    await g.redis_session.set("a", 1)
    re_data = await g.redis_session.get("a")
    print(re_data)
    re_data = await g.rdb.get("a")
    print(re_data)
    return await list_app01(page, limit)


async def create_app01_view(item: App01CreateReq):
    await create_app01(item.name, item.description, item.sex, item.password1, item.password2)
    # print(g, g.db)
    # print(g._vars)
    return {"data": "success"}


async def delete_app01_view(record_id: str):
    await delete_app01(record_id)
    return {"data": "success"}

