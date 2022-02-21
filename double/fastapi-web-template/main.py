import sys
# import uvloop
import asyncio
import logging
import uvicorn


from app.ws import create_ws_manager
from core.utils.api_exception import http_exception_handler, APIException
from core.config.common import config
from core.middleware import register_http_middleware
from core.storage import create_db, rdb, mgdb
from core.utils.logs import log_init, sys_log
from fastapi import FastAPI


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
)

sys.setrecursionlimit(1500)

# windows不支持 提升速度
# asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())


def configure_models() -> None:
    """
    add model to sqla metadata
    """
    # +gencode:configure-model
    # noinspection PyUnresolvedReferences
    # 导入model就会创建对应数据库
    from app.app01 import models
    # from app.ws import models


def register_router(app: FastAPI) -> None:
    """
    注册路由
    """
    # +gencode:register-router
    from app.app01.apis import router as app01_router
    app.include_router(app01_router)

    from app.ws.apis import router as ws_router
    app.include_router(ws_router, prefix="/wss")


def register_redis_mongodb(app: FastAPI) -> None:
    """
    把redis挂载到app对象上面
    :param app:
    :return:
    """

    @app.on_event('startup')
    async def startup_event():
        """
        获取链接
        :return:
        """
        sys_log.info(f'获取链接')
        app.state.redis = await rdb.create()
        app.state.mongo = await mgdb.create()

    @app.on_event('shutdown')
    async def shutdown_event():
        """
        关闭链接
        :return:
        """
        sys_log.info(f'关闭链接')
        app.state.redis.close()
        app.state.mongo.close()
        await app.state.redis.wait_closed()
        await app.state.mongo.wait_closed()


def init_sync(app):
    # 初始化日志
    sys_log.info(f'初始化日志')
    log_init()
    # 初始化中间件
    sys_log.info(f'初始化中间件')
    register_http_middleware(app)
    # 初始化路由
    sys_log.info(f'初始化路由')
    register_router(app)
    # 初始化模型
    sys_log.info(f'初始化模型')
    configure_models()
    # 初始化数据库链接
    sys_log.info(f'初始化数据库链接')
    register_redis_mongodb(app)


def init_async():
    try:
        loop = asyncio.get_running_loop()
    except RuntimeError:  # if cleanup: 'RuntimeError: There is no current event loop..'
        loop = None
    
    # 将协程加入事件循环中
    if loop and loop.is_running():
        loop.create_task(create_db())
        loop.create_task(create_ws_manager())


# 初始化app对象，配置文档路径
app = FastAPI(
    name=config.SERVICE_NAME,
    openapi_url="/v1/openapi/openapi.json",
    docs_url="/v1/openapi/docs",
    redoc_url="/v1/openapi/redoc",
    debug=not config.PROD,
    exception_handlers={APIException: http_exception_handler},
)


# 同步初始化
init_sync(app)
# 异步初始化
init_async()


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, log_level="debug", debug=not config.PROD)
