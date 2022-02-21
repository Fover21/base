import logging

import aioredis
from core.config.common import config
from core.middleware import g

import asyncio

logger = logging.getLogger(__name__)


class MyRedis:
    pool = None

    def __init__(self, pool=None):
        self.pool = pool

    @classmethod
    async def create(cls) -> aioredis.Redis:
        #     https://aioredis.readthedocs.io/en/latest/getting-started/
        #     redis://[[username]:[password]]@localhost:6379/0
        #     rediss://[[username]:[password]]@localhost:6379/0
        #     unix://[[username]:[password]]@/path/to/socket.sock?db=0
        #     """
        #     # _pool = await aioredis.from_url("127.0.0.1", port=6379, db=0, password='', decode_responses=True)
        _pool = await aioredis.from_url(config.REDIS_CACHE_URI, port=config.REDIS_CACHE_PORT,
                                        password=config.REDIS_CACHE_PASSWORD, db=config.REDIS_CACHE_DB,
                                        encoding="utf-8",
                                        decode_responses=True)
        cls.pool = _pool
        return _pool


rdb = MyRedis()
