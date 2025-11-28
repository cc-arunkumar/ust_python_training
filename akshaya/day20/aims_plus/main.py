# Importing the necessary modules and classes for validation and API routing
# From utils.validate_csv_data_util import validate_and_save_data - Function to validate CSV data and save it
# Importing model classes for different entities (Asset, Employee, Vendor, Maintenance)
from src.models.asset_model import AssetModel
from src.models.employee_model import EmployeeModel
from src.models.vendor_model import VendorModel
from src.models.maintenance_model import MaintenanceModel

# Importing the routers for different API endpoints related to assets, employees, maintenance, vendors, and login
from src.api.asset_api import asset_router
from src.api.employee_api import emp_router
from src.api.maintenance_api import log_router
from src.api.vendor_api import vendor_router
from src.api.login_api import login_router

# FastAPI instance to create the main application
from fastapi import FastAPI

# Initializing the FastAPI app with a title for the API documentation
app = FastAPI(title="UST AIMS PLUS")

# Including the routers in the app for various API endpoints (asset, employee, maintenance, vendor, login)
app.include_router(login_router)  # Routes for handling user login and authentication
app.include_router(asset_router)  # Routes for asset management (CRUD operations)
app.include_router(emp_router)  # Routes for employee management (CRUD operations)
app.include_router(log_router)  # Routes for maintenance log management (CRUD operations)
app.include_router(vendor_router)  # Routes for vendor management (CRUD operations)

# Validating and saving the data from CSV files to validated files for each respective model
# The following lines are commented out, but they will perform the validation and saving of data:
# validate_and_save_data('src/data/asset_inventory.csv', 'src/result/validated_assets.csv', AssetModel)
# validate_and_save_data('src/data/employee_directory.csv', 'src/result/validated_employees.csv', EmployeeModel)
# validate_and_save_data('src/data/vendor_master.csv', 'src/result/validated_vendors.csv', VendorModel)
# validate_and_save_data('src/data/maintenance_log.csv', 'src/result/validated_maintenance.csv', MaintenanceModel)

# Each line of validation and saving refers to a specific model that validates data from the CSV and stores it in the result folder
# AssetModel: Handles validation of asset data
# EmployeeModel: Handles validation of employee data
# VendorModel: Handles validation of vendor data
# MaintenanceModel: Handles validation of maintenance log data
