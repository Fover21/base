package c_mongo_lx

import (
	"github.com/gin-gonic/gin"
	"net/http"
	"web_app2/logic/l_mongo_lx"
	"web_app2/settings"
)

func MgInsertHandler(c *gin.Context) {

	_ = l_mongo_lx.MgInsert()
	c.String(http.StatusOK, settings.Conf.Version)
}
