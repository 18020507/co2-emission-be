import logging
from fastapi import Depends

from app.api.repository import role_repository
from app.helpers.paging import PaginationParams
from app.schemas.sche_role import CreateRole


async def get_list_role(params: PaginationParams = Depends()):
    logging.info("===> get list role service <===")
    list_role = await role_repository.get_list_role(params)
    return list_role


async def create_role(data: CreateRole):
    logging.info("===> create role service <===")
    role = await role_repository.create_role(data)
    return role
