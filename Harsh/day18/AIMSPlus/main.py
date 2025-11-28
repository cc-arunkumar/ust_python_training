from fastapi import FastAPI
from src.api.asset_api import register_asset_api      # import asset API routes
from src.api.vendor_api import register_vendor_api    # import vendor API routes
from src.api.maintenance_api import register_maintenance_api  # import maintenance API routes
from src.api.employee_api import register_employee_api        # import employee API routes

# Initialize FastAPI application with title
app = FastAPI(title="AIMS+")

# Register all API modules with the app
register_asset_api(app)          # attach asset endpoints
register_employee_api(app)       # attach employee endpoints
register_vendor_api(app)         # attach vendor endpoints
register_maintenance_api(app)    # attach maintenance endpoints
