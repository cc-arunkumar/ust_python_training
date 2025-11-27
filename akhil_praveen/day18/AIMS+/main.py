from src.models.assetsinventory import AssetInventory
from src.models.employeedirectory import EmployeeDirectory
from src.models.maintainancelog import MaintenanceLog
from src.models.vendormaster import VendorMaster
from fastapi import FastAPI,HTTPException
from src.api.asset_api import asset_router
 
import csv
 

app = FastAPI(title="UST AIMS+")

app.include_router(asset_router)
 
# path = "C:/Users/Administrator/Desktop/ust_python_training/akhil_praveen/day18/AIMS+/database/sample_data/"
 
# with open(path + "vendor_master.csv", "r") as vendor_file:
#     with open(path + "final/vendor_master.csv", "w", newline="") as final_vendor_file:
#         vendor_data = csv.DictReader(vendor_file)
#         header = vendor_data.fieldnames
#         new_vendor = csv.DictWriter(final_vendor_file, header[1:])
#         new_vendor.writeheader()
 
#         for data in vendor_data:
#             try:
                
#                 emp = VendorMaster(**data)
#                 del data["vendor_id"]
#                 new_vendor.writerow(data)
#             except Exception as e:
#                 print(f"Error: {e}")
#                 print("Unable to process record")
 
 
 
# with open(path + "employee_directory.csv", "r") as emp_file:
#     with open(path + "final/employee_directory.csv", "w", newline="") as final_emp_file:
#         emp_data = csv.DictReader(emp_file)
#         header = emp_data.fieldnames
#         new_emp = csv.DictWriter(final_emp_file, header)
#         new_emp.writeheader()
 
#         for data in emp_data:
#             try:
                
#                 emp = EmployeeDirectory(**data)
#                 new_emp.writerow(data)
#             except Exception as e:
#                 print(f"Error: {e}")
#                 print("Unable to process record")
 
# with open(path + "asset_inventory.csv", "r") as asset_file:
#     with open(path + "final/asset_inventory.csv", "w", newline="") as final_asset_file:
#         asset_data = csv.DictReader(asset_file)
#         header = asset_data.fieldnames
#         new_asset = csv.DictWriter(final_asset_file, header)
#         new_asset.writeheader()
 
#         for data in asset_data:
#             try:
            
#                 asset = AssetInventory(**data)
#                 new_asset.writerow(data)
#             except Exception as e:
#                 print(f"Error: {e}")

# with open(path + "maintenance_log.csv", "r") as maintain_file:
#     with open(path + "final/maintenance_log.csv", "w", newline="") as final_maintain_file:
#         maintain_data = csv.DictReader(maintain_file)
#         header = maintain_data.fieldnames
#         new_maintain = csv.DictWriter(final_maintain_file, header[1:])
#         new_maintain.writeheader()
 
#         for data in maintain_data:
#             try:
                
#                 emp = MaintenanceLog(**data)
#                 del data["log_id"]
#                 new_maintain.writerow(data)
#             except Exception as e:
#                 print(f"Error: {e}")
#                 print("Unable to process record")
 
 
 
 