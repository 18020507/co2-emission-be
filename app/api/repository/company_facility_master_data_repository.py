import logging
from botocore.exceptions import ClientError
from fastapi import HTTPException, Depends
from fastapi_sqlalchemy import db
from starlette import status

from app.models import Company, CompanyFacilityMasterData
from app.schemas.sche_base import DataResponse
from app.helpers.paging import paginate, PaginationParams
from app.schemas.sche_company import CreateCompanyInformation
from app.schemas.sche_create_company_facility_master_data import CreateCompanyFacilityMasterData


async def get_company_facility_master_data(company_id: int):
    try:
        logging.info("===> get company facility master data repository <===")
        response = db.session.query(CompanyFacilityMasterData).filter(
            CompanyFacilityMasterData.company_id == company_id).all()
        return DataResponse().success_response(response)
    except ClientError as e:
        logging.error("===> Error company_facility_master_data_repository.get_company_facility_master_data <===")
        logging.error(e)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=e.response)


async def create_company_facility_master_data(data: list[CreateCompanyFacilityMasterData]):
    try:
        logging.info("===> create create_company_facility_master_data repository <===")
        for item in data:
            new_company_information = CompanyFacilityMasterData(
                company_id=item.company_id,
                facility_address=item.facility_address,
                facility_type=item.facility_type,
                employee_no=item.employee_no,
                forklift_no=item.forklift_no,
            )
            db.session.add(new_company_information)
        db.session.commit()
        return DataResponse().success_response(data)
    except ClientError as e:
        logging.error("===> Error company_repository.create_company_information <===")
        logging.error(e)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=e.response)
