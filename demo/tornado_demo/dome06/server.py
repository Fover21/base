import tornado.web
import tornado.ioloop
import config # 新建的config.py文件
import urls # 新建的urls.py文件

# 获取参数的方法一
# 1、定义参数
# import tornado.options
# tornado.options.define(name,default=None,type=None,help=None,metavar=None,multiple=False,group=None,callback=None)
# name ： 变量名
# default : 默认值
# type : 数据类型
# help : 帮助提示信息
# metavar :
# multiple: 设置选项变量是否可以为多个值，默认为False
# group :
# callback :
# 例：
# tornado.options.define("port",default=8000,type=int,help="端口号")
# tornado.options.define("list",default=[],type=str,help="测试参数",multiple=True)
# 2、在主程序中读取cmd参数
# tornado.options.parse_command_line() # 将命令行的参数保存到tornado.options.options
# 3、使用 tornado.options.options.name 取出变量的值


# 获取参数的方法二
# import tornado.options
# 1、新建配置文件 vim config，内容如下
#     port=7000
#     list=["a1","b1"]
# 2、在主程序中读取配置文件参数
# tornado.options.parse_config_file("config") # 从配置文件导入参数
# 3、使用 tornado.options.options.name 取出变量的值

# 注意，当使用tornado.options.parse_config_file("config")和tornado.options.parse_command_line()
# 时会默认开启logging模块，如果需要关闭使用：tornado.option.option.loggin=None，且需要在读取配置之前使用。

# 获取参数的方法三（推荐）
# 1、import config
# 2、新建配置文件 vim config.py，内容如下
#     options={
#         "port":7000,
#         "list":["a1","b1"]
#     }
# 3、使用 config.options["port"] 取出变量的值


if __name__=="__main__":

    # 参数读取方法一
    # tornado.options.parse_command_line()
    # 参数读取方法二
    # tornado.options.parse_config_file("config")

    # 将url拆分出新文件urls.py
    # app=tornado.web.Application([
    #     (r"/",IndexHandler), # 路由映射
    #     (r"/dome/",DomeHandler)
    # ])
    app=tornado.web.Application(urls.url,**config.settings)

    app.listen(config.options["port"]) # app.listen只能启动单进程
    # 不建议使用以下方式启动不进程：
    # 1：每个子进程都会从父进程中复制一份IOLoop的实例，如果在创建子进程前修改了IOLoop会影响到所有的子进程
    # 2：所有的进程都是有一个命令启动的，无法做到不停止服务的情况下修改代码
    # 3：所有进程共享一个端口，想要分别监控会很困难
    # httpserver=tornado.httpserver.HTTPServer(app)
    # httpserver.bind(8001) # 绑定端口
    # httpserver.start(5) # 5 是进程数 ，当值<=0 时 启动CPU核心数的进程

    tornado.ioloop.IOLoop.current().start()

