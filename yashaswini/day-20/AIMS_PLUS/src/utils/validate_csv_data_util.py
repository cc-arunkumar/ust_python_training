import csv

# Importing custom model classes for validation and structured data handling
from models.assets_inventory import AssetInventory
from models.employee_directory import EmployeeDirectory
from models.maintenance_log import MaintenanceLog
from models.vendor_master import VendorMaster

# Base path for input and output CSV files
path = "C:/Users/Administrator/Desktop/ust_python_training-1/yashaswini/day-13/my-first-fastapi-app/day-18/aims_final_project/database/sample_data/"

# ---------------------------
# Process Vendor Master Data
# ---------------------------
with open(path + "vendor_master.csv", "r") as vendor_file:
    # Open output file in write mode, ensuring newline handling for CSV
    with open(path + "final/vendor_master.csv", "w", newline="") as final_vendor_file:
        vendor_data = csv.DictReader(vendor_file)   # Read input CSV as dictionary
        header = vendor_data.fieldnames             # Extract header fields
        # Skip 'vendor_id' column when writing to final file
        new_vendor = csv.DictWriter(final_vendor_file, header[1:])
        new_vendor.writeheader()                    # Write header row to output file
        
        # Iterate through each record in vendor_master.csv
        for data in vendor_data:
            try:
                # Validate data against VendorMaster model
                emp = VendorMaster(**data)
                # Remove vendor_id before writing to final file
                del data["vendor_id"]
                new_vendor.writerow(data)
            except Exception as e:
                # Log error for debugging and skip problematic records
                print(f"Error: {e}")
                print("Unable to process record")

# ---------------------------
# Process Employee Directory Data
# ---------------------------
with open(path + "employee_directory.csv", "r") as emp_file:
    with open(path + "final/employee_directory.csv", "w", newline="") as final_emp_file:
        emp_data = csv.DictReader(emp_file)
        header = emp_data.fieldnames
        new_emp = csv.DictWriter(final_emp_file, header)
        new_emp.writeheader()
        
        for data in emp_data:
            try:
                # Validate data against EmployeeDirectory model
                emp = EmployeeDirectory(**data)
                new_emp.writerow(data)
            except Exception as e:
                print(f"Error: {e}")
                print("Unable to process record")

# ---------------------------
# Process Asset Inventory Data
# ---------------------------
with open(path + "asset_inventory.csv", "r") as asset_file:
    with open(path + "final/asset_inventory.csv", "w", newline="") as final_asset_file:
        asset_data = csv.DictReader(asset_file)
        header = asset_data.fieldnames
        new_asset = csv.DictWriter(final_asset_file, header)
        new_asset.writeheader()
        
        for data in asset_data:
            try:
                # Validate data against AssetInventory model
                asset = AssetInventory(**data)
                new_asset.writerow(data)
            except Exception as e:
                print(f"Error: {e}")

# ---------------------------
# Process Maintenance Log Data
# ---------------------------
with open(path + "maintenance_log.csv", "r") as maintain_file:
    with open(path + "final/maintenance_log.csv", "w", newline="") as final_maintain_file:
        maintain_data = csv.DictReader(maintain_file)
        header = maintain_data.fieldnames
        # Skip 'log_id' column when writing to final file
        new_maintain = csv.DictWriter(final_maintain_file, header[1:])
        new_maintain.writeheader()
        
        for data in maintain_data:
            try:
                # Validate data against MaintenanceLog model
                emp = MaintenanceLog(**data)
                # Remove log_id before writing to final file
                del data["log_id"]
                new_maintain.writerow(data)
            except Exception as e:
                print(f"Error: {e}")
                print("Unable to process record")