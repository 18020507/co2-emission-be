from pydantic import BaseModel


class CreateActivity(BaseModel):
    activity_type_name: str
