import csv  # Import csv module to handle reading/writing CSV files
import datetime  # Import datetime module to work with dates
import re  # Import regex module for pattern matching (validation)

# Define valid sets for department, location, and status fields
valid_departments = {"IT", "HR", "Finance", "Admin", "Sales", "Support"}  # Allowed departments
valid_locations = {"Trivandrum", "Bangalore", "Chennai", "Hyderabad"}  # Allowed office locations
valid_statuses = {"Active", "Inactive", "Resigned"}  # Allowed employee statuses

valid_rows = []  # List to store rows that pass validation checks

# File paths for input and output CSV files
input_file = r"C:\Users\Administrator\Desktop\ust_python_training\Rohit\day20\AIIMS_PLUS\database\employee_directory(in).csv"  # Input file path
output_file = r"C:\Users\Administrator\Desktop\ust_python_training\Rohit\day20\AIIMS_PLUS\database\new_employee_directory(in).csv"  # Output file path

# Open the input CSV file for reading
with open(input_file, newline="", encoding="utf-8") as infile:
    reader = csv.DictReader(infile)  # Read CSV rows as dictionaries (keys = column names)
    fieldnames = reader.fieldnames  # Store header field names for later writing

    # Iterate through each row in the input CSV
    for row in reader:
        errors = []  # Initialize list to collect validation errors for this row

        # emp_code must start with "USTEMP-" followed by 4 digits (e.g., USTEMP-1234)
        if not re.match(r"^USTEMP-\d{4}$", row["emp_code"]):
            errors.append("Invalid emp_code")

        # email must follow standard email format (username@domain.extension)
        if not re.match(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$", row["email"]):
            errors.append("Invalid email")

        # phone must be exactly 10 digits (no spaces, no special characters)
        if not re.match(r"^\d{10}$", row["phone"]):
            errors.append("Invalid phone")

        # department must be one of the allowed departments
        if row["department"] not in valid_departments:
            errors.append("Invalid department")

        # location must be one of the allowed office locations
        if row["location"] not in valid_locations:
            errors.append("Invalid location")

        # join_date must exist and should not be empty
        if not row["join_date"]:
            errors.append("Missing join_date")
        

        # status must be one of the allowed statuses
        if row["status"] not in valid_statuses:
            errors.append("Invalid status")

        # If errors exist, print them with emp_code reference
        if errors:
            print(f"Row {row.get('emp_code','?')} errors: {errors}")
        else:
            valid_rows.append(row)  # If no errors, add row to valid_rows list

# Write all valid rows to the output CSV file
with open(output_file, "w", newline="", encoding="utf-8") as outfile:
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)  # Create writer with same headers
    writer.writeheader()  # Write header row
    writer.writerows(valid_rows)  # Write all valid rows

# Print summary of validation process
print(f"Validation complete. {len(valid_rows)} valid rows written.")
