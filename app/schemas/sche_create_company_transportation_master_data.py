from pydantic import BaseModel


class CreateCompanyTransportationMasterData(BaseModel):
    company_id: int
    vehicle_type: str
    vehicle_name: str
    vehicle_model: str
    vehicle_year: int
    vehicle_mileage: int
