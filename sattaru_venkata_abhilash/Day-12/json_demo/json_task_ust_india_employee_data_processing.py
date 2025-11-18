import json
import re
 
# Open and read the raw JSON employee file
with open("employees_raw.json","r") as employee_file:
    json_reader = json.load(employee_file)
   
    # Extract the list of employee records
    employee_data = json_reader['employees']

# Extract all header names from the first employee entry
headers = list(employee_data[0].keys())

# Lists to store valid and invalid employee records
errors_list = []
clean_list = []

# Process each employee record
for row in employee_data:

    # Check if the 2nd field (e.g., name) is empty
    if row[headers[1]] == "":
        errors = {"emp_id": row[headers[0]], "error_reason": "missing field"}
        errors_list.append(errors)
        continue
   
    # Normalize whitespace inside the name (remove multiple spaces)
    row[headers[1]] = " ".join(row[headers[1]].split())
   
    # Validate age is an integer
    try:
        age = int(row[headers[2]])
    except (ValueError, TypeError):
        errors = {"emp_id": row[headers[0]], "error_reason": "Age parse to int"}
        errors_list.append(errors)    
        continue              
 
    # Validate age range
    if not (18 < row[headers[2]] < 65):
        errors = {"emp_id": row[headers[0]], "error_reason": "age range"}
        errors_list.append(errors)
        continue

    # Validate salary is a valid positive integer
    try:
        salary = int(row[headers[7]])

        # Salary <= 0 is not allowed
        if salary <= 0:
            errors = {"emp_id": row[headers[0]], "error_reason": "salary negative"}
            errors_list.append(errors)
            continue

        # Salary cannot be empty
        elif salary == '':
            errors = {"emp_id": row[headers[0]], "error_reason": "salary empty"}
            errors_list.append(errors)
            continue

    except (ValueError, TypeError):
        errors = {"emp_id": row[headers[0]], "error_reason": "salary"}
        errors_list.append(errors)
        continue

    # Validate phone number length must be exactly 10 digits
    if not (len(row[headers[8]]) == 10):
        errors = {"emp_id": row[headers[0]], "error_reason": "length phone number"}
        errors_list.append(errors)
        continue
 
    # Validate phone number can be converted to integer
    try:
        phone_numer = int(row[headers[8]])
    except (ValueError, TypeError):
        errors = {"emp_id": row[headers[0]], "error_reason": "phone number parse"}
        errors_list.append(errors)
        continue
   
    # Validate email format using regex
    patterns = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if not re.match(patterns, row[headers[9]]):
        errors = {"emp_id": row[headers[0]], "error_reason": "email"}
        errors_list.append(errors)
        continue

    # Validate department field is not missing
    if row[headers[6]] == "" or row[headers[8]] is None:
        errors = {"emp_id": row[headers[0]], "error_reason": "department missing"}
        errors_list.append(errors)
        continue

    # If all validations pass, add to cleaned list
    clean_list.append(row)

# Print counts for debugging
print(len(clean_list))
print(len(errors_list))

# Prepare cleaned employee JSON output
cleaned_list = {}
cleaned_list["cleaned_employee"] = clean_list

# Prepare error JSON output
new_error = {}
new_error["errors"] = errors_list
 
# Write errors into employees_errors.json
with open("employees_errors.json ","w") as file:
    write = json.dump(new_error, file, indent=2)

# Write valid employees into employees_cleaned.json
with open("employees_cleaned.json","w") as cleaned_file:
    write = json.dump(cleaned_list, cleaned_file, indent=2)