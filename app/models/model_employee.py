from sqlalchemy import Column, String, Boolean, DateTime, ForeignKey, Integer

from app.models.model_base import BareBaseModel


class Employee(BareBaseModel):
    __tablename__ = "employee"
    facility_master_data_id = Column(Integer, ForeignKey('company_facility_master_data.id'))
    full_name = Column(String)
    status = Column(Boolean, default=True)


