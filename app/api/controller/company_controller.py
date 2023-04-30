import logging

from app.api.controller import auth_controller
from app.helpers.login_manager import login_required
from app.helpers.paging import PaginationParams
from botocore.exceptions import ClientError
from app.api.service import auth_service, role_service, company_service

from fastapi import APIRouter, Depends

from app.schemas.sche_company import CreateCompanyInformation, UpdateCompanyInformation
from config.route import Route

router = APIRouter()


@router.get(Route.V1.GET_LIST_COMPANY_INFORMATION, dependencies=[Depends(login_required)])
async def get_company_information(params: PaginationParams = Depends()):
    logging.info("===>>> company_controller.py <<<===")
    logging.info("===>>> function get_company_information <<<===")
    try:
        response = await company_service.get_company_information(params)
        return response
    except ClientError or Exception as e:
        logging.error("===>>> Error company_controller.get_company_information <<<===")
        logging.error(e)


@router.get(Route.V1.GET_COMPANY_INFORMATION_BY_ID, dependencies=[Depends(login_required)])
async def get_company_information_by_id(company_id: int):
    logging.info("===>>> company_controller.py <<<===")
    logging.info("===>>> function get_company_information_by_id <<<===")
    try:
        response = await company_service.get_company_information_by_id(company_id)
        return response
    except ClientError or Exception as e:
        logging.error("===>>> Error company_controller.get_company_information <<<===")
        logging.error(e)


@router.post(Route.V1.CREATE_COMPANY_INFORMATION, dependencies=[Depends(login_required)])
async def create_company_information(data: CreateCompanyInformation):
    logging.info("===>>> company_controller.py <<<===")
    logging.info("===>>> function create_company_information <<<===")
    try:
        response = await company_service.create_company_information(data)
        return response
    except ClientError or Exception as e:
        logging.error("===>>> Error role_controller.get_list_role <<<===")
        logging.error(e)


@router.put(Route.V1.UPDATE_COMPANY_INFORMATION, dependencies=[Depends(login_required)])
async def update_company_information(data: UpdateCompanyInformation):
    logging.info("===>>> company_controller.py <<<===")
    logging.info("===>>> function update_company_information <<<===")
    try:
        response = await company_service.update_company_information(data)
        return response
    except ClientError or Exception as e:
        logging.error("===>>> Error role_controller.get_list_role <<<===")
        logging.error(e)
