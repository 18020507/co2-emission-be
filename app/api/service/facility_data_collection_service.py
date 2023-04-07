import logging

from app.api.repository import facility_data_collection_repository
from app.helpers.paging import PaginationParams
from app.schemas.sche_create_company_facility_master_data import CreateCompanyFacilityMasterData
from app.schemas.sche_create_facility_data import CreateFacilityData


async def get_facility_data_collection(company_id: int, fuel_source_name: str, activity_type_name: str):
    logging.info("===> get facility_data_collection service <===")
    response = await facility_data_collection_repository.get_facility_data_collection(company_id, fuel_source_name,
                                                                                      activity_type_name)
    return response


async def create_facility_data_collection(data: list[CreateFacilityData]):
    logging.info("===>  create company_facility_master_data service <===")
    response = await facility_data_collection_repository.create_facility_data_collection(data)
    return response
