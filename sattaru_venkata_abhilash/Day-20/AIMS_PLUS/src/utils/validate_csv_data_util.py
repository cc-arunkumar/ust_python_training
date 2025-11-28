#validate_csv

import csv  # Importing the csv module to handle CSV file operations
from src.models.asset_model import AssetInventory  # Importing the AssetInventory model for validation
from src.models.employee_model import EmployeeDirectory  # Importing the EmployeeDirectory model for validation
from src.models.maintenance_model import MaintenanceLogModel  # Importing the MaintenanceLogModel for validation
from src.models.vendor_model import VendorModel  # Importing the VendorModel for validation

# Initialize lists to store valid and invalid rows for asset data
valid_rows_asset = []  # List to store valid asset data
invalid_rows_asset = []  # List to store invalid asset data

# Define the required fields for asset data
required_fields_asset = [
    "asset_tag", "asset_type", "serial_number", "manufacturer", "model",
    "purchase_date", "warranty_years", "condition_status", "assigned_to",
    "location", "asset_status"
]

# Open the asset inventory CSV file for reading
with open("asset_inventory.csv", "r") as file:
    csv_reader = csv.DictReader(file)  # Read the CSV file as a dictionary

    # Iterate through each row in the CSV file
    for row in csv_reader:
        try:
            # Validate and create an AssetInventory model instance
            valid = AssetInventory(**row)
            # Append valid rows to valid_rows_asset list
            valid_rows_asset.append(valid.model_dump())
        except Exception as e:
            # In case of an error, add the error message to the row and append to invalid_rows_asset list
            row['error'] = str(e)
            invalid_rows_asset.append(row)

# Define the field names for the validated asset inventory CSV file
fieldnames_asset_valid = [
    "asset_tag", "asset_type", "serial_number", "manufacturer", "model",
    "purchase_date", "warranty_years", "condition_status", "assigned_to", "location",
    "asset_status", "last_updated"
]

# Write valid rows to the validated asset inventory CSV file
with open("validated_asset_inventory.csv", "w", newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames_asset_valid)  # Prepare to write valid data
    writer.writeheader()  # Write the header row

    for row in valid_rows_asset:
        # Remove the 'asset_id' field if present, as it is auto-generated in the database
        row.pop('asset_id', None)
        # Format the 'last_updated' field if it exists (date format: YYYY-MM-DD HH:MM:SS)
        if 'last_updated' in row:
            row['last_updated'] = row['last_updated'].strftime('%Y-%m-%d %H:%M:%S')
        # Write each valid row to the CSV file
        writer.writerow(row)

# --- Employee Data Processing ---
valid_rows_emp = []  # List to store valid employee data
invalid_rows_emp = []  # List to store invalid employee data

# Define the required fields for employee data
required_fields_emp = [
    "emp_code", "full_name", "email", "phone", "department",
    "location", "join_date", "status"
]

# Open the employee directory CSV file for reading
with open("employee_directory.csv", "r") as file:
    csv_reader = csv.DictReader(file)  # Read the CSV file as a dictionary
    header = csv_reader.fieldnames  # Read the CSV file header

    # Iterate through each row in the employee directory CSV file
    for row in csv_reader:
        try:
            # Validate and create an EmployeeDirectory model instance
            valid = EmployeeDirectory(**row)
            # Append valid rows to valid_rows_emp list
            valid_rows_emp.append(valid.model_dump())
        except Exception as e:
            # In case of an error, add the error message to the row and append to invalid_rows_emp list
            row['error'] = str(e)
            invalid_rows_emp.append(row)

# Write valid employee rows to the validated employee directory CSV file
with open("validated_employee_directory.csv", "w", newline='') as file:
    writer = csv.DictWriter(file, fieldnames=required_fields_emp)  # Prepare to write valid data
    writer.writeheader()  # Write the header row

    for row in valid_rows_emp:
        # Remove the 'emp_id' field if present, as it is auto-generated in the database
        row.pop('emp_id', None)
        # Write each valid employee row to the CSV file
        writer.writerow(row)

# --- Maintenance Log Data Processing ---
valid_rows_maintain = []  # List to store valid maintenance log data
invalid_rows_maintain = []  # List to store invalid maintenance log data

# Define the required fields for maintenance log data
required_fields_maintain = [
    "log_id", "asset_tag", "maintenance_type", "vendor_name", "description",
    "cost", "maintenance_date", "technician_name", "status"
]

# Open the maintenance log CSV file for reading
with open("maintenance_log.csv", "r") as file:
    csv_reader = csv.DictReader(file)  # Read the CSV file as a dictionary
    header = csv_reader.fieldnames  # Read the CSV file header

    # Iterate through each row in the maintenance log CSV file
    for row in csv_reader:
        try:
            # Validate and create a MaintenanceLogModel instance
            valid = MaintenanceLogModel(**row)
            # Append valid rows to valid_rows_maintain list
            valid_rows_maintain.append(valid.model_dump())
        except Exception as e:
            # In case of an error, add the error message to the row and append to invalid_rows_maintain list
            row['error'] = str(e)
            invalid_rows_maintain.append(row)

# Write valid maintenance log rows to the validated maintenance log CSV file
with open("validated_maintenance_log.csv", "w", newline='') as file:
    writer = csv.DictWriter(file, fieldnames=required_fields_maintain)  # Prepare to write valid data
    writer.writeheader()  # Write the header row

    for row in valid_rows_maintain:
        # Write each valid maintenance log row to the CSV file
        writer.writerow(row)

# --- Vendor Data Processing ---
valid_rows_vendor = []  # List to store valid vendor data
invalid_rows_vendor = []  # List to store invalid vendor data

# Define the required fields for vendor data
required_fields_vendor = [
    "vendor_id", "vendor_name", "contact_person", "contact_phone", "gst_number",
    "email", "address", "city", "active_status"
]

# Open the vendor master CSV file for reading
with open("vendor_master.csv", "r") as file:
    csv_reader = csv.DictReader(file)  # Read the CSV file as a dictionary
    header = csv_reader.fieldnames  # Read the CSV file header

    # Iterate through each row in the vendor master CSV file
    for row in csv_reader:
        try:
            # Validate and create a VendorModel instance
            valid = VendorModel(**row)
            # Append valid rows to valid_rows_vendor list
            valid_rows_vendor.append(valid.model_dump())
        except Exception as e:
            # In case of an error, add the error message to the row and append to invalid_rows_vendor list
            row['error'] = str(e)
            invalid_rows_vendor.append(row)

# Write valid vendor rows to the validated vendor master CSV file
with open("validated_vendor_master.csv", "w", newline='') as file:
    writer = csv.DictWriter(file, fieldnames=required_fields_vendor)  # Prepare to write valid data
    writer.writeheader()  # Write the header row

    for row in valid_rows_vendor:
        # Write each valid vendor row to the CSV file
        writer.writerow(row)