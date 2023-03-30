import logging

from app.api.repository import facility_data_collection_repository
from app.helpers.paging import PaginationParams
from app.schemas.sche_create_company_facility_master_data import CreateCompanyFacilityMasterData
from app.schemas.sche_create_facility_data import CreateFacilityData


async def get_facility_data_collection(facility_id: str):
    logging.info("===> get facility_data_collection service <===")
    response = await facility_data_collection_repository.get_facility_data_collection(facility_id)
    return response


async def get_all_facility_id(company_id: int):
    logging.info("===> get_all_facility_id service <===")
    response = await facility_data_collection_repository.get_all_facility_id(company_id)
    return response


async def create_facility_data_collection(data: list[CreateFacilityData]):
    logging.info("===>  create company_facility_master_data service <===")
    response = await facility_data_collection_repository.create_facility_data_collection(data)
    return response
