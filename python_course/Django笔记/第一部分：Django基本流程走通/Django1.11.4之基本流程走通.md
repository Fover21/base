# Django1.11.4之基本流程走通

## 设计模式

### MVC

#### 核心思想

##### 解耦

#### 浏览器请求发送给Controller，Controller把需求发给Model,Model返回数据给Controller,Controller把数据传送给View渲染，View返回给浏览器

#### 编程模式

##### Model（模型）

###### 应用程序中处理数据逻辑的部分

###### 通常模型对象负责在数据库中存取数据

##### View（视图）

###### 处理数据显示的部分

###### 通常视图是依据模型数据创建的

##### Controller（控制器）

###### 处理用户交互的部分

###### 负责从视图读取数据，通知用户输入，并向模型发送数据

#### 优点

##### 降低了各功能模块之间的耦合性，方便重构代码，最大程度上实现了代码重用

### MTV

#### 概述

##### 本质与MVC没有区别，各组件之间为了保持松耦合关系

#### 编程模式

##### Model（模型）

###### 负责业务对象与数据库的对象（ORM）

##### Template（模板）相当于MVC里的View

###### 负责把页面展示给用户

##### View（视图）相当于MVC里的Controller

###### 负责业务逻辑，并在适当时候调用Model和Template

#### 注意

##### Django还有一个url分发器，作用是将一个个URL分发给不同的View处理

#### 图解

##### 双击放大

##### 说明：1.用户输入URL，通过URL控制器进行正则匹配，匹配到相应的视图函数，交给视图处理；2.视图交给Model去取数据，Model取完数据返回给视图；3.视图再把需要展示的数据传给模板（就是html页面）

## 安装 Django1.11.4版本

### Django与Python对应版本自行百度

### 安装步骤

#### 进入终端

#### 输入 pip install Django==1.11.4

#### 验证是否安装成功

##### 进入Python环境

##### import django

##### django.get_version()

## 创建项目

### 创建目录

### 打开终端进入刚才创建的目录下

### 输入  django-admin startproject djangodemo(最后一个是项目名称)

### 输入   tree .  /F    查看目录层级

### 目录层级

#### manage.py

##### 一个命令行工具，用于我们和Django的交互

#### project目录

##### __init__.py

###### 空文件，告诉Python这个目录应该被看做一个Python包

##### settings.py

###### 项目配置文件

##### urls.py

###### URL分发器，项目的URL声明

##### wsgi.py

###### 项目与WSGI兼容的web服务器入口

## 基本操作

### 设计表结构

#### 数据库的知识，随意设计就行了

#### 班级表

#### 学生表

### 配置数据库

#### Django默认数据库是SQLite

#### settings.py中，通过DATABASES配置数据库

#### 配置MySQL

##### 用pymysql库

##### 在__init__.py中写入两行代码

###### import pymysql
pymysql.install_as_MySQLdb()

##### settings.py中

###### DATABASES = {
	'default': {
	    'ENGINE': 'django.db.backends.mysql',
	    'NAME': 'djangodemo2',
	    'USER': 'root',
	    'PASSWORD': '123456',
	    'HOST': 'localhost',
	    'PORT': '3306',
	}
}

####### NAME中填数据库名

####### USER和PASSWORD分别是用户名和密码

####### HOST为数据库服务器ip，直接填本地主机

####### PORT为3306默认端口

### 创建应用

#### 一个项目可以创建多个应用，每个应用负责一种业务

#### 打开终端，进入项目目录，结构为：

##### │  manage.py
└─djangodemo2
	   settings.py
	   urls.py
	   wsgi.py
	   __init__.py

#### 执行python manage.py startapp myApp

##### 创建一个名为myApp的应用

#### myApp目录说明

##### admin.py

###### 站点配置

##### models.py

###### 模型

##### views.py

###### 视图

### 激活应用（将应用配置到项目中）

#### settings.py文件中，将myApp加入到INSTALLED_APPS中

##### # Application definition

INSTALLED_APPS = [
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'myApp'
]

### 定义模型（对接数据库）

#### 一个数据库表对应一个模型

#### 在models.py中定义

##### from django.db import models

##### 模型类要继承models.Model类

##### class Grades(models.Model):
	name = models.CharField(max_length=20)
	date = models.DateTimeField()
	girl_num = models.IntegerField()
	boy_num = models.IntegerField()
	isDelete = models.BooleanField(default=False)

	# 更改Grades.objects.all()的输出内容
	def __str__(self):
	    return "%s-%d-%d" % (self.name, self.girl_num, self.boy_num)


class Students(models.Model):
	name = models.CharField(max_length=20)
	gender = models.BooleanField(default=True)
	age = models.IntegerField()
	contend = models.CharField(max_length=20)
	isDelete = models.BooleanField(default=False)
	# 外键
	grade = models.ForeignKey("Grades")

###### 两个类对应库中的两个表，字段名与老师的略有不同

#### 说明：不需要定义主键，主键在生成表时自动添加，并默认值自动添加

### 生成数据表

#### 生成迁移文件

##### 终端中执行：  python manage.py makemigrations 

###### myApp的目录migrations下生成一个迁移文件

#### 执行迁移

##### 终端中执行： python manage.py migrate

###### 数据库中会生成一系列表

#### 如果重新迁移的话，需要删除0001.initial.py文件，把数据库也一块删除，然后再生成迁移文件，再迁移

#### 新增一张表的话不需要重新迁移，直接生成0002的迁移文件，再执行迁移即可

#### 修改原表的字段的话，需要重新迁移

### 测试操作数据

#### 进入python shell

##### 执行python manage.py shell

#### 引入一些包

##### from myApp.models import Grades, Students
from django.utils import timezone
from datatime import *

#### 查询班级表所有数据

##### Grades.objects.all()

#### 添加数据

##### 本质：创建一个模型类的对象实例

##### grade1  = Grades()

###### 创建一个空实例

##### grade1.name = 'python'

###### 名字

##### grade1.date = datetime(yaer=2020, month=4, day=23)

###### 日期

##### grade1.save()

###### 将刚才创建的grade1实例传给数据库，创建一条数据

##### 重写类的__str__函数使之更好地显示数据

###### class Grades(models.Model):

####### name = models.CharField(max_length=20)

####### date = models.DateTimeField()

####### girl_num = models.IntegerField()

####### boy_num = models.IntegerField()

####### isDelete = models.BooleanField(default=False)

####### # 更改Grades.objects.all()的输出内容

####### def __str__(self):

######## return "%s-%d-%d" % (self.name, self.girl_num, self.boy_num)

#### 查看某个数据

##### Grades.objects.all()

###### 查询所有

##### 类名.objects.get(pk=2)

###### 查询id为2的那一条数据

##### 分支主题

#### 修改数据

##### 模型对象.属性 = 新值

###### grade.name = 'c++'

##### 模型对象.save()

###### grade.save()

#### 删除数据（物理删除）

##### g = Grades.objects.get(pk=2)

##### g.delete()

#### 关联对象

##### stu = Students()

##### stu.name = 'zcz'

##### ......

##### 获得关联对象的集合

###### 需求：获取某个班级的所有学生

###### 类名.关联的类名小写_set.all()

####### grade1.students_set.all()

######## students_set是自带的方法

##### 需求：创建某个人，属于某个班级

###### stu3 = grade1.setudents_set.create(name=u'曾志伟', gender=True, ......)

###### 会直接添加到数据库，不用再进行save()

## 启动服务器

### 格式

#### python manage.py runserver ip:port

#### ip不写代表本机ip

#### port不写默认是8000

### 说明

#### Python写的轻量级web服务器，仅在开发测试时使用

### 启动

#### 打开终端没进入项目目录

#### python manage.py runserver

#### 别忘了启动数据库

#### 浏览器输入  127.0.0.1:8000检查

### 分支主题

## Admin站点管理

### 更好的管理数据库的数据，相当于一个后台管理系统

### 概述

#### 内容发布

##### 负责添加、修改、删除数据

#### 公告访问

### 配置Admin应用

#### 在settings.py中的INSTALLED_APPS中添加django.contrib.admin

##### 默认已经添加

### 创建管理员用户

#### python manage.py createsuperuser

#### 输入账号密码

#### 浏览器127.0.0.1:8000/admin进入

### 汉化

#### settings.py文件

##### LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'Asia/Shanghai'

### 管理数据表

#### 修改admin.py文件

##### 引入models中的类

###### from .models import Grades, Students

##### 添加注册

###### admin.site.register(Grades)
admin.site.register(Students)

#### 自定义管理页面

##### 定义类class GradesAdmin(admin.ModelAdmin):

##### 列表页属性

###### list_display = ['pk', 'name', 'date', 'girl_num', 'boy_num', 'isDelete']

####### 修改页面显示的字段

###### list_filter = ['name']

####### 过滤器，在页面右侧

###### search_fields = ['name']

####### 搜索框

###### list_per_page = 5

####### 每页最多显示多少条数据

##### 添加、修改页属性

###### fields = ['girl_num', 'boy_num', 'name', 'date', 'isDelete']

####### 规定属性的先后顺序

###### fieldsets = [
('num', {'fields': ['girl_num', 'boy_num']}),
('base', {'fields': ['name', 'date', 'isDelete']}),
]

####### 给属性分组

###### 注意：fields和fieldsets不能同时使用

##### 关联对象

###### 需求：在创建一个班级的时候可以同时添加几个学生

####### class StudentsInfo(admin.TabularInline):

######## model = Students

######## extra = 0

####### class StudentsInfo(admin.StackedInline):

######## 和上一个排版不一样

####### class GradesAdmin(admin.ModelAdmin):

######## inlines = [StudentsInfo]

##### 布尔值显示问题

###### 写函数

###### def sex(self):
	if self.gender:
	    return '男'
	else:
	    return '女'
# 设置页面列的名称
sex.short_description = '性别'
list_display = ['pk', 'name', 'age', sex, 'contend', 'grade', 'isDelete']

##### 执行动作的位置问题

###### actions_on_bottom = True
actions_on_top = False

##### 使用装饰器完成注册

###### @admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):

##### 分支主题

## 视图的基本使用

### 概述

#### 在django中，视图对web请求进行回应

#### 视图就是一个Python函数， 在views.py文件中定义

### 定义视图

#### from django.http import HttpResponse

#### def index(request):

##### return HttpResponse('zcz is a goood boy. ')

### 配置url

#### 修改project目录下的urls.py文件

##### from django.conf.urls import url, include
from django.contrib import admin


urlpatterns = [
	url(r'^admin/', admin.site.urls),
	url(r'^', include('myApp.urls')),

]

#### 在myApp应用目录下创建一个urls.py文件

##### from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index),
	url(r'^(\d+)/$', views.detail),
	url(r'^grades/$', views.grades),
	url(r'^students/$', views.students),
	url(r'^grades/(\d+)/$', views.get_student_id),
]

## 模板的基本使用

### 概述

#### 模板就是HTML页面，可以根据视图传过来的数据对页面进行填充

### 创建模板

#### 新建templates文件夹

##### 在templates中新建myApp文件夹

### 配置模板路径

#### 修改settings.py文件下的TEMPLATES

##### 'DIRS': [os.path.join(BASE_DIR, 'templates')],

### 定义grades.html和students.html模板

#### 模板语法

##### {{ 输出值，可以使变量，可以使对象.属性 }}

##### {% 执行代码 %}

### http://127.0.0.1:8000/grades

#### 写grades.html模板

##### {% for grade in grades %}
<li>
	<a href="#">{{ grade.name }}</a>
</li>
{% endfor %}

#### 定义视图 

##### from .models import Grades, Students
def grades(request):
	# 去模型里取数据
	grades_list = Grades.objects.all()
	# 将数据传递给模板， 模板再渲染页面， 将渲染好的页面返回给浏览器
	return render(request, 'myApp/grades.html', {'grades': grades_list})

#### 配置URL 

##### url(r'^grades/$', views.grades),

#### 说明：代码只有部分，全代码仍需要去看视频

#### 流程总结

##### 写模板，也就是HTML页面

##### 页面要与数据库交互，因此要定义视图

##### 视图负责去模型中取得相应的数据（因为模型负责和数据库对接，所以要拿数据库的数据必须经过模型）

##### 视图在模型中取得了相应的数据，再返回给模板渲染

### 点击班级，显示对应班级的所有学生

#### 定义视图

##### def get_student_id(request, num):

###### grade = Grades.objects.get(pk=num)

####### 获得对应的班级对象

###### student_list = grade.students_set.all()

####### 获得该班级的学生列表

###### return render(request, 'myApp/students.html', {'students': student_list})

#### 配置url

##### url(r'^grades/(\d+)/$', views.get_student_id),

#### 流程解析

##### 点击grades.html页面的超链接，观察地址栏，可以看到会返回类似于localhost:8000/grades/1的地址，所以需要配置相应的url

##### 而数据的处理需要交给views层，所以需要定义相对应的视图

##### 需要注意，虽然地址栏是grades/1，但是显示的是students.html的内容，原因是视图返回了myApp/students.html以及相对应的学生列表

#### 说明：代码仍旧不全，全代码还请去看视频

## 流程梳理

### 创建工程

#### 执行   dijango-admin startproject project

### 创建项目

#### 执行  python manage.py startapp myApp

### 激活项目

#### 修改 settings.py中的INSTALLED_APPS

### 配置数据库

#### 修改__init__.py,引入pymysql包

#### 修改settings.py文件中的DATABASES

### 创建模型类

#### 在项目目录下的models.py文件中

### 生成迁移文件

#### 执行 python manage.py makemigrations

### 执行迁移

#### 执行  python manage.py migrate

### 配置ADMIN站点

### 创建模板目录/项目模板目录

### 在settings.py文件的TEMPLATES中配置模板路径

### 在project下修改urls.py

### 在项目目录下创建urls.py
