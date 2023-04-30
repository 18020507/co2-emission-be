from datetime import datetime
import logging
from botocore.exceptions import ClientError
from fastapi import HTTPException, Depends
from fastapi_sqlalchemy import db
from starlette import status

from app.models import Company, CompanyFacilityMasterData, TransportationMasterData, FuelSource
from app.models.model_role import Role
from app.schemas.sche_base import DataResponse
from app.helpers.paging import paginate, PaginationParams
from app.schemas.sche_company import CreateCompanyInformation, UpdateCompanyInformation
from app.schemas.sche_role import CreateRole


async def get_company_information(params: PaginationParams = Depends()):
    try:
        logging.info("===> get company information repository <===")
        _query = db.session.query(Company)
        company_information = paginate(model=Company, query=_query, params=params)
        return company_information
    except ClientError as e:
        logging.error("===> Error company_repository.get_company_information <===")
        logging.error(e)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=e.response)


async def get_company_information_by_id(company_id: int):
    try:
        logging.info("===> get company information repository <===")
        response = db.session.query(Company).filter(Company.id == company_id).all()
        return DataResponse().success_response(response)
    except ClientError as e:
        logging.error("===> Error company_repository.get_company_information_by_id <===")
        logging.error(e)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=e.response)


async def create_company_information(data: CreateCompanyInformation, user_id: int):
    try:
        logging.info("===> create role repository <===")
        new_company_information = Company(
            legal_name=data.legal_name,
            contact_name=data.contact_name,
            legal_address=data.legal_address,
            contact_email=data.contact_email,
            employer_identification_number=data.employer_identification_number,
            contact_phone_number=data.contact_phone_number,
            company_number_of_facilities=data.company_number_of_facilities,
            company_sector=data.company_sector,
            company_industry=data.company_industry,
            company_service=data.company_service,
            created_by=user_id
        )

        db.session.add(new_company_information)
        db.session.commit()

        return DataResponse().success_response(data)
    except ClientError as e:
        logging.error("===> Error company_repository.create_company_information <===")
        logging.error(e)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=e.response)


async def update_company_information(data: UpdateCompanyInformation):
    try:
        logging.info("===> update company repository <===")
        current_time = datetime.now()
        current_company = db.session.query(Company).get(data.company_id)
        if current_company is None:
            raise Exception('Company not exist')
        current_company.legal_name = current_company.legal_name if data.legal_name is None else data.legal_name
        current_company.contact_name = current_company.contact_name if data.contact_name is None else data.contact_name
        current_company.legal_address = current_company.legal_address if data.legal_address is None else data.legal_address
        current_company.contact_email = current_company.contact_email if data.contact_email is None else data.contact_email
        current_company.employer_identification_number = current_company.employer_identification_number if data.employer_identification_number is None else data.employer_identification_number
        current_company.contact_phone_number = current_company.contact_phone_number if data.contact_phone_number is None else data.contact_phone_number
        current_company.company_number_of_facilities = current_company.company_number_of_facilities if data.company_number_of_facilities is None else data.company_number_of_facilities
        current_company.company_sector = current_company.company_sector if data.company_sector is None else data.company_sector
        current_company.company_service = current_company.company_service if data.company_service is None else data.company_service
        current_company.updated_at = current_time
        db.session.commit()

        return DataResponse().success_response(data)
    except ClientError as e:
        logging.error("===> Error company_repository.update_company_information <===")
        logging.error(e)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=e.response)
