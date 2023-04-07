import logging
from botocore.exceptions import ClientError
from fastapi import HTTPException, Depends
from fastapi_sqlalchemy import db
from starlette import status

from app.models import Company, CompanyFacilityMasterData, FolkliftMasterData
from app.schemas.sche_base import DataResponse
from app.helpers.paging import paginate, PaginationParams
from app.schemas.sche_company import CreateCompanyInformation
from app.schemas.sche_create_company_facility_master_data import CreateCompanyFacilityMasterData
from app.schemas.sche_create_forklift_master_data import CreateForkliftMasterData


async def get_forklift_master_data(facility_master_data_id: int):
    try:
        logging.info("===> get_forklift_master_data repository <===")
        response = db.session.query(FolkliftMasterData).filter(
            FolkliftMasterData.facility_master_data_id == facility_master_data_id).all()
        return DataResponse().success_response(response)
    except ClientError as e:
        logging.error("===> Error forklift_master_data_repository.get_forklift_master_data <===")
        logging.error(e)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=e.response)


async def create_forklift_master_data(data: list[CreateForkliftMasterData]):
    try:
        logging.info("===> create_forklift_master_data repository <===")
        for item in data:
            new_forklift_master = FolkliftMasterData(
                facility_master_data_id=item.facility_master_data_id,
                forklift_model=item.forklift_model,
                fuel_type=item.fuel_type,
                fuel_efficiency=item.fuel_efficiency,
                units=item.units,
            )
            db.session.add(new_forklift_master)
        db.session.commit()
        return DataResponse().success_response(data)
    except ClientError as e:
        logging.error("===> Error forklift_master_data_repository.create_forklift_master_data <===")
        logging.error(e)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=e.response)
