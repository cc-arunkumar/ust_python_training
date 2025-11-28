import csv
from typing import List
from pydantic import ValidationError
from datetime import date

# Function to read CSV file and return data as a list of dictionaries
def read_csv(file_path: str) -> List[dict]:
    with open(file_path, newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)  # Read the CSV into a dictionary format
        data = [row for row in reader]  # Convert reader to a list of dictionaries
        print(f"Read {len(data)} rows from {file_path}")  # Print the number of rows read
        return data

# Function to write data to a CSV file
def write_csv(file_path: str, data: List[dict]):
    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())  # Use the keys of the first row as fieldnames
        writer.writeheader()  # Write the header row
        writer.writerows(data)  # Write all data rows
        print(f"Written {len(data)} rows to {file_path}")  # Print the number of rows written

# Function to validate data against a model and save the valid data to an output CSV file
def validate_and_save_data(input_file: str, output_file: str, model_class):
    data = read_csv(input_file)  # Read data from the input CSV file
    if not data:  # Check if the file contains no data
        print("No data found in the input file.")  # Print a message if the file is empty
        return

    valid_data = []  # Initialize an empty list to store valid data

    # Iterate over each row in the data
    for row in data:
        try:
            # Convert all fields of type date in the model to proper date objects, if present
            for field, field_type in model_class.__annotations__.items():
                if field_type is date and row.get(field):
                    try:
                        row[field] = date.fromisoformat(row[field])  # Convert string to date
                    except ValueError:
                        print(f"Invalid date in {field}: {row[field]} → setting to None")  # Handle invalid date format
                        row[field] = None  # Set invalid dates to None

            # Handle optional fields (set empty strings or missing fields to None)
            if "assigned_to" in row and row["assigned_to"] == "":  # If "assigned_to" is empty, set it to None
                row["assigned_to"] = None
            if "last_updated" in row and not row["last_updated"]:  # If "last_updated" is missing or empty, set it to None
                row["last_updated"] = None

            # Validate the row using the model class
            validated_row = model_class(**row)
            valid_data.append(validated_row.dict())  # Add validated row to valid_data list
            print("Row validated successfully")  # Print success message for validated row

        except ValidationError as e:  # Catch validation errors if the row doesn't match the model schema
            print(f" Validation failed for row: {row}")  # Print the row that failed validation
            for err in e.errors():  # Iterate over all validation errors
                print(f"   - {err['loc']}: {err['msg']}")  # Print the location and error message for each validation issue

    # If there is valid data, write it to the output CSV file
    if valid_data:
        write_csv(output_file, valid_data)  # Write the valid data to the output CSV file
    else:
        # If no valid data, create an empty file with headers
        with open(output_file, mode='w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)  # Create a CSV writer object
            writer.writerow(model_class.__annotations__.keys())  # Write the model's field names as headers
        print(f" No valid data, created empty file {output_file}")  # Print a message indicating an empty file was created
