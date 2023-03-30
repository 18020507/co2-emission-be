import logging
from botocore.exceptions import ClientError
from fastapi import HTTPException
from fastapi_sqlalchemy import db
from starlette import status

from app.models import FuelSource, ActivityType
from app.schemas.sche_base import DataResponse
from app.schemas.sche_create_activity import CreateActivity


async def get_activity(company_id: int):
    try:
        logging.info("===> get_activity repository <===")
        response = db.session.query(ActivityType).filter(
            ActivityType.company_id == company_id).all()
        return DataResponse().success_response(response)
    except ClientError as e:
        logging.error("===> Error activity_repository.get_activity <===")
        logging.error(e)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=e.response)


async def create_activity(company_id: int, data: list[CreateActivity]):
    try:
        logging.info("===> create_activity repository <===")
        for item in data:
            new_activity = ActivityType(
                activity_type_name=item.activity_type_name,
                company_id=company_id,
            )
            db.session.add(new_activity)
        db.session.commit()
        return DataResponse().success_response(data)
    except ClientError as e:
        logging.error("===> Error activity_repository.create_activity <===")
        logging.error(e)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=e.response)
