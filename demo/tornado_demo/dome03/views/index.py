from tornado.web import RequestHandler


# 反向解析示例
class HomeHandler(RequestHandler):

    def get(self, *agrs, **kwagrs):
        self.write("反向解析示例")

# 普通路由示例
class IndexHandler(RequestHandler):

    def get(self, *agrs, **kwagrs):

        # 反向解析时取出name中的值
        url = self.reverse_url("indexHome")
        self.write("普通路由示例<br>")
        self.write("<a href='%s'>反向解析示例</a><br>"%(url))
        self.write("<a href='/sunck'>带参数示例</a>")

# 传参数示例
class SunckHandler(RequestHandler):

    # 该方法会在HTTP方法之前使用
    def initialize(self, word1, word2):
        self.word1 = word1
        self.word2 = word2

    def get(self, *agrs, **kwagrs):
        self.write("传参数示例：word1=%s,word2=%s" % (self.word1, self.word2))
