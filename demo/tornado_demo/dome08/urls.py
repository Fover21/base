from views import index
url=[
	(r"/",index.IndexHandler), # 路由映射
	(r"/async",index.AsyncHandler), # 异步执行
	(r"/asynccoroutine",index.AsyncCoroutineHandler), # 异步执行
	(r"/asynccoroutine2",index.AsyncCoroutine2Handler), # 异步执行
	(r"/taking",index.TakingHandler), # 同步执行
	(r"/testing",index.TestingHandler), # 测试
]