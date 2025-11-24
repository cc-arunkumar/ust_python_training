import json
import re

# Define the path where input and output JSON files are located
path = "C:/Users/303391/Desktop/ust_python_training/arjun_j_s/day_12/task2/"

# ------------------------------------------------------------
# Function: clean_name
# Purpose: Normalize employee names by removing extra spaces
# ------------------------------------------------------------
def clean_name(name):
    name_split = name.split()   # Split name into words
    new_name = ""
    for i in name_split:
        new_name += i + " "     # Rebuild name with single spaces
    return new_name.strip()     # Remove trailing space

# ------------------------------------------------------------
# Function: validate
# Purpose: Validate employee record fields against requirements
# ------------------------------------------------------------
def validate(item, req):
    try:
        for data in item:
            # Check if field exists in required keys
            if data in req:
                # Ensure field is not empty or None
                if (len(str(item[data]).strip()) == 0 or item[data] == None):
                    return False, "No valid value"
                else:
                    # Validate age (between 18 and 65)
                    if data == req[2] and int(item[req[2]]):
                        if int(item[req[2]]) > 65 or int(item[req[2]]) < 18:
                            return False, "Not a valid age for employee"
                    # Validate salary (non-negative)
                    if data == req[7] and int(item[req[7]]) < 0:
                        return False, "Not valid salary"
                    # Validate phone number (must be 10 digits)
                    if data == req[8] and int(item[req[8]]) and len(str(item[req[8]])) != 10:
                        return False, "Not a valid phone number"
                    # Validate email (must contain exactly one '@')
                    if data == req[9] and len(item[req[9]].split("@")) != 2:
                        return False, "Not a valid email"
            else:
                # If any required field is missing
                return False, "Field Missing"
    except Exception as e:
        # Catch unexpected errors during validation
        return False, str(e)
    else:
        # If all validations pass
        return True, "Success"

# ------------------------------------------------------------
# Main Program Execution
# ------------------------------------------------------------

# Load raw employee data from JSON file
with open(path + "employees_raw.json", "r") as employee_data_file:
    emp_data = json.load(employee_data_file)
    emp_cleaned = []   # List to store valid employee records
    emp_skipped = []   # List to store invalid employee records with error messages
    
    # Extract required field names from the first employee record
    req = list(emp_data["employees"][0].keys())
    
    # Validate each employee record
    for data in emp_data["employees"]:
        condition, stmt = validate(data, req)
        if condition:
            # Clean employee name before saving
            data[req[1]] = clean_name(data[req[1]])
            emp_cleaned.append(data)
        else:
            # Store skipped record with reason for failure
            emp_skipped.append({data[req[0]]: stmt})

# Save cleaned employee records into a new JSON file
with open(path + "employees_cleaned.json", "w") as employee_data_file:
    json.dump(emp_cleaned, employee_data_file, indent=2)

# Save skipped employee records with error messages into another JSON file
with open(path + "employees_error.json", "w") as employee_data_file:
    json.dump(emp_skipped, employee_data_file, indent=2)

# Print summary statistics
print("Total records", len(emp_data["employees"]))
print("Total cleaned", len(emp_cleaned))
print("Total skipped", len(emp_skipped))