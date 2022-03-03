import logging

from aiomysql import sa
from core.config.common import config


logger = logging.getLogger(__name__)


class MyMysql:
    pool = None

    def __init__(self, pool=None):
        self.pool = pool

    @classmethod
    async def create(cls):
        pool = None
        try:
            pool = await sa.create_engine(
                host=config.MYSQL_HOST,
                port=config.MYSQL_PORT,
                user=config.MYSQL_USER,
                password=config.MYSQL_PASSWORD,
                db=config.MYSQL_DB,
                connect_timeout=config.MYSQL_CONNECT_TIMEOUT
            )

            cls.pool = pool
            return pool
        except Exception as e:
            logger.error(f"连接mysql异常 {e}")
        return pool


mdb = MyMysql()
