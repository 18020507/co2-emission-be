from sqlalchemy import Column, String, Boolean, DateTime, ForeignKey, Integer

from app.models.model_base import BareBaseModel


class Client(BareBaseModel):
    __tablename__ = "clients"
    company_id = Column(Integer, ForeignKey('companies.id'))
    client_name = Column(String)



