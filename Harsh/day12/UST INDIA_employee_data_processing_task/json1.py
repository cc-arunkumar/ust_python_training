import json

with open(r"C:\Users\Administrator\Desktop\Training\ust_python_training\harsh\day12\UST INDIA_employee_data_processing_task\employees_raw.json") as json_data_file:
    j1 = json.load(json_data_file)
    employees = j1["employees"]

clear = []
clear_count = 0
error = []
error_count = 0

for emp in employees:
    try:
        # Required fields check
        if not emp["emp_id"] or not emp["name"] or not emp["age"] or not emp["salary"] or not emp["department"] or not emp["phone"] or not emp["email"]:
            error_count += 1
            error.append({"emp_id": emp["emp_id"], "error_reason": "Missing or empty required field"})
            continue

        # Name cleaning
        name=emp["name"].split()
        emp["name"] = " ".join(name)

        # Age validation
        try:
            emp["age"] = int(emp["age"])
            if emp["age"] < 18 or emp["age"] > 65:
                error_count += 1
                error.append({"emp_id": emp["emp_id"], "error_reason": "Invalid age"})
                continue
        except Exception:
            error_count += 1
            error.append({"emp_id": emp["emp_id"], "error_reason": "Age not numeric"})
            continue

        # Salary validation
        try:
            emp["salary"] = float(emp["salary"])
            if emp["salary"] <= 0 :
                error_count += 1
                error.append({"emp_id": emp["emp_id"], "error_reason": "Invalid salary"})
                continue
        except Exception:
            error_count += 1
            error.append({"emp_id": emp["emp_id"], "error_reason": "Salary not numeric"})
            continue

        # Phone validation
        if not (emp["phone"].isdigit() and len(emp["phone"]) == 10):
            error_count += 1
            error.append({"emp_id": emp["emp_id"], "error_reason": "Invalid phone number"})
            continue

        # Email validation
        if "@" not in emp["email"] or emp["email"].startswith("@") or emp["email"].endswith("@"):
            error_count += 1
            error.append({"emp_id": emp["emp_id"], "error_reason": "Invalid email"})
            continue

        # Department validation
        if emp["department"].strip() == "":
            error_count += 1
            error.append({"emp_id": emp["emp_id"], "error_reason": "Invalid department"})
            continue

        # If all validations pass → add to cleaned list
        clear_count += 1
        clear.append(emp)

    except Exception as e:
        error_count += 1
        error.append({"emp_id": emp["emp_id"] if "emp_id" in emp else "UNKNOWN", "error_reason": str(e)})

# Save outputs
with open("employees_cleaned.json", "w") as f:
    json.dump({"cleaned_employees": clear}, f, indent=2)

with open("employees_errors.json", "w") as f:
    json.dump({"errors": error}, f, indent=2)

print("clean data", clear_count)
print("error data", error_count)
