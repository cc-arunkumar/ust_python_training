# JSON
# UST INDIA – Employee Data Processing

# Task
# Scenario
# UST HR India collects employee data from different offices:
# Trivandrum
# Kochi
# Bangalore
# Chennai
# Pune
# Hyderabad
# The raw data is stored in a employees_raw.json file.

# However, the data:
# contains missing fields
# contains invalid salaries
# contains wrong phone formats
# contains extra spaces
# contains mixed languages (Indian names)
# contains multiple religions, genders, regions
# contains employees from all over India

# Your task:
# 1. Read the raw JSON
# 2. Validate & clean the data
# 3. Generate a new clean JSON file employees_cleaned.json
# 4. Generate an error file employees_errors.json
import json
import re

# Load raw employee data from JSON file
with open("employees_raw.json", "r") as employee_file:
    json_reader = json.load(employee_file)
    employee_data = json_reader['employees']

# Extract header (field) names from the first record
headers = list(employee_data[0].keys())

# Lists for storing valid data and rows with errors
errors_list = []
clean_list = []


# Iterate through each employee row and validate fields
for row in employee_data:

    # ---------- Check for missing values in all required columns ----------
    for k in headers:
        if row[k] == "":
            errors = {"emp_id": row[headers[0]], "error_reason": "missing field"}
            errors_list.append(errors)
            continue

    # ---------- Normalize full name (remove extra spaces) ----------
    row[headers[1]] = " ".join(row[headers[1]].split())

    # ---------- Validate Age: must be an integer ----------
    try:
        age = int(row[headers[2]])
    except (ValueError, TypeError):
        errors = {"emp_id": row[headers[0]], "error_reason": "Age parse to int"}
        errors_list.append(errors)
        continue

    # ---------- Validate Age Range: must be 19–64 ----------
    if not (18 < age < 65):
        errors = {"emp_id": row[headers[0]], "error_reason": "age range"}
        errors_list.append(errors)
        continue

    # ---------- Validate Salary ----------
    try:
        salary = int(row[headers[7]])

        # Salary must be positive
        if salary <= 0:
            errors = {"emp_id": row[headers[0]], "error_reason": "salary negative"}
            errors_list.append(errors)
            continue

        # Salary cannot be empty
        elif salary == "":
            errors = {"emp_id": row[headers[0]], "error_reason": "salary empty"}
            errors_list.append(errors)
            continue

    except (ValueError, TypeError):
        # Non-integer salary
        errors = {"emp_id": row[headers[0]], "error_reason": "salary"}
        errors_list.append(errors)
        continue

    # ---------- Validate Phone Number Length (must be exactly 10 digits) ----------
    if not (len(row[headers[8]]) == 10):
        errors = {"emp_id": row[headers[0]], "error_reason": "length phone number"}
        errors_list.append(errors)
        continue

    # ---------- Validate phone number is numeric ----------
    try:
        phone_number = int(row[headers[8]])
    except (ValueError, TypeError):
        errors = {"emp_id": row[headers[0]], "error_reason": "phone number parse"}
        errors_list.append(errors)
        continue

    # ---------- Validate Email Format Using Regex ----------
    email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if not re.match(email_pattern, row[headers[9]]):
        errors = {"emp_id": row[headers[0]], "error_reason": "email"}
        errors_list.append(errors)
        continue

    # ---------- Validate Department and Phone Number Presence ----------
    if row[headers[6]] == "" or row[headers[8]] is None:
        errors = {"emp_id": row[headers[0]], "error_reason": "department missing"}
        errors_list.append(errors)
        continue

    # If all checks passed, append to clean list
    clean_list.append(row)


# Print summary counts
print(len(clean_list))    
print(len(errors_list))    


# Write Cleaned Data to JSON File
cleaned_list = {"cleaned_employee": clean_list}

with open("employees_cleaned.json", "w") as cleaned_file:
    json.dump(cleaned_list, cleaned_file, indent=2)


# Write Errors to JSON File
new_error = {"errors": errors_list}

with open("employees_errors.json", "w") as file:
    json.dump(new_error, file, indent=2)
