from sqlalchemy import Column, String, Boolean, DateTime, ForeignKey, Integer

from app.models.model_base import BareBaseModel


class CompanyFacilityMasterData(BareBaseModel):
    __tablename__ = "company_facility_master_data"
    company_id = Column(Integer, ForeignKey("companies.id"))
    facility_address = Column(String)
    facility_type = Column(String)
    employee_no = Column(Integer)
    forklift_no = Column(Integer)
