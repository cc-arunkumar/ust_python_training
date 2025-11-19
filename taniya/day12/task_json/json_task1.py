import json

with open(r"C:\Users\Administrator\Desktop\Training\ust_python_training\taniya\day12\task_json\employee_raw.json") as file:
    data = json.load(file)
    my_emp = data["employees"]

error = []
clear_data = []
clear_count = 0
error_count = 0

for emp in my_emp:
    emp_id = emp.get("emp_id")
    error_reason = None

    # Validate required fields
    string_fields = ["emp_id", "name", "department", "phone", "email"]
    numeric_fields = ["age", "salary"]

    missing = False
    for field in string_fields:
        if not isinstance(emp.get(field), str) or not emp[field].strip():
            missing = True
            break
    for field in numeric_fields:
        if emp.get(field) in [None, ""]:
            missing = True
            break

    if missing:
        error.append({"emp_id": emp_id, "error_reason": "Missing required field(s)"})
        error_count += 1
        continue

    # Clean name spacing
    emp["name"] = " ".join(emp["name"].split(" "))

    # Validate age
    try:
        emp["age"] = int(emp["age"])
        if emp["age"] < 18 or emp["age"] > 65:
            error_reason = "Invalid age"
    except:
        error_reason = "Age is not a number"

    # Validate salary
    if not error_reason:
        try:
            emp["salary"] = int(emp["salary"])
            if emp["salary"] <= 0:
                error_reason = "Invalid salary"
        except:
            error_reason = "Salary is not numeric"

    # Validate phone
    if not error_reason:
        if not (emp["phone"].isdigit() and len(emp["phone"]) == 10):
            error_reason = "Invalid phone number"

    # Validate email
    if not error_reason:
        email = emp["email"]
        if "@" not in email or email.startswith("@") or email.endswith("@"):
            error_reason = "Invalid email"

    # Validate department
    if not error_reason:
        if emp["department"].strip() == "":
            error_reason = "Invalid department"

    # Final decision
    if error_reason:
        error.append({"emp_id": emp_id, "error_reason": error_reason})
        error_count += 1
    else:
        clear_data.append(emp)
        clear_count += 1

# Save results
with open("employees_cleaned.json", "w", encoding="utf-8") as file1:
    json.dump(clear_data, file1, indent=2)

with open("employees_error.json", "w", encoding="utf-8") as file2:
    json.dump(error, file2, indent=2)

print(f"Valid employees: {clear_count}")
print(f"Invalid employees: {error_count}")