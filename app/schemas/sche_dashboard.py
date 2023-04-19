from pydantic import BaseModel


class DashboardDTO(BaseModel):
    gas: float
    diesel: float
    propane: float
    electricity: float
    total: float


class DashboardChartDTO(BaseModel):
    chart_gas: list
    chart_diesel: list
    chart_propane: list
    chart_electricity: list
