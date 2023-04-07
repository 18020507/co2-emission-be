import logging
from fastapi import Depends

from app.api.repository import role_repository, company_repository, company_facility_master_data_repository, \
    forklift_master_data_repository
from app.helpers.paging import PaginationParams
from app.schemas.sche_company import CreateCompanyInformation
from app.schemas.sche_create_company_facility_master_data import CreateCompanyFacilityMasterData
from app.schemas.sche_create_forklift_master_data import CreateForkliftMasterData
from app.schemas.sche_role import CreateRole


async def get_forklift_master_data(facility_master_data_id: int):
    logging.info("===> get_forklift_master_data service <===")
    response = await forklift_master_data_repository.get_forklift_master_data(facility_master_data_id)
    return response


async def create_forklift_master_data(data: list[CreateForkliftMasterData]):
    logging.info("===>  create_forklift_master_data service <===")
    response = await forklift_master_data_repository.create_forklift_master_data(data)
    return response


