import logging

from app.api.repository import facility_data_collection_repository, transport_data_collection_repository
from app.helpers.paging import PaginationParams
from app.schemas.sche_create_company_facility_master_data import CreateCompanyFacilityMasterData
from app.schemas.sche_create_facility_data import CreateFacilityData
from app.schemas.sche_create_trans_data import CreateTransportData


async def get_trans_data_collection(company_id: int, client_name: str, fuel_source_name: str):
    logging.info("===> get get_trans_data_collection service <===")
    response = await transport_data_collection_repository.get_trans_data_collection(company_id, client_name,
                                                                                    fuel_source_name)
    return response


async def create_trans_data_collection(data: list[CreateTransportData]):
    logging.info("===>  create trans_data_collection service <===")
    response = await transport_data_collection_repository.create_trans_data_collection(data)
    return response
