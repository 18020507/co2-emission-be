import logging
from botocore.exceptions import ClientError
from fastapi import HTTPException, Depends
from fastapi_sqlalchemy import db
from starlette import status

from app.models import CompanyFacilityMasterData, FacilityActivity, FuelSource, ActivityType
from app.schemas.sche_base import DataResponse
from app.schemas.sche_create_facility_data import CreateFacilityData, FacilityActivityDTO


async def get_facility_data_collection(company_id: int, fuel_source_name: str, activity_type_name: str):
    try:
        logging.info("===> get_facility_data_collection repository <===")
        if fuel_source_name and activity_type_name:
            response = db.session.query(FacilityActivity, CompanyFacilityMasterData, FuelSource, ActivityType).join(
                CompanyFacilityMasterData,
                FacilityActivity.company_facility_master_data_id == CompanyFacilityMasterData.id) \
                .join(FuelSource, FacilityActivity.fuel_source_id == FuelSource.id) \
                .join(ActivityType, FacilityActivity.activity_type_id == ActivityType.id).filter(
                CompanyFacilityMasterData.company_id == company_id).filter(
                FuelSource.fuel_source_name == fuel_source_name).filter(
                ActivityType.activity_type_name == activity_type_name).all()
        elif fuel_source_name and not activity_type_name:
            response = db.session.query(FacilityActivity, CompanyFacilityMasterData, FuelSource, ActivityType).join(
                CompanyFacilityMasterData,
                FacilityActivity.company_facility_master_data_id == CompanyFacilityMasterData.id) \
                .join(FuelSource, FacilityActivity.fuel_source_id == FuelSource.id) \
                .join(ActivityType, FacilityActivity.activity_type_id == ActivityType.id).filter(
                CompanyFacilityMasterData.company_id == company_id).filter(
                FuelSource.fuel_source_name == fuel_source_name).all()
        elif activity_type_name and not fuel_source_name:
            response = db.session.query(FacilityActivity, CompanyFacilityMasterData, FuelSource, ActivityType).join(
                CompanyFacilityMasterData,
                FacilityActivity.company_facility_master_data_id == CompanyFacilityMasterData.id) \
                .join(FuelSource, FacilityActivity.fuel_source_id == FuelSource.id) \
                .join(ActivityType, FacilityActivity.activity_type_id == ActivityType.id).filter(
                CompanyFacilityMasterData.company_id == company_id).filter(
                ActivityType.activity_type_name == activity_type_name).all()
        else:
            response = db.session.query(FacilityActivity, CompanyFacilityMasterData, FuelSource, ActivityType).join(
                CompanyFacilityMasterData,
                FacilityActivity.company_facility_master_data_id == CompanyFacilityMasterData.id) \
                .join(FuelSource, FacilityActivity.fuel_source_id == FuelSource.id) \
                .join(ActivityType, FacilityActivity.activity_type_id == ActivityType.id).filter(
                CompanyFacilityMasterData.company_id == company_id).all()
        return_response = []
        for item in response:
            dto = FacilityActivityDTO(
                company_facility_master_data_id=item[1].id,
                facility_id=item[0].id,
                company_id=item[1].company_id,
                date=item[0].date,
                fuel_source_name=item[2].fuel_source_name,
                activity_type_name=item[3].activity_type_name,
                fuel_amount=item[0].fuel_amount,
                Units=item[0].Units
            )
            return_response.append(dto)

        return DataResponse().success_response(return_response)
    except ClientError as e:
        logging.error("===> Error facility_data_collection_repository.get_facility_data_collection <===")
        logging.error(e)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=e.response)


async def create_facility_data_collection(data: list[CreateFacilityData]):
    try:
        logging.info("===> create_facility_data_collection repository <===")
        for item in data:
            # check if data is true
            new_fuel_source_id_type = convert_to_int(item.fuel_source_id)
            new_activity_type_id_type = convert_to_int(item.activity_type_id)
            if new_fuel_source_id_type and new_activity_type_id_type is not None:
                # check if the record already exists
                existing_record = db.session.query(FacilityActivity).filter(
                    FacilityActivity.company_facility_master_data_id == item.company_facility_master_data_id,
                    FacilityActivity.date == item.date,
                    FacilityActivity.fuel_source_id == item.fuel_source_id,
                    FacilityActivity.activity_type_id == item.activity_type_id,
                    FacilityActivity.fuel_amount == item.fuel_amount,
                    FacilityActivity.Units == item.Units
                ).first()
                if not existing_record:
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


def convert_to_int(data):
    try:
        return int(data)
    except ValueError:
        return None
