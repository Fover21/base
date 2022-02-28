import tornado.web
from views import index
url=[
	(r"/",index.IndexHandler), # 路由映射
	(r"/sunck",index.SunckHandler,{"word1":"good","word2":"nice"}), # 路由映射，传参数,在view中接收
	tornado.web.url(r"/home",index.HomeHandler,name="indexHome") # 反向解析
]