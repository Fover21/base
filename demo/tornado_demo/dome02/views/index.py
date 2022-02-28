from tornado.web import RequestHandler
class IndexHandler(RequestHandler):

    def get(self,*agrs,**kwagrs):
        self.write("Hi dome02!!")