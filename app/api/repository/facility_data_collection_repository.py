import logging
from botocore.exceptions import ClientError
from fastapi import HTTPException, Depends
from fastapi_sqlalchemy import db
from starlette import status

from app.models import CompanyFacilityMasterData, FacilityActivity
from app.schemas.sche_base import DataResponse
from app.schemas.sche_create_facility_data import CreateFacilityData


async def get_facility_data_collection(facility_id: str):
    try:
        logging.info("===> get_facility_data_collection repository <===")
        list_facility_id = facility_id.split(',')
        response = []
        for item in list_facility_id:
            response_company_facility_data = db.session.query(FacilityActivity).filter(
                FacilityActivity.company_facility_master_data_id == int(item)).all()
            response = response + response_company_facility_data
        return DataResponse().success_response(response)
    except ClientError as e:
        logging.error("===> Error facility_data_collection_repository.get_facility_data_collection <===")
        logging.error(e)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=e.response)


async def get_all_facility_id(company_id: int):
    try:
        logging.info("===> get_all_facility_id repository <===")
        response = db.session.query(CompanyFacilityMasterData).filter(
            CompanyFacilityMasterData.company_id == company_id).all()
        list_facility_id = []
        for item in response:
            list_facility_id.append({'facility_id': item.id})
        return DataResponse().success_response(list_facility_id)
    except ClientError as e:
        logging.error("===> Error facility_data_collection_repository.get_all_facility_id <===")
        logging.error(e)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=e.response)


async def create_facility_data_collection(data: list[CreateFacilityData]):
    try:
        logging.info("===> create_facility_data_collection repository <===")
        for item in data:
            new_facility_data = FacilityActivity(
                company_facility_master_data_id=item.company_facility_master_data_id,
                date=item.date,
                fuel_source_id=item.fuel_source_id,
                activity_type_id=item.activity_type_id,
                fuel_amount=item.fuel_amount,
                Units=item.Units,
            )
            db.session.add(new_facility_data)
        db.session.commit()
        return DataResponse().success_response(data)
    except ClientError as e:
        logging.error("===> Error facility_activity.create_facility_data_collection <===")
        logging.error(e)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=e.response)
