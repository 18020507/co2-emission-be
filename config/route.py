class Route:
    class V1:
        API = 'api'
        VERSION = 'v1'
        prefix_api = '/' + API + '/' + VERSION

        # HEALTHCHECK
        HEALTH_CHECK = '/'

        #         Auth
        LOGIN = '/login'
        REGISTER = '/register'
        GET_USER_DETAIL = '/user_detail'
        CHANGE_PASSWORD = '/change_password'

        #         Role
        GET_LIST_ROLE = '/role'
        CREATE_ROLE = '/role'

        #         Company
        GET_LIST_COMPANY_INFORMATION = '/company'
        GET_COMPANY_INFORMATION_BY_ID = '/company/{company_id}'
        CREATE_COMPANY_INFORMATION = '/company'

        #         Facility Master Data
        GET_FACILITY_MASTER_DATA = '/facility-master-data/{company_id}'
        CREATE_FACILITY_MASTER_DATA = '/facility-master-data'

        #         Forklift Master Data
        GET_FORKLIFT_MASTER_DATA = '/forklift-master-data/{facility_master_data_id}'
        CREATE_FORKLIFT_MASTER_DATA = '/forklift-master-data'

        #         Transportation Master Data
        GET_TRANSPORTATION_MASTER_DATA = '/transportation-master-data/{company_id}'
        CREATE_TRANSPORTATION_MASTER_DATA = '/transportation-master-data'

        #         Facility Data Collection
        GET_FACILITY_DATA_COLLECTION = '/facility-collection/{company_id}'
        CREATE_FACILITY_DATA_COLLECTION = '/facility-collection'

        #         Transportation Data Collection
        GET_TRANSPORTATION_DATA_COLLECTION = '/transportation-collection/{company_id}'
        CREATE_TRANSPORTATION_DATA_COLLECTION = '/transportation-collection'

        #         Fuel Source
        GET_FUEL_SOURCE = '/fuel-source/{company_id}'
        CREATE_FUEL_SOURCE = '/fuel-source/{company_id}'

        #         Activity
        GET_ACTIVITY = '/activity/{company_id}'
        CREATE_ACTIVITY = '/activity/{company_id}'

        #         Report
        GET_SUMMARY_REPORT = '/report-summary'
        GET_STATIONARY_COMBUSTION_REPORT = '/report-stationary/{company_id}'
        GET_MOBILE_COMBUSTION_REPORT = '/report-mobile-combustion/{company_id}'


