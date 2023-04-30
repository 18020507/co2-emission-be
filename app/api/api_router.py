from fastapi import APIRouter

from app.api.controller import auth_controller, api_healthcheck, role_controller, company_controller, \
    company_facility_master_data_controller, company_trans_master_data_controller, facility_data_collection_controller, \
    transport_data_collection_controller, forllift_master_data_controller, fuel_source_controller, activity_controller, \
    report_controller, dashboard_controller, client_controller
from config.route import Route

router = APIRouter()

router.include_router(api_healthcheck.router, tags=["health-check"], prefix="/healthcheck")

router.include_router(auth_controller.router, prefix=Route.V1.prefix_api, tags=["Auth"],
                      responses={404: {"description": "Not found"}})

router.include_router(role_controller.router, prefix=Route.V1.prefix_api, tags=["Role"],
                      responses={404: {"description": "Not found"}})

router.include_router(company_controller.router, prefix=Route.V1.prefix_api, tags=["Company"],
                      responses={404: {"description": "Not found"}})

router.include_router(company_facility_master_data_controller.router, prefix=Route.V1.prefix_api,
                      tags=["Company Facility Master Data"], responses={404: {"description": "Not found"}})

router.include_router(forllift_master_data_controller.router, prefix=Route.V1.prefix_api,
                      tags=["Forklift Master Data"], responses={404: {"description": "Not found"}})

router.include_router(company_trans_master_data_controller.router, prefix=Route.V1.prefix_api,
                      tags=["Company Transportation Master Data"], responses={404: {"description": "Not found"}})

router.include_router(facility_data_collection_controller.router, prefix=Route.V1.prefix_api,
                      tags=["Facility Data Collection"], responses={404: {"description": "Not found"}})

router.include_router(transport_data_collection_controller.router, prefix=Route.V1.prefix_api,
                      tags=["Trans Data Collection"], responses={404: {"description": "Not found"}})

router.include_router(fuel_source_controller.router, prefix=Route.V1.prefix_api,
                      tags=["Fuel Source"], responses={404: {"description": "Not found"}})

router.include_router(activity_controller.router, prefix=Route.V1.prefix_api,
                      tags=["Activity Type"], responses={404: {"description": "Not found"}})

router.include_router(client_controller.router, prefix=Route.V1.prefix_api,
                      tags=["Client"], responses={404: {"description": "Not found"}})

router.include_router(report_controller.router, prefix=Route.V1.prefix_api,
                      tags=["Report"], responses={404: {"description": "Not found"}})

router.include_router(dashboard_controller.router, prefix=Route.V1.prefix_api,
                      tags=["Dashboard"], responses={404: {"description": "Not found"}})




