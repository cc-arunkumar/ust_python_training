#Employee Data Processor

#Code 
import json

with open("employees_raw.json", "r") as f:
    data = json.load(f)

required_fields = data.get("required_fields", ["emp_id","name","age","salary","department","phone","email"])
valid_employees = []
error_employees = []

def validate_name(name : str) -> str:
    return " ".join(name.strip().split())

def is_valid_phone(phone):
    return bool(phone.isnumeric()==True and len(phone)==10)

def validate_employee(emp):    
    errors = []
    for field in required_fields:
        if field not in emp or emp[field] is None or str(emp[field]).strip() == "":
            errors.append(f"{field} is empty")
    
    if "name" in emp and emp["name"]:
        emp["name"] = validate_name(emp["name"])
    
    try:
        age = int(emp["age"])
        if age < 18 or age > 65:
            errors.append("Invalid age (must be 18-65)")
    except Exception:
        errors.append("Age must be numeric")

    try:
        salary = int(emp["salary"])
        if salary <= 0:
            errors.append("Salary must be positive")
    except Exception:
        errors.append("Salary must be positive : ")
        
    email = emp.get("email", "")
    if "@" not in email or email.startswith("@") or email.endswith("@"):
        errors.append("Invalid email")

    dept = emp.get("department", "")
    if dept is None or str(dept).strip() == "":
        errors.append("Invalid department")
        
    
    if not  is_valid_phone(emp["phone"]):
        return False,"Invalid phone No",emp

    return errors

for emp in data.get("employees", []):
    errors = validate_employee(emp)
    if errors:
        error_employees.append({
            "emp_id": emp.get("emp_id", "N/A"),
            "error_reason": errors
        })
    else:
        valid_employees.append(emp)
 
        
with open("employees_error.json","w",newline="") as outfile:
    writer = json.dump(error_employees,outfile,indent=2)
with open("employees_cleaned.json","w",newline="") as infile:
    writer = json.dump(valid_employees,infile,indent=2)


print("Valid employees count:", len(valid_employees))
print("Error employees count:", len(error_employees))

#Output
# Valid employees count: 26
# Error employees count: 24
