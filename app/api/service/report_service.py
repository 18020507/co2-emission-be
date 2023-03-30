import logging

from app.api.repository import report_repository


async def get_stationary_combustion_report(company_id: int):
    logging.info("===> get_stationary_combustion_report service <===")
    response = await report_repository.get_stationary_combustion_report(company_id)
    return response


async def get_mobile_combustion_report(company_id: int):
    logging.info("===> get_mobile_combustion_report service <===")
    response = await report_repository.get_mobile_combustion_report(company_id)
    return response
