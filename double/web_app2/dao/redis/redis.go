package redis

import (
	"context"
	"fmt"
	"web_app2/settings"

	"github.com/go-redis/redis"
)

//Background返回一个非空的Context。 它永远不会被取消，没有值，也没有期限。
//它通常在main函数，初始化和测试时使用，并用作传入请求的顶级上下文。
var ctx = context.Background()

// 声明一个全局的rdb变量
var rdb *redis.Client

// Init 初始化连接
func Init(cfg *settings.RedisConfig) (err error) {
	rdb = redis.NewClient(&redis.Options{
		Addr: fmt.Sprintf("%s:%d",
			cfg.Host,
			cfg.Port,
		),
		Password: cfg.Password, // no password set
		DB:       cfg.DB,       // use default DB
		PoolSize: cfg.PoolSize,
	})

	_, err = rdb.Ping().Result()
	return
}

func Close() {
	_ = rdb.Close()
}
