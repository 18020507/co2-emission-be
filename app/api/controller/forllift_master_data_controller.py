import logging

from app.helpers.login_manager import login_required
from app.helpers.paging import PaginationParams
from botocore.exceptions import ClientError
from app.api.service import auth_service, role_service, company_service, company_facility_master_data_service, \
    forklift_master_data_service

from fastapi import APIRouter, Depends

from app.schemas.sche_company import CreateCompanyInformation
from app.schemas.sche_create_company_facility_master_data import CreateCompanyFacilityMasterData
from app.schemas.sche_create_company_transportation_master_data import CreateCompanyTransportationMasterData
from app.schemas.sche_create_forklift_master_data import CreateForkliftMasterData
from config.route import Route

router = APIRouter()


@router.get(Route.V1.GET_FORKLIFT_MASTER_DATA, dependencies=[Depends(login_required)])
async def get_forklift_master_data(facility_master_data_id: int):
    logging.info("===>>> forklift_master_data_controller.py <<<===")
    logging.info("===>>> function get_forklift_master_data <<<===")
    try:
        response = await forklift_master_data_service.get_forklift_master_data(facility_master_data_id)
        return response
    except ClientError or Exception as e:
        logging.error("===>>> Error forklift_master_data_controller.get_forklift_master_data <<<===")
        logging.error(e)


@router.post(Route.V1.CREATE_FORKLIFT_MASTER_DATA, dependencies=[Depends(login_required)])
async def create_forklift_master_data(facility_master_data_id: int, data: list[CreateForkliftMasterData]):
    logging.info("===>>> forklift_master_data_controller.py <<<===")
    logging.info("===>>> function create_forklift_master_data <<<===")
    try:
        response = await forklift_master_data_service.create_forklift_master_data(facility_master_data_id, data)
        return response
    except ClientError or Exception as e:
        logging.error("===>>> Error forklift_master_data_controller.create_forklift_master_data <<<===")
        logging.error(e)

