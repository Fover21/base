from tornado.web import RequestHandler
import tornado
import pymysql
import pymysql.cursors
import sys
sys.path.append("..")
import config

class StaticFileHandler(tornado.web.StaticFileHandler):
    def __init__(self,*args,**kwargs):
        super(StaticFileHandler,self).__init__(*args,**kwargs) # 调用父对象的初始化
        self.xsrf_token # 这样HTML中不使用{% module xsrf_form_html() %} 的情况下，就不必像dome04中，在每一个视图里写一次这句话

class IndexHandler(RequestHandler):
    def get(self,*agrs,**kwagrs):
        self.write("<a href='/temp'>模板测试</a><br>")
        self.write("<a href='/index.html'>静态页面测试</a><br>")
        self.write("<a href='/database'>数据库测试</a><br>")

class TempHandler(RequestHandler):

    def get(self,*agrs,**kwagrs):

    	def mySum(n1,n2):
    		return n1+n2
    	num=10
    	par={"name":"root","pwd":"admin"}
    	ls=["abc",100,"def"]
    	str="<a href='/'>自动转义测试</a>"
    	self.render("temp.html",num=num,par=par,ls=ls,mySum=mySum,str1=str)

class ExtendsHandler(RequestHandler):
    def get(self,*agrs,**kwagrs):
    	title="模板继承测试"
    	self.render("extends.html",title=title)

class DatabaseHandler(RequestHandler):
    def get(self,*agrs,**kwagrs):
        title="数据库测试"
        conn=pymysql.connect(**config.dbsetting)
        cur = conn.cursor()
        cur.execute("SELECT * FROM users")
        stus = cur.fetchall()
        self.render("database.html",title=title,stus=stus)