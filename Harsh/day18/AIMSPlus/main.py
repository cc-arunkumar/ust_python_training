from fastapi import FastAPI
from src.api.asset_api import register_asset_api
from src.api.vendor_api import register_vendor_api
from src.api.maintenance_api import register_maintenance_api
from src.api.employee_api import register_employee_api

app = FastAPI(title="AIMS+")
register_asset_api(app)
register_employee_api(app)
register_vendor_api(app)
register_maintenance_api(app)

