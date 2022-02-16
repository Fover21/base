package l_mongo_lx

import (
	"web_app2/dao/gmongo"
)

func MgInsert() (err error) {
	return gmongo.InsertUser()
}
