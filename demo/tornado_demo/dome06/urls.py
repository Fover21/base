from views import index
import config
import os
from tornado.web import StaticFileHandler
url=[
	(r"/",index.IndexHandler), # 路由映射
	(r"/temp",index.TempHandler), # 模板界面
	(r"/extends",index.ExtendsHandler), # 模板继承
	(r"/database",index.DatabaseHandler), # 数据库测试

	# 下面这句会匹配所有的路径，最好放在最后
	(r"/(.*)$",index.StaticFileHandler,{"path":os.path.join(config.BASE_DIRS,"static/html"),"default_filename":"index.html"}), # StaticFileHandler测试
]