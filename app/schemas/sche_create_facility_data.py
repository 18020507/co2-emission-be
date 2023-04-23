from pydantic import BaseModel


class FacilityActivityDTO(BaseModel):
    company_facility_master_data_id: int
    facility_id: int
    company_id: int
    date: str
    fuel_source_name: str
    activity_type_name: str
    fuel_amount: float
    Units: str


class CreateFacilityData(BaseModel):
    company_facility_master_data_id: int
    date: str
    fuel_source_id: str
    activity_type_id: str
    fuel_amount: float
    Units: str
