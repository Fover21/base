import os
import pymysql
BASE_DIRS=os.path.dirname(__file__)  #获取当前文件所在的目录

#参数
options={
    "port":8000,
}
#数据库设置
dbsetting={
    "host":"127.0.0.1",
    "user":"root",
    "password":"592100",
    "db":"tornado_db",
    "charset":"utf8",
    "cursorclass":pymysql.cursors.DictCursor,
}
#配置
settings={
	"static_path":os.path.join(BASE_DIRS,"static"),
	"template_path":os.path.join(BASE_DIRS,"templates"),
	"debug":True,
}
