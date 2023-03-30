import logging
from datetime import datetime
from typing import Optional

from botocore.exceptions import ClientError
from starlette import status

from app.api.repository import auth_repository
from app.models import User
from app.schemas.sche_base import DataResponse
from app.schemas.sche_user import Login, Register
from app.core.security import create_access_token
from fastapi import HTTPException
from fastapi_sqlalchemy import db


async def login(user: Login):
    logging.info("===>>> auth_service.py <<<===")
    logging.info("===>>> function login <<<===")
    user = auth_repository.UserService().authenticate(email=user.username_id, password=user.password)
    if not user:
        raise HTTPException(status_code=400, detail='Incorrect email or password')

    user.last_login = datetime.now()
    db.session.commit()

    return {
        'access_token': create_access_token(user_id=user.id)
    }


async def register(user: Register, role_id: str, company_id: Optional[str]):
    logging.info("===>>> auth_service.py <<<===")
    logging.info("===>>> function login <<<===")
    try:
        exist_user = db.session.query(User).filter(User.email == user.email).first()
        if exist_user:
            raise Exception('Email already exists')
        auth_repository.UserService().register_user(user, role_id, company_id)
        return {
            'full_name': user.full_name,
            'email': user.email,
        }
    except ClientError or Exception as e:
        logging.error("===>>> Error auth_service.register <<<===")
        logging.error(e)
        raise HTTPException(status_code=status.HTTP_424_FAILED_DEPENDENCY, detail=e.response)


async def change_password(email: str, current_password: str, new_password: str, confirm_new_password: str):
    logging.info("===>>> auth_service.py <<<===")
    logging.info("===>>> function login <<<===")
    try:
        if new_password != confirm_new_password:
            return DataResponse().custom_response("400", "Password mới và confirm password khác nhau", [])
        else:
            return auth_repository.UserService().change_password(email=email,
                                                                 current_password=current_password,
                                                                 new_password=new_password)
    except ClientError or Exception as e:
        logging.error("===>>> Error auth_service.change_password <<<===")
        logging.error(e)
        raise HTTPException(status_code=status.HTTP_424_FAILED_DEPENDENCY, detail=e.response)
