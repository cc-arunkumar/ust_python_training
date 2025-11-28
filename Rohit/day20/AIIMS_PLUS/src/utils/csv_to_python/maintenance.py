import csv  # Import csv module to read and write CSV files
from datetime import datetime  # Import datetime for potential date validation (not used here yet)
import re  # Import regex module for pattern-based validation

errors = []  # List to store all error messages across rows
final_rows = []  # List to store rows that pass validation

# File paths for input and output CSV files
input_file = r"C:\Users\Administrator\Desktop\ust_python_training\Rohit\day20\AIIMS_PLUS\database\sample_data\maintenance_log(in).csv"  # Input file path
output_file = r"C:\Users\Administrator\Desktop\ust_python_training\Rohit\day20\AIIMS_PLUS\database\sample_data\final\validated_maintenance_log(in).csv"  # Output file path

# Open the input CSV file in read mode
with open(input_file, mode="r", encoding="utf-8") as file1:
    reader = csv.DictReader(file1)  # Read CSV rows as dictionaries (keys = column names)
    fieldnames = reader.fieldnames  # Keep original headers for writing output later

    # Iterate through each row in the input CSV
    for row in reader:
        asset_tag = row.get("asset_tag")  # Asset tag (must start with UST-)
        maintenance_type = row.get("maintenance_type")  # Type of maintenance (Repair/Service/Upgrade)
        vendor_name = row.get("vendor_name")  # Vendor performing maintenance
        description = row.get("description")  # Description of maintenance work
        cost = row.get("cost")  # Cost of maintenance
        maintenance_date = row.get("maintenance_date")  # Date of maintenance (not validated here)
        technician_name = row.get("technician_name")  # Technician performing maintenance
        status = row.get("status")  # Status of maintenance (Completed/Pending)

        # Allowed values for validation
        maintenance_types = ["Repair", "Service", "Upgrade"]  # Valid maintenance types
        valid_status = ["Completed", "Pending"]  # Valid statuses

        row_errors = []  # Collect errors for this specific row

        # Asset tag validation: must exist and start with "UST-"
        if not asset_tag or not asset_tag.startswith("UST-"):
            row_errors.append(f"Invalid asset tag: {asset_tag}")

        # Maintenance type validation: must be one of the allowed types
        if maintenance_type not in maintenance_types:
            row_errors.append(f"Invalid maintenance type: {maintenance_type}")

        # Vendor name validation: must contain only letters and spaces
        if not vendor_name or not re.match(r"^[A-Za-z ]+$", vendor_name):
            row_errors.append(f"Invalid vendor name: {vendor_name}")

        # Description validation: must exist and be at least 10 characters long
        if not description or len(description) < 10:
            row_errors.append("Description too short")

        # Cost validation: must be a valid decimal number with up to 2 decimal places
        try:
            cost_val = float(cost)  # Try converting cost to float
            # Regex ensures format like 123.45 (up to 2 decimal places)
            if not re.match(r'^\d+\.\d{1,2}$', str(cost_val)):
                row_errors.append(f"Invalid cost format: {cost}")
        except Exception:  # If conversion fails, cost is invalid
            row_errors.append(f"Cost must be a valid decimal number: {cost}")

        # Technician name validation: must contain only letters and spaces
        if not technician_name or not re.match(r"^[A-Za-z ]+$", technician_name):
            row_errors.append(f"Invalid technician name: {technician_name}")

        # Status validation: must be one of the allowed statuses
        if status not in valid_status:
            row_errors.append(f"Invalid status: {status}")

        # Final decision: if errors exist, add them to global errors list
        if row_errors:
            errors.extend(row_errors)  # Add this row’s errors to overall list
        else:
            final_rows.append(row)  # If no errors, add row to valid rows list

# Write valid rows into new CSV file
with open(output_file, mode="w", newline="", encoding="utf-8") as file_out:
    writer = csv.DictWriter(file_out, fieldnames=fieldnames)  # Create writer with same headers
    writer.writeheader()  # Write header row
    writer.writerows(final_rows)  # Write all valid rows

# Print summary of validation results
print(f"Valid rows written: {len(final_rows)}")  # Show count of valid rows
print(f"Errors found: {len(errors)}")  # Show count of errors
for e in errors:  # Print each error message
    print("-", e)
