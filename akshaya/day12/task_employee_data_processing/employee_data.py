import json

def load_employees(file_path):
    
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
            return data.get("employees", [])
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading file: {e}")
        return []


def get_required_fields(employees):
    # Dynamically get required fields from first employee.
    if not employees:
        return []
    return list(employees[0].keys())   


def is_valid_age(age):
    try:
        age = int(age)
        return 18 <= age <= 65
    except Exception:
        return False


def is_valid_salary(salary):
    try:
        return float(salary) > 0
    except Exception:
        return False


def is_valid_phone(phone):
    return isinstance(phone, str) and phone.isdigit() and len(phone) == 10


def is_valid_email(email):
    return isinstance(email, str) and "@" in email and "." in email.split("@")[-1]


def validate_employee(emp, required_fields):
    # Validate every employee.
    # Check missing or empty fields
    for field in required_fields:
        if field not in emp:
            return False
        value = emp[field]
        if value is None or value == "" or (isinstance(value, str) and value.strip() == ""):
            return False

    # Field-specific validation
    if not is_valid_age(emp.get("age")):
        return False

    if not is_valid_salary(emp.get("salary")):
        return False

    if not is_valid_phone(emp.get("phone")):
        return False

    if not is_valid_email(emp.get("email")):
        return False

    if not emp.get("department") or emp["department"].strip() == "":
        return False

    return True


def process_employees(file_path):
    employees = load_employees(file_path)
    total = len(employees)

    required = get_required_fields(employees)

    valid_count = 0
    invalid_count = 0

    for emp in employees:
        if validate_employee(emp, required):
            valid_count += 1
        else:
            invalid_count += 1

    print(f"Total employees: {total}")
    print(f"Valid employees: {valid_count}")
    print(f"Invalid employees: {invalid_count}")


process_employees("employees_raw.json")


