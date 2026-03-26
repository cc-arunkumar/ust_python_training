import csv
from datetime import datetime
import os

os.makedirs("cleaned", exist_ok=True)

VALID_LOCATIONS = ["TVM", "Bangalore", "Chennai", "Hyderabad"]

# ===================== 1. EMPLOYEE DIRECTORY =====================

print("\nValidating employee_directory.csv ...")

valid_departments = ["HR", "IT", "Admin", "Finance"]
valid_status = ["Active", "Inactive", "Resigned"]

employee_dir_skipped = 0
employee_valid_rows = []

with open("database/sample_data/employee_directory.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:

        if not row["emp_code"].startswith("USTEMP-"):
            employee_dir_skipped += 1
            continue

        if not row["full_name"].replace(" ", "").isalpha():
            employee_dir_skipped += 1
            continue

        if not row["email"].endswith("@ust.com"):
            employee_dir_skipped += 1
            continue

        if not (row["phone"].isdigit() and len(row["phone"]) == 10 and row["phone"][0] in "6789"):
            employee_dir_skipped += 1
            continue

        if row["department"] not in valid_departments:
            employee_dir_skipped += 1
            continue

        if row["location"] not in VALID_LOCATIONS:
            employee_dir_skipped += 1
            continue

        try:
            join_date = datetime.strptime(row["join_date"], "%Y-%m-%d")
            if join_date > datetime.now():
                employee_dir_skipped += 1
                continue
        except:
            employee_dir_skipped += 1
            continue

        if row["status"] not in valid_status:
            employee_dir_skipped += 1
            continue

        employee_valid_rows.append(row)

with open("cleaned/employee_directory_validated.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=employee_valid_rows[0].keys())
    writer.writeheader()
    writer.writerows(employee_valid_rows)

print("employee_directory.csv validated")
print("Skipped records:", employee_dir_skipped)


# ===================== 2. ASSET INVENTORY =====================

print("\nValidating asset_inventory.csv ...")

valid_types = ["Laptop", "Monitor", "Keyboard", "Mouse"]
valid_manufacturers = ["Dell", "HP", "Lenovo", "Samsung"]
valid_condition = ["New", "Good", "Used", "Damaged"]
valid_status_asset = ["Available", "Assigned", "Repair", "Retired"]

asset_skipped = 0
asset_valid_rows = []
serial_numbers = []

with open("database/sample_data/asset_inventory.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:

        if not row["asset_tag"].startswith("UST-"):
            asset_skipped += 1
            continue

        if row["asset_type"] not in valid_types:
            asset_skipped += 1
            continue

        if row["serial_number"] == "" or row["serial_number"] in serial_numbers:
            asset_skipped += 1
            continue

        serial_numbers.append(row["serial_number"])

        if row["manufacturer"] not in valid_manufacturers:
            asset_skipped += 1
            continue

        if row["model"].strip() == "":
            asset_skipped += 1
            continue

        try:
            purchase_date = datetime.strptime(row["purchase_date"], "%Y-%m-%d")
            if purchase_date > datetime.now():
                asset_skipped += 1
                continue
        except:
            asset_skipped += 1
            continue

        try:
            warranty = int(row["warranty_years"])
            if warranty < 1 or warranty > 5:
                asset_skipped += 1
                continue
        except:
            asset_skipped += 1
            continue

        if row["condition_status"] not in valid_condition:
            asset_skipped += 1
            continue

        if row["assigned_to"].strip() != "" and not row["assigned_to"].replace(" ", "").isalpha():
            asset_skipped += 1
            continue

        if row["location"] not in VALID_LOCATIONS:
            asset_skipped += 1
            continue

        if row["asset_status"] not in valid_status_asset:
            asset_skipped += 1
            continue

        asset_valid_rows.append(row)

with open("cleaned/asset_inventory_validated.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=asset_valid_rows[0].keys())
    writer.writeheader()
    writer.writerows(asset_valid_rows)

print("asset_inventory.csv validated")
print("Skipped records:", asset_skipped)


# ===================== 3. VENDOR MASTER =====================

print("\nValidating vendor_master.csv ...")

valid_vendor_status = ["Active", "Inactive"]

vendor_skipped = 0
vendor_valid_rows = []

with open("database/sample_data/vendor_master.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:

        # Safely check vendor_name
        vendor_name = row.get("vendor_name", "")
        if not vendor_name or not vendor_name.replace(" ", "").isalpha():
            vendor_skipped += 1
            continue

        # Safely check contact_person
        contact_person = row.get("contact_person", "")
        if not contact_person or not contact_person.replace(" ", "").isalpha():
            vendor_skipped += 1
            continue

        # Phone validation
        contact_phone = row.get("contact_phone", "")
        if not (contact_phone.isdigit() and len(contact_phone) == 10 and contact_phone[0] in "6789"):
            vendor_skipped += 1
            continue

        # GST number
        gst_number = row.get("gst_number", "")
        if len(gst_number) != 15:
            vendor_skipped += 1
            continue

        # Email
        email = row.get("email", "")
        if "@" not in email:
            vendor_skipped += 1
            continue

        # Address
        address = row.get("address", "")
        if len(address) > 200:
            vendor_skipped += 1
            continue

        # City
        city = row.get("city", "")
        if city not in VALID_LOCATIONS:
            vendor_skipped += 1
            continue

        # Status
        active_status = row.get("active_status", "")
        if active_status not in valid_vendor_status:
            vendor_skipped += 1
            continue

        vendor_valid_rows.append(row)

if vendor_valid_rows:
    with open("cleaned/vendor_master_validated.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=vendor_valid_rows[0].keys())
        writer.writeheader()
        writer.writerows(vendor_valid_rows)

print("vendor_master.csv validated")
print("Skipped records:", vendor_skipped)

# ===================== 4. MAINTENANCE LOG =====================

print("\nValidating maintenance_log.csv ...")

valid_types_maint = ["Repair", "Service", "Upgrade"]
valid_status_maint = ["Completed", "Pending"]

maintenance_skipped = 0
maintenance_valid_rows = []

with open("database/sample_data/maintenance_log.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:

        asset_tag = row.get("asset_tag", "")
        if not asset_tag or not asset_tag.startswith("UST-"):
            maintenance_skipped += 1
            continue

        maintenance_type = row.get("maintenance_type", "")
        if maintenance_type not in valid_types_maint:
            maintenance_skipped += 1
            continue

        vendor_name = row.get("vendor_name", "")
        if not vendor_name or not vendor_name.replace(" ", "").isalpha():
            maintenance_skipped += 1
            continue

        description = row.get("description", "")
        if len(description.strip()) < 10:
            maintenance_skipped += 1
            continue

        try:
            cost = float(row.get("cost", "0"))
            if cost <= 0:
                maintenance_skipped += 1
                continue
        except:
            maintenance_skipped += 1
            continue

        try:
            maint_date = datetime.strptime(row.get("maintenance_date", ""), "%Y-%m-%d")
            if maint_date > datetime.now():
                maintenance_skipped += 1
                continue
        except:
            maintenance_skipped += 1
            continue

        technician_name = row.get("technician_name", "")
        if not technician_name or not technician_name.replace(" ", "").isalpha():
            maintenance_skipped += 1
            continue

        status = row.get("status", "")
        if status not in valid_status_maint:
            maintenance_skipped += 1
            continue

        maintenance_valid_rows.append(row)

if maintenance_valid_rows:
    with open("cleaned/maintenance_log_validated.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=maintenance_valid_rows[0].keys())
        writer.writeheader()
        writer.writerows(maintenance_valid_rows)

print("✅ maintenance_log.csv validated")
print(" Skipped records:", maintenance_skipped)

