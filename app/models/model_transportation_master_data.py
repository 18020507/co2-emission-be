from sqlalchemy import Column, String, Boolean, DateTime, ForeignKey, Integer

from app.models.model_base import BareBaseModel


class TransportationMasterData(BareBaseModel):
    __tablename__ = "transportation_master_data"
    company_id = Column(Integer, ForeignKey('companies.id'))
    vehicle_type = Column(String)
    vehicle_name = Column(String)
    vehicle_model = Column(String)
    vehicle_year = Column(Integer)
    vehicle_mileage = Column(Integer)
