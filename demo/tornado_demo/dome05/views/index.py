from tornado.web import RequestHandler
class IndexHandler(RequestHandler):
    def get(self,*agrs,**kwagrs):
        self.write("<a href='/header'>Header设置</a><br>")
        self.write("<a href='/status'>返回状态码设置</a><br>")
        self.write("<a href='/redirect'>重定向至状态码页面</a><br>")
        self.write("<a href='/error'>返回错误界面</a><br>")


class HeaderHandler(RequestHandler):

    # set_default_headers 会在请求之前执行
    def set_default_headers(self):
        self.set_header("Content-Type","text/html")

    def get(self,*agrs,**kwagrs):
        jsonStr = {"username":"username","password":"password"}
        self.write(jsonStr)


class StatusHandler(RequestHandler):
    def get(self,*agrs,**kwagrs):
        self.set_status(999,"who am i?")
        self.write("请查看状态码")

class RedirectHandler(RequestHandler):
    def get(self,*agrs,**kwagrs):
        self.redirect("/status")

class ErrorHandler(RequestHandler):
    def write_error(self,status_code,**kwagrs):
        if status_code==500:
            self.write("服务器内部出错了")
        if status_code==404:
            self.write("页面找不到了")

    def get(self,*agrs,**kwagrs):
        flag=self.get_query_argument("flag",default="")
        if flag=='0':
            self.send_error(500)
        if flag=='1':
            self.send_error(404)
        self.write("<a href='/error?flag=0'>返回500服务器内部错误</a><br>")
        self.write("<a href='/error?flag=1'>返回404页面找不到错误</a><br>")