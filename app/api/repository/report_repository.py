import logging
from botocore.exceptions import ClientError
from fastapi import HTTPException
from fastapi_sqlalchemy import db
from starlette import status

from app.models import CompanyFacilityMasterData, FacilityActivity, TransportationMasterData, TransActivity
from app.schemas.sche_base import DataResponse


async def get_stationary_combustion_report(company_id: int):
    try:
        logging.info("===> get_stationary_combustion_report repository <===")
        company_facility_master = db.session.query(CompanyFacilityMasterData).filter(
            CompanyFacilityMasterData.company_id == company_id).all()
        response = []
        for facility in company_facility_master:
            list_facility_activity = db.session.query(FacilityActivity).filter(
                FacilityActivity.company_facility_master_data_id == int(facility.id)).all()
            fuel_amount = 0
            for facility_item in list_facility_activity:
                fuel_amount = fuel_amount + facility_item.fuel_amount
            response.append(
                {'date': 2023, 'facility_id': facility.id, 'amount_of_fuel': fuel_amount, 'units': 'gal', 'co2': 0})
        return DataResponse().success_response(response)
    except ClientError as e:
        logging.error("===> Error fuel_source_repository.get_fuel_source <===")
        logging.error(e)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=e.response)


async def get_mobile_combustion_report(company_id: int):
    try:
        logging.info("===> get_mobile_combustion_report repository <===")
        trans_facility_master = db.session.query(TransportationMasterData).filter(
            TransportationMasterData.company_id == company_id).all()
        response = []
        for trans in trans_facility_master:
            list_trans_activity = db.session.query(TransActivity).filter(
                TransActivity.transportation_master_data_id == int(trans.id)).all()
            fuel_amount = 0
            for trans_item in list_trans_activity:
                fuel_amount = fuel_amount + trans_item.fuel_amount
            response.append(
                {'date': 2023, 'vehicle_id': trans.id, 'amount_of_fuel': fuel_amount, 'units': 'gal', 'co2': 0})
        return DataResponse().success_response(response)
    except ClientError as e:
        logging.error("===> Error fuel_source_repository.get_fuel_source <===")
        logging.error(e)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=e.response)
