from pydantic import BaseModel


class CreateCompanyFacilityMasterData(BaseModel):
    facility_address: str
    facility_type: str
    employee_no: int
    forklift_no: int
