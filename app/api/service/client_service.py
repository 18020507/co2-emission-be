import logging

from app.api.repository import client_repository
from app.schemas.sche_create_client import CreateClient


async def get_client(company_id: int):
    logging.info("===> get_client service <===")
    response = await client_repository.get_client(company_id)
    return response


async def create_client(company_id: int, data: list[CreateClient]):
    logging.info("===>  create_client service <===")
    response = await client_repository.create_client(company_id, data)
    return response
