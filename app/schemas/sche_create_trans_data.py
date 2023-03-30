from pydantic import BaseModel


class CreateTransportData(BaseModel):
    transportation_master_data_id: int
    client_id: int
    date: str
    fuel_source_id: int
    fuel_amount: float
    distance_travel: int
