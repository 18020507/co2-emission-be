import logging

import jwt
from fastapi import Depends
from fastapi.security import HTTPBearer

from app.api.repository import role_repository, company_repository, auth_repository
from app.core.config import settings
from app.helpers.paging import PaginationParams
from app.models import User
from app.schemas.sche_company import CreateCompanyInformation
from app.schemas.sche_role import CreateRole
from app.schemas.sche_token import TokenPayload
from app.schemas.sche_user import UserDTO

reusable_oauth2 = HTTPBearer(
    scheme_name='Authorization'
)


async def get_company_information(params: PaginationParams = Depends()):
    logging.info("===> get company information service <===")
    response = await company_repository.get_company_information(params)
    return response


async def create_company_information(data: CreateCompanyInformation):
    logging.info("===> create company service <===")
    user_id = auth_repository.UserService().get_user_id_from_token(data.token_str)
    response = await company_repository.create_company_information(data, user_id)
    return response
