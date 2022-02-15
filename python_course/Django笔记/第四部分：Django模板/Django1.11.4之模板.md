# Django1.11.4之模板

## 视频中跳了一部分内容

## 定义模板

### 变量

#### 语法

##### {{ var }}

#### 视图传递给模板的数据

#### 要遵守标识符规则

#### 注意

##### 如果{{ var}}中var不存在，则是空字符串

#### 在模板中使用点语法

##### 例如

###### {{ student.name }}

##### 先当成字典来处理，再当成属性或者方法，再当成索引

#### 在模板中调用对象的方法

##### 注意，在模板中不能传递参数

##### 例子

###### 调用无参方法getName（）

####### {{ student.getName }}

### 标签

#### 语法

##### {% tag %}

#### 作用

##### 在输出中创建文本

##### 控制逻辑和循环

#### 类型

##### if

###### 格式与Python语法类似

###### 格式1

####### {% if表达式 %}

####### 语句

####### {% endif %}}

###### 格式2

####### {% if 表达式1 %}

####### 语句1

####### {% else %}

####### 语句2

####### {% endif %}

###### 格式3

####### {% if 表达式1 %}

####### 语句1

####### {% elif 表达式2 %}

####### 语句2

####### {% else %}

####### 语句3

####### {% endif %}

###### 例子

####### 分支主题

##### for

###### 格式1

####### {% for 变量 in 列表%}

####### 语句

####### {% endfor %}

###### 格式2

####### {% for 变量 in 列表%}

####### 语句1

####### {% empty %}

####### 语句2

######## 注意

######### 列表为空或者不存在时才执行语句2

####### {% endfor %}

###### {{ forloop.counter}}

####### 表示当前是第几次循环

##### comment

###### 格式

####### {% comment %}

####### 注释的内容

####### {% endcomment%}

###### 作用

####### 多行代码注释，不显示在页面中

##### ifequal/ifnotequal

###### 作用

####### 判断是否相等/不等

###### 格式

####### {% ifequal 值1  值2 %}

####### 语句

####### {% endifequal %}

####### 含义：两值相等则执行语句

##### include

###### 作用

####### 加载模板并以标签内的参数渲染

###### 格式

####### {% include 模板目录  参数1, 参数2,, ..... , 参数n %}

##### url

###### 作用

####### 反向解析

###### 格式

####### {% url'namespace:name'  p1  p2%}

##### csrf_token

###### 作用

####### 用于跨站请求伪造保护

###### 格式

####### {% csrf_token %}

##### block, extends

###### 作用

####### 用于模板的继承

##### autoescape

###### 作用

####### 用户HTML转义

### 过滤器

#### 语法

##### {{ var|过滤器 }}

#### 作用

##### 在变量被显示前修改它

###### 把名字都改成大写

#### lower

##### 小写

#### upper

##### 大写

#### 过滤器可以传递参数，参数用引号引起来

##### join

###### 格式

####### {{ 列表|join:'#' }}

###### 例子

####### 分支主题

####### 分支主题

####### 分支主题

#### 如果一个变量没有被提供，或者值为false、空，则可以使用默认值

##### default

###### 格式

####### {{ var|default:'zzzzz' }}

###### 例子

####### <h1>{{ tt|default:"hahaha" }}</h1>

#### 根据给定格式转换日期为字符串

##### date

###### 格式

####### {{} dateVal|date:'y-m-d' }

#### HTML转义

##### escape

#### 加减乘除

##### add, widthratio

###### 加减统一用add实现

####### {{ num|add:-5 }}

###### 乘除要用widthratio

####### num/2*5

######## {% widthratio num 2 5 %}

### 注释

#### 单行注释

##### 语法

###### {# 注释 #}

#### 多行注释

##### {% comment %}

## 反向解析

### 地址的动态组合

### 例子

#### 项目的urls.py中要加namespace

##### url(r'^', include('myApp.urls', namespace='app'))

#### app中的urls.py中要带name

##### url(r'^good/$', views.good, name='good')

#### 模板中

##### <a href="{% url 'app:good' 参数 %}" >链接</a>

####  

##### return render(request, 'myApp/good.html', {'num': id})

## 模板继承

### 作用

#### 可以减少页面的内容的重复定义，实现页面的重用

### block标签

#### 在父模板中预留区域，子模板去填充

#### 语法

##### {% block 标签名%}

##### {% endblock 标签名%}

#### 父模板

##### <div id="main">

##### {% block main %}

##### {% endblock main %}

##### </div>

#### 子模板

##### {% extends 'myApp/base.html' %}

##### {% block main %}

##### 内容

##### {% endblock main %}

### extends标签

#### 继承模板，需要写在模板文件的第一行

#### 语法

##### {% entends 父模板路径 %}

### 例子

#### 定义一个父模板

#### 定义子模板

## HTML转义

### 将code当成普通字符串

#### return render(request, 'myApp/index.html', {'code': '<h1>zcz is a nice man</h1>'})

#### {{ code }}   或者   {{ code|escape }}

### 将code当成HTML语言解析出来

#### 关掉HTML转义

#### 方法一

##### return render(request, 'myApp/index.html', {'code': '<h1>zcz is a nice man</h1>'})

##### {{ code|safe }}

#### 方法二

##### {% autoescape off %}

##### {{ code }}

##### {% endautoescape %}

##### 若把off改成on，则是按普通字符串处理

## CSRF

### 跨站请求伪造

#### 某些恶意网站包含链接、表单、按钮、js，利用登录用户在浏览器中认证，从而攻击服务

#### 比如把网站源代码copy到本地，form表单的action改为网站的主机路径，不断地进行提交

### 防止CSRF

#### 方法一

##### 在settings.py文件的MIDDLEWARE中添加

###### 'django.middleware.csrf.CsrfViewMiddleware',

##### 但是这样把自己也防住了

#### 方法二

##### settings.py文件的中间件中不添加csrf

##### 在相应HTML文件中，<form>表单第一行添加{% csrf_token %}

##### {% csrf_token %}实际上会动态生成如下代码

######  <input type='hidden' name='csrfmiddlewaretoken' value='5OD10BWI39hxxQDV8LhbVrH4lICDJkvl5cYNamuQkvI8U15S0eps5i5LcQHsrcQA' />

###### 在页面的源代码中可以看到，隐藏这个token就达到了防止csrf的效果，但也不是绝对的安全，因为只要知道了这一串token，照样可以进行csrf攻击

## 验证码

### 作用

#### 在用户注册、登录页面的时候使用，为了防止暴力请求，减轻服务器的压力

#### 防止CSRF的一种方式
