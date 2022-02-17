import logging
from logging import handlers
from core.config.common import config

sys_log = logging.getLogger('app_log')
sys_log.setLevel(level=logging.DEBUG)


def log_init():
    sys_log.setLevel(level=logging.DEBUG)
    formatter = logging.Formatter(
        '进程ID:%(process)d - '
        '线程ID:%(thread)d- '
        '日志时间:%(asctime)s - '
        '代码路径:%(pathname)s:%(lineno)d - '
        '日志等级:%(levelname)s - '
        '日志信息:%(message)s'
    )
    sys_log.handlers.clear()

    file_handler_error = handlers.TimedRotatingFileHandler(f'{config.LOG_PATH}{config.LOG_NAME}_logs.error.log',
                                                           encoding='utf-8', when='D', backupCount=config.BACK_COUNT)
    file_handler_error.setLevel(level=logging.ERROR)
    file_handler_error.setFormatter(formatter)
    # 设置过滤器将级别划分
    file_handler_error_filter = logging.Filter()
    file_handler_error_filter.filter = lambda r: r.levelno >= logging.WARNING
    file_handler_error.addFilter(file_handler_error_filter)

    file_handler = handlers.TimedRotatingFileHandler(f'{config.LOG_PATH}{config.LOG_NAME}_logs.info.log',
                                                     encoding='utf-8', when='D', backupCount=config.BACK_COUNT)
    file_handler.setLevel(level=logging.INFO)
    file_handler.setFormatter(formatter)
    # 设置过滤器将级别划分
    file_handler_filter = logging.Filter()
    file_handler_filter.filter = lambda r: r.levelno < logging.WARNING
    file_handler.addFilter(file_handler_filter)

    sys_log.addHandler(file_handler_error)
    sys_log.addHandler(file_handler)
