import json   

cleaned = []   
errors = []    

# read raw employee data from JSON file
with open("employees_raw.json", "r") as employee_data_processing:
    data = json.load(employee_data_processing)
    employees = data["employees"]

# get all field names from first employee record
required_fields = list(employees[0].keys())

# loop through each employee record
for emp in employees:
    # check if any required field is missing or empty
    missing = any(emp[field] is None or str(emp[field]).strip() == "" for field in required_fields)
    if missing:
        errors.append({"id": emp[required_fields[0]], "error_reason": "field is none"})
        continue

    # clean up name (remove extra spaces)
    emp[required_fields[1]] = " ".join(emp[required_fields[1]].split())

    # validate age
    age = int(emp[required_fields[2]])
    if age < 18 or age > 65:
        errors.append({"id": emp[required_fields[0]], "error_reason": "Age is not valid"})
        continue

    # validate email
    if "@" not in emp[required_fields[9]] or emp[required_fields[9]].count("@") != 1:
        errors.append({"id": emp[required_fields[0]], "error_reason": "Invalid email"})
        continue

    try:
        # validate salary and phone number
        salary = int(emp[required_fields[7]])
        phone = str(emp[required_fields[8]])

        if salary <= 0:
            errors.append({"id": emp[required_fields[0]], "error_reason": "Invalid Salary"})
            continue

        if not phone.isdigit() or len(phone) != 10:
            errors.append({"id": emp[required_fields[0]], "error_reason": "Invalid phone number"})
            continue
    except Exception:
        errors.append({"id": emp[required_fields[0]], "error_reason": "invalid phone number"})
        continue

    # if all checks pass, add to cleaned list
    cleaned.append(emp)

# print summary counts
print("Cleaned Employees:", len(cleaned))
print("Error Employees:", len(errors))

# save errors to employees_errors.json
with open("employees_errors.json", "a") as employee_data_processing:
    json.dump(errors, employee_data_processing, indent=2)

# save cleaned employees to employees_cleaned.json
with open("employees_cleaned.json", "a") as employee_data_processing:
    json.dump(cleaned, employee_data_processing, indent=2)



#o/p:
# Cleaned Employees: 26
# Error Employees: 24