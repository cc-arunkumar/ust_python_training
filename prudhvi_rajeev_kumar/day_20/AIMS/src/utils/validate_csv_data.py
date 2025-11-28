# validate_csv_data.py
import csv
import datetime
import os

# --- Validators ---
def validate_date(date_str):
    """Check if date is in YYYY-MM-DD format and valid."""
    try:
        datetime.datetime.strptime(date_str.strip(), "%Y-%m-%d")
        return True
    except Exception:
        return False

def validate_email(email_str):
    """Check if email contains '@' and ends with ust.com."""
    return email_str and "@" in email_str and email_str.strip().endswith("ust.com")

def validate_non_empty(value):
    """Ensure field is not empty."""
    return bool(value and value.strip())

def validate_numeric(value):
    """Ensure field is numeric (int/float)."""
    try:
        float(value)
        return True
    except Exception:
        return False

# --- Generic CSV validator ---
def validate_csv(input_file, output_file, validations):
    if not os.path.exists(input_file):
        print(f"File not found: {input_file}")
        return

    with open(input_file, newline="", encoding="utf-8") as infile, \
         open(output_file, "w", newline="", encoding="utf-8") as outfile:

        reader = csv.DictReader(infile)
        writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)
        writer.writeheader()

        success, fail = 0, 0

        for row in reader:
            valid = True
            for field, func in validations.items():
                if not func(row[field]):
                    print(f"Invalid {field}: {row[field]} in row {row}")
                    valid = False
                    break

            if valid:
                writer.writerow(row)
                success += 1
            else:
                fail += 1

    print(f"Validation complete for {os.path.basename(input_file)}")
    print(f"Valid rows: {success}, Invalid rows: {fail}")
    print(f"Valid data written to: {output_file}\n")


# --- File paths ---
base_path = r"C:\Users\Administrator\Desktop\Prudhvi_Rajeev\ust_python_training\prudhvi_rajeev_kumar\day_18\AIMS\database\sample_data"


employee_file = os.path.join(base_path, "employee_directory.csv")
asset_file = os.path.join(base_path, "asset_inventory.csv")
vendor_file = os.path.join(base_path, "vendor_master.csv")
maintenance_file = os.path.join(base_path, "maintenance_log.csv")

# --- Run validations for all tables ---
if __name__ == "__main__":
    # Employees
    validate_csv(
        employee_file,
        employee_file.replace(".csv", "_valid.csv"),
        {
            "emp_code": validate_non_empty,
            "full_name": validate_non_empty,
            "email": validate_email,
            "phone": validate_non_empty,
            "department": validate_non_empty,
            "location": validate_non_empty,
            "join_date": validate_date,
            "status": validate_non_empty
        }
    )

    # Assets
    validate_csv(
        asset_file,
        asset_file.replace(".csv", "_valid.csv"),
        {
            "asset_tag": validate_non_empty,
            "asset_type": validate_non_empty,
            "serial_number": validate_non_empty,
            "manufacturer": validate_non_empty,
            "model": validate_non_empty,
            "purchase_date": validate_date,
            "warranty_years": validate_numeric,
            "condition_status": validate_non_empty,
            "assigned_to": validate_non_empty,
            "location": validate_non_empty,
            "asset_status": validate_non_empty,
            "last_updated": validate_date
        }
    )

    # Vendors
    validate_csv(
        vendor_file,
        vendor_file.replace(".csv", "_valid.csv"),
        {
            "vendor_id": validate_non_empty,
            "vendor_name": validate_non_empty,
            "contact_person": validate_non_empty,
            "contact_phone": validate_non_empty,
            "gst_number": validate_non_empty,
            "email": validate_email,
            "address": validate_non_empty,
            "city": validate_non_empty,
            "active_status": validate_non_empty
        }
    )

    # Maintenance
    validate_csv(
        maintenance_file,
        maintenance_file.replace(".csv", "_valid.csv"),
        {
            "log_id": validate_non_empty,
            "asset_tag": validate_non_empty,
            "maintenance_type": validate_non_empty,
            "vendor_name": validate_non_empty,
            "description": validate_non_empty,
            "cost": validate_numeric,
            "maintenance_date": validate_date,
            "technician_name": validate_non_empty,
            "status": validate_non_empty
        }
    )
