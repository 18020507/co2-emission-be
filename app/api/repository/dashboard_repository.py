import logging
from botocore.exceptions import ClientError
from fastapi import HTTPException, Depends
from fastapi_sqlalchemy import db
from starlette import status

from app.models import CompanyFacilityMasterData, FacilityActivity, FuelSource
from app.schemas.sche_base import DataResponse
from app.schemas.sche_dashboard import DashboardDTO, DashboardChartDTO


async def get_dashboard_data(company_id: int):
    try:
        logging.info("===> get_dashboard_data repository <===")
        total_gas = await get_dashboard_item_data(company_id, "natural_gas")
        total_propane = await get_dashboard_item_data(company_id, "propane")
        total_electricity = await get_dashboard_item_data(company_id, "electricity")
        total_diesel = await get_dashboard_item_data(company_id, "diesel")
        total = total_gas + total_diesel + total_electricity + total_propane
        dto = DashboardDTO(
            gas=total_gas,
            diesel=total_diesel,
            propane=total_propane,
            electricity=total_electricity,
            total=total
        )

        return DataResponse().success_response(dto)
    except ClientError as e:
        logging.error("===> Error dashboard_repository.get_dashboard_data <===")
        logging.error(e)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=e.response)


async def get_dashboard_chart_data(company_id: int):
    try:
        logging.info("===> get_dashboard_chart_data repository <===")
        response_gas_line = await get_dashboard_chart_item_data(company_id, "natural_gas")
        response_propane_line = await get_dashboard_chart_item_data(company_id, "propane")
        response_diesel_line = await get_dashboard_chart_item_data(company_id, "diesel")
        response_electricity_line = await get_dashboard_chart_item_data(company_id, "electricity")
        dto = DashboardChartDTO(
            chart_gas=response_gas_line,
            chart_diesel=response_diesel_line,
            chart_propane=response_propane_line,
            chart_electricity=response_electricity_line,
        )
        return DataResponse().success_response(dto)
    except ClientError as e:
        logging.error("===> Error dashboard_repository.get_dashboard_data <===")
        logging.error(e)
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=e.response)


async def get_dashboard_chart_item_data(company_id: int, fuel_source_name: str):
    data = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    response = db.session.query(FacilityActivity, CompanyFacilityMasterData, FuelSource).join(
        CompanyFacilityMasterData,
        FacilityActivity.company_facility_master_data_id == CompanyFacilityMasterData.id). \
        join(FuelSource, FacilityActivity.fuel_source_id == FuelSource.id).filter(
        CompanyFacilityMasterData.company_id == company_id).filter(
        FuelSource.fuel_source_name == fuel_source_name).all()
    for item in response:
        date = item[0].date
        month = int(date.split('/')[0])
        data[month-1] = data[month-1] + item[0].fuel_amount
    return data


async def get_dashboard_item_data(company_id: int, fuel_source_name: str):
    total = 0
    response = db.session.query(FacilityActivity, CompanyFacilityMasterData, FuelSource).join(
        CompanyFacilityMasterData,
        FacilityActivity.company_facility_master_data_id == CompanyFacilityMasterData.id). \
        join(FuelSource, FacilityActivity.fuel_source_id == FuelSource.id).filter(
        CompanyFacilityMasterData.company_id == company_id).filter(
        FuelSource.fuel_source_name == fuel_source_name).all()
    for item in response:
        total = total + item[0].fuel_amount
    return total
