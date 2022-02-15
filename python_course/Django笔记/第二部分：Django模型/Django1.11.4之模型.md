# Django1.11.4之模型

## 流程梳理

### 创建工程

#### 执行<django-admin startproject project>

### 创建项目

### 激活项目

### 配置数据库

#### 修改__init__.py文件

#### 修改settings.py文件中的DATABASES

### 创建模型类

#### 在项目目录下的models.py文件中

### 生成迁移文件

#### 执行<python manage.py makemigrations>

### 执行迁移

#### 执行<python manage.py migrate>

### 配置站点

### 创建模板目录/项目模板目录

### 在settings.py文件中TEMPLATES配置模板路径

### 在project下修改urls.py

### 在项目目录下创建urls.py

## 定义模型

### Django都各种数据库提供了很好的支持，为这些数据库提供了同意的调用API，可以根据不同的业务需求选择不同的数据库 

### 配置数据库

#### 修改工程目录下的__init__.py文件

#### 在settings.py文件中修改DATABASES

### 开发流程

#### 配置数据库

#### 定义模型类

##### 一个模型类对应一个数据库中的表

#### 生成迁移文件

##### 生成数据表

#### 使用模型类进行增删改查(CRUD)

### ORM

#### 概括

##### 对象、关系、映射

##### Object/Relational Mapping

#### 图解

#####  

#### ORM把数据库映射为对象

##### 数据库的表（table） --> 类（class）
记录（record，行数据）--> 对象（object）
字段（field）--> 对象的属性（attribute）

#### 任务

##### 根据对象的类型生成表结构

##### 将对象、列表的操作转换为SQL语句

##### 将SQL语句查询到的结果转换为对象、列表

#### 优点

##### 减轻了开发人员的工作量，不需要面对因数据库的变更而修改代码

### 定义属性

#### 模型、属性、表、字段间的关系

##### 一个模型类在数据库中对应一张表，在模型类中定义的属性，对应该模型对照表中的一个字段

#### 定义属性

##### 概述

###### ·django根据属性的类型确定以下信息

####### ·当前选择的数据库支持字段的类型
·渲染管理表单时使用的默认html控件
·在管理站点最低限度的验证

###### ·django会为表增加自动增长的主键列，每个模型只能有一个主键列，如果使用选项设置某属性为主键列后，则django不会再生成默认的主键列

###### ·属性命名限制

####### ·遵循标识符规则
·由于django的查询方式，不允许使用连续的下划线

##### 库

###### ·定义属性时，需要字段类型，字段类型被定义在django.db.models.fields目录下，为了方便使用，被导入到django.db.models中

###### ·使用方式

####### ·导入from django.db import models
·通过models.Field创建字段类型的对象，赋值给属性

##### 逻辑删除

###### ·对于重要数据都做逻辑删除，不做物理删除，实现方法是定义isDelete属性，类型为BooleanField，默认值为False

##### 字段类型

###### AutoField

####### 一个根据实际ID自动增长的IntegerField,通常不指定

####### 一个主键字段将自动添加到模型中

###### ·CharField（max_length-字符长度）

####### ·字符串，默认的表单样式是TextInput

###### ·TextField

####### ·大文本字段，一般超过4000使用，默认的表单控件是Textarea

###### ·IntegerField

####### 整数

###### ·DecimalField（max_digits=None，decimal_places=None）

####### ·使用python的Decimal实例表示的十进制浮点数

####### 参数说明

######## ·DecimalField.max_digits
·位数总数

######## ·DecimalField.decimal_places
·小数点后的数字位数

###### FloatField

####### 用Python的float实例来表示的浮点数

###### BooleanField

####### true/false字段，此字段的默认表单控制是CheckboxInput

###### ·NullBooleanField

####### 支持null、true、false三种值

###### DateField([auto_now=False，auto_now_add=False]）

####### ·使用Python的datetime.date实例表示的日期

####### ·参数说明

######## ·DateField.auto_now
·每次保存对象时，自动设置该字段为当前时间，用于“最后一次修改”的时间戳，它总是使用当前日期，默认为false·

######## DateField.auto_now_add
·当对象第一次被创建时自动设置当前时间，用于创建的时间戳，它总是使用当前日期，默认为false

####### 说明

######## ·该字段默认对应的表单控件是一个TextInput.在管理员站点添加了一个Javascript写的日历控件，和一个“Today”的快捷按钮，包含了一个额外的invalid_date错误消息键

####### 注意

######## ·auto_now_add，auto_now，and default 这些设置是相排斥的，他们之间的任何组合将会发生错误的结果

###### TimeField

####### 使用Python的datetime.time实例表示的时间，参数同DateField

###### DateTimeField

####### 使用Python的datetime，参数同DateField

###### FileField

####### 一个上传文件的字段

###### ImageField

####### 继承了FileField的所有属性和方法，但对上传的对象进行校验，确保它是个有效的image

##### 字段选项

###### 概述

####### .通过字段选项，可以实现对字段的约束
·在字段对象时通过关键字参数指定

###### null

####### ·如果为True，Django将空值以NULL存储到数据库中，默认值是False

###### blank

####### ·如果为True，则该字段允许为空白，默认值是False

###### ·注意

####### ·null是数据库范畴的概念，blank是表单验证证范畴的

###### ·db_column

####### .字段的名称，如果未指定，则使用属性的名称

###### ·db_index

####### .若值为True，则在表中会为此字段创建索引

###### ·default

####### ·默认值

###### ·primary_key

####### ·若为True，则该字段会成为模型的主键字段

###### ·unique

####### ·如果为true，这个字段在表中必须有唯一值

##### 关系

###### 分类

####### ·Foreignkey：一对多，将字段定义在多的端中

####### ·ManyToManyField：多对多，将字段定义在两端中

####### ·OneToOneField：一对一，将字段定义在任意一端中

###### 用一访问多

####### 格式

######## 对象、模型类小写_set

####### 示例

######## grade.students_set

###### 用一访问一

####### 格式

######## 对象、模型类小写

####### 示例

######## grade.students

###### 访问id

####### 格式

######## 对象.属性_id

####### 示例

######## student.sgrade_id

### 创建模型类

### 元选项

#### 在模型类中定义Meta类，用于设置元信息

##### db_table

###### 定义数据表名，如果不写数据，则数据表明默认为<项目名_类名>

##### ordering

###### 对象的默认排序字段，获取对象的列表时可以使用

###### ordering['id']

####### 升序

###### ordering['-id']

####### 降序

###### 排序会增加数据库的开销

## 模型成员 

### 类属性

#### objects查询器

##### 是Manager类型的一个对象，作用是和数据库进行交互

##### 当定义模型类时没有指定管理器，则Django为模型创建一个名为objects的管理器

#### 自定义管理器

##### stuObj  = models.Manager()

##### 当为模型指定管理器，Django就不再为模型类生成objects管理器

#### 自定义管理器Manager类

##### 模型管理器是Django的模型与数据库进行交互的接口，一个模型可以有多个模型管理器

##### 作用

###### 向管理器类中添加额外的方法

###### 修改管理器返回的原始查询集

####### 重写get_queryset()方法

##### 代码示例

###### 

####### class StudentsManager(models.Manager):

######## def get_queryset(self):

######### return super(StudentsManager, self).get_queryset().filter(isDelete=False)

### 创建对象

#### 目的：向数据库中添加数据

#### 当创建对象时，Django不会对数据库进行读写操作，当调用save()方法时才与数据库交互，将对象保存到数据库表中

#### 注意：__init__方法已经在父类models.Model中使用，在自定义的模型中无法使用

#### 方法两种

##### 在模型类中增加一个类方法

###### @classmethod
def createStudent(cls, name, age, gender, contend, lastTime, createTime, grade, isDelete=False):
	stu = cls(name=name, age=age, gender=gender, contend=contend, lastTime=lastTime, createTime=createTime, grade=grade, isDelete=isDelete)
	return stu

###### 视图中的应用

####### def addstudent(request):

######## grade = Grades.objects.get(pk=1)

######## stu = Students.createStudent('刘德华', 34, True, 'zzzzz', '2020-5-20', '2020-5-20', grade)

######## stu.save()

######## return HttpResponse('success!')

##### 在自定义管理器中添加一个方法

###### 分支主题

####### class StudentsManager(models.Manager):

######## def get_queryset(self):

######### return super(StudentsManager, self).get_queryset().filter(isDelete=False)

######## def createStudent(self, name, age, gender, contend, lastT, createT, grade, isD=False):

######### stu = self.model()  # Students类型

######### stu.name = name

######### stu.age = age

######### stu.gender = gender

######### stu.contend = contend

######### stu.lastTime = lastT

######### stu.createTime = createT

######### stu.grade = grade

######### return stu

## 模型查询

### 概述

#### 查询集表示从数据库中获取的对象的集合

#### 查询集可以有多个过滤器

#### 过滤器就是一个函数，基于所给的参数限制查询集结果

#### 从SQL角度来说，查询集合select语句等价，过滤器就像where条件

### 查询集

#### 在管理器上调用过滤器方法返回查询集

#### 查询集经过过滤器筛选后返回新的查询集，所以可以写成链式调用

#### 惰性执行

##### 创建查询集不会带来任何数据库的访问，直到调用数据时，才会访问数据库

#### 直接访问数据的情况

##### 迭代

##### 序列化

##### 与if合用

#### 返回查询集的方法称为过滤器

##### all()

###### 返回查询集的所有数据

##### filter()

###### 返回符合条件的数据

###### filter(键=值)

###### filter(键=值, 键=值)

###### filter(键=值).filter(键=值)

##### exclude()

###### 过滤掉符合条件的数据

##### order_by()

###### 排序

##### values()

###### 一条数据就是一个对象（字典），返回一个列表

#### 返回单个数据

##### get()

###### 返回一个满足条件的对象

###### 注意

####### 如果没有找到符合条件的对象，会引发<模型类.DoesNotExist>的异常

####### 如果找到多个对象，也会引发<模型类.MultipleObjectsReturned>异常

##### count()

###### 返回当前查询集中的对象个数

##### first()

###### 返回查询集中的第一个对象

##### last()

###### 返回查询集中的最后一个对象

##### exists()

###### 判断查询集中是否有数据，返回True或False

#### 限制查询集

##### 查询集返回列表，可以使用切片的方法进行限制，就等同于SQL中的LIMIT语句

##### 注意：下标不能用负数

##### 例：students_list = Students.stuObj2.all()[0:5]

#### 查询集的缓存

##### 概述

###### 每个查询集都包含一个缓存，来最小化的对数据库访问

###### 在新建的查询集中，缓存首次为空，第一次对查询集求值，会发生数据缓存，Django会将查询出来的数据做一个缓存并返回查询结果，以后的查询直接使用缓存

#### 字段查询

##### 概述

###### 实现了SQL中的where语句，作为方法filter(),exclude(),get()的参数

###### 语法

####### 属性名称__比较运算符 = 值   （下划线是两个）

###### 外键

####### 属性名_id

###### 转义

####### SQL的LIKE语句中使用%是为了匹配占位，匹配%用<where like "\%">

####### filter中%没有匹配占位的功能

##### 比较运算符

###### exact

####### 判断，大小写敏感

####### 例如：filter(isDelete=False)

###### contains

####### 是否包含，大小写敏感

####### 例子

######## 查询名字中带“孙”的学生

######### students_list = Students.stuObj2.filter(name__contains='孙')

###### startswith, endswith

####### 以value开头或结尾，大小写敏感

####### 例子

######## 查询名字以“刘”开头的学生

######### students_list = Students.stuObj2.filter(name__startswith='刘')

###### 以上四个运算符在前面加上i,就表示不区分大小写

####### iexact, icontains, istartswith, iendswith

###### isnul, isnotnull

####### 是否为空

####### filter(name__isnull=False)

###### in

####### 是否包含在范围内

####### 例子

######## 查询孙武和刘德华

######### students_list = Students.stuObj2.filter(name__in=['刘德华', '孙武'])

###### gt, gte, lt, lte

####### 大于，大于等于， 小于， 小于等于

######## 查询年龄大于20的学生

######### students_list = Students.stuObj2.filter(age__gt=20)

###### year, month, day, week_day, hour, minute, second

####### 查询lastTime是2020年的学生

######## students_list = Students.stuObj2.filter(lastTime__year=2020)

###### 跨关联查询

####### 处理join查询

######## 语法

######### 模型类名__属性名__比较运算符

######## 例子

######### 找出姓名里带有“刘”的同学的班级

########## grades_list = Grades.graObj.filter(students__name__contains='刘')

###### 查询快捷

####### pk

######## 主键

##### 聚合函数

###### 使用aggregate()函数返回聚合函数的值

###### Avg

###### Count

###### Max

####### 例子

######## maxAge = Students.stuObj2.aggregate(Max('age'))
print(maxAge)

###### Min

###### Sum

##### F对象

###### 实现模型的A属性与B属性进行比较

####### 找到女生比男生多的班级

######## g = Grades.graObj.filter(girl_num__gt=F('boy_num'))
print(g)

###### 支持F对象的算术运算

####### 例子

######## g = Grades.graObj.filter(girl_num__gt=F('boy_num')+20)
print(g)

##### Q对象

###### 概述

####### 过滤器的方法中的关键字参数，条件为And模式

###### Q对象目的

####### 实现or关系的查询

###### 例子

####### students_list = Students.stuObj2.filter(Q(pk__lte=3) | Q(age__gt=50))

####### ~代表取反

######## students_list = Students.stuObj2.filter(~Q(pk__lte=3))
