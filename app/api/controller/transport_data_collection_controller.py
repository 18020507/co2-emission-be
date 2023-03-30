import logging

from app.helpers.login_manager import login_required
from app.helpers.paging import PaginationParams
from botocore.exceptions import ClientError
from app.api.service import company_transportation_master_data_service, facility_data_collection_service, \
    transport_data_collection_service

from fastapi import APIRouter, Depends

from app.schemas.sche_create_company_transportation_master_data import CreateCompanyTransportationMasterData
from app.schemas.sche_create_facility_data import CreateFacilityData
from app.schemas.sche_create_trans_data import CreateTransportData
from config.route import Route

router = APIRouter()


@router.get(Route.V1.GET_TRANSPORTATION_DATA_COLLECTION, dependencies=[Depends(login_required)])
async def get_transport_data_collection(trans_id: str):
    logging.info("===>>> transport_data_collection_controller.py <<<===")
    logging.info("===>>> function get_transport_data_collection <<<===")
    try:
        response = await transport_data_collection_service.get_trans_data_collection(trans_id)
        return response
    except ClientError or Exception as e:
        logging.error("===>>> Error company_facility_master_data_controller.get_company_facility_master_data <<<===")
        logging.error(e)


@router.get(Route.V1.GET_ALL_TRANSPORTATION_IN_COMPANY, dependencies=[Depends(login_required)])
async def get_all_transport(company_id: int):
    logging.info("===>>> transport_data_collection_controller.py <<<===")
    logging.info("===>>> function get_transport_data_collection <<<===")
    try:
        response = await transport_data_collection_service.get_all_trans(company_id)
        return response
    except ClientError or Exception as e:
        logging.error(
            "===>>> Error company_facility_master_data_controller.get_company_facility_master_data <<<===")
        logging.error(e)


@router.post(Route.V1.CREATE_TRANSPORTATION_DATA_COLLECTION, dependencies=[Depends(login_required)])
async def create_transport_data_collection(data: list[CreateTransportData]):
    logging.info("===>>> transport_data_collection_controller.py <<<===")
    logging.info("===>>> function create_transport_data_collection <<<===")
    try:
        response = await transport_data_collection_service.create_trans_data_collection(data)
        return response
    except ClientError or Exception as e:
        logging.error("===>>> Error trans_data_controller.create_facility_data_collection <<<===")
        logging.error(e)
