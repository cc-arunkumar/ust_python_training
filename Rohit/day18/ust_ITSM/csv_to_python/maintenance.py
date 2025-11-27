import csv
from datetime import datetime
import re

errors = []
final_rows = []

input_file = r"C:\Users\Administrator\Desktop\ust_python_training\Rohit\day18\ust_ITSM\data\maintenance_log(in).csv"
output_file = r"C:\Users\Administrator\Desktop\ust_python_training\Rohit\day18\ust_ITSM\data\new_maintenance_log(in).csv"

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

        row_errors = []  # collect errors per row

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
            final_rows.append(row)

# Write valid rows into new CSV
with open(output_file, mode="w", newline="", encoding="utf-8") as file_out:
    writer = csv.DictWriter(file_out, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(final_rows)

print(f"Valid rows written: {len(final_rows)}")
print(f"Errors found: {len(errors)}")
for e in errors:
    print("-", e)
