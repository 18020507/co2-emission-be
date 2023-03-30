from sqlalchemy import Column, String, Boolean, DateTime, ForeignKey, Integer, Float

from app.models.model_base import BareBaseModel


class FacilityActivity(BareBaseModel):
    __tablename__ = "facility_activity"
    company_facility_master_data_id = Column(Integer, ForeignKey('company_facility_master_data.id'))
    date = Column(String)
    fuel_source_id = Column(Integer, ForeignKey('fuel_source.id'))
    activity_type_id = Column(Integer, ForeignKey('activity_type.id'))
    fuel_amount = Column(Float)
    Units = Column(String)
