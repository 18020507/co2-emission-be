import logging
from fastapi import Depends

from app.api.repository import role_repository, company_repository, company_facility_master_data_repository, \
    forklift_master_data_repository, fuel_source_repository, activity_repository
from app.helpers.paging import PaginationParams
from app.schemas.sche_company import CreateCompanyInformation
from app.schemas.sche_create_activity import CreateActivity
from app.schemas.sche_create_company_facility_master_data import CreateCompanyFacilityMasterData
from app.schemas.sche_create_forklift_master_data import CreateForkliftMasterData
from app.schemas.sche_create_fuel_source import CreateFuelSource
from app.schemas.sche_role import CreateRole


async def get_activity(company_id: int):
    logging.info("===> get_activity service <===")
    response = await activity_repository.get_activity(company_id)
    return response


async def create_activity(company_id: int, data: list[CreateActivity]):
    logging.info("===>  create_activity service <===")
    response = await activity_repository.create_activity(company_id, data)
    return response


