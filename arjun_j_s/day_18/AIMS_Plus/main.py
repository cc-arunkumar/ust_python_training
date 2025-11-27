from src.models.asset_model import AssetInventory
from src.models.employee_model import EmployeeDirectory
from src.models.maintenance_model import MaintenanceLog
from src.models.vendor_model import VendorMaster
from fastapi import FastAPI
from src.api.asset_api import asset_router
from src.api.employee_api import emp_router
from src.api.maintenance_api import log_router
from src.api.vendor_api import vendor_router

app = FastAPI(title="AIMS Plus")

app.include_router(asset_router)
app.include_router(emp_router)
app.include_router(log_router)
app.include_router(vendor_router)


# import csv

# path = "D:/ust_python_training-1/arjun_j_s/day_18/AIMS_Plus/database/sample_data/"

# with open(path + "asset_inventory.csv", "r") as asset_file:
#     with open(path + "final/asset_inventory.csv", "w", newline="") as new_asset_file:
#         asset_data = csv.DictReader(asset_file)
#         header = asset_data.fieldnames
#         new_asset = csv.DictWriter(new_asset_file, header)
#         new_asset.writeheader()

#         for data in asset_data:
#             try:
#                 # Validate row against model
#                 asset = AssetInventory(**data)
#                 new_asset.writerow(data)
#             except Exception as e:
#                 print(f"Error: {e}")


# with open(path + "employee_directory.csv", "r") as emp_file:
#     with open(path + "final/employee_directory.csv", "w", newline="") as new_emp_file:
#         emp_data = csv.DictReader(emp_file)
#         header = emp_data.fieldnames
#         new_emp = csv.DictWriter(new_emp_file, header)
#         new_emp.writeheader()

#         for data in emp_data:
#             try:
#                 # Validate row against model
#                 emp = EmployeeDirectory(**data)
#                 new_emp.writerow(data)
#             except Exception as e:
#                 print(f"Error: {e}")


# with open(path + "maintenance_log.csv", "r") as maintain_file:
#     with open(path + "final/maintenance_log.csv", "w", newline="") as new_maintain_file:
#         maintain_data = csv.DictReader(maintain_file)
#         header = maintain_data.fieldnames
#         new_maintain = csv.DictWriter(new_maintain_file, header[1::])
#         new_maintain.writeheader()

#         for data in maintain_data:
#             try:
#                 # Validate row against model
#                 emp = MaintenanceLog(**data)
#                 del data["log_id"]
#                 new_maintain.writerow(data)
#             except Exception as e:
#                 print(f"Error: {e}")


# with open(path + "vendor_master.csv", "r") as vendor_file:
#     with open(path + "final/vendor_master.csv", "w", newline="") as new_vendor_file:
#         vendor_data = csv.DictReader(vendor_file)
#         header = vendor_data.fieldnames
#         new_vendor = csv.DictWriter(new_vendor_file, header[1::])
#         new_vendor.writeheader()

#         for data in vendor_data:
#             try:
#                 # Validate row against model
#                 emp = VendorMaster(**data)
#                 del data["vendor_id"]
#                 new_vendor.writerow(data)
#             except Exception as e:
#                 print(f"Error: {e}")


