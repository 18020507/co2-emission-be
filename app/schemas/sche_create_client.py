from pydantic import BaseModel


class CreateClient(BaseModel):
    client_name: str
