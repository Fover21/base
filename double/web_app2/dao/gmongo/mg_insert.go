package gmongo

import (
	"context"
	"go.uber.org/zap"
)

type Student struct {
	Name string
	Age  int
}

func InsertUser() (err error) {
	s1 := Student{"小红", 12}
	//fmt.Println(s1)
	// 指定获取要操作的数据集
	collection := client.Database("bigdata").Collection("student")
	_, err = collection.InsertOne(context.TODO(), s1)
	if err != nil {
		zap.L().Error("collection InsertOne error", zap.Error(err))
		return
	}

	//fmt.Println("Inserted a single document: ", insertResult.InsertedID)
	return nil
}
