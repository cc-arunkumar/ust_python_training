import json
file_path = r"C:\Users\Administrator\Desktop\Prudhvi_Rajeev\ust_python_training\prudhvi_rajeev_kumar\day_12\json task\employees_raw.json"

with open(file_path, mode="r", encoding="utf-8") as file:
    data = json.load(file)
employees = data["employees"]

def clean_name(name: str) -> str:
    return " ".join(name.split()).strip()

def validate_age(age):
    try:
        age = int(age)
        return 18 <= age <= 65
    except (TypeError, ValueError):
        return False

def validate_salary(salary):
    if salary is None:
        return False
    if isinstance(salary, str):
        salary = salary.replace(",", "").strip()
        if salary == "":
            return False
        try:
            salary = int(salary)
        except ValueError:
            return False
    if isinstance(salary, (int, float)):
        return salary > 0
    return False

def validate_phone(phone):
    if not isinstance(phone, str):
        return False
    phone = "".join(ch for ch in phone if ch.isdigit())
    return len(phone) == 10

def validate_email(email):
    if not isinstance(email, str):
        return False
    email = email.strip()
    if "@" not in email:
        return False
    local, _, domain = email.partition("@")
    return bool(local) and bool(domain)

def validate_department(dept):
    return isinstance(dept, str) and dept.strip() != ""

cleaned_employees = []
error_employees = []

required_fields = ["emp_id", "name", "age", "salary", "department", "phone", "email"]

for emp in employees:
    errors = []

    for field in required_fields:
        if field not in emp or emp[field] is None or (isinstance(emp[field], str) and emp[field].strip() == ""):
            errors.append(f"{field} is required")

    
    if "name" in emp and isinstance(emp["name"], str):
        emp["name"] = clean_name(emp["name"])

   
    if not validate_age(emp.get("age")):
        errors.append("Invalid age")

   
    if not validate_salary(emp.get("salary")):
        errors.append("Salary must be positive numeric")

    else:
        if isinstance(emp["salary"], str):
            emp["salary"] = int(emp["salary"].replace(",", "").strip())

   
    if not validate_phone(emp.get("phone")):
        errors.append("Invalid phone number")

    if not validate_email(emp.get("email")):
        errors.append("Invalid email")

    
    if not validate_department(emp.get("department")):
        errors.append("Invalid department")

    
    if errors:
        error_employees.append({
            "emp_id": emp.get("emp_id", "UNKNOWN"),
            "error_reason": "; ".join(errors)
        })
    else:
        cleaned_employees.append(emp)


with open("employees_cleaned.json", mode="w", encoding="utf-8") as f:
    json.dump({"cleaned_employees": cleaned_employees}, f, indent=4)

with open("employees_errors.json", mode="w", encoding="utf-8") as f:
    json.dump({"errors": error_employees}, f, indent=4)

