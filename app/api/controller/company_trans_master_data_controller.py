import logging

from app.helpers.login_manager import login_required
from app.helpers.paging import PaginationParams
from botocore.exceptions import ClientError
from app.api.service import company_transportation_master_data_service

from fastapi import APIRouter, Depends

from app.schemas.sche_create_company_transportation_master_data import CreateCompanyTransportationMasterData
from config.route import Route

router = APIRouter()


@router.get(Route.V1.GET_TRANSPORTATION_MASTER_DATA, dependencies=[Depends(login_required)])
async def get_company_transportation_master_data(company_id: int):
    logging.info("===>>> company_transportation_master_data_controller.py <<<===")
    logging.info("===>>> function get_company_transportation_master_data <<<===")
    try:
        response = await company_transportation_master_data_service.get_company_transportation_master_data(company_id)
        return response
    except ClientError or Exception as e:
        logging.error("===>>> Error company_facility_master_data_controller.get_company_facility_master_data <<<===")
        logging.error(e)


@router.post(Route.V1.CREATE_TRANSPORTATION_MASTER_DATA, dependencies=[Depends(login_required)])
async def create_company_transportation_master_data(data: list[CreateCompanyTransportationMasterData]):
    logging.info("===>>> company_transportation_master_data_controller.py <<<===")
    logging.info("===>>> function create_company_transportation_master_data <<<===")
    try:
        response = await company_transportation_master_data_service.create_company_transportation_master_data(data)
        return response
    except ClientError or Exception as e:
        logging.error("===>>> Error company_facility_master_data_controller.get_company_facility_master_data <<<===")
        logging.error(e)
