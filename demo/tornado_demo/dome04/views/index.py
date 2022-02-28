from tornado.web import RequestHandler

# 上传文件使用
import os
import config

# 反向解析示例
class HomeHandler(RequestHandler):

    def get(self, *agrs, **kwagrs):
        self.write("反向解析示例")

# 普通路由示例
class IndexHandler(RequestHandler):

    def get(self, *agrs, **kwagrs):

        # 反向解析时取出name中的值
        url = self.reverse_url("indexHome")
        self.write("普通路由示例,配置文件中开启了xrsf防止跨站请求<br>")
        self.write("<a href='%s'>反向解析示例</a><br>"%(url))
        self.write("<a href='/sunck'>带参数示例</a><br>")
        self.write("<a href='/uri/a/b/c'>提取URI的特定部分</a><br>")
        self.write("<a href='/get?a=1&b=2'>GET</a><br>")
        self.write("<a href='/post'>POST</a><br>")
        self.write("<a href='/postnoxsrf'>POST[没有Xsrf]</a><br>")
        self.write("<a href='/setxsrf'>手动设置xrsf，并手动设置POST的Xsrf</a><br>")
        self.write("<a href='/ajaxxsrf'>ajax 的xrsf测试</a><br>")
        self.write("<a href='/request?test=test'>requset对象</a><br>")
        self.write("<a href='/upfile'>上传文件</a><br>")

# 传参数示例
class SunckHandler(RequestHandler):

    # 该方法会在HTTP方法之前使用
    def initialize(self, word1, word2):
        self.word1 = word1
        self.word2 = word2

    def get(self, *agrs, **kwagrs):
        self.write("传参数示例：word1=%s,word2=%s" % (self.word1, self.word2))

# 提取URI的特定部分
class UriHandler(RequestHandler):
    #使用h1,h2,h3获取路由中获取的3个值
    def get(self,h1,h2,h3,*agrs,**kwagrs):
        self.write("h1=%s,h2=%s,h3=%s"%(h1,h2,h3))

# 注意：get_argument 在GET和POST请求中都可以获取参数
# GET get_query_argument
class GetHandler(RequestHandler):
    def get(self,*agrs,**kwagrs):
        # 原型：self.get_query_argument(name,default="",strip=True)
        # name : 参数名；default：如果没有找到name，返回的值；strip：是否去前后空格
        a=self.get_argument("a") # get_argument 在GET请求中获取参数
        b=self.get_query_argument("b")
        c=self.get_query_argument("c",default="没有此参数")
        self.write("a=%s,b=%s,c=%s"%(a,b,c))

# POST get_body_argument
class PostHandler(RequestHandler):
    def get(self,*agrs,**kwagrs):
        #返回静态页面
        self.render('post.html')
    def post(self,*agrs,**kwagrs):
        # 原型：self.get_body_argument(name,default="",strip=True)
        # name : 参数名；default：如果没有找到name，返回的值；strip：是否去前后空格
        name=self.get_argument("username")# get_argument 在POST请求中获取参数
        password=self.get_body_argument("password")
        hobbyList=self.get_body_arguments("hobby") # 注意，多个同名参数使用get_body_arguments
        test=self.get_body_argument("test",default="没有此参数")
        self.write("name=%s<br>password=%s<br>hobbyList=%s<br>text=%s<br>"%(name,password,hobbyList,test))

# POST No xrsf
class PostNoXsrfHandler(RequestHandler):
    def get(self,*agrs,**kwagrs):
        #返回静态页面
        self.render('postnoxsrf.html')
    def post(self,*agrs,**kwagrs):
        # 原型：self.get_body_argument(name,default="",strip=True)
        # name : 参数名；default：如果没有找到name，返回的值；strip：是否去前后空格
        name=self.get_argument("username")# get_argument 在POST请求中获取参数
        password=self.get_body_argument("password")
        hobbyList=self.get_body_arguments("hobby") # 注意，多个同名参数使用get_body_arguments
        test=self.get_body_argument("test",default="没有此参数")
        self.write("name=%s<br>password=%s<br>hobbyList=%s<br>text=%s<br>"%(name,password,hobbyList,test))
# 手动设置xrsf并手动配置post
class SetXsrfHandler(RequestHandler):
    def get(self,*agrs,**kwagrs):
        self.xsrf_token
        # self.finish()
        self.render('setxsrf.html')
    def post(self,*agrs,**kwagrs):
        # 原型：self.get_body_argument(name,default="",strip=True)
        # name : 参数名；default：如果没有找到name，返回的值；strip：是否去前后空格
        name=self.get_argument("username")# get_argument 在POST请求中获取参数
        password=self.get_body_argument("password")
        hobbyList=self.get_body_arguments("hobby") # 注意，多个同名参数使用get_body_arguments
        test=self.get_body_argument("test",default="没有此参数")
        self.write("name=%s<br>password=%s<br>hobbyList=%s<br>text=%s<br>"%(name,password,hobbyList,test))

#ajax xsrf测试
class AjaxXsrfHandler(RequestHandler):
    def get(self,*agrs,**kwagrs):
        self.xsrf_token
        # self.finish()
        self.render('ajaxxsrf.html')

    def post(self,*agrs,**kwagrs):
        name=self.get_body_argument("username")# get_argument 在POST请求中获取参数
        pwd=self.get_body_argument("password")
        self.write("username：%s,password:%s"%(name,pwd))

# request对象
class RequestTestHandler(RequestHandler):
    def get(self,*agrs,**kwagrs):
        
        method=self.request.method
        host=self.request.host
        uri=self.request.uri
        path=self.request.path
        headers=self.request.headers
        query=self.request.query
        version=self.request.version
        body=self.request.body
        remote_ip=self.request.remote_ip
        files=self.request.files
        self.write(
            "[method]=%s<br>[host]=%s<br>[uri]=%s<br>[path]=%s<br>[headers]=%s<br>[query]=%s<br>[version]=%s<br>[body]=%s<br>[remote_ip]=%s<br>[files]=%s<br>"
            %(method,host,uri,path,headers,query,version,body,remote_ip,files)
        )
        #返回静态页面
        self.render('request.html')
    def post(self,*agrs,**kwagrs):
        method=self.request.method
        host=self.request.host
        uri=self.request.uri
        path=self.request.path
        headers=self.request.headers
        query=self.request.query
        version=self.request.version
        body=self.request.body
        remote_ip=self.request.remote_ip
        files=self.request.files
        self.write(
            "[method]=%s<br>[host]=%s<br>[uri]=%s<br>[path]=%s<br>[headers]=%s<br>[query]=%s<br>[version]=%s<br>[body]=%s<br>[remote_ip]=%s<br>[files]=%s<br>"
            %(method,host,uri,path,headers,query,version,body,remote_ip,files)
        )

# 上传文件
class UPFileHandler(RequestHandler):
    def get(self,*agrs,**kwagrs):
        #返回静态页面
        self.render('upfile.html')
    def post(self,*agrs,**kwagrs):
        files=self.request.files
        for upFileName in files:
            upFileList=files[upFileName]
            for upFileObj in upFileList:
                #保存文件需要引入 import os和import config.py
                filepath=os.path.join(config.BASE_DIRS,'upfile/'+upFileObj.filename)
                with open(filepath,"wb") as f:
                    f.write(upFileObj.body)
        
        self.write("上传成功")