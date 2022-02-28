from views import index
url=[
	(r"/",index.IndexHandler), # 路由映射
	(r"/header",index.HeaderHandler), # 路由映射
	(r"/status",index.StatusHandler), # 状态码
	(r"/redirect",index.RedirectHandler), # 重定向
	(r"/error",index.ErrorHandler), # 错误处理
]