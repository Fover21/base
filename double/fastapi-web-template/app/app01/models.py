
# -*- coding: utf-8 -*-
import uuid

from core.storage import Base
from sqlalchemy import Column, String, SmallInteger


def gen_id():
   return uuid.uuid4().hex


class App01(Base):
    __tablename__ = "app01"
    id = Column(String(36), primary_key=True, default=gen_id)
    name = Column(String(128), nullable=False)
    sex = Column(SmallInteger, nullable=False)
    description = Column(String(512), nullable=False)


