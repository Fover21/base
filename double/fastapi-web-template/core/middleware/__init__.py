import time
from fastapi import FastAPI
from fastapi.responses import JSONResponse

from .fastapi_globals import GlobalsMiddleware, g
from .session import DbSessionMiddleware

from starlette.middleware.cors import CORSMiddleware
from starlette.requests import Request

from core.utils.logs import sys_log


# 捕获全局异常
async def catch_exceptions_middleware(request: Request, call_next):
    try:
        return await call_next(request)
    except Exception as e:
        # you probably want some kind of logging here
        sys_log.error(e)
        import traceback
        sys_log.error(traceback.format_exc())
        return JSONResponse(content={"detail": "Internal server error"}, status_code=500)


# 指定允许跨域请求的url
origins = [
    "*"
]
 

def register_http_middleware(app: FastAPI):
    """
    add middleware
    """
    app.middleware('http')(catch_exceptions_middleware)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    # use g.db for get sqla session
    app.add_middleware(DbSessionMiddleware)

    # the global object: g
    app.add_middleware(GlobalsMiddleware)
