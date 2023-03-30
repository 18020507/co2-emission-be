from pydantic import BaseModel


class CreateFacilityData(BaseModel):
    company_facility_master_data_id: int
    date: str
    fuel_source_id: int
    activity_type_id: int
    fuel_amount: float
    Units: str
