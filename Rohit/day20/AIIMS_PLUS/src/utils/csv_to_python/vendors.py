import csv   # Import csv module to handle reading and writing CSV files
import re    # Import regex module for pattern-based validation

error_list = []   # List to store invalid rows along with their error messages
answer_rows = []  # List to store valid rows that pass all checks
valid_cities = ["Mumbai","Delhi","Bangalore","Chennai","Hyderabad","Pune","Kolkata"]  # Allowed city values

# File paths for input and output CSV files
input_file = r'C:\Users\Administrator\Desktop\ust_python_training\Rohit\day20\AIIMS_PLUS\database\vendor_master(in).csv'  # Input CSV file path
output_file = r'C:\Users\Administrator\Desktop\ust_python_training\Rohit\day20\AIIMS_PLUS\database\new_vendor_master(in).csv'  # Output CSV file path

# Open the input CSV file in read mode
with open(input_file, mode='r', newline='', encoding='utf-8') as file2:
    reader = csv.DictReader(file2)  # Read CSV rows as dictionaries (keys = column names)
    all_fields = reader.fieldnames  # Store header field names for later writing

    # Iterate through each row in the input CSV
    for row in reader:
        errors = []  # Collect validation errors for this row
        try:
            # Vendor name validation: must be 1–100 alphabetic characters or spaces
            if not re.match(r"^[A-Za-z\s]{1,100}$", row["vendor_name"]):
                errors.append(f"Invalid vendor_name for vendor_id {row['vendor_id']}")

            # Contact person validation: must be 1–100 alphabetic characters or spaces
            if not re.match(r"^[A-Za-z\s]{1,100}$", row["contact_person"]):
                errors.append(f"Invalid contact_person for vendor_id {row['vendor_id']}")

            # Contact phone validation: must be a 10-digit number starting with 6–9
            if not re.match(r"^[6-9]\d{9}$", row["contact_phone"]):
                errors.append(f"Invalid contact_phone for vendor_id {row['vendor_id']}")

            # GST number validation: must be exactly 15 alphanumeric characters
            if not re.match(r"^[A-Za-z0-9]{15}$", row["gst_number"]):
                errors.append(f"Invalid gst_number for vendor_id {row['vendor_id']}")

            # Email validation: must follow standard email format
            if not re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", row["email"]):
                errors.append(f"Invalid email for vendor_id {row['vendor_id']}")

            # Address validation: must not exceed 200 characters
            if len(row["address"]) > 200:
                errors.append(f"Invalid address length for vendor_id {row['vendor_id']}")

            # City validation: must be one of the allowed cities
            if row["city"] not in valid_cities:
                errors.append(f"Invalid city '{row['city']}' for vendor_id {row['vendor_id']}")

            # Active status validation: must be either "Active" or "Inactive"
            if row["active_status"] not in ["Active", "Inactive"]:
                errors.append(f"Invalid active_status for vendor_id {row['vendor_id']}")
        except Exception as e:  # Catch unexpected errors during validation
            errors.append(f"Error: {e}")

        # If no errors, add row to valid rows list
        if not errors:
            answer_rows.append(row)
        else:
            # If errors exist, add row with vendor_id and error messages to error_list
            error_list.append({"vendor_id": row["vendor_id"], "errors": errors})

# Write valid rows into new CSV file
with open(output_file, mode='w', newline='', encoding='utf-8') as file_out:
    writer = csv.DictWriter(file_out, fieldnames=all_fields)  # Create writer with same headers
    writer.writeheader()  # Write header row
    writer.writerows(answer_rows)  # Write all valid rows

# Print summary of validation results
print(f"Total valid rows written: {len(answer_rows)}")  # Show count of valid rows
print(f"Total invalid rows: {len(error_list)}")  # Show count of invalid rows
