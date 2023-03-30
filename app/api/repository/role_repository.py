import logging
import uuid
from botocore.exceptions import ClientError
from fastapi import HTTPException, Depends
from fastapi_sqlalchemy import db
from starlette import status

from app.models.model_role import Role
from app.schemas.sche_base import DataResponse
from app.helpers.paging import paginate, PaginationParams
from app.schemas.sche_role import CreateRole


async def get_list_role(params: PaginationParams = Depends()):
    try:
        logging.info("===> get list role repository <===")
        _query = db.session.query(Role)
        list_role = paginate(model=Role, query=_query, params=params)
        return list_role
    except ClientError as e:
        logging.error("===> Error role_repository.get_list_role <===")
        logging.error(e)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=e.response)


async def create_role(data: CreateRole):
    try:
        logging.info("===> create role repository <===")
        new_role = Role(
            role_name=data.role_name,
            description=data.description,
        )
        db.session.add(new_role)
        db.session.commit()
        return DataResponse().success_response(data)
    except ClientError as e:
        logging.error("===> Error role_repository.create_role <===")
        logging.error(e)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=e.response)
