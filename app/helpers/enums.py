import enum


class UserRole(enum.Enum):
    ADMIN = 'admin'
    MANAGER = 'manager'
    ACCOUNTANT = 'accountant'
    LOGISTIC = 'logistics'
    CUSTOMER = 'customer'
