import logging
from typing import Any, Optional

from botocore.exceptions import ClientError

from app.api.repository import auth_repository
from app.api.service import auth_service

from fastapi import APIRouter, Depends

from app.models import User
from app.schemas.sche_base import DataResponse
from app.schemas.sche_user import Login, Register, ChangePassword, UserDTO
from config.route import Route

router = APIRouter()


@router.post(Route.V1.LOGIN)
async def login(user: Login):
    logging.info("===>>> auth_controller.py <<<===")
    logging.info("===>>> function login <<<===")
    try:
        response = await auth_service.login(user=user)
        return response
    except ClientError or Exception as e:
        logging.error("===>>> Error auth_controller.login <<<===")
        logging.error(e)


@router.post(Route.V1.REGISTER)
async def register(user: Register, role_id: str, company_id: Optional[str] = None):
    logging.info("===>>> auth_controller.py <<<===")
    logging.info("===>>> function register <<<===")
    try:
        response = await auth_service.register(user=user, role_id=role_id, company_id=company_id)
        return response
    except ClientError or Exception as e:
        logging.error("===>>> Error auth_controller.register <<<===")
        logging.error(e)


@router.get(Route.V1.GET_USER_DETAIL)
async def get_user_detail(current_user: UserDTO = Depends(auth_repository.UserService().get_current_user)) -> Any:
    return DataResponse().success_response(data=current_user)


@router.post(Route.V1.CHANGE_PASSWORD)
async def change_password(data: ChangePassword, user: User = Depends(auth_repository.UserService().get_current_user)):
    logging.info("===>>> auth_controller.py <<<===")
    logging.info("===>>> function change password <<<===")
    try:
        response = await auth_service.change_password(user.email, data.current_password, data.new_password,
                                                      data.confirm_new_password)
        return response
    except ClientError or Exception as e:
        logging.error("===>>> Error auth_controller.change_password <<<===")
        logging.error(e)
