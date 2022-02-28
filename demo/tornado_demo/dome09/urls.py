from views import index
url=[
	(r"/",index.IndexHandler), # 路由映射
	(r"/login",index.LoginHandler), # 登录
	(r"/home",index.HomeHandler), # 主界面
	(r"/cart",index.CartHandler), # 主界面2
]