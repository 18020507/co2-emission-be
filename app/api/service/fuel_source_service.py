import logging

from app.api.repository import fuel_source_repository
from app.schemas.sche_create_fuel_source import CreateFuelSource


async def get_fuel_source(company_id: int):
    logging.info("===> get_fuel_source service <===")
    response = await fuel_source_repository.get_fuel_source(company_id)
    return response


async def create_fuel_source(company_id: int, data: list[CreateFuelSource]):
    logging.info("===>  create_fuel_source service <===")
    response = await fuel_source_repository.create_fuel_source(company_id, data)
    return response
