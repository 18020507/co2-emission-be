from pydantic import BaseModel


class CreateForkliftMasterData(BaseModel):
    facility_master_data_id: int
    forklift_model: str
    fuel_type: str
    fuel_efficiency: float
    units: str
