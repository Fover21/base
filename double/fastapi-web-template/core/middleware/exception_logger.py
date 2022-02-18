from fastapi.responses import JSONResponse
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
