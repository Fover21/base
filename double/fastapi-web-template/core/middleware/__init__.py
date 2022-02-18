import time
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from .fastapi_globals import GlobalsMiddleware, g
from .session import DbSessionMiddleware
from .exception_logger import catch_exceptions_middleware

from core.config.common import config


def register_http_middleware(app: FastAPI):
    """
    add middleware
    """
    app.middleware('http')(catch_exceptions_middleware)
    app.add_middleware(
        CORSMiddleware,
        allow_origins=config.ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    # use g.db for get sqla session
    app.add_middleware(DbSessionMiddleware)

    # the global object: g
    app.add_middleware(GlobalsMiddleware)
