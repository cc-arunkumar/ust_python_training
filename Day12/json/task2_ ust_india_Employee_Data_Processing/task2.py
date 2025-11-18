# JSON
#  UST INDIA – Employee Data Processing 
# Task 
# Scenario
#  UST HR India collects employee data from different offices:
#  Trivandrum
#  Kochi
#  Bangalore
#  Chennai
#  Pune
#  Hyderabad
#  The raw data is stored in a 
# However, the data:
#  contains missing fields
#  contains invalid salaries
#  employees_raw.json file.
#  contains wrong phone formats
#  contains extra spaces
#  contains mixed languages Indian names)
#  contains multiple religions, genders, regions
#  contains employees from all over India
#  Your task:
#   Read the raw JSON
#   Validate & clean the data
# Generate a new clean JSON file 
# employees_cleaned.json
# Generate an error file 
# employees_errors.json

import json

input_path = "Day12\\json\\task2_ ust_india_Employee_Data_Processing\\employees_raw.json"

#list to store valid and invalid
valid_employees = []
error_employees = []

with open(input_path, "r") as reading_json:
    load_file = json.load(reading_json)

# store the employee list in another variable
column_files = load_file["employees"]

#In the list get first row key values
expected_fields = list(column_files[0].keys())

#Iterate the json file with employee list
for emp in load_file["employees"]:
    missing_fields = []  # Reset for each employee

    # Check for missing or empty required fields
    for field in expected_fields:
        if field not in emp or emp[field] is None or str(emp[field]).strip() == "":
            missing_fields.append(field)

    # Name cleaning
    if "name" in emp and emp["name"] is not None and str(emp["name"]).strip() != "":
        emp["name"] = " ".join(str(emp["name"]).split())

    # Age validation
    age = emp.get("age")
    if age is None or str(age).strip() == "":
        missing_fields.append("age (missing)")
    else:
        try:
            age_int = int(age)
            if age_int < 18 or age_int > 65:
                missing_fields.append("age (must be 18-65)")
        except (ValueError, TypeError):
            missing_fields.append("age (must be a number)")

    # Salary validation
    salary = emp.get("salary")
    if salary is None or str(salary).strip() == "" or not str(salary).isdigit() or int(salary) <= 0:
        missing_fields.append("salary (must be positive number)")

    # Phone number validation (fixed logic!)
    pn = str(emp.get("phone", "")).strip()
    if not (pn.isdigit() and len(pn) == 10):
        missing_fields.append("phone (must be 10 digits)")

    # Email validation
    email = str(emp.get("email", "")).strip()
    if not ("@" in email and "." in email.split("@")[-1] and not email.startswith("@") and not email.endswith("@")):
        missing_fields.append("email (invalid format)")

    # Department validation
    dep = emp.get("department")
    if dep is None or str(dep).strip() == "":
        missing_fields.append("department (cannot be empty)")

    # Decide where to put the employee
    if missing_fields:
        error_employees.append({
            "emp_id": emp.get("emp_id", "unknown"),
            "data": emp,
            "errors": missing_fields
        })
    else:
        valid_employees.append(emp)

# seperate files for valid and error
output_valid_path = "Day12\\json\\task2_ ust_india_Employee_Data_Processing\\valid_employees.json"
output_error_path = "Day12\\json\\task2_ ust_india_Employee_Data_Processing\\error_employees.json"

with open(output_valid_path, "w") as f:
    json.dump({"employees": valid_employees}, f, indent=4)

with open(output_error_path, "w") as f:
    json.dump({"employees": error_employees}, f, indent=4)

print(f"Processing complete!")
print(f"Valid employees: {len(valid_employees)}")
print(f"Error employees: {len(error_employees)}")

# sample output:

# Processing complete!
# Valid employees: 26
# Error employees: 24