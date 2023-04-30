import logging

from app.api.service import client_service
from app.helpers.login_manager import login_required
from botocore.exceptions import ClientError

from fastapi import APIRouter, Depends

from app.schemas.sche_create_client import CreateClient
from config.route import Route

router = APIRouter()


@router.get(Route.V1.GET_CLIENT, dependencies=[Depends(login_required)])
async def get_client(company_id: int):
    logging.info("===>>> client_controller.py <<<===")
    logging.info("===>>> function get_client <<<===")
    try:
        response = await client_service.get_client(company_id)
        return response
    except ClientError or Exception as e:
        logging.error("===>>> Error client_controller.get_client <<<===")
        logging.error(e)


@router.post(Route.V1.CREATE_CLIENT, dependencies=[Depends(login_required)])
async def create_client(company_id: int, data: list[CreateClient]):
    logging.info("===>>> client_controller.py <<<===")
    logging.info("===>>> function create_fuel_source <<<===")
    try:
        response = await client_service.create_client(company_id, data)
        return response
    except ClientError or Exception as e:
        logging.error("===>>> Error client_controller.create_client <<<===")
        logging.error(e)

