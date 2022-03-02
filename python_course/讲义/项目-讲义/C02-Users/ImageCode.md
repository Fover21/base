# 图片验证码

### 1.  后端接口设计：

**访问方式**： GET   `/image_codes/(?P<image_code_id>[\w-]+)/`

**请求参数**： 路径参数

| 参数          | 类型       | 是否必须 | 说明           |
| ------------- | ---------- | -------- | ----------- |
| image_code_id | uuid字符串 | 是       | 图片验证码编号 |

**返回数据**：

验证码图片

##### 视图原型

```python
# url('^image_codes/(?P<image_code_id>[\w-]+)/$', views.ImageCodeView.as_view()), 
class ImageCodeView(APIView):
    """
    图片验证码
    """
    pass
```

### 2.  具体视图实现

在verifications/views.py中实现视图

```python
class ImageCodeView(APIView):
    """
    图片验证码
    """

    def get(self, request, image_code_id):
        """
        获取图片验证码
        """
        # 生成验证码图片
        text, image = captcha.generate_captcha()

        redis_conn = get_redis_connection("verify_codes")
        redis_conn.setex("img_%s" % image_code_id, constants.IMAGE_CODE_REDIS_EXPIRES, text)

        # 固定返回验证码图片数据，不需要REST framework框架的Response帮助我们决定返回响应数据的格式
        # 所以此处直接使用Django原生的HttpResponse即可
        return HttpResponse(image, content_type="images/jpg")
```

说明：

**django-redis提供了get_redis_connection的方法，通过调用get_redis_connection方法传递redis的配置名称可获取到redis的连接对象，通过redis连接对象可以执行redis命令。**

我们需要在配置文件中添加一个新的redis配置，用于存放验证码数据

```python
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://10.211.55.5:6379/0",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
    "session": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://10.211.55.5:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    },
    "verify_codes": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://10.211.55.5:6379/2",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}
```

### 3. 设置域名

我们现在为前端和后端分别设置两个不同的域名

| 位置 | 域名            |
| ---- | --------------- |
| 前端 | www.meiduo.site |
| 后端 | api.meiduo.site |

编辑`/etc/hosts`文件，可以设置本地域名

```shell
sudo vim /etc/hosts
```

在文件中增加两条信息

```shell
127.0.0.1   api.meiduo.site
127.0.0.1   www.meiduo.site
```

> windows系统中若设置本地域名，hosts文件在如下目录：
>
> ```shell
> C:\Windows\System32\drivers\etc
> ```

我们在前端front_end_pc/js目录中，创建host.js文件用以为前端保存后端域名

```js
var host = 'http://api.meiduo.site:8000';
```

在所有需要访问后端接口的前端页面中都引入host.js，使用`host`变量即可指代后端域名。

#### 修改settings配置中的ALLOWED_HOSTS

一旦不再使用127.0.0.1访问Django后端，需要在配置文件中修改ALLOWED_HOSTS，增加可以访问后端的域名

```python
ALLOWED_HOSTS = ['api.meiduo.site', '127.0.0.1', 'localhost', 'www.meiduo.site']
```

### 4.  前端Vue代码：

js/register.js

```js
data: {
    ...
	image_code_id: '',  // 图片验证码编号
    image_code_url: '',  // 验证码图片路径
},
mounted: function() {
    this.generate_image_code();
},
methods: {
    // 生成uuid
	generate_uuid: function(){
		var d = new Date().getTime();
		if(window.performance && typeof window.performance.now === "function"){
			d += performance.now(); //use high-precision timer if available
		}
		var uuid = 'xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx'.replace(/[xy]/g, function(c) {
			var r = (d + Math.random()*16)%16 | 0;
			d = Math.floor(d/16);
			return (c =='x' ? r : (r&0x3|0x8)).toString(16);
		});
		return uuid;
	},
    // 生成一个图片验证码的编号，并设置页面中图片验证码img标签的src属性
	generate_image_code: function(){
		// 生成一个编号
		// 严格一点的使用uuid保证编号唯一， 不是很严谨的情况下，也可以使用时间戳
		this.image_code_id = this.generate_uuid();

		// 设置页面中图片验证码img标签的src属性
		this.image_code_url = this.host + "/image_codes/" + this.image_code_id + "/";
	},
    ...
}
```

## 