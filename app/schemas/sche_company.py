from pydantic import BaseModel


class CreateCompanyInformation(BaseModel):
    token_str: str
    legal_name: str
    contact_name: str
    legal_address: str
    contact_email: str
    employer_identification_number: int
    contact_phone_number: str
    company_number_of_facilities: int
    company_sector: str
    company_industry: str
    company_service: str
