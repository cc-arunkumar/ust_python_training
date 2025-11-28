from src.models.asset_model import AssetInventory
from src.models.employee_model import EmployeeModel
from src.models.vendor_model import VendorModel
from src.models.maintenance_model import MaintenanceLog

import csv
from typing import List
from pydantic import ValidationError
from datetime import date
from fastapi import FastAPI
from src.api.asset_api import asset_router
from src.api.employee_api import employee_router
from src.api.maintenance_api import maintenance_router
from src.api.vendor_api import vendor_router


app = FastAPI(title="AIMS PLUS")
app.include_router(asset_router)
app.include_router(employee_router)
app.include_router(maintenance_router)
app.include_router(vendor_router)

# def read_csv(file_path: str) -> List[dict]:
#     with open(file_path,mode='r') as file:
#         reader = csv.DictReader(file)
#         data = [row for row in reader]
#         print(f"Read {len(data)} rows from {file_path}")
#         return data

# def write_csv(file_path: str, data: List[dict]):
#     with open(file_path, mode='w') as file:
#         writer = csv.DictWriter(file, fieldnames=data[0].keys())
#         writer.writeheader()
#         writer.writerows(data)
#         print(f"Written {len(data)} rows to {file_path}")

# def validate_and_save_data(input_file: str, output_file: str, model_class):
#     data = read_csv(input_file)
#     if not data:
#         print("No data found in the input file.")
#         return

#     valid_data = []
#     for row in data:
#         try:
#             # Convert all fields of type date safely
#             for field, field_type in model_class.__annotations__.items():
#                 if field_type is date and row.get(field):
#                     try:
#                         row[field] = date.fromisoformat(row[field])
#                     except ValueError:
#                         print(f"Invalid date in {field}: {row[field]} → setting to None")
#                         row[field] = None

#             # optional fields
#             if "assigned_to" in row and row["assigned_to"] == "":
#                 row["assigned_to"] = None
#             if "last_updated" in row and not row["last_updated"]:
#                 row["last_updated"] = None

#             validated_row = model_class(**row)
#             valid_data.append(validated_row.dict())
#             print("Row validated successfully")

#         except ValidationError as e:
#             print(f"Validation failed for row: {row}")
#             for err in e.errors():
#                 print(f"   - {err['loc']}: {err['msg']}")

#     if valid_data:
#         write_csv(output_file, valid_data)
    



# # Validating and saving each table's data
# validate_and_save_data('database/sample_data/raw_csv/asset_inventory.csv', 'database/sample_data/final_data/validated_assets.csv', AssetInventory)
# validate_and_save_data('database/sample_data/raw_csv/employee_directory.csv', 'database/sample_data/final_data/validated_employees.csv', EmployeeModel)
# validate_and_save_data('database/sample_data/raw_csv/vendor_master.csv', 'database/sample_data/final_data/validated_vendors.csv', VendorModel)
# validate_and_save_data('database/sample_data/raw_csv/maintenance_log.csv', 'database/sample_data/final_data/validated_maintenance.csv', MaintenanceLog)
