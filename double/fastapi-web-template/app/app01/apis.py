
# -*- coding: utf-8 -*-
from fastapi import APIRouter

from core.dependencies import base_dependen
from core.schema.base import DataSchema, PageSchema
from app.app01.views import list_app01_view, create_app01_view, delete_app01_view
from app.app01.schema import App01ListRes


router = APIRouter(prefix="/v1/app01", tags=["app01 project"])

router.add_api_route(
    name="list app01",
    path="/",
    endpoint=list_app01_view,
    methods=["GET"],
    # response_model=PageSchema[App01ListRes],
    dependencies=[base_dependen, ]
)

router.add_api_route(
    name="create app01",
    path="/",
    endpoint=create_app01_view,
    methods=["POST"],
    dependencies=[base_dependen, ],
)

router.add_api_route(
    name="delete app01",
    path="/",
    endpoint=delete_app01_view,
    methods=["DELETE"],
    dependencies=[base_dependen, ]
)
