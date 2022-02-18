import logging

import aiomongo
from aiomongo.client import AioMongoClient
from core.config.common import config
from core.middleware import g

logger = logging.getLogger(__name__)


class MyMongo:

    def __init__(self, pool=None):
        self.pool = pool

    @classmethod
    def create(cls):
        _pool = aiomongo.create_client(config.MONGO_CACHE_URI)
        # 操作
        # db = (await _pool)["bigdata"]
        # collection = db["bigdata"]
        # c = await collection.find_one({})
        return cls(pool=_pool)

    @classmethod
    def mongo_session(cls) -> AioMongoClient:
        mongo = cls.create()
        g.mongo_session = mongo.pool
        return g.mongo_session


mgdb = MyMongo()