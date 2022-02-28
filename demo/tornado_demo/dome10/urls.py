from views import index
url=[
	(r"/",index.IndexHandler), # 路由映射
	(r"/home",index.HomeHandler), # 
	(r"/chat",index.ChatHandler), # 
]