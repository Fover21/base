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
        _pool = None
        try:
            _pool = await aiomongo.create_client(config.MONGO_CACHE_URI)
            # 操作
            # db = (await _pool)["bigdata"]
            # collection = db["bigdata"]
            # c = await collection.find_one({})
            cls.pool = _pool
            return _pool
        except Exception as e:
            logger.error(f"连接mongodb异常 {e}")
        return _pool


mgdb = MyMongo()
