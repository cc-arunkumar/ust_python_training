# Script to bulk import CSV data into Asset, Employee, Maintenance, and Vendor tables

import csv
from ..crud.asset_crud import Asset
from ..crud.employee_crud import Employee
from ..crud.maintenance_crud import Maintain
from ..crud.vendor_crud import Vendor

# Path to the CSV file containing sample data
path = "D:/ust_python_training-1/arjun_j_s/day_18/AIMS_Plus/database/sample_data/final/"

# -------------------- Asset Data Import --------------------
with open(path, "r") as asset_file:
    asset_data = csv.DictReader(asset_file)   # Read CSV as dictionary
    asset_data = list(asset_data)             # Convert to list for iteration
    for data in asset_data:
        try:
            Asset().create_asset(data)        # Insert asset record into DB
        except Exception as e:
            raise e

# -------------------- Employee Data Import --------------------
with open(path, "r") as emp_file:
    emp_data = csv.DictReader(emp_file)
    emp_data = list(emp_data)
    for data in emp_data:
        try:
            Employee().create_emp(data)       # Insert employee record into DB
        except Exception as e:
            raise e

# -------------------- Maintenance Log Import --------------------
with open(path, "r") as log_file:
    log_data = csv.DictReader(log_file)
    log_data = list(log_data)
    for data in log_data:
        try:
            Maintain().create_maintenance(data)  # Insert maintenance record into DB
        except Exception as e:
            raise e

# -------------------- Vendor Data Import --------------------
with open(path, "r") as vendor_file:
    vendor_data = csv.DictReader(vendor_file)
    vendor_data = list(vendor_data)
    for data in vendor_data:
        try:
            Vendor().create_vendor(data)      # Insert vendor record into DB
        except Exception as e:
            raise e