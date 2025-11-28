import csv
import datetime
import re

# -----------------------------
# VALIDATION RULES / MASTER DATA
# -----------------------------
valid_asset_types = ["Laptop", "Monitor", "Keyboard", "Mouse"]
valid_manufacturers = ["Dell", "HP", "Samsung", "Lenovo","LG"]
valid_conditions = ["New", "Good", "Used", "Damaged"]
valid_locations = ["Hyderabad", "Bangalore", "Chennai", "Trivandrum"]
valid_statuses = ["Available", "Assigned", "Repair", "Retired","Fair"]

valid_cities = ["Mumbai","Delhi","Bangalore","Chennai","Hyderabad","Pune","Kolkata"]

valid_vendors = []  # Stores validated vendor rows
valid_rows = []     # Stores validated asset rows
serial_numbers_seen = set()  # Track duplicate serial numbers

valid_maintenance_types = ["Repair", "Service", "Upgrade"]
valid_maintencance_statuses = ["Completed", "Pending"]

valid_departments_employee = {"IT", "HR", "Finance", "Admin", "Sales", "Support"}
valid_locations_employee = {"Trivandrum", "Bangalore", "Chennai", "Hyderabad"}
valid_statuses_employee = {"Active", "Inactive", "Resigned"}

valid_rows_employee = []  # Store only rows that pass validation

# -----------------------------
# VALIDATE ASSET INVENTORY
# -----------------------------
with open(r'C:\Users\Administrator\Desktop\Training\ust_python_training\harsh\day18\AIMSPlus\database\sample_data\asset_inventory.csv', mode='r') as file1:
    reader = csv.DictReader(file1)
    all_fields = reader.fieldnames
    
    for row in reader:
        errors = []
        try:
            # Asset tag must start with "UST-"
            if not row["asset_tag"].startswith("UST-"):
                errors.append("Invalid asset_tag")

            # Model cannot be blank
            if not row["model"]:
                errors.append("Model cannot be blank")

            # Serial number must be unique and non-empty
            if not row["serial_number"]:
                errors.append("Serial number cannot be empty")
            elif row["serial_number"] in serial_numbers_seen:
                errors.append(f"Duplicate serial number: {row['serial_number']}")
            else:
                serial_numbers_seen.add(row["serial_number"])

            # Validate asset type and manufacturer
            if row["asset_type"] not in valid_asset_types:
                errors.append("Invalid asset_type")
            if row["manufacturer"] not in valid_manufacturers:
                errors.append("Invalid manufacturer")

            # Purchase date must not be in the future
            purchase_date = datetime.datetime.strptime(row["purchase_date"], "%Y-%m-%d")
            if purchase_date > datetime.datetime.today():
                errors.append("Purchase date cannot be in the future")

            # Warranty years must be between 1 and 5
            warranty_years = int(row["warranty_years"])
            if not (1 <= warranty_years <= 5):
                errors.append("Warranty years must be between 1 and 5")

            # Validate condition, location, and status
            if row["condition_status"] not in valid_conditions:
                errors.append("Invalid condition_status")
            if row["location"] not in valid_locations:
                errors.append("Invalid location")
            if row["asset_status"] not in valid_statuses:
                errors.append("Invalid asset_status")
        
        except ValueError as e:
            errors.append(str(e))

        # Only add row if no errors
        if not errors:
            valid_rows.append(row)

# Save validated asset inventory
output_file = r'C:\Users\Administrator\Desktop\Training\ust_python_training\harsh\day18\AIMSPlus\database\sample_data\final_data\validated_asset_inventory.csv'
with open(output_file, mode='w', newline='') as file2:
    writer = csv.DictWriter(file2, fieldnames=all_fields)
    writer.writeheader()
    writer.writerows(valid_rows)

print(f"Validation completed. {len(valid_rows)} valid rows saved to '{output_file}'.")


# -----------------------------
# VALIDATE VENDOR MASTER
# -----------------------------
with open(r'C:\Users\Administrator\Desktop\Training\ust_python_training\harsh\day18\AIMSPlus\database\sample_data\vendor_master.csv', mode='r') as file2:
    reader = csv.DictReader(file2)
    all_fields = reader.fieldnames
    
    for row in reader:
        errors = []
        try:
            # Vendor name: alphabets + spaces, max 100 chars
            if not re.match(r"^[A-Za-z\s]{1,100}+$", row["vendor_name"]):
                errors.append("Invalid vendor_name. Only alphabets and spaces allowed and max 100 characters.")
            
            # Contact person: alphabets only, max 100 chars
            if not re.match(r"^[A-Za-z\s]{1,100}+$", row["contact_person"]):
                errors.append("Invalid contact_person. Only alphabets allowed and max 100 characters.")
            
            # Contact phone: must be valid Indian mobile number
            if not re.match(r"^[6-9]\d{9}$", row["contact_phone"]):
                errors.append("Invalid contact_phone. Must be a 10-digit Indian mobile number starting with 6, 7, 8, or 9.")
            
            # GST number: exactly 15 alphanumeric characters
            if not re.match(r"^[A-Za-z0-9]{15}$", row["gst_number"]):
                errors.append("Invalid gst_number. Must be exactly 15 alphanumeric characters.")
            
            # Email validation
            if not re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", row["email"]):
                errors.append("Invalid email format.")
            
            # Address length check
            if len(row["address"]) > 200:
                errors.append("Invalid address. Address must be less than or equal to 200 characters.")
            
            # City must be in valid list
            if row["city"] not in valid_cities:
                errors.append(f"Invalid city. Must be one of the valid Indian cities. Given: {row['city']}")
            
            # Active status must be Active/Inactive
            if row["active_status"] not in ["Active", "Inactive"]:
                errors.append("Invalid active_status. Must be 'Active' or 'Inactive'.")
        except Exception as e:
            errors.append(f"Error:{e}")
            
        if not errors:
            valid_vendors.append(row)

# Save validated vendor master
with open(r'C:\Users\Administrator\Desktop\Training\ust_python_training\harsh\day18\AIMSPlus\database\sample_data\final_data\validated_vendor_master.csv', mode='w', newline='') as file2:
    writer = csv.DictWriter(file2, fieldnames=all_fields)
    writer.writeheader()
    writer.writerows(valid_vendors)
    
print(f"Validation completed. {len(valid_vendors)} valid vendors saved to 'updated_vendor_master.csv'.")


# -----------------------------
# VALIDATE MAINTENANCE LOG
# -----------------------------
with open(r'C:\Users\Administrator\Desktop\Training\ust_python_training\harsh\day18\AIMSPlus\database\sample_data\maintenance_log.csv', mode='r') as file3:
    reader = csv.DictReader(file3)
    all_fields = reader.fieldnames
    maintenance_rows = []
    
    for row in reader:
        errors = []
        try:
            # Asset tag format check
            if not row["asset_tag"].startswith("UST-"):
                errors.append("Invalid asset_tag format")

            # Maintenance type validation
            if row["maintenance_type"] not in valid_maintenance_types:
                errors.append("Invalid maintenance_type")

            # Vendor name alphabets only
            if not re.match(r'^[A-Za-z\s]+$', row["vendor_name"]):
                errors.append("Invalid vendor_name (alphabets only)")

            # Description must be at least 10 chars
            if not row["description"] or len(row["description"]) < 10:
                errors.append("Description must be at least 10 characters")

            # Cost validation: >0 and two decimals
            try:
                cost = float(row["cost"])
                if cost <= 0 or not re.match(r'^\d+\.\d{2}$', row["cost"]):
                    errors.append("Invalid cost format (must be >0 with two decimals)")
            except ValueError:
                errors.append("Cost must be a valid decimal number")

            # Maintenance date validation
            try:
                maintenance_date = datetime.datetime.strptime(row["maintenance_date"], "%Y-%m-%d")
                if maintenance_date > datetime.datetime.today():
                    errors.append("Maintenance date cannot be in the future")
            except ValueError:
                errors.append("Invalid maintenance_date format (YYYY-MM-DD expected)")

            # Technician name alphabets only
            if not re.match(r'^[A-Za-z\s]+$', row["technician_name"]):
                errors.append("Invalid technician_name (alphabets only)")

            # Status validation
            if row["status"] not in valid_maintencance_statuses:
                errors.append("Invalid status")

        except Exception as e:
            errors.append(str(e))

        if not errors:
            maintenance_rows.append(row)

# Save validated maintenance log
with open(r'C:\Users\Administrator\Desktop\Training\ust_python_training\harsh\day18\AIMSPlus\database\sample_data\final_data\validated_maintenance_valid.csv', mode='w', newline='') as valid_file:
    writer = csv.DictWriter(valid_file, fieldnames=all_fields)
    writer.writeheader()
    writer.writerows(maintenance_rows)

print(f"Validation completed. {len(maintenance_rows)} valid maintenance rows saved to 'updated_maintenance_valid.csv'.")


# -----------------------------
# READ AND VALIDATE EMPLOYEE DIRECTORY
# -----------------------------
with open(r"C:\Users\Administrator\Desktop\Training\ust_python_training\harsh\day18\AIMSPlus\database\sample_data\employee_directory.csv", 
          newline="", encoding="utf-8") as infile:
    reader = csv.DictReader(infile)
    for row in reader:
        errors = []  # Collect validation errors for each row
        try:
            # emp_code must start with USTEMP- followed by digits
            if not re.match(r"^USTEMP-\d+$", row["emp_code"]):
                errors.append("Invalid emp_code")

            # email must follow proper format
            if not re.match(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$", row["email"]):
                errors.append("Invalid email")

            # phone must be exactly 10 digits
            if not re.match(r"^[6-9]\d{9}$", row["phone"]):
                errors.append("Invalid phone")

            # department must be one of the valid departments
            if row["department"] not in valid_departments_employee:
                errors.append("Invalid department")

            # location must be one of the valid locations
            if row["location"] not in valid_locations_employee:
                errors.append("Invalid location")

            # join_date must be in YYYY-MM-DD format and not in the future
            try:
                join_date_obj = datetime.datetime.strptime(row["join_date"], "%Y-%m-%d").date()
                if join_date_obj > datetime.date.today():
                    errors.append("Join date cannot be in the future")
            except ValueError:
                errors.append("Invalid join_date format")

            # status must be one of the valid statuses
            if row["status"] not in valid_statuses_employee:
                errors.append("Invalid status")

        except Exception as e:
            # Catch any unexpected errors
            errors.append(str(e))

        # If no errors, add row to valid_rows
        if not errors:
            valid_rows_employee.append(row)

# -----------------------------
# WRITE VALIDATED DATA TO NEW CSV
# -----------------------------
with open(r"C:\Users\Administrator\Desktop\Training\ust_python_training\harsh\day18\AIMSPlus\database\sample_data\final_data\validated_employee_directory.csv", 
          "w", newline="", encoding="utf-8") as outfile:
    writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)
    writer.writeheader()
    writer.writerows(valid_rows_employee)

print(f"Validation complete. {len(valid_rows_employee)} valid rows written.")
