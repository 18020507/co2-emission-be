import logging

from app.helpers.login_manager import login_required
from botocore.exceptions import ClientError
from app.api.service import dashboard_service

from fastapi import APIRouter, Depends

from config.route import Route

router = APIRouter()


@router.get(Route.V1.GET_DASHBOARD_DATA, dependencies=[Depends(login_required)])
async def get_dashboard_data(company_id: int):
    logging.info("===>>> dashboard_controller <<<===")
    logging.info("===>>> function get_dashboard_data <<<===")
    try:
        response = await dashboard_service.get_dashboard_data(company_id)
        return response
    except ClientError or Exception as e:
        logging.error("===>>> Error dashboard_controller.get_dashboard_data <<<===")
        logging.error(e)


@router.get(Route.V1.GET_DASHBOARD_CHART_DATA, dependencies=[Depends(login_required)])
async def get_dashboard_chart_data(company_id: int):
    logging.info("===>>> dashboard_controller <<<===")
    logging.info("===>>> function get_dashboard_chart_data <<<===")
    try:
        response = await dashboard_service.get_dashboard_chart_data(company_id)
        return response
    except ClientError or Exception as e:
        logging.error("===>>> Error dashboard_controller.get_dashboard_chart_data <<<===")
        logging.error(e)
