import logging
from app.helpers.paging import PaginationParams
from botocore.exceptions import ClientError
from app.api.service import auth_service, role_service

from fastapi import APIRouter, Depends

from app.schemas.sche_role import CreateRole
from config.route import Route

router = APIRouter()


@router.get(Route.V1.GET_LIST_ROLE)
async def get_list_role(params: PaginationParams = Depends()):
    logging.info("===>>> role_controller.py <<<===")
    logging.info("===>>> function get_list_role <<<===")
    try:
        response = await role_service.get_list_role(params)
        return response
    except ClientError or Exception as e:
        logging.error("===>>> Error role_controller.get_list_role <<<===")
        logging.error(e)


@router.post(Route.V1.CREATE_ROLE)
async def create_role(data: CreateRole):
    logging.info("===>>> role_controller.py <<<===")
    logging.info("===>>> function create_role <<<===")
    try:
        response = await role_service.create_role(data)
        return response
    except ClientError or Exception as e:
        logging.error("===>>> Error role_controller.create_role <<<===")
        logging.error(e)
