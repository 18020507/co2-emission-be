import logging
from botocore.exceptions import ClientError
from fastapi import HTTPException
from fastapi_sqlalchemy import db
from starlette import status

from app.models import FuelSource
from app.schemas.sche_base import DataResponse
from app.schemas.sche_create_fuel_source import CreateFuelSource


async def get_fuel_source(company_id: int):
    try:
        logging.info("===> get_fuel_source repository <===")
        response = db.session.query(FuelSource).filter(
            FuelSource.company_id == company_id).all()
        return DataResponse().success_response(response)
    except ClientError as e:
        logging.error("===> Error fuel_source_repository.get_fuel_source <===")
        logging.error(e)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=e.response)


async def create_fuel_source(company_id: int, data: list[CreateFuelSource]):
    try:
        logging.info("===> create_fuel_source repository <===")
        for item in data:
            new_fuel_source = FuelSource(
                company_id=company_id,
                fuel_source_name=item.fuel_source_name,
                unit_type=item.unit_type,
            )
            db.session.add(new_fuel_source)
        db.session.commit()
        return DataResponse().success_response(data)
    except ClientError as e:
        logging.error("===> Error fuel_source_repository.create_fuel_source <===")
        logging.error(e)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=e.response)
