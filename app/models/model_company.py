from sqlalchemy import Column, String, Boolean, DateTime, ForeignKey, Integer

from app.models.model_base import BareBaseModel


class Company(BareBaseModel):
    __tablename__ = "companies"
    legal_name = Column(String)
    contact_name = Column(String)
    legal_address = Column(String)
    contact_email = Column(String)
    employer_identification_number = Column(Integer)
    contact_phone_number = Column(String)
    company_number_of_facilities = Column(Integer)
    company_sector = Column(String)
    company_industry = Column(String)
    company_service = Column(String)
    created_by = Column(Integer, ForeignKey('users.id'))

