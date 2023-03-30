from sqlalchemy import Column, String, Boolean, DateTime, ForeignKey, Integer

from app.models.model_base import BareBaseModel


class ActivityType(BareBaseModel):
    __tablename__ = "activity_type"
    activity_type_name = Column(String)
    company_id = Column(Integer, ForeignKey('companies.id'))



