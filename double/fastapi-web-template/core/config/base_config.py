import os


def str2bool(v):
    if v is None or isinstance(v, bool):
        return v
    return v.lower() in ("yes", "true", "t", "1")


def str2int(v):
    if v is None:
        return v
    if v == "":
        return None
    return int(v)


def str2float(v):
    if v is None:
        return v
    return int(v)


class Base:
    # ------------------- Middleware ---------------------
    # 指定允许跨域请求的url
    ORIGINS = ["*"]
    
    # ------------------- log ---------------------
    # 日志路径
    LOG_PATH = './log/'
    # 日志名称
    LOG_NAME = 'app'
    # 日志保存个数
    BACK_COUNT = 30
    
    # ------------------- mongo ---------------------
    KAFKA_BOOTSTRAP_SERVERS: list = ["192.168.10.10:9092"]
    KAFKA_TOPIC: str = "topic"
    
    # ------------------- mongo ---------------------
    # mongodb:'mongodb://root:root1234%40AWJSW@192.168.8.209:27017/fanwen?authSource=admin',
    MONGO_CACHE_URI: str = "mongodb://rshy:root1234%40AWJSW@192.168.10.10:27017/bigdata?authSource=admin"
    
    # ------------------- redis ---------------------
    REDIS_CACHE_URI: str = "redis://192.168.10.10"
    REDIS_CACHE_PORT: int = 6379
    REDIS_CACHE_DB: int = "1"
    REDIS_CACHE_PASSWORD: str = ""

    # ------------------- mysql ---------------------
    MYSQL_HOST: str = "192.168.10.5"
    MYSQL_PORT: int = 3306
    MYSQL_DB: str = "log"
    MYSQL_USER: str = "wzy"
    MYSQL_PASSWORD: str = "root1234"
    MYSQL_CONNECT_TIMEOUT: int = 10

    # ------------------- need config ---------------------
    DATABASE_MYSQL_URL = os.getenv("DATABASE_MYSQL_URL", "wzy:root1234@192.168.10.5:3306/log")

    # ------------------- option ---------------------
    CONFIG_NAME = "BASE"
    SERVICE_NAME = os.getenv("SERVICE_NAME", "fastapi-web")

    TZ = os.getenv("TZ", "Asia/Shanghai")

    TOKEN_SECRET_KEY = os.getenv("TOKEN_SECRET_KEY", "token_secret_key")

    # db
    DATABASE_URL = os.getenv("DATABASE_URL", f"mysql+aiomysql://{DATABASE_MYSQL_URL}?charset=utf8mb4")
    # 为 True 时候会把sql语句打印出来，当然，你可以通过配置logger来控制输出
    SHOW_SQL = str2bool(os.getenv("SHOW_SQL", "False"))
    # # show_sql控制, 收集每一条执行sql记录存放到g对象里，最终会在接口返回报文里添加这些记录
    RETURN_SQL = str2bool(os.getenv("RETURN_SQL", "False"))
    DATABASE_URL_ENCODING = os.getenv("DATABASE_URL_ENCODING", "utf8mb4")

    DB_POOL_RECYCLE = str2int(os.getenv("DB_POOL_RECYCLE", 3600))
    DB_MAX_OVERFLOW = str2int(os.getenv("DB_MAX_OVERFLOW", 20))
    DB_POOL_SIZE = str2int(os.getenv("DB_POOL_SIZE", 5))
