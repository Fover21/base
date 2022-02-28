from tornado.web import RequestHandler
# WebSocketHandler
from tornado.websocket import WebSocketHandler
class IndexHandler(RequestHandler):

    def get(self,*agrs,**kwagrs):
        self.write("<a href='/home'>聊天界面</a>")

class HomeHandler(RequestHandler):

    def get(self,*agrs,**kwagrs):
        self.render("home.html")

class ChatHandler(WebSocketHandler):
    # 保存所有的用户
    users=[]
    # self 里面是用户的信息
    def open(self):
        self.users.append(self)
        for user in self.users:
            user.write_message("欢迎[%s]登录"%(self.request.remote_ip))

    # 当客户端发送消息过来时调用
    def on_message(self,message):
        for user in self.users:
            user.write_message("[%s]：%s"%(self.request.remote_ip,message))

    # 当客户端链接关闭后调用
    def on_close(self):
        self.users.remove(self)
        for user in self.users:
            user.write_message("[%s]离开了"%(self.request.remote_ip))
        

    #判断源origin，对于符合条件的链接允许
    def check_origin(self,origin):
        return True

    # 关闭webSocket是调用
    def close(self):
        pass