# Import all the models, so that Base has them before being
# imported by Alembic
from app.models.model_base import Base  # noqa
from app.models.model_user import User  # noqa
from app.models.model_activity_type import ActivityType  # noqa
from app.models.model_client_master_data import ClientMasterData  # noqa
from app.models.model_company import Company  # noqa
from app.models.model_company_facility_master_data import CompanyFacilityMasterData  # noqa
from app.models.model_employee import Employee  # noqa
from app.models.model_folklift_master_data import FolkliftMasterData  # noqa
from app.models.model_role import Role  # noqa
from app.models.model_transportation_master_data import TransportationMasterData  # noqa
from app.models.model_fuel_source import FuelSource  # noqa
from app.models.model_facility_activity import FacilityActivity
from app.models.model_trans_activity import TransActivity


