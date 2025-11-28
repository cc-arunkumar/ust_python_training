# validate_csv_data.py
import csv
import datetime
import os
import re

# --- Validators ---
def validate_date(date_str, allow_future=False):
    """Check if date is in YYYY-MM-DD format and valid. Optionally disallow future dates."""
    try:
        dt = datetime.datetime.strptime(date_str.strip(), "%Y-%m-%d").date()
        if not allow_future and dt > datetime.date.today():
            return False
        return True
    except Exception:
        return False

def validate_email(email_str):
    """Basic email validation."""
    return bool(email_str and re.match(r"[^@]+@[^@]+\.[^@]+", email_str.strip()))

def validate_non_empty(value):
    return bool(value and value.strip())

def validate_numeric(value, min_val=None, max_val=None):
    try:
        num = int(value)
        if min_val is not None and num < min_val:
            return False
        if max_val is not None and num > max_val:
            return False
        return True
    except Exception:
        return False

def validate_asset_tag(tag):
    return tag.startswith("UST")

def validate_asset_type(value):
    return value in {"Laptop", "Monitor", "Keyboard", "Mouse"}

def validate_serial_number(value, seen_serials=set()):
    if not value or not re.match(r"^[A-Za-z0-9\-]+$", value):
        return False
    if value in seen_serials:
        return False
    seen_serials.add(value)
    return True

def validate_manufacturer(value):
    return value in {"Dell", "HP", "Samsung", "Lenovo", "LG"}

def validate_condition_status(value):
    return value in {"New", "Good", "Used", "Damaged", "Fair"}

def validate_location(value):
    return value in {"Hyderabad", "Trivandrum", "Bangalore", "Chennai", "Kolkata", "TVM"}

def validate_asset_status(value):
    return value in {"Available", "Assigned", "Repair", "Retired"}

def validate_vendor_name(value):
    return bool(value and re.match(r"^[A-Za-z\s]{1,100}$", value))

def validate_contact_person(value):
    return bool(value and re.match(r"^[A-Za-z\s]{1,100}$", value))

def validate_contact_phone(value):
    return bool(re.match(r"^[6-9]\d{9}$", value))

def validate_gst_number(value):
    return bool(re.match(r"^[A-Za-z0-9]{15}$", value))

def validate_address(value):
    return bool(value and len(value) <= 200)

def validate_city(value):
    return value in {"Hyderabad", "Trivandrum", "Bangalore", "Chennai"}

def validate_active_status(value):
    return value in {"Active", "Inactive"}

def validate_maintenance_type(value):
    return value in {"Repair", "Service", "Upgrade"}

def validate_vendor_alpha(value):
    return bool(value and re.match(r"^[A-Za-z\s]+$", value))

def validate_description(value):
    return bool(value and len(value.strip()) >= 10)

def validate_cost(value):
    try:
        num = float(value)
        return num > 0 and re.match(r"^\d+(\.\d{1,2})?$", value)
    except Exception:
        return False

def validate_technician_name(value):
    return bool(value and re.match(r"^[A-Za-z\s]+$", value))

def validate_status(value):
    return value in {"Completed", "Pending"}

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

# --- Run validations ---
if __name__ == "__main__":
    # Assets
    validate_csv(
        asset_file,
        asset_file.replace(".csv", "_valid.csv"),
        {
            "asset_tag": validate_asset_tag,
            "asset_type": validate_asset_type,
            "serial_number": validate_serial_number,
            "manufacturer": validate_manufacturer,
            "model": validate_non_empty,
            "purchase_date": lambda v: validate_date(v, allow_future=False),
            "warranty_years": lambda v: validate_numeric(v, 1, 5),
            "condition_status": validate_condition_status,
            "assigned_to": validate_non_empty,  # optional, but if present must be non-empty
            "location": validate_location,
            "asset_status": validate_asset_status
        }
    )

    # Vendors
    # validate_csv(
    #     vendor_file,
    #     vendor_file.replace(".csv", "_valid.csv"),
    #     {
    #         "vendor_name": validate_vendor_name,
    #         "contact_person": validate_contact_person,
    #         "contact_phone": validate_contact_phone,
    #         "gst_number": validate_gst_number,
    #         "email": validate_email,
    #         "address": validate_address,
    #         "city": validate_city,
    #         "active_status": validate_active_status
    #     }
    # )

    # # Maintenance
    # validate_csv(
    #     maintenance_file,
    #     maintenance_file.replace(".csv", "_valid.csv"),
    #     {
    #         "asset_tag": validate_asset_tag,
    #         "maintenance_type": validate_maintenance_type,
    #         "vendor_name": validate_vendor_alpha,
    #         "description": validate_description,
    #         "cost": validate_cost,
    #         "maintenance_date": lambda v: validate_date(v, allow_future=False),
    #         "technician_name": validate_technician_name,
    #         "status": validate_status
    #     }
    # )
