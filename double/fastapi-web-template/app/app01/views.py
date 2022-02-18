# -*- coding: utf-8 -*-
import pickle

from typing import Any, Optional
from app.app01.app01 import list_app01, create_app01, delete_app01
from app.app01.schema import App01CreateReq
from core.middleware import g
from aiomongo.client import AioMongoClient
from core.storage import rdb, mgdb, create_mongodb
import asyncio


async def list_app01_view(
    page: Optional[int] = 1,
    limit: Optional[int] = 10,
):
    # print(g, g.db)
    print("g.redis_session", rdb.pool)
    # print("g.db", g.db)
    await rdb.pool.set("a", 1)
    re_data = await rdb.pool.get("a")
    print(re_data)

    db = (await create_mongodb())["bigdata"]
    collection = db["bigdata"]
    print(collection)
    c = await collection.find_one({})
    print(c)
    # return await list_app01(page, limit)
    return {"data": "success"}


async def create_app01_view(item: App01CreateReq):
    await create_app01(item.name, item.description, item.sex, item.password1, item.password2)
    # print(g, g.db)
    # print(g._vars)
    return {"data": "success"}


async def delete_app01_view(record_id: str):
    await delete_app01(record_id)
    return {"data": "success"}

