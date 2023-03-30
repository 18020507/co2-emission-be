import logging
import uuid
from botocore.exceptions import ClientError
from fastapi import HTTPException, Depends
from fastapi_sqlalchemy import db
from starlette import status

from app.models import Company, CompanyFacilityMasterData, TransportationMasterData, FuelSource
from app.models.model_role import Role
from app.schemas.sche_base import DataResponse
from app.helpers.paging import paginate, PaginationParams
from app.schemas.sche_company import CreateCompanyInformation
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

        # new_company_facility_master_data = CompanyFacilityMasterData(
        #     company_id=Company.id,
        #     facility_address="",
        #     facility_type="",
        #     employee_no="",
        #     forklift_no=0,
        # )
        # db.session.add(new_company_facility_master_data)
        # db.session.commit()
        #
        # new_transport_master_data = TransportationMasterData(
        #     company_id=Company.id,
        #     vehicle_type="",
        #     vehicle_name="",
        #     vehicle_model="",
        #     vehicle_year=0,
        #     vehicle_mileage=0,
        #     vehicle_fuel_source_id=0,
        # )
        #
        # new_fuel_source = FuelSource(
        #     company_id=Company.id,
        #     fuel_source_name="",
        #     unit_type=""
        # )
        #
        # db.session.add(new_transport_master_data)
        # db.session.commit()
        return DataResponse().success_response(data)
    except ClientError as e:
        logging.error("===> Error company_repository.create_company_information <===")
        logging.error(e)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=e.response)