from pydantic import BaseModel


class CreateFuelSource(BaseModel):
    fuel_source_name: str
    unit_type: str
