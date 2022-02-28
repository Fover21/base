import os
BASE_DIRS=os.path.dirname(__file__)  #获取当前文件所在的目录

#参数
options={
    "port":8000,
}
#配置
settings={
	"static_path":os.path.join(BASE_DIRS,"static"),
	"template_path":os.path.join(BASE_DIRS,"templates"),
	"debug":True,
	"login_url":"/login",
	"xsrf_cookies":True,
	# 生成办法：
	#import base64,uuid
 	#base64.b64encode(uuid.uuid4().bytes+uuid.uuid4().bytes)
	"cookie_secret":"X7tTQtXETRWGYmQOaXKbQ5gsSNcaREutud+1zMFQVpY=",

}
