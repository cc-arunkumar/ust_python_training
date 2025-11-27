import csv

error = []
answer_rows = []
serial_number_Set = set()

# Allowed values
allowed_asset_types = {"Laptop", "Monitor", "Keyboard", "Mouse"}
allowed_manufacturers = {"Dell", "HP", "Samsung", "Lenovo"}
allowed_conditions = {"New", "Good", "Used", "Damaged"}
allowed_locations = {"TVM", "Chennai", "Hyderabad", "Bangalore"}
allowed_status = {"Available", "Assigned", "Repair", "Retired"}

input_file = r"C:\Users\Administrator\Desktop\ust_python_training\Rohit\day18\ust_ITSM\data\asset_inventory(in).csv"
output_file = r"C:\Users\Administrator\Desktop\ust_python_training\Rohit\day18\ust_ITSM\data\new_inventory.csv"

with open(input_file, mode="r", encoding="utf-8") as file1:
    reader = csv.DictReader(file1)
    rows = list(reader)

    for row in rows:
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
        try:
            # Asset tag check
            output = asset_tag.split("-")
            if output[0] != "UST":
                raise ValueError("Asset tag must start with UST")

            # Asset type check
            if asset_type not in allowed_asset_types:
                raise ValueError("Invalid asset type")

            # Serial number check
            if not serial_number or serial_number in serial_number_Set:
                raise ValueError("Duplicate or missing serial number")
            serial_number_Set.add(serial_number)

            # Model check
            if not model or not model.strip():
                raise ValueError("Model is missing")

            # Warranty years check
            try:
                warranty_years = int(warranty_years)
                if warranty_years < 1 or warranty_years > 5:
                    raise ValueError("Warranty years must be between 1 and 5")
            except Exception:
                raise ValueError("Warranty years must be an integer")

            # Condition status check
            if condition_status not in allowed_conditions:
                raise ValueError("Invalid condition status")

            # Manufacturer check
            if manufacturer not in allowed_manufacturers:
                raise ValueError("Invalid manufacturer")

            # Location check
            if location not in allowed_locations:
                raise ValueError("Invalid location")

            # Asset status check
            if asset_status not in allowed_status:
                raise ValueError("Invalid asset status")

        except Exception as e:
            error.append(f"{asset_id}: {str(e)}")
            continue

        answer_rows.append(row)

if answer_rows:
    with open(output_file, mode="w", encoding="utf-8", newline="") as file1:
        fieldnames = answer_rows[0].keys()
        writer = csv.DictWriter(file1, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(answer_rows)

print(f"Valid rows written: {len(answer_rows)}")
print("Errors:")
for e in error:
    print("-", e)
