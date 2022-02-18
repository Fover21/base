
# -*- coding: utf-8 -*-
from typing import List, Optional
from core.schema import BaseSchema
from pydantic.fields import Field

from pydantic import BaseModel, Field, validator, root_validator
from typing import Optional, Dict, List


class App01ListRes(BaseSchema):
    id: Optional[str] = Field(description="id")
    name: Optional[str] = Field(description="名称")
    description: Optional[str] = Field(description="描述")


class App01CreateReq(BaseSchema):
    name: Optional[str] = Field(description="名称")
    description: Optional[str] = Field(description="描述")
    sex: Optional[int] = Field(..., description="性别")
    password1: Optional[str] = Field(None, description="密码1")
    password2: Optional[str] = Field(None, description="密码2")

    # 这个配置优先级比 Field 中 example 参数高
    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "name": "Foo 名字",
                "sex": "",
                "password1": "",
                "password2": "",
            }
        }

    @validator("name")
    # values通过验证的才记录
    def validate_name(cls, value, values, **kwargs):
        # print(value)
        # print(values)
        # print(kwargs)
        if value == "string":
            raise ValueError("错误")
        return value

    @validator("*")
    # values 顺序验证 通过验证的才记录
    def validate_sex(cls, value, values, **kwargs):
        # print(value)
        # print(values)
        if value == "string---":
            raise ValueError("错误")
        return value

    #
    @validator('password2')
    def passwords_match(cls, v, values, **kwargs):
        # print(values)
        if 'password1' in values and v != values['password1']:
            print("-----", values)
            raise ValueError('passwords do not match')
        return v

    # 根验证器  -- 最后执行  pre=True -最先执行
    @root_validator
    def check_passwords_match(cls, values):
        # print(1111, values)
        return values

