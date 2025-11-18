import json

file_path = r"C:\Users\Administrator\Desktop\Prudhvi_Rajeev\ust_python_training\prudhvi_rajeev_kumar\day_12\json task\employees_raw.json"

with open(file_path, mode='r', encoding='utf-8') as file:
    json_reader = json.load(file)
    changes = json_reader["employees"]

def clean_name(name: str) -> str:
    return " ".join(name.split()).strip()

def validate_phone(phone) -> bool:
    if not isinstance(phone, str):
        return False
    phone = phone.strip()
    return phone.isdigit() and len(phone) == 10

def validate_email(email) -> bool:
    if not isinstance(email, str):
        return False
    email = email.strip()    
    if "@" not in email:
        return False
    local, _, domain = email.partition("@")
    return bool(local) and bool(domain)

def validate_salary(salary) -> bool:
    if salary is None:
        return False

    if isinstance(salary, str):
        salary = salary.strip()
        if salary == "":
            return False
        if not salary.isdigit():  
            return False
        salary = int(salary)
    
    if isinstance(salary, (int, float)):
        return salary > 0
    
    return False


required_fields = set(changes[0].keys())
cleaned_employees = []
error_employees = []

for emp in changes:
    is_invalid = False
    for field in required_fields:
        if field not in emp or emp[field] is None or (isinstance(emp[field], str) and emp[field].strip() == ""):
            is_invalid = True
    
    if "name" in emp and isinstance(emp["name"], str):
        emp["name"] = clean_name(emp["name"])
    
    age = emp.get("age")
    if not isinstance(age, int) or age < 18 or age > 65:
        is_invalid = True

    if emp.get("department").strip() == "":
        is_invalid = True
        
    if not validate_salary(emp.get("salary")):
        is_invalid = True
    
    if not validate_phone(emp.get("phone")):
        is_invalid = True
        
    if is_invalid:
        error_employees.append(emp)
    else:
        cleaned_employees.append(emp)

with open("employees_cleaned.json", mode='w') as output:
    json.dump(cleaned_employees, output, indent=4)

with open("employees_error.json", mode='w') as new_output:
    json.dump(error_employees, new_output, indent=4)

print(len(error_employees))
print(len(cleaned_employees))