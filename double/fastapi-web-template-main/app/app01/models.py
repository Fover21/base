
import uuid

from core.storage import Base
from sqlalchemy import Column, String


class App01(Base):
    __tablename__ = "app01"
    id = Column(String(36), primary_key=True, default=str(uuid.uuid4()))
    name = Column(String(128), nullable=False)
    description = Column(String(512), nullable=False)

