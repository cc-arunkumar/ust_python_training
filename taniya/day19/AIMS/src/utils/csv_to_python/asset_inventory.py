import csv  # Import the csv module to handle reading and writing CSV files

error = []  # List to store error messages for invalid rows
answer_rows = []  # List to store valid rows that pass all checks
serial_number_Set = set()  # Set to track unique serial numbers and prevent duplicates

# Allowed values (validation constraints for different fields)
allowed_asset_types = {"Laptop", "Monitor", "Keyboard", "Mouse"}  # Valid asset types
allowed_manufacturers = {"Dell", "HP", "Samsung", "Lenovo","LG"}  # Valid manufacturers
allowed_conditions = {"New", "Good", "Used", "Damaged"}  # Valid condition statuses
allowed_locations = {"Trivandrum", "Chennai", "Hyderabad", "Bangalore"}  # Valid office locations
allowed_status = {"Available", "Assigned", "Repair", "Retired","Fair"}  # Valid asset statuses

# File paths for input and output CSV files
input_file = r"C:\Users\Administrator\Desktop\Training\ust_python_training\taniya\day19\AIMS\database\sample_data\asset_inventory(in).csv"  # Input file path
output_file = r"C:\Users\Administrator\Desktop\Training\ust_python_training\taniya\day19\AIMS\database\sample_data\final\validated_inventory.csv"  # Output file path

# Open the input CSV file in read mode
with open(input_file, mode="r", encoding="utf-8") as file1:
    reader = csv.DictReader(file1)  # Read CSV as a dictionary (column names as keys)
    rows = list(reader)  # Convert reader object into a list of rows (dicts)

    # Iterate through each row in the CSV
    for row in rows:
        asset_id = row.get("asset_id")  # Get asset ID
        asset_tag = row.get("asset_tag")  # Get asset tag (must start with UST)
        asset_type = row.get("asset_type")  # Get asset type
        serial_number = row.get("serial_number")  # Get serial number (must be unique)
        manufacturer = row.get("manufacturer")  # Get manufacturer name
        model = row.get("model")  # Get model name
        purchase_date = row.get("purchase_date")   # Get purchase date (not validated)
        warranty_years = row.get("warranty_years")  # Get warranty years
        condition_status = row.get("condition_status")  # Get condition status
        assigned_to = row.get("assigned_to")  # Get assigned employee (optional validation)
        location = row.get("location")  # Get location
        asset_status = row.get("asset_status")  # Get asset status

        try:
            # Asset tag check (must start with "UST")
            output = asset_tag.split("-")  # Split asset tag by "-"
            if output[0] != "UST":  # First part must be "UST"
                raise ValueError("Asset tag must start with UST")

            # Asset type check (must be in allowed list)
            if asset_type not in allowed_asset_types:
                raise ValueError("Invalid asset type")

            # Serial number check (must be unique and not empty)
            if not serial_number or serial_number in serial_number_Set:
                raise ValueError("Duplicate or missing serial number")
            serial_number_Set.add(serial_number)  # Add serial number to set

            # Model check (must not be empty or whitespace)
            if not model or not model.strip():
                raise ValueError("Model is missing")

            # Warranty years check (must be integer between 1 and 5)
            try:
                warranty_years = int(warranty_years)  # Convert to integer
                if warranty_years < 1 or warranty_years > 5:  # Validate range
                    raise ValueError("Warranty years must be between 1 and 5")
            except Exception:  # Handle non-integer values
                raise ValueError("Warranty years must be an integer")

            # Condition status check (must be in allowed list)
            if condition_status not in allowed_conditions:
                raise ValueError("Invalid condition status")

            # Manufacturer check (must be in allowed list)
            if manufacturer not in allowed_manufacturers:
                raise ValueError("Invalid manufacturer")

            # Location check (must be in allowed list)
            if location not in allowed_locations:
                raise ValueError("Invalid location")

            # Asset status check (must be in allowed list)
            if asset_status not in allowed_status:
                raise ValueError("Invalid asset status")

        except Exception as e:  # Catch validation errors
            error.append(f"{asset_id}: {str(e)}")  # Store error with asset ID
            continue  # Skip this row and move to the next

        answer_rows.append(row)  # Add valid row to answer_rows

# If there are valid rows, write them to the output CSV file
if answer_rows:
    with open(output_file, mode="w", encoding="utf-8", newline="") as file1:
        fieldnames = answer_rows[0].keys()  # Get column names from first row
        writer = csv.DictWriter(file1, fieldnames=fieldnames)  # Create CSV writer
        writer.writeheader()  # Write header row
        writer.writerows(answer_rows)  # Write all valid rows

# Print summary of results
print(f"Valid rows written: {len(answer_rows)}")  # Show count of valid rows
print("Errors:")  # Print error section
for e in error:  # Iterate through errors
    print("-", e)  # Print each error with a dash
