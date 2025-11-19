import json
import re

processed_list = []
errors_list = []

with open(r"C:\Users\Administrator\Desktop\ust_python_training\Rohit\day12\assignment\employees_raw.json", "r") as file:
    data = json.load(file)
    employees = data["employees"]

    for emp in employees:
        error_reason = None

        required_fields = ["emp_id", "name", "age", "salary", "department", "phone", "email"]
        for field in required_fields:
            if not emp.get(field):
                error_reason = f"Missing or empty field: {field}"
                break

        if not error_reason and "name" in emp:
            emp["name"] = " ".join(emp["name"].split())

        if not error_reason:
            try:
                emp["age"] = int(emp["age"])
                if emp["age"] < 18 or emp["age"] > 65:
                    error_reason = "Invalid age"
            except (TypeError, ValueError):
                error_reason = "Age must be numeric"

        if not error_reason:
            try:
                emp["salary"] = float(emp["salary"])
                if emp["salary"] <= 0:
                    error_reason = "Salary must be positive"
            except (TypeError, ValueError):
                error_reason = "Invalid salary format"

        if not error_reason:
            if not re.match(r'^\d{10}$', str(emp["phone"])):
                error_reason = "Invalid phone number"


        if not error_reason:
            if "@" not in emp["email"] or  emp["email"].startswith("@") or emp["email"].endswith("@"):
                error_reason = "Invalid email"
            

        if not error_reason:
            if emp["department"].strip() =="" :
                error_reason = "Invalid department"

       
        if error_reason:
            errors_list.append({"emp_id": emp.get("emp_id", "UNKNOWN"), "error_reason": error_reason})
        else:
            processed_list.append(emp)


with open(r"C:\Users\Administrator\Desktop\ust_python_training\Rohit\day12\assignment\employees_cleaned.json", "w") as outfile:
    json.dump({"cleaned_employees": processed_list}, outfile, indent=2)

# Save errors
with open(r"C:\Users\Administrator\Desktop\ust_python_training\Rohit\day12\assignment\employees_errors.json", "w") as errfile:
    json.dump({"errors": errors_list}, errfile, indent=2)

print(f"Valid employees: {len(processed_list)}")
print(f"Errors: {len(errors_list)}")
