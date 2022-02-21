import logging

import aiomongo, asyncio
from aiomongo.client import AioMongoClient
from core.config.common import config
from core.middleware import g

logger = logging.getLogger(__name__)


class MyMongo:
    pool = None

    def __init__(self, pool=None):
        self.pool = pool

    @classmethod
    async def create(cls) -> aiomongo.AioMongoClient:
        _pool = await aiomongo.create_client(config.MONGO_CACHE_URI)
        # 操作
        # db = (await _pool)["bigdata"]
        # collection = db["bigdata"]
        # c = await collection.find_one({})
        cls.pool = _pool
        return _pool


mgdb = MyMongo()
