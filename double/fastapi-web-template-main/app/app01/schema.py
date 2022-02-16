# -*- coding: utf-8 -*-
from typing import List, Optional
from core.schema import BaseSchema
from pydantic.fields import Field


class App01ListRes(BaseSchema):
    id: Optional[str] = Field(description="id")
    name: Optional[str] = Field(description="名称")
    description: Optional[str] = Field(description="描述")


class App01CreateReq(BaseSchema):
    name: Optional[str] = Field(description="名称")
    description: Optional[str] = Field(description="描述")

