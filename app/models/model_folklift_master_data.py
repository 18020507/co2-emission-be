from sqlalchemy import Column, String, Boolean, DateTime, ForeignKey, Integer, Float

from app.models.model_base import BareBaseModel


class FolkliftMasterData(BareBaseModel):
    __tablename__ = "folklift_master_data"
    facility_master_data_id = Column(Integer, ForeignKey('company_facility_master_data.id'))
    forklift_model = Column(String)
    fuel_type = Column(String)
    fuel_efficiency = Column(Float)
    units = Column(String)



