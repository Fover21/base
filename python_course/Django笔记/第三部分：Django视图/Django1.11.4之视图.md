# Django1.11.4之视图

## 概述

### 作用

#### 视图接收web请求，并响应web请求

### 本质

#### 视图就是一个Python函数

### 响应

#### 网页

##### 重定向

##### 错误视图

###### 404

###### 500

#### JSON数据

### 过程

#### 用户在浏览器输入网址

#### Django获取网址信息

##### 去除ip与端口

#### 交给url管理器逐个匹配urlconf，匹配成功进入对应的视图函数

#### 视图管理器找到对应的视图函数去执行，返回结果给浏览器

#### 双击放大 

## url配置

### 配置流程

#### 制定根级url配置文件

##### settings.py文件

##### ROOT_URLCONF = 'demo.urls'

##### 默认已实现

#### urlpatterns

##### 一个url实例的列表

##### 里面存的是url对象

###### 三个参数

####### 正则表达式

####### 视图名称

####### 名称

#### url匹配正则的注意事项

##### 如果想要从url中获取一个值，需要对正则加小括号

###### r'^(\d+)/$'

###### 匹配数字

##### 匹配正则前方不需要加反斜杠/

##### 正则前需要加r表示字符串不转义

### 引入其他url配置

#### 在应用中创建urls.py文件，定义本应用的url配置，方便不同项目的url管理，在工程urls文件中使用include()方法

##### include('myApp.urls')

#### 匹配过程

##### project中的urls.py中匹配到某个项目

##### 进入匹配的项目再去匹配某个view

### url的反向解析

#### 概述

##### 如果在视图、模板中使用了硬编码（即路径是写死的），在url配置发生改变时，动态生成链接的地址

#### 解决

##### 在使用连接时，通过url配置的名称，动态生成url地址

#### 作用

##### 使用url模板

## 视图函数

### 定义视图

#### 本质：一个函数

#### 视图参数

##### 一个HTTPrequest的实例，是浏览器发过来的

##### 通过正则表达式获取的参数

#### 位置

##### 一般在views.py文件下

### 错误视图

#### 404

##### 找不到网页时（url匹配不成功）返回

##### 在templates目录下定义404.html

###### request_path

####### 导致错误的网址

##### 配置settings.py

###### DEBUG = True

####### 如果为True则永远不调用404.HTML

###### ALLOWED_HOSTS = ['*']

#### 500

##### 在视图代码中出现错误（服务器代码）

#### 400

##### 错误出现在客户的操作

## HttpRequest对象

### 概述

#### 服务器接收http请求后，会根据报文创建一个HttpRequest对象

#### 视图的第一个参数就是HttpRequest对象

#### HttpRequest对象是Django创建的，之后调用视图时传递给视图

### 属性

#### path

##### 请求的完整路径（不包括域名和端口）

#### method

##### 表示请求的方式

###### GET

###### POST

#### encoding

##### 表示浏览器提交的数据的编码方式

###### 一般为utf-8

#### GET

##### 类似字典的对象，包含了get请求的所有参数

#### POST

##### 类似字典的对象，包含了post请求的所有参数

#### FILES

##### 类似字典的对象，包含了所有上传的文件

#### COOKIES

##### 字典，包含所有的cookie

#### session

##### 类似字典的对象，表示当前的会话

### 方法

#### is_ajax()

##### 如果是通过XMLHttpRequest发起的，返回True

### Quertict对象

#### request对象中的GET，POST都属于QueryDict对象

#### 方法

##### get()

###### 作用：根据键获取值

###### 只能获取一个值

###### www.zcz.com/abc?a=1&b=2&c=3

##### getlist()

###### 作用：将键的值以列表的形式返回

###### 可以获取多个值

###### www.zcz.com/abc?a=1&a=2........

####### 两个a都可以取到，但get()做不到

### GET属性

#### http://127.0.0.1:8000/get1?a=1&b=2&c=3

##### # TODO 获取get传递的数据
def get1(request):
	a = request.GET.get('a')
	b = request.GET.get('b')
	c = request.GET.get('c')
	return HttpResponse(a + '  ' + b + '  ' + c)

#### http://127.0.0.1:8000/get2?a=1&a=2&b=3&c=3

##### def get2(request):
	a = request.GET.getlist('a')
	a1 = a[0]
	a2 = a[1]
	b = request.GET.get('b')
	c = request.GET.get('c')
   return HttpResponse(a1 + '  ' + a2 + '  ' + b + '  ' + c)

### POST属性

#### 使用表单提交实现post请求

#### 关闭csrf

##### 注释掉sdttings.py的MIDDLEWARE中的某行

###### #'django.middleware.csrf.CsrfViewMiddleware',

#### def showregister(request):
	return render(request, 'myApp/register.html')


def register(request):
	name = request.POST.get('name')
	return HttpResponse(name)

## HttpResponse对象

### 概述

#### 作用：给浏览器返回数据

#### HttpRequest对象是由Django创建的，HttpResponse对象是程序员创建

### 返回的用法

#### 不调用模板，直接返回数据

##### def index(request):
   return HttpResponse('zcz is a goood boy. ')

#### 调用模板

##### 使用render方法

###### 原型

####### render(request, templateName, [content])

###### 作用

####### 结合数据和模板，返回完成的HTML

###### 参数

####### request

######## 请求体对象

####### templateName

######## 模板路径

####### content

######## 传递给需要渲染在模板上的数据

###### 示例

####### def showregister(request):
   return render(request, 'myApp/register.html')

### 属性

#### content

##### 表示返回的内容的类型

#### charset

##### 编码格式

#### status_code

##### 响应状态码

###### 200

###### 304

###### 404

#### content-type

##### 指定输出的MIME类型

### 方法

#### init

##### 使用页面的内容实例化HttpResponse对象

#### write(content)

##### 以文件的形式写入

#### flush()

##### 以文件的形式输出缓冲区

#### set_cookie(key, value, max_age=None, expires = None)

#### delete_cookie(key)

##### 删除cookie

##### 注意

###### 如果cookie不存在，则当什么都没发生

### 子类HttpResponseRedirect

#### 功能

##### 重定向，服务器端跳转

###### # 重定向
def redirect1(request):
	return HttpResponseRedirect("/redirect2/")

def redirect2(request):
	return HttpResponse('我是重定向后的视图')

###### 注意，/redirect2/是绝对路径， 不加第一个单斜杠是相对路径

#### 简写

##### redirect(to,)

###### # 重定向
def redirect1(request):
	# return HttpResponseRedirect("/redirect2/")
	return redirect('/redirect2')

#### to推荐使用反向解析

### 子类JsonResponse

#### 返回json数据，一般用于异步请求（ajax）

#### __init__(self, data)

#### data

##### 字典的对象

#### 注意

##### Content-type类型为application/json

## 状态保持

### http协议是无状态的，每次请求都是一次新的请求，不记得以前的请求

### 客户端与服务器端的一次通信就是一次会话

### 实现状态的保持，就在客户端或服务端存储有关会话的数据

### 存储方式

#### cookie

##### 所有数据都存储在客户端，但不要存储敏感数据

#### session

##### 所有数据存储在服务端，在客户端用cookie存储session_id

### 状态保持的目的

#### 在一段时间内跟踪请求者的状态，可以实现跨页面访问当前的请求者的数据

#### 注意

##### 不同的请求者之间不会共享数据

### 启用session

#### settings.py文件中

##### INSTALLED_APPS

###### 'django.contrib.sessions',

##### MIDDLEWARE

###### 'django.contrib.sessions.middleware.SessionMiddleware',

#### 默认启用

### 使用session

#### 启用session后，每个HttpRequest对象都有一个session属性，就是一个类似字典的对象

#### get(key, default=None)

##### 根据键获取session值

#### clear()

##### 清空所有的会话

#### flush()

##### 删除当前会话并删除cookie中对应的session_id

#### 实例

##### def main(request):
	username = request.session.get('uname', '游客')
	return render(request, 'myApp/main.html', {'username': username})


def login(request):
	return render(request, 'myApp/login.html')


def showmain(request):
	uname = request.POST.get('username')
	print('---------')
	request.session['uname'] = uname
	return redirect('/main/')


# 清除 session
def clear(request):
	#1 logout(request)
	#2 request.session.clear()
	#3 request.session.flush()
	return redirect('/main/')

### 设置过期时间

#### set_expiry(value)

#### 如果不设置，两个星期后过期

#### 整数

#### 时间对象

#### 0

##### 关闭浏览器时失效

#### None

##### 永不过期

### 存储session的位置

#### 数据库

##### 默认在数据库

###### SESSION_ENGINE

#### 缓存

##### 只存储在本地内存中，如果丢失不能找回，比数据库块

#### 数据库+缓存

##### 优先从本地缓存中读取，读取不到再去数据库中读取

### 使用redis缓存session

#### pip install django-redis-sessions

#### settings.py文件添加

##### SESSION_ENGINE = 'redis_sessions.session'
SESSION_REDIS_HOST = 'localhost'
SESSION_REDIS_PORT = 6379
SESSION_REDIS_DB = 0
SESSION_REDIS_PASSWORD = '123456'
SESSION_REDIS_PREFIX = 'session'
