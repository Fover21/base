from tornado.web import RequestHandler
import time
import json
from tornado.httpclient import AsyncHTTPClient
import tornado
class IndexHandler(RequestHandler):

    def get(self,*agrs,**kwagrs):
        self.write("<a href='/taking' target='_blank'>同步耗时操作页面</a><br>")
        self.write("<a href='/async' target='_blank'>回调异步耗时操作页面</a><br>")
        self.write("<a href='/asynccoroutine' target='_blank'>协程异步耗时操作页面</a><br>")
        self.write("<a href='/asynccoroutine2' target='_blank'>协程异步耗时操作页面2</a><br>")
        self.write("<a href='/testing' target='_blank'>耗时操作执行时的测试页面</a><br>")
# 回调的异步
class AsyncHandler(RequestHandler):
    def on_response(self,response):
        if response.error:
            self.send_error(500)
        else:
            data=json.loads(response.body)
            self.write(data)
        self.finish() # 当response结束后关闭通信通道

    @tornado.web.asynchronous # get结束后不关闭通信通道用于异步执行on_response
    def get(self,*agrs,**kwagrs):
        url="http://tieba.baidu.com/present/getForumRank?user_id=1484168&forum_id=4432902&pn=0&ps=4&type=1&red_tag=n0430527443"
        clent=AsyncHTTPClient()
        clent.fetch(url,self.on_response)

# 协程的异步
class AsyncCoroutineHandler(RequestHandler):

    @tornado.gen.coroutine
    def get(self,*agrs,**kwagrs):
        url="http://tieba.baidu.com/present/getForumRank?user_id=1484168&forum_id=4432902&pn=0&ps=4&type=1&red_tag=n0430527443"
        clent=AsyncHTTPClient()
        res = yield clent.fetch(url) # 异步操作在fetch中
        if res.error:
            self.send_error(500)
        else:
            data = json.loads(res.body)
            self.write(data)

# 协程的异步
class AsyncCoroutine2Handler(RequestHandler):

    @tornado.gen.coroutine
    def get(self,*agrs,**kwagrs):
        res=yield self.getdata()
        self.write(res)

    @tornado.gen.coroutine
    def getdata(self):
        url="http://tieba.baidu.com/present/getForumRank?user_id=1484168&forum_id=4432902&pn=0&ps=4&type=1&red_tag=n0430527443"
        clent=AsyncHTTPClient()
        res = yield clent.fetch(url)
        if res.error:
            res={"error":0}
        else:
            res = json.loads(res.body)
        raise tornado.gen.Return(res)
        

class TakingHandler(RequestHandler):

    def get(self,*agrs,**kwagrs):
        time.sleep(10)
        self.write("taking执行完毕")

class TestingHandler(RequestHandler):

    def get(self,*agrs,**kwagrs):
        self.write("testing执行完毕")