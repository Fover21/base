from tornado.web import RequestHandler
import tornado
class IndexHandler(RequestHandler):

    def get(self,*agrs,**kwagrs):
        self.write("<a href='/login'>登录</a><br>")
        self.write("<a href='/home'>HOME</a><br>")
        self.write("<a href='/cart'>CART</a><br>")
        
class BaseHandler(RequestHandler):
    def get_current_user(self):
        flag=self.get_query_argument("flag",None)
        if flag=="logined":
            return True
        return False # 返回true执行@tornado.web.authenticated装饰的函数否则不执行
        

class LoginHandler(RequestHandler):

    def get(self,*agrs,**kwagrs):
        next=self.get_query_argument("next","")
        url="login?next="+next
        self.render("login.html",url=url)

    def post(self,*agrs,**kwagrs): 
        u=self.get_secure_cookie("u",value=None)
        print(u)
        username=self.get_body_argument("username")
        password=self.get_body_argument("password")
        next=self.get_query_argument("next","")
        if username =='admin' and password=="admin":
            # ========普通cookie========
            # self.set_cookie(name.value,domain=None,expires=None,parh="/",expires_days=)
            # name : cookie名
            # value ： cookie值
            # domain ： 提交cookie时匹配的域名
            # path ： 提交cookie时匹配的路径
            # expires ： 设置有效期，可以是时间戳整数，时间元祖，datetime类型的值 UTC时间
            # expires_days ： 设置有效期，天数，优先级低于expires

            # ========获取cookie========
            # cookie=self.get_cookie(name,default)
            # name : cookie名
            # 如果name不存在，返回default的值

            # ========删除cookie========
            # self.clear_cookie(name,path="/",domain=None)
            # 删除名为name并同时匹配path和domain的cookie
            # self.clear_all_cookie(path="/",domain=None)
            # 删除同时匹配path和domain的所有cookie

            # ========安全cookie，设置带有签名和时间戳的cookie========
            # self.set_secure_cookie(name,value,expires_days=30,version=None,**kwagrs)
            # 参数参考普通cookie

            # ========获取安全cookie========
            # self.get_secure_cookie(name,value=None,max_age_days=31,min_version=None)
            # name : cookie名
            # value ： 如果没有name的默认值
            # max_age_days : 过滤安全cookie的时间戳，设置时默认时间是30天，这里默认是31天

            self.set_secure_cookie("u","admin")


            self.redirect(next+"?flag=logined")
        else:
            self.redirect("/login?next="+next)



class HomeHandler(BaseHandler):
    # 增加get_current_user函数
    # def get_current_user(self):
    #     flag=self.get_query_argument("flag",None)
    #     if flag=="logined":
    #         return True
    #     return False # 返回true执行@tornado.web.authenticated装饰的函数否则不执行

    @tornado.web.authenticated
    def get(self,*agrs,**kwagrs):
        self.render("home.html")

class CartHandler(BaseHandler):
    # 增加get_current_user函数
    # def get_current_user(self):
    #     flag=self.get_query_argument("flag",None)
    #     if flag=="logined":
    #         return True
    #     return False # 返回true执行@tornado.web.authenticated装饰的函数否则不执行

    @tornado.web.authenticated
    def get(self,*agrs,**kwagrs):
        self.render("cart.html")