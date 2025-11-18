# UST INDIA - Employee Data Processing Task
# 1. Read the raw JSON
# 2. Validate & clean the data
# 3. Generate a new clean JSON file employees_cleaned.json
# 4. Generate an error file employees_errors.json


import json

# Lists to track valid and invalid employee records
valid_employees=[]
invalid_employees=[]

# Validation function
def validate_employee(emp, required_fields):
    try:
        # Check required fields
        for field in required_fields:
            if field not in emp or emp[field] in [None, "", " "]:
                return False, "Missing field"

        # Clean name spacing
        emp["name"]=" ".join(emp["name"].split())

        # Age validation
        try:
            emp["age"]=int(emp["age"])
            if emp["age"]<18 or emp["age"]>65:
                return False, "Age is not valid"
        except:
            return False, "Age is not valid"

        # Salary validation
        try:
            emp["salary"]=int(emp["salary"])
            if emp["salary"]<=0:
                return False,"Invalid salary"
        except:
            return False,"Invalid salary"

        # Phone validation
        if not str(emp["phone"]).isdigit() or len(str(emp["phone"])) != 10:
            return False, "Invalid phone number"

        # Email validation (simple check, no regex)
        if "@" not in emp["email"]:
            return False, "Invalid email format"
        parts = emp["email"].split("@")
        if len(parts) != 2 or not parts[0] or not parts[1]:
            return False, "Invalid email format"

        # Department validation
        if emp["department"] in [None, "", " "]:
            return False, "Invalid department"

    except Exception:
        return False, "Invalid details"

    # If all checks pass
    return True, "Valid"

# Main program
def process_employees():
    with open("employees_raw.json", "r") as file:
        data = json.load(file)

    employees = data["employees"]
    print("Total employees:", len(employees))

    required_fields = ["emp_id", "name", "age", "salary", "department", "phone", "email"]

    for emp in employees:
        flag, reason = validate_employee(emp, required_fields)
        if flag:
            valid_employees.append(emp)
        else:
            invalid_employees.append({"emp_id": emp.get("emp_id", "UNKNOWN"), "error_reason": reason})

    # Save cleaned employees
    with open("employees_cleaned.json", "w") as f:
        json.dump({"cleaned_employees": valid_employees}, f, indent=2)

    # Save errors
    with open("employees_errors.json", "w") as f:
        json.dump({"errors": invalid_employees}, f, indent=2)

    # Print summary
    print("Valid employees:", len(valid_employees))
    print("Invalid employees:", len(invalid_employees))

# Run the program
process_employees()


# Output
# Total employees: 50
# Valid employees: 26
# Invalid employees: 24
