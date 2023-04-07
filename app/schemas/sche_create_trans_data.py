from pydantic import BaseModel


class CreateTransportData(BaseModel):
    transportation_master_data_id: int
    client_id: int
    date: str
    fuel_source_id: int
    fuel_amount: float
    distance_travel: int


class TransActivityDTO(BaseModel):
    company_facility_master_data_id: int
    trans_id: int
    company_id: int
    date: str
    fuel_source_name: str
    client_name: str
    fuel_amount: float
    distance_travel: int
