import logging
from botocore.exceptions import ClientError
from fastapi import HTTPException
from fastapi_sqlalchemy import db
from starlette import status

from app.models import ClientMasterData
from app.schemas.sche_base import DataResponse
from app.schemas.sche_create_client import CreateClient


async def get_client(company_id: int):
    try:
        logging.info("===> get_client repository <===")
        response = db.session.query(ClientMasterData).filter(ClientMasterData.company_id == company_id).all()
        return DataResponse().success_response(response)
    except ClientError as e:
        logging.error("===> Error client_repository.get_client <===")
        logging.error(e)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=e.response)


async def create_client(company_id: int, data: list[CreateClient]):
    try:
        logging.info("===> create_client repository <===")
        for item in data:
            new_client = ClientMasterData(
                company_id=company_id,
                client_name=item.client_name,
            )
            db.session.add(new_client)
        db.session.commit()
        return DataResponse().success_response(data)
    except ClientError as e:
        logging.error("===> Error client_repository.create_client <===")
        logging.error(e)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=e.response)
