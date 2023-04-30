import logging

from app.helpers.login_manager import login_required
from botocore.exceptions import ClientError
from app.api.service import fuel_source_service

from fastapi import APIRouter, Depends
from app.schemas.sche_create_fuel_source import CreateFuelSource
from config.route import Route

router = APIRouter()


@router.get(Route.V1.GET_FUEL_SOURCE, dependencies=[Depends(login_required)])
async def get_fuel_source(company_id: int):
    logging.info("===>>> fuel_source_controller.py <<<===")
    logging.info("===>>> function get_fuel_source <<<===")
    try:
        response = await fuel_source_service.get_fuel_source(company_id)
        return response
    except ClientError or Exception as e:
        logging.error("===>>> Error fuel_source_controller.get_forklift_master_data <<<===")
        logging.error(e)


@router.post(Route.V1.CREATE_FUEL_SOURCE, dependencies=[Depends(login_required)])
async def create_fuel_source(company_id: int, data: list[CreateFuelSource]):
    logging.info("===>>> fuel_source_controller.py <<<===")
    logging.info("===>>> function create_fuel_source <<<===")
    try:
        response = await fuel_source_service.create_fuel_source(company_id, data)
        return response
    except ClientError or Exception as e:
        logging.error("===>>> Error fuel_source_controller.create_fuel_source <<<===")
        logging.error(e)

