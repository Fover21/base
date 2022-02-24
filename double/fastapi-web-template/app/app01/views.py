# -*- coding: utf-8 -*-
import pickle

from typing import Any, Optional
from app.app01.app01 import list_app01, create_app01, delete_app01
from app.app01.schema import App01CreateReq
from core.middleware import g
from core.storage import rdb, mgdb
import asyncio
from fastapi import Request


async def list_app01_view(
    request: Request,
    page: Optional[int] = 1,
    limit: Optional[int] = 10,
):
    # print("request", request)
    # print("request", request.app.__dict__)
    # # print("request", request.app.state.redis)
    #
    # # 操作redis
    # await request.app.state.redis.set("a", 1)
    # re_data = await request.app.state.redis.get("a")
    # print(re_data)
    #
    # # 操作mongodb
    db = request.app.state.mongo["bigdata"]
    collection = db["bigdata"]
    print(collection)
    c = await collection.find_one({})
    print(c)

    # 执行原生的sql
    # stmt = await g.db.execute(f"select * from app01")
    # print("stmt", stmt.fetchall())
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

