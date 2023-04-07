import logging
from botocore.exceptions import ClientError
from fastapi import HTTPException, Depends
from fastapi_sqlalchemy import db
from starlette import status

from app.models import Company, CompanyFacilityMasterData, TransportationMasterData
from app.schemas.sche_base import DataResponse
from app.helpers.paging import paginate, PaginationParams
from app.schemas.sche_company import CreateCompanyInformation
from app.schemas.sche_create_company_facility_master_data import CreateCompanyFacilityMasterData
from app.schemas.sche_create_company_transportation_master_data import CreateCompanyTransportationMasterData


async def get_company_transportation_master_data(company_id: int):
    try:
        logging.info("===> get company transportation master data repository <===")
        response = db.session.query(TransportationMasterData).filter(
            TransportationMasterData.company_id == company_id).all()
        return DataResponse().success_response(response)
    except ClientError as e:
        logging.error(
            "===> Error company_transportation_master_data_repository.get_company_transportation_master_data <===")
        logging.error(e)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=e.response)


async def create_company_transportation_master_data(data: list[CreateCompanyTransportationMasterData]):
    try:
        logging.info("===> create create_company_transportation_master_data repository <===")
        for item in data:
            # Check if the record already exists
            existing_record = db.session.query(TransportationMasterData).filter(
                TransportationMasterData.company_id == item.company_id,
                TransportationMasterData.vehicle_type == item.vehicle_type,
                TransportationMasterData.vehicle_name == item.vehicle_name,
                TransportationMasterData.vehicle_model == item.vehicle_model,
                TransportationMasterData.vehicle_year == item.vehicle_year,
                TransportationMasterData.vehicle_mileage == item.vehicle_mileage
            ).first()
            # If the record doesn't exist, add it to the session
            if not existing_record:
                new_transportation_information = TransportationMasterData(
                    company_id=item.company_id,
                    vehicle_type=item.vehicle_type,
                    vehicle_name=item.vehicle_name,
                    vehicle_model=item.vehicle_model,
                    vehicle_year=item.vehicle_year,
                    vehicle_mileage=item.vehicle_mileage,
                )
                db.session.add(new_transportation_information)
        db.session.commit()
        return DataResponse().success_response(data)
    except ClientError as e:
        logging.error("===> Error company_repository.create_company_information <===")
        logging.error(e)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=e.response)
