import logging

from app.helpers.login_manager import login_required
from botocore.exceptions import ClientError
from app.api.service import facility_data_collection_service

from fastapi import APIRouter, Depends

from app.schemas.sche_create_facility_data import CreateFacilityData
from config.route import Route

router = APIRouter()


@router.get(Route.V1.GET_FACILITY_DATA_COLLECTION, dependencies=[Depends(login_required)])
async def get_facility_data_collection(facility_id: str):
    logging.info("===>>> facility_data_collection_controller.py <<<===")
    logging.info("===>>> function get_facility_data_collection <<<===")
    try:
        response = await facility_data_collection_service.get_facility_data_collection(facility_id)
        return response
    except ClientError or Exception as e:
        logging.error("===>>> Error company_facility_master_data_controller.get_company_facility_master_data <<<===")
        logging.error(e)


@router.get(Route.V1.GET_ALL_FACILITY_IN_COMPANY, dependencies=[Depends(login_required)])
async def get_all_facility_id(company_id: int):
    logging.info("===>>> facility_data_collection_controller.py <<<===")
    logging.info("===>>> function get_all_facility_id <<<===")
    try:
        response = await facility_data_collection_service.get_all_facility_id(company_id)
        return response
    except ClientError or Exception as e:
        logging.error("===>>> Error company_facility_master_data_controller.get_company_facility_master_data <<<===")
        logging.error(e)


@router.post(Route.V1.CREATE_FACILITY_DATA_COLLECTION, dependencies=[Depends(login_required)])
async def create_facility_data_collection(data: list[CreateFacilityData]):
    logging.info("===>>> facility_data_collection_controller.py <<<===")
    logging.info("===>>> function create_facility_data_collection <<<===")
    try:
        response = await facility_data_collection_service.create_facility_data_collection(data)
        return response
    except ClientError or Exception as e:
        logging.error("===>>> Error facility_data_controller.create_facility_data_collection <<<===")
        logging.error(e)
