import logging
from botocore.exceptions import ClientError
from fastapi import HTTPException, Depends
from fastapi_sqlalchemy import db
from starlette import status

from app.models import Company, CompanyFacilityMasterData, FacilityActivity, TransActivity, TransportationMasterData
from app.schemas.sche_base import DataResponse
from app.schemas.sche_create_trans_data import CreateTransportData


async def get_trans_data_collection(trans_id: str):
    try:
        logging.info("===> get_trans_data_collection repository <===")
        list_trans_id = trans_id.split(',')
        response = []
        for item in list_trans_id:
            response_company_trans_data = db.session.query(TransActivity).filter(
                TransActivity.transportation_master_data_id == int(item)).all()
            response = response + response_company_trans_data
        return DataResponse().success_response(response)
    except ClientError as e:
        logging.error("===> Error facility_data_collection_repository.get_trans_data_collection <===")
        logging.error(e)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=e.response)


async def get_all_trans(company_id: int):
    try:
        logging.info("===> get_trans_data_collection get_all_trans <===")
        response = db.session.query(TransportationMasterData).filter(
            TransportationMasterData.company_id == company_id).all()
        list_trans_id = []
        for item in response:
            list_trans_id.append({'trans_id': item.id})
        return DataResponse().success_response(list_trans_id)

    except ClientError as e:
        logging.error("===> Error facility_data_collection_repository.get_facility_data_collection <===")
        logging.error(e)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=e.response)


async def create_trans_data_collection(data: list[CreateTransportData]):
    try:
        logging.info("===> create_trans_data_collection repository <===")
        for item in data:
            new_trans_data = TransActivity(
                transportation_master_data_id=item.transportation_master_data_id,
                date=item.date,
                client_id=item.client_id,
                fuel_source_id=item.fuel_source_id,
                fuel_amount=item.fuel_amount,
                distance_travel=item.distance_travel,
            )
            db.session.add(new_trans_data)
        db.session.commit()
        return DataResponse().success_response(data)
    except ClientError as e:
        logging.error("===> Error trans_activity.create_trans_data_collection <===")
        logging.error(e)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=e.response)
