import logging
from botocore.exceptions import ClientError
from fastapi import HTTPException, Depends
from fastapi_sqlalchemy import db
from starlette import status

from app.models import Company, TransActivity, TransportationMasterData, \
    ClientMasterData, FuelSource
from app.schemas.sche_base import DataResponse
from app.schemas.sche_create_trans_data import CreateTransportData, TransActivityDTO


async def get_trans_data_collection(company_id: int, client_name: str, fuel_source_name: str):
    try:
        logging.info("===> get_trans_data_collection repository <===")
        if client_name and fuel_source_name:
            response = db.session.query(TransActivity, TransportationMasterData, FuelSource, ClientMasterData).join(
                TransportationMasterData,
                TransActivity.transportation_master_data_id == TransportationMasterData.id) \
                .join(FuelSource, TransActivity.fuel_source_id == FuelSource.id) \
                .join(ClientMasterData, TransActivity.client_id == ClientMasterData.id).filter(
                TransportationMasterData.company_id == company_id).filter(
                FuelSource.fuel_source_name == fuel_source_name).filter(
                ClientMasterData.client_name == client_name).all()
        elif client_name and not fuel_source_name:
            response = db.session.query(TransActivity, TransportationMasterData, FuelSource, ClientMasterData).join(
                TransportationMasterData,
                TransActivity.transportation_master_data_id == TransportationMasterData.id) \
                .join(FuelSource, TransActivity.fuel_source_id == FuelSource.id) \
                .join(ClientMasterData, TransActivity.client_id == ClientMasterData.id).filter(
                TransportationMasterData.company_id == company_id).filter(
                ClientMasterData.client_name == client_name).all()
        elif not client_name and fuel_source_name:
            response = db.session.query(TransActivity, TransportationMasterData, FuelSource, ClientMasterData).join(
                TransportationMasterData,
                TransActivity.transportation_master_data_id == TransportationMasterData.id) \
                .join(FuelSource, TransActivity.fuel_source_id == FuelSource.id) \
                .join(ClientMasterData, TransActivity.client_id == ClientMasterData.id).filter(
                TransportationMasterData.company_id == company_id).filter(
                ClientMasterData.client_name == client_name).all()
        else:
            response = db.session.query(TransActivity, TransportationMasterData, FuelSource, ClientMasterData).join(
                TransportationMasterData,
                TransActivity.transportation_master_data_id == TransportationMasterData.id) \
                .join(FuelSource, TransActivity.fuel_source_id == FuelSource.id) \
                .join(ClientMasterData, TransActivity.client_id == ClientMasterData.id).filter(
                TransportationMasterData.company_id == company_id).all()
        return_response = []
        for item in response:
            dto = TransActivityDTO(
                company_facility_master_data_id=item[1].id,
                trans_id=item[0].id,
                company_id=item[1].company_id,
                date=item[0].date,
                fuel_source_name=item[2].fuel_source_name,
                client_name=item[3].client_name,
                fuel_amount=item[0].fuel_amount,
                distance_travel=item[0].distance_travel
            )
            return_response.append(dto)

        return DataResponse().success_response(return_response)
    except ClientError as e:
        logging.error("===> Error facility_data_collection_repository.get_trans_data_collection <===")
        logging.error(e)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=e.response)


async def create_trans_data_collection(data: list[CreateTransportData]):
    try:
        logging.info("===> create_trans_data_collection repository <===")
        for item in data:
            # check if the record already exists
            existing_record = db.session.query(TransActivity).filter(
                TransActivity.transportation_master_data_id == item.transportation_master_data_id,
                TransActivity.date == item.date,
                TransActivity.client_id == item.client_id,
                TransActivity.fuel_source_id == item.fuel_source_id,
                TransActivity.fuel_amount == item.fuel_amount,
                TransActivity.distance_travel == item.distance_travel
            ).first()
            if not existing_record:
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
