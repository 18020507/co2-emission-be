from pydantic import BaseModel


class CreateRole(BaseModel):
    role_name: str
    description: str
