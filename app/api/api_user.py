import logging
from typing import Any

from fastapi import APIRouter, Depends, HTTPException
from fastapi_sqlalchemy import db

from app.helpers.exception_handler import CustomException
from app.helpers.login_manager import permission_required
from app.helpers.paging import Page, PaginationParams, paginate
from app.schemas.sche_base import DataResponse
from app.schemas.sche_user import UserItemResponse, UserCreateRequest, UserUpdateMeRequest
from app.services.srv_user import UserService
from app.models import User

logger = logging.getLogger()
router = APIRouter()


@router.get("", response_model=Page[UserItemResponse])
@permission_required('admin', 'guest')
def get(params: PaginationParams = Depends(), current_user: User = Depends(UserService().get_current_user)) -> Any:
    """
    API Get list User
    """
    try:
        _query = db.session.query(User)
        users = paginate(model=User, query=_query, params=params)
        return users
    except Exception as e:
        return HTTPException(status_code=400, detail=logger.error(e))


@router.post("", response_model=DataResponse[UserItemResponse])
@permission_required('admin')
def create(user_data: UserCreateRequest = Depends(),
           current_user: User = Depends(UserService().get_current_user)) -> Any:
    """
    API Create User
    """
    try:
        exist_user = db.session.query(User).filter(User.email == user_data.email).first()
        if exist_user:
            raise Exception('Email already exists')
        new_user = UserService().create_user(user_data)
        return DataResponse().success_response(data=new_user)
    except Exception as e:
        raise CustomException(http_code=400, code='400', message=str(e))


@router.get("/me", response_model=DataResponse[UserItemResponse])
def detail(current_user: User = Depends(UserService().get_current_user)) -> Any:
    """
    API get current User
    """
    return DataResponse().success_response(data=current_user)


@router.put("/me", response_model=DataResponse[UserItemResponse])
def create(user_data: UserUpdateMeRequest = Depends(),
           current_user: User = Depends(UserService().get_current_user)) -> Any:
    """
    API Create User
    """
    try:
        if user_data.email is not None:
            exist_user = db.session.query(User).filter(
                User.email == user_data.email, User.id != current_user.id).first()
            if exist_user:
                raise Exception('Email already exists')
        updated_user = UserService().update_me(data=user_data, current_user=current_user)
        return DataResponse().success_response(data=updated_user)
    except Exception as e:
        raise CustomException(http_code=400, code='400', message=str(e))
