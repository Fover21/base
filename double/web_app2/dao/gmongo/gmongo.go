package gmongo

import (
	"context"
	"fmt"
	"go.mongodb.org/mongo-driver/mongo"
	"go.mongodb.org/mongo-driver/mongo/options"
	"time"
	"web_app2/settings"
)

//var mgo *mongo.Database
var client *mongo.Client

func Init(cfg *settings.MongoConfig) (Cli *mongo.Client) {
	client = NewClient(cfg)
	return client
}
func NewClient(cfg *settings.MongoConfig) (Cli *mongo.Client) {
	/*op:=options.ClientOptions{uri: setting.MongoSetting.ApplyURI,
		MaxPoolSize: &(setting.MongoSetting.MaxPoolSize),
	}*/
	// ApplyURI: "mongodb://192.168.10.10:27017",
	ApplyURI := fmt.Sprintf("mongodb://%s:%s@%s:%d/%s", cfg.User, cfg.Password, cfg.Host, cfg.Port, cfg.DbName)
	//fmt.Println(ApplyURI)
	Cli, err := mongo.Connect(context.TODO(), options.Client().ApplyURI(ApplyURI))
	if err != nil {
		fmt.Println(err)
		return nil
	}
	// ping5次，都不通认为失败
	for i := 0; i < 5; i++ {
		err := Cli.Ping(context.TODO(), nil)
		if err == nil {
			//return client.Database(cfg.DbName)
			return Cli
		}
		time.Sleep(100 * time.Microsecond)
	}
	return nil
}

func Close() {
	// 断开连接
	_ = client.Disconnect(context.TODO())
}
