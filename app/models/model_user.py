from sqlalchemy import Column, String, Boolean, DateTime, ForeignKey, Integer

from app.models.model_base import BareBaseModel


class User(BareBaseModel):
    __tablename__ = "users"
    full_name = Column(String)
    user_name = Column(String)
    email = Column(String, unique=True)
    hashed_password = Column(String)
    phone_number = Column(String)
    status = Column(Boolean, default=True)
    role_id = Column(Integer, ForeignKey('roles.id'))
    last_login = Column(DateTime)
    company_id = Column(Integer, ForeignKey('companies.id'))
