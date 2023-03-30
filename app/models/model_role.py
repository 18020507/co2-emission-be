from sqlalchemy import Column, String, Boolean, DateTime

from app.models.model_base import BareBaseModel


class Role(BareBaseModel):
    __tablename__ = "roles"
    role_name = Column(String)
    description = Column(String)

