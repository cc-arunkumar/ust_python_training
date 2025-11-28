import csv

error = []   # list to store error messages
valid = []   # list to store valid rows
serial_number_Set = set()   # set to track unique serial numbers


# Input and output file paths
input_file = r"C:\Users\Administrator\Desktop\PTraining\ust_python_training\sohan-kumar-rout\day-18\AIMS+\database\sampledata\asset_inventory(in).csv"
output_file = r"C:\Users\Administrator\Desktop\PTraining\ust_python_training\sohan-kumar-rout\day-18\AIMS+\database\sampledata\finaldata\validated_asset.csv"


#-------ASSET------------------


# Read input CSV file
with open(input_file, mode="r", encoding="utf-8") as file1:
    reader = csv.DictReader(file1)   # read rows as dictionary
    rows = list(reader)

    for row in rows:
        # Extract fields from each row
        asset_id = row.get("asset_id")
        asset_tag = row.get("asset_tag")
        asset_type = row.get("asset_type")
        serial_number = row.get("serial_number")
        manufacturer = row.get("manufacturer")
        model = row.get("model")
        
        
        purchase_date = row.get("purchase_date")   # kept but not validated
        warranty_years = row.get("warranty_years")
        condition_status = row.get("condition_status")
        assigned_to = row.get("assigned_to")
        location = row.get("location")
        asset_status = row.get("asset_status")
        last_updated = row.get("last_updated")

        try:
            # Validate asset_tag format
            output = asset_tag.split("-")
            if output[0] != "UST": raise ValueError("Asset tag must start with UST")

            # Validate asset type
            if asset_type not in ["Laptop", "Monitor", "Keyboard", "Mouse"]: raise ValueError("Invalid asset type")

            # Validate serial number (must be unique and not empty)
            if not serial_number or serial_number in serial_number_Set: raise ValueError("Duplicate or missing serial number")
            serial_number_Set.add(serial_number)

            # Validate model (must not be empty)
            if not model or not model.strip(): raise ValueError("Model is missing")

            # Validate warranty years (must be integer between 1 and 5)
            try:
                warranty_years = int(warranty_years)
                if warranty_years < 1 or warranty_years > 5: raise ValueError("Warranty years must be between 1 and 5")
            except Exception: raise ValueError("Warranty years must be an integer")

            # Validate condition status
            if condition_status not in ["New", "Good", "Used", "Damaged"]: raise ValueError("Invalid condition status")

            # Validate manufacturer
            if manufacturer not in ["Dell", "HP", "Samsung", "Lenovo"]: raise ValueError("Invalid manufacturer")

            # Validate location
            if location not in ["Trivandrum", "Chennai", "Hyderabad", "Bangalore"]: raise ValueError("Invalid location")

            # Validate asset status
            if asset_status not in ["Available", "Assigned", "Repair", "Retired"]: raise ValueError("Invalid asset status")

        except Exception as e:
            # If any validation fails, add error message
            error.append(f"{asset_id}: {str(e)}")
            continue

        # If all validations pass, add row to valid list
        valid.append(row)

# Write valid rows to output CSV file
if valid:
    with open(output_file, mode="w", encoding="utf-8", newline="") as file1:
        fieldnames = valid[0].keys()   
        writer = csv.DictWriter(file1, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(valid)

# Print summary of results
print(len(valid))
# print("Errors:")
# for e in error:
#     print("-", e)


#-----------EMPLOYEE------------

import csv
import datetime
import re



valid_rows = []

input_file = r"C:\Users\Administrator\Desktop\PTraining\ust_python_training\sohan-kumar-rout\day-18\AIMS+\database\sampledata\employee_directory(in).csv"
output_file = r"C:\Users\Administrator\Desktop\PTraining\ust_python_training\sohan-kumar-rout\day-18\AIMS+\database\sampledata\finaldata\validated_employee.csv"

with open(input_file, newline="", encoding="utf-8") as infile:
    reader = csv.DictReader(infile)
    fieldnames = reader.fieldnames

    for row in reader:
        errors = []

        # emp_code must start with USTEMP- and 4 digits
        if not re.match(r"^USTEMP-\d{4}$", row["emp_code"]):
            errors.append("Invalid emp_code")

        # email format
        if not re.match(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$", row["email"]):
            errors.append("Invalid email")

        # phone must be 10 digits
        if not re.match(r"^\d{10}$", row["phone"]):
            errors.append("Invalid phone")

        # department check
        if row["department"] not in ["IT", "HR", "Finance", "Admin", "Sales", "Support"]:
            errors.append("Invalid department")

        # location check
        if row["location"] not in ["Trivandrum", "Bangalore", "Chennai", "Hyderabad"]:
            errors.append("Invalid location")

        if not row["join_date"]:
            errors.append("Missing join_date")
        # status check
        if row["status"] not in ["Active", "Inactive", "Resigned"]:
            errors.append("Invalid status")

        if errors:
            print(f"Row {row.get('emp_code','?')} errors: {errors}")
        else:
            valid_rows.append(row)

# Write valid rows to new CSV
with open(output_file, "w", newline="", encoding="utf-8") as outfile:
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(valid_rows)

print(f"Validation complete. {len(valid_rows)} valid rows written.")

#------VENDOR-----------------------
import csv 
import re

error_list = []
answer_rows = []
valid_cities = ["Mumbai","Delhi","Bangalore","Chennai","Hyderabad","Pune","Kolkata"]

raw_vendor_file = r'C:\Users\Administrator\Desktop\PTraining\ust_python_training\sohan-kumar-rout\day-18\AIMS+\database\sampledata\vendor_master(in).csv'
valid_vendor_file = r'C:\Users\Administrator\Desktop\PTraining\ust_python_training\sohan-kumar-rout\day-18\AIMS+\database\sampledata\finaldata\validated_vendors.csv'


with open(raw_vendor_file, mode='r', newline='',) as outfile:
    reader = csv.DictReader(outfile)
    all_fields = reader.fieldnames

    for row in reader:
        errors = []
        try:
            if not re.match(r"^[A-Za-z\s]{1,100}$", row["vendor_name"]):
                errors.append(f"Invalid vendor_name for vendor_id {row['vendor_id']}")

            if not re.match(r"^[A-Za-z\s]{1,100}$", row["contact_person"]):
                errors.append(f"Invalid contact_person for vendor_id {row['vendor_id']}")

            if not re.match(r"^[6-9]\d{9}$", row["contact_phone"]):
                errors.append(f"Invalid contact_phone for vendor_id {row['vendor_id']}")

            if not re.match(r"^[A-Za-z0-9]{15}$", row["gst_number"]):
                errors.append(f"Invalid gst_number for vendor_id {row['vendor_id']}")

            if not re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", row["email"]):
                errors.append(f"Invalid email for vendor_id {row['vendor_id']}")

            if len(row["address"]) > 200:
                errors.append(f"Invalid address length for vendor_id {row['vendor_id']}")

            if row["city"] not in ["Mumbai","Delhi","Bangalore","Chennai","Hyderabad","Pune","Kolkata"]:
                errors.append(f"Invalid city '{row['city']}' for vendor_id {row['vendor_id']}")

            if row["active_status"] not in ["Active", "Inactive"]:
                errors.append(f"Invalid active_status for vendor_id {row['vendor_id']}")
        except Exception as e:
            errors.append(f"Error: {e}")

        if not errors:
            answer_rows.append(row)
        else:
            error_list.append({"vendor_id": row["vendor_id"], "errors": errors})

# Write valid rows into new CSV
with open(valid_vendor_file, mode='w', newline='', encoding='utf-8') as file_out:
    writer = csv.DictWriter(file_out, fieldnames=all_fields)
    writer.writeheader()
    writer.writerows(answer_rows)

# print(len(answer_rows))
# print(len(error_list))

#-----------MAINTENANCE----------

import csv
from datetime import datetime
import re

errors = []
valid_rows = []

input_file = r"C:\Users\Administrator\Desktop\PTraining\ust_python_training\sohan-kumar-rout\day-18\AIMS+\database\sampledata\maintenance_log(in).csv"
output_file = r"C:\Users\Administrator\Desktop\PTraining\ust_python_training\sohan-kumar-rout\day-18\AIMS+\database\sampledata\finaldata\validated_maintenance.csv"


with open(input_file, mode="r", encoding="utf-8") as file1:
    reader = csv.DictReader(file1)
    fieldnames = reader.fieldnames  # keep original headers

    for row in reader:
        asset_tag = row.get("asset_tag")
        maintenance_type = row.get("maintenance_type")
        vendor_name = row.get("vendor_name")
        description = row.get("description")
        cost = row.get("cost")
        maintenance_date = row.get("maintenance_date")
        technician_name = row.get("technician_name")
        status = row.get("status")

        maintenance_types = ["Repair", "Service", "Upgrade"]
        valid_status = ["Completed", "Pending"]

        row_errors = []  

        if not asset_tag or not asset_tag.startswith("UST-"):
            row_errors.append(f"Invalid asset tag: {asset_tag}")

        if maintenance_type not in maintenance_types:
            row_errors.append(f"Invalid maintenance type: {maintenance_type}")

        if not vendor_name or not re.match(r"^[A-Za-z ]+$", vendor_name):
            row_errors.append(f"Invalid vendor name: {vendor_name}")

        if not description or len(description) < 10:
            row_errors.append("Description too short")

        try:
             
            cost_val = float(cost)
            if  not re.match(r'^\d+\.\d{1,2}$', str(cost_val)):
                row_errors.append(f"Invalid cost format: {cost}")
        except Exception:
            row_errors.append(f"Cost must be a valid decimal number: {cost}")

        # Technician name check
        if not technician_name or not re.match(r"^[A-Za-z ]+$", technician_name):
            row_errors.append(f"Invalid technician name: {technician_name}")

        # Status check
        if status not in valid_status:
            row_errors.append(f"Invalid status: {status}")

        # Final decision
        if row_errors:
            errors.extend(row_errors)
        else:
            valid_rows.append(row)

# Write valid rows into new CSV
with open(output_file, mode="w", newline="", encoding="utf-8") as file_out:
    writer = csv.DictWriter(file_out, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(valid_rows)

print(f"Valid rows written: {len(valid_rows)}")
print(f"Errors found: {len(errors)}")
for e in errors:
    print("-", e)