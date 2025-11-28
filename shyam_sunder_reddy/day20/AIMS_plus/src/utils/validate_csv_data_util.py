from models import asset_model
from models import vendor_model
from models import employee_model
from models import maintenance_model
import csv
import datetime

# -------------------------------
# Example CSV validation workflow 
# -------------------------------
valid_count = 0
invalid_count = 0
valid = []
headers = []

with open("../database/sample_data/asset_inventory.csv", "r") as file:
    reader = csv.DictReader(file)
    headers = reader.fieldnames
    for row in reader:
        clean_row = {k.strip(): (v.strip() if v else None) for k, v in row.items()}
        try:
            asset = asset_model.Asset(**clean_row)              # Validate using Pydantic model
            errors = asset_model.validate_asset(asset)          # Apply business rules
            if errors:
                invalid_count += 1
            else:
                valid.append(row)
        except asset_model.ValidationError as e:
            invalid_count += 1

print("\nSummary:")
print(f"Valid rows: {valid_count}")
print(f"Invalid rows: {invalid_count}")
print(headers)
print(valid)

# Write valid rows to final CSV
with open("../database/sample_data/final/validated_asset_inventory.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=headers)
    writer.writeheader()
    writer.writerows(valid)



# -------------------------------
# Example CSV validation workflow 
# -------------------------------
valid_count = 0
invalid_count = 0
headers = []
valid = []

with open("../database/sample_data/employee_directory.csv", "r") as file:
    reader = csv.DictReader(file)
    headers = reader.fieldnames
    for row in reader:
        clean_row = {k.strip(): (v.strip() if v else None) for k, v in row.items()}
        try:
            employee = employee_model.Employee(**clean_row)         # Validate using Pydantic schema
            errors = employee_model.validate_employee(employee)     # Apply business rules
            if errors:
                # print("Row failed business rules:", clean_row)
                # print("Errors:", errors)
                invalid_count += 1
            else:
                valid.append(row)
                valid_count += 1
        except employee_model.ValidationError as e:
            print("Row failed schema validation:", clean_row)
            print(e)
            invalid_count += 1

print("\nSummary:")
print(f"Valid rows: {valid_count}")
print(f"Invalid rows: {invalid_count}")

# Example summary output:
# Valid rows: 88
# Invalid rows: 12

# Write valid rows to final CSV
with open("../database/sample_data/final/validated_employee_directory.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=headers)
    writer.writeheader()
    writer.writerows(valid)



# -------------------------------
# Example CSV validation workflow 
# -------------------------------
headers = []
valid = []
with open("../database/sample_data/vendor_master.csv", "r") as file:
    reader = csv.DictReader(file)
    headers = reader.fieldnames
    count = 0
    for row in reader:
        # Clean up whitespace in CSV values
        clean_row = {k.strip(): (v.strip() if v else None) for k, v in row.items()}
        try:
            vendor = vendor_model.VendorMaster(**clean_row)       # Validate schema
            if not vendor_model.validate(vendor):          # Apply business rules
                count += 1
            else:
                valid.append(row)
        except Exception as e:
            count += 1

# Write valid rows to final CSV
with open("../database/sample_data/final/validated_vendor_master.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=headers)
    writer.writeheader()
    writer.writerows(valid)



# -------------------------------
# Example CSV validation workflow 
# -------------------------------
headers = []
valid = []
with open("../database/sample_data/maintenance_log.csv", "r") as file:
    reader = csv.DictReader(file)
    headers = reader.fieldnames
    count = 0
    for row in reader:
        # Clean up whitespace in CSV values
        clean_row = {k.strip(): (v.strip() if v else None) for k, v in row.items()}
        
        # Convert maintenance_date string to date object
        if clean_row.get("maintenance_date"):
            try:
                clean_row["maintenance_date"] = datetime.strptime(
                    clean_row["maintenance_date"], "%Y-%m-%d"
                ).date()
            except ValueError:
                # Skip rows with bad date format
                continue
        
        try:
            new_maintenance = maintenance_model.MaintenanceLog(**clean_row)   # Validate schema
            if not maintenance_model.validate_maintenance(new_maintenance):   # Apply business rules
                count += 1
            else:
                valid.append(row)
        except Exception as e:
            count += 1

# Write valid rows to final CSV
with open("../database/sample_data/final/validated_maintenance_log.csv", "w", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=headers)
    writer.writeheader()
    writer.writerows(valid)