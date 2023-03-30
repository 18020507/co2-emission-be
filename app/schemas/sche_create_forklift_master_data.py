from pydantic import BaseModel


class CreateForkliftMasterData(BaseModel):
    forklift_model: str
    fuel_type: str
    fuel_efficiency: float
    units: str
