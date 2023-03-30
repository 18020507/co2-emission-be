import logging

from app.helpers.login_manager import login_required
from app.helpers.paging import PaginationParams
from botocore.exceptions import ClientError
from app.api.service import auth_service, role_service, company_service, company_facility_master_data_service, \
    forklift_master_data_service, fuel_source_service, activity_service, report_service

from fastapi import APIRouter, Depends

from app.schemas.sche_company import CreateCompanyInformation
from app.schemas.sche_create_activity import CreateActivity
from app.schemas.sche_create_company_facility_master_data import CreateCompanyFacilityMasterData
from app.schemas.sche_create_company_transportation_master_data import CreateCompanyTransportationMasterData
from app.schemas.sche_create_forklift_master_data import CreateForkliftMasterData
from config.route import Route

router = APIRouter()


@router.get(Route.V1.GET_SUMMARY_REPORT, dependencies=[Depends(login_required)])
async def get_summary_report(company_id: int):
    logging.info("===>>> activity_controller.py <<<===")
    logging.info("===>>> function get_activity <<<===")
    try:
        response = await activity_service.get_activity(company_id)
        return response
    except ClientError or Exception as e:
        logging.error("===>>> Error activity_controller.get_activity <<<===")
        logging.error(e)


@router.get(Route.V1.GET_STATIONARY_COMBUSTION_REPORT, dependencies=[Depends(login_required)])
async def get_stationary_combustion_report(company_id: int):
    logging.info("===>>> report_controller.py <<<===")
    logging.info("===>>> function get_stationary_combustion_report <<<===")
    try:
        response = await report_service.get_stationary_combustion_report(company_id)
        return response
    except ClientError or Exception as e:
        logging.error("===>>> Error report_controller.get_stationary_combustion_report <<<===")
        logging.error(e)


@router.get(Route.V1.GET_MOBILE_COMBUSTION_REPORT, dependencies=[Depends(login_required)])
async def get_mobile_combustion_report(company_id: int):
    logging.info("===>>> report_controller.py <<<===")
    logging.info("===>>> function get_mobile_combustion_report <<<===")
    try:
        response = await report_service.get_mobile_combustion_report(company_id)
        return response
    except ClientError or Exception as e:
        logging.error("===>>> Error report_controller.get_stationary_combustion_report <<<===")
        logging.error(e)
