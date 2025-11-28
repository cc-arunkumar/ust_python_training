import csv

error = []   # list to store error messages
valid = []   # list to store valid rows
serial_number_Set = set()   # set to track unique serial numbers

# Allowed values for validation
allowed_asset_types = {"Laptop", "Monitor", "Keyboard", "Mouse"}
allowed_manufacturers = {"Dell", "HP", "Samsung", "Lenovo"}
allowed_conditions = {"New", "Good", "Used", "Damaged"}
allowed_locations = {"TVM", "Chennai", "Hyderabad", "Bangalore"}
allowed_status = {"Available", "Assigned", "Repair", "Retired"}

# Input and output file paths
input_file = r"C:\Users\Administrator\Desktop\PTraining\ust_python_training\sohan-kumar-rout\day-18\AIMS+\database\sampledata\asset_inventory(in).csv"
output_file = r"C:\Users\Administrator\Desktop\PTraining\ust_python_training\sohan-kumar-rout\day-18\AIMS+\database\sampledata\finaldata\asset_inventory_checked.csv"

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
            if output[0] != "UST":
                raise ValueError("Asset tag must start with UST")

            # Validate asset type
            if asset_type not in allowed_asset_types:
                raise ValueError("Invalid asset type")

            # Validate serial number (must be unique and not empty)
            if not serial_number or serial_number in serial_number_Set:
                raise ValueError("Duplicate or missing serial number")
            serial_number_Set.add(serial_number)

            # Validate model (must not be empty)
            if not model or not model.strip():
                raise ValueError("Model is missing")

            # Validate warranty years (must be integer between 1 and 5)
            try:
                warranty_years = int(warranty_years)
                if warranty_years < 1 or warranty_years > 5:
                    raise ValueError("Warranty years must be between 1 and 5")
            except Exception:
                raise ValueError("Warranty years must be an integer")

            # Validate condition status
            if condition_status not in allowed_conditions:
                raise ValueError("Invalid condition status")

            # Validate manufacturer
            if manufacturer not in allowed_manufacturers:
                raise ValueError("Invalid manufacturer")

            # Validate location
            if location not in allowed_locations:
                raise ValueError("Invalid location")

            # Validate asset status
            if asset_status not in allowed_status:
                raise ValueError("Invalid asset status")

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
print("Errors:")
for e in error:
    print("-", e)
