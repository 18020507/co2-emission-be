from sqlalchemy import Column, String, Boolean, DateTime, ForeignKey, Integer, Float

from app.models.model_base import BareBaseModel


class TransActivity(BareBaseModel):
    __tablename__ = "trans_activity"
    transportation_master_data_id = Column(Integer, ForeignKey('transportation_master_data.id'))
    client_id = Column(Integer, ForeignKey('client_master_data.id'))
    date = Column(String)
    fuel_source_id = Column(Integer, ForeignKey('fuel_source.id'))
    fuel_amount = Column(Float)
    distance_travel = Column(Integer)
