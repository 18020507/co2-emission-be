import logging
from fastapi import Depends

from app.api.repository import role_repository, company_repository, company_facility_master_data_repository
from app.helpers.paging import PaginationParams
from app.schemas.sche_company import CreateCompanyInformation
from app.schemas.sche_create_company_facility_master_data import CreateCompanyFacilityMasterData
from app.schemas.sche_role import CreateRole


async def get_company_facility_master_data(company_id: int):
    logging.info("===> get company facility master data service <===")
    response = await company_facility_master_data_repository.get_company_facility_master_data(company_id)
    return response


async def create_company_facility_master_data(data: list[CreateCompanyFacilityMasterData]):
    logging.info("===>  create company_facility_master_data service <===")
    response = await company_facility_master_data_repository.create_company_facility_master_data(data)
    return response


