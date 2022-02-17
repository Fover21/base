import os

from .base_config import Base, str2bool


class DevConfig(Base):
    CONFIG_NAME = "DEV"

    DATABASE_MYSQL_URL = os.getenv("DATABASE_MYSQL_URL", "wzy:root1234@192.168.10.5:3306/log")

    PROD = str2bool(os.getenv("PROD", "False"))

    # db
    DATABASE_URL = os.getenv("DATABASE_URL", f"mysql+aiomysql://{DATABASE_MYSQL_URL}?charset=utf8mb4")
    # 为 True 时候会把sql语句打印出来，当然，你可以通过配置logger来控制输出
    SHOW_SQL = str2bool(os.getenv("SHOW_SQL", "False"))
    # show_sql控制, 收集每一条执行sql记录存放到g对象里，最终会在接口返回报文里添加这些记录
    RETURN_SQL = str2bool(os.getenv("RETURN_SQL", "False"))
