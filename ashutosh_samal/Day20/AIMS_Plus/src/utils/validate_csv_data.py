import os
import csv
from src.model.asset_model import AssetCreate
from src.model.employee_model import EmployeeCreate
from src.model.maintenance_model import MaintenanceCreate
from src.model.vendor_model import VendorCreate

# Define the root directory of your project (you can adjust this to match the actual path)
root_dir = r"C:\Users\Administrator\Desktop\training\ust_python_training\ashutosh_samal\Day20\AIMS_Plus\database\sample_data"

# Dictionary to store the relative file names and the model classes
file_info = {
    "asset": {
        "input_filename": "asset_inventory.csv",
        "output_filename": "valid_asset.csv",
        "model": AssetCreate
    },
    "employee": {
        "input_filename": "employee_directory.csv",
        "output_filename": "valid_employee.csv",
        "model": EmployeeCreate
    },
    "maintenance": {
        "input_filename": "maintenance_log.csv",
        "output_filename": "valid_maintenance.csv",
        "model": MaintenanceCreate
    },
    "vendor": {
        "input_filename": "vendor_master.csv",
        "output_filename": "valid_vendor.csv",
        "model": VendorCreate
    }
}

# Function to validate and process the CSV data dynamically
def validate_csv(input_file_path: str, output_file_path: str, model_class):
    valid_rows = []  # List to store valid rows
    errors = []  # List to store rows with errors

    # Open the input CSV file for reading
    with open(input_file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)  # Read the CSV as a dictionary
        fieldnames = reader.fieldnames  # Get the field names (columns) from the CSV

        # Open the output CSV file for writing validated data
        with open(output_file_path, mode='w', newline='', encoding='utf-8') as output_file:
            writer = csv.DictWriter(output_file, fieldnames=fieldnames)  # Write header to output file
            writer.writeheader()

            # Iterate over each row in the CSV
            for row in reader:
                try:
                    model_instance = model_class(**row)  # Validate the row using the provided model class
                    valid_rows.append(row)  # Add valid rows to the list
                    writer.writerow(row)  # Write valid rows to the output CSV

                except Exception as e:
                    errors.append({
                        "row": row,  # Store the row with validation error
                        "message": str(e)  # Store the validation error message
                    })

    # If there are any validation errors, print them
    if errors:
        print("Validation failed with errors:")
        for error in errors:
            print(f"Row {error['row']}: {error['message']}")

    # Return the success message with the count of valid records
    return f"Successfully imported {len(valid_rows)} valid records."


# Loop through the file information dictionary to dynamically construct paths and validate
for model_key, model_info in file_info.items():
    input_file_path = os.path.join(root_dir, model_info["input_filename"])
    output_file_path = os.path.join(root_dir, model_info["output_filename"])
    model_class = model_info["model"]

    # Execute the CSV validation and processing for the current model
    result = validate_csv(input_file_path, output_file_path, model_class)
    print(f"{model_key.capitalize()} Result: {result}")  # Print the result for each model validation
