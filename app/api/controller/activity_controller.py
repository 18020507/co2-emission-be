import logging

from app.helpers.login_manager import login_required
from app.helpers.paging import PaginationParams
from botocore.exceptions import ClientError
from app.api.service import auth_service, role_service, company_service, company_facility_master_data_service, \
    forklift_master_data_service, fuel_source_service, activity_service

from fastapi import APIRouter, Depends

from app.schemas.sche_company import CreateCompanyInformation
from app.schemas.sche_create_activity import CreateActivity
from app.schemas.sche_create_company_facility_master_data import CreateCompanyFacilityMasterData
from app.schemas.sche_create_company_transportation_master_data import CreateCompanyTransportationMasterData
from app.schemas.sche_create_forklift_master_data import CreateForkliftMasterData
from config.route import Route

router = APIRouter()


@router.get(Route.V1.GET_ACTIVITY, dependencies=[Depends(login_required)])
async def get_activity(company_id: int):
    logging.info("===>>> activity_controller.py <<<===")
    logging.info("===>>> function get_activity <<<===")
    try:
        response = await activity_service.get_activity(company_id)
        return response
    except ClientError or Exception as e:
        logging.error("===>>> Error activity_controller.get_activity <<<===")
        logging.error(e)


@router.post(Route.V1.CREATE_ACTIVITY, dependencies=[Depends(login_required)])
async def create_activity(company_id: int, data: list[CreateActivity]):
    logging.info("===>>> activity_controller.py <<<===")
    logging.info("===>>> function create_activity <<<===")
    try:
        response = await activity_service.create_activity(company_id, data)
        return response
    except ClientError or Exception as e:
        logging.error("===>>> Error fuel_source_controller.create_fuel_source <<<===")
        logging.error(e)

