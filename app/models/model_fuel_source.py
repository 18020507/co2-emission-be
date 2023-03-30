from sqlalchemy import Column, String, Boolean, DateTime, ForeignKey, Integer

from app.models.model_base import BareBaseModel


class FuelSource(BareBaseModel):
    __tablename__ = "fuel_source"
    company_id = Column(Integer, ForeignKey('companies.id'))
    fuel_source_name = Column(String)
    unit_type = Column(String)



