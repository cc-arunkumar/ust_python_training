from models.asset_model import AssetInventory
from src.models.employee_model import Employee 
from src.models.maintenance_model import MaintenanceLog
from src.models.vendor_model import Vendor
import csv
from pydantic import ValidationError
import os

# Function to validate the CSV file
def validate_csv(csv_path):
    errors_list = []
    validated_list = []
    try:
        with open(csv_path, mode="r") as file:
            reader = csv.DictReader(file)
            for index, row in enumerate(reader, start=1):
                try:
                    asset_data = AssetInventory(**row)  # Validate using Pydantic model
                    validated_list.append(asset_data(exclude_unset=True))  
                    # Convert to dict
                except ValidationError as e:
                    errors_list.append(f"row:{index}: {e}")
            
            # Writing valid data to a new CSV file
            output_file_path = r"C:\UST PYTHON\Praveen\ust_python_training\praveen_d\day_18\task_2\aims_plus\database\output_data\valid_asset.csv"
            with open(output_file_path, mode="w", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=reader.fieldnames)
                writer.writeheader()
                writer.writerows(validated_list)

    except Exception as e:
        pass
        # print(f"An error occurred: {str(e)}")
    finally:
        print(f"Asset Valid_list:{len(validated_list)}")
        

# Example usage
csv_path = r'C:\UST PYTHON\Praveen\ust_python_training\praveen_d\day_18\task_2\aims_plus\database\sample_data\asset_inventory.csv'
validate_csv(csv_path)


# Function to validate each row in employee directory
def validate_employee(row):
    try:
        # Create Employee model instance to validate the row
        Employee(**row)
        return None  # All validations passed
    except ValidationError as e:
        raise ValidationError(f"Validation failed for row: {e.errors()}")

# Function to validate the entire CSV and write errors to a new file
def validate_csv(csv_path, output_file_path):
    errors = []
    valid_employee_list = []  # List to store valid rows
    try:
        with open(csv_path, mode='r') as file:
            reader = csv.DictReader(file)
            header = reader.fieldnames

            # Process each row in the CSV
            for index, row in enumerate(reader, start=1):
                try:
                    validate_employee(row)
                    valid_employee_list.append(row)
                except ValidationError as e:
                    errors.append(f"Row {index}: {e.message}")

        # Output file path for writing the valid employee rows
        output_file = os.path.join(output_file_path, "valid_employee.csv")

        # Write the valid rows to a new CSV file
        with open(output_file, mode='w', newline='') as output_file:
            writer = csv.DictWriter(output_file, fieldnames=header)
            writer.writeheader()
            writer.writerows(valid_employee_list)  # Write valid rows

        # Print the result based on the validation
        if errors:
            return f"Validation completed with errors. Errors are written to {output_file_path}."
        else:
            return f"No errors found. {len(valid_employee_list)} rows were validated successfully."

    except Exception as e:
        return f"An error occurred: {str(e)}"

# Example usage
csv_path_employee = r"C:\UST PYTHON\Praveen\ust_python_training\praveen_d\day_18\task_2\aims_plus\database\sample_data\employee_directory.csv"
output_file_path_employee = r'C:\UST PYTHON\Praveen\ust_python_training\praveen_d\day_18\task_2\aims_plus\database\output_data'

validation_result = validate_csv(csv_path_employee, output_file_path_employee)

print(validation_result)



# Function to validate a row in the CSV
def validate_maintenance(row, log_ids):
    try:
        # Create Pydantic model instance to validate the row
        MaintenanceLog(**row)
        return None  # All validations passed
    except ValidationError as e:
        raise ValidationError(f"Validation failed: {e.errors()}")


# Function to validate the entire CSV and write valid rows to a new file
def validate_csv(csv_path, output_file_path):
    log_ids = set()  # Set to track unique log_ids
    valid_maintenance = []

    try:
        with open(csv_path, mode='r') as file:
            reader = csv.DictReader(file)
            header = reader.fieldnames

            # Process each row in the CSV
            for index, row in enumerate(reader, start=1):
                try:
                    # Validate each maintenance row using the functions
                    validate_maintenance(row, log_ids)
                    valid_maintenance.append(row)  # If validation passes, add to valid list
                except ValidationError as e:
                    # Errors are handled here, but not saved in a separate file
                    pass
                    # print(f"Row {index}: {e.message}")

        # Output file path for writing the valid maintenance rows
        output_file = os.path.join(output_file_path, "valid_maintenance.csv")

        # Write the valid rows to a new CSV file
        with open(output_file, mode='w', newline='') as output_file:
            writer = csv.DictWriter(output_file, fieldnames=header)
            writer.writeheader()
            writer.writerows(valid_maintenance)  # Write valid rows

        # Return the result based on the validation
        if valid_maintenance:
            return f"All data is valid. {len(valid_maintenance)} rows validated successfully."
        else:
            return "No valid data found."

    except Exception as e:
        return f"An error occurred: {str(e)}"


# Example usage
csv_path_maintenance = 'C:\\UST PYTHON\\Praveen\\ust_python_training\\praveen_d\\day_18\\task_2\\aims_plus\\database\\sample_data\\maintenance_log.csv'
output_file_path_maintenance = r'C:\UST PYTHON\Praveen\ust_python_training\praveen_d\day_18\task_2\aims_plus\database\output_data'

# Run the validation
validation_result = validate_csv(csv_path_maintenance, output_file_path_maintenance)
# print(validation_result)


# Function to validate a row in the CSV
def validate_vendor(row, vendor_ids):
    try:
        # Create Pydantic model instance to validate the row
        Vendor(**row)
        return None  # All validations passed
    except ValidationError as e:
        raise ValidationError(f"Validation failed: {e.errors()}")


# Function to validate the entire CSV and write valid rows to a new file
def validate_csv(csv_path, output_file_path):
    vendor_ids = set()  # Set to track unique vendor_ids
    errors = []
    valid_vendor_list = []  # List to store valid rows

    try:
        with open(csv_path, mode='r') as file:
            reader = csv.DictReader(file)
            header = reader.fieldnames

            # Process each row in the CSV
            for index, row in enumerate(reader, start=1):
                try:
                    # Validate each vendor row using the functions
                    validate_vendor(row, vendor_ids)
                    valid_vendor_list.append(row)  # If validation passes, add to valid list
                except ValidationError as e:
                    # Errors are handled here, but not saved in a separate file
                    # print(f"Row {index}: {e.message}")
                    pass

        # Output file path for writing the valid vendor rows
        output_file = os.path.join(output_file_path, "valid_vendor.csv")

        # Write the valid rows to a new CSV file
        with open(output_file, mode='w', newline='') as output_file:
            writer = csv.DictWriter(output_file, fieldnames=header)
            writer.writeheader()
            writer.writerows(valid_vendor_list)  # Write valid rows

        # Return the result based on the validation
        if valid_vendor_list:
            return f"No errors found. {len(valid_vendor_list)} rows were validated successfully."
        else:
            return "No valid data found."

    except Exception as e:
        return f"An error occurred: {str(e)}"


# Example usage
csv_path_vendor = 'C:\\UST PYTHON\\Praveen\\ust_python_training\\praveen_d\\day_18\\task_2\\aims_plus\\database\\sample_data\\vendor_master.csv'
output_file_path_vendor = r'C:\UST PYTHON\Praveen\ust_python_training\praveen_d\day_18\task_2\aims_plus\database\output_data'

# Run the validation
validation_result = validate_csv(csv_path_vendor, output_file_path_vendor)
# print(validation_result)
