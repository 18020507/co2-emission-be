import logging

from app.api.repository import dashboard_repository


async def get_dashboard_data(company_id: int):
    logging.info("===> get_dashboard_data service <===")
    response = await dashboard_repository.get_dashboard_data(company_id)
    return response


async def get_dashboard_chart_data(company_id: int):
    logging.info("===> get_dashboard_chart_data service <===")
    response = await dashboard_repository.get_dashboard_chart_data(company_id)
    return response

