package routes

import (
	"net/http"
	"web_app2/controller"
	"web_app2/controller/c_mongo_lx"
	"web_app2/logger"
	"web_app2/middlewares/auth"
	"web_app2/middlewares/cors"
	"web_app2/settings"

	"github.com/gin-contrib/pprof"
	"github.com/gin-gonic/gin"
)

func Setup(mode string) *gin.Engine {
	if mode == gin.ReleaseMode {
		gin.SetMode(gin.ReleaseMode)
	}
	r := gin.New()
	r.Use(logger.GinLogger(), logger.GinRecovery(true))
	r.Use(cors.Cors())

	v1 := r.Group("/api/v1")
	v1.Use(auth.JWTAuthMiddleware())
	{
		v1.GET("/ping", func(c *gin.Context) {
			// 如果是登录的用户,判断请求头中是否有 有效的JWT  ？
			c.String(http.StatusOK, "pong")
		})
	}

	// 练习
	v5 := r.Group("/api/v5")
	{
		v5.GET("/mg/insert", c_mongo_lx.MgInsertHandler)
	}

	// 注册业务路由
	r.POST("/signup", controller.SignUpHandler)
	// 登陆
	r.POST("/login", controller.LoginHandler)

	// 获取版本信息
	r.GET("/version", auth.JWTAuthMiddleware(), func(c *gin.Context) {
		// 如果是登录的用户,判断请求头中是否有 有效的JWT  ？
		c.String(http.StatusOK, settings.Conf.Version)
	})

	pprof.Register(r) // 注册pprof相关路由  /debug/pprof  看程序运行情况
	// 未匹配路由返回统一值
	r.NoRoute(func(c *gin.Context) {
		c.JSON(http.StatusOK, gin.H{
			"msg": "404",
		})
	})
	return r
}
