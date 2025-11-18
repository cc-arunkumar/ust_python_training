#Task UST INDIA – Employee Data Processing
import json

RAW_FILE = "employees_raw_new.json"
CLEAN_FILE = "employees_cleaned.json"
ERROR_FILE = "employees_errors.json"

required_fields= ["emp_id", "name", "age", "salary", "department", "phone", "email"]

def clean_name(name: str):
    return " ".join(name.strip().split())

def is_valid_age(age):
    try:
        age_int = int(age)
        return 18 <= age_int <= 65
    except Exception:
        return False

def is_valid_salary(salary):
    try:
        salary_int = int(salary)
        return salary_int > 0
    except Exception:
        return False

def is_valid_phone(phone):
    return bool(phone.isnumeric()==True and len(phone)==10)

def is_valid_email(email):
    if "@" not in email:
        return False
    parts = email.split("@")
    return len(parts) == 2 and parts[0] != "" and parts[1] != ""

def validate_employee(emp):

    for field in required_fields:
        if field not in emp or str(emp[field])=="" or emp[field]==None:
            return False, f"Missing field: {field}", emp

    emp["name"] = clean_name(emp["name"])

    if not is_valid_age(emp["age"]):
        return False, "Invalid age", emp
    emp["age"] = int(emp["age"])

    if not is_valid_salary(emp["salary"]):
        return False, "Salary must be positive number", emp
    emp["salary"] = int(emp["salary"])

    if not is_valid_phone(emp["phone"]):
        return False, "Invalid phone number", emp

    if not is_valid_email(emp["email"]):
        return False, "Invalid email", emp
    
    if emp["department"].strip() == "":
        return False, "Invalid department", emp

    return True, "", emp

with open(RAW_FILE, "r") as f:
    data = json.load(f)

    employees = data.get("employees", [])
    cleaned = []
    errors = []

    for emp in employees:
        valid, reason, cleaned_emp = validate_employee(emp)
        if valid:
            cleaned.append(cleaned_emp)
        else:
            errors.append({"emp_id": emp.get("emp_id", "UNKNOWN"), "error_reason": reason})

    with open(CLEAN_FILE, "w") as f:
        json.dump({"cleaned_employees": cleaned}, f, indent=2)

    with open(ERROR_FILE, "w") as f:
        json.dump({"errors": errors}, f, indent=2)

    print(f"Valid employees: {len(cleaned)}")
    print(f"Invalid Employees: {len(errors)}")

#Sample Execution
# Valid employees: 26
# Invalid Employees: 24
