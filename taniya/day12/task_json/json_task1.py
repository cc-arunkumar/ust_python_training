import json

# Open and load the raw employee JSON file
with open(r"C:\Users\Administrator\Desktop\Training\ust_python_training\taniya\day12\task_json\employee_raw.json") as file:
    data = json.load(file)
    my_emp = data["employees"]   # Extract the list of employees

# Initialize lists and counters for valid and invalid employees
error = []          # Store invalid employee records with reasons
clear_data = []     # Store valid employee records
clear_count = 0     # Counter for valid employees
error_count = 0     # Counter for invalid employees

# Process each employee record
for emp in my_emp:
    emp_id = emp.get("emp_id")   # Get employee ID
    error_reason = None          # Track reason for invalidation

    # -------------------------------
    # Validate required fields
    # -------------------------------
    string_fields = ["emp_id", "name", "department", "phone", "email"]
    numeric_fields = ["age", "salary"]

    missing = False
    # Check string fields (must be non-empty strings)
    for field in string_fields:
        if not isinstance(emp.get(field), str) or not emp[field].strip():
            missing = True
            break
    # Check numeric fields (must not be None or empty string)
    for field in numeric_fields:
        if emp.get(field) in [None, ""]:
            missing = True
            break

    # If any required field is missing, mark as error
    if missing:
        error.append({"emp_id": emp_id, "error_reason": "Missing required field(s)"})
        error_count += 1
        continue

    # -------------------------------
    # Clean name spacing
    # -------------------------------
    emp["name"] = " ".join(emp["name"].split(" "))   # Normalize spaces in name

    # -------------------------------
    # Validate age
    # -------------------------------
    try:
        emp["age"] = int(emp["age"])                 # Convert age to integer
        if emp["age"] < 18 or emp["age"] > 65:       # Age must be between 18 and 65
            error_reason = "Invalid age"
    except:
        error_reason = "Age is not a number"

    # -------------------------------
    # Validate salary
    # -------------------------------
    if not error_reason:
        try:
            emp["salary"] = int(emp["salary"])       # Convert salary to integer
            if emp["salary"] <= 0:                   # Salary must be positive
                error_reason = "Invalid salary"
        except:
            error_reason = "Salary is not numeric"

    # -------------------------------
    # Validate phone number
    # -------------------------------
    if not error_reason:
        if not (emp["phone"].isdigit() and len(emp["phone"]) == 10):
            error_reason = "Invalid phone number"

    # -------------------------------
    # Validate email
    # -------------------------------
    if not error_reason:
        email = emp["email"]
        # Email must contain '@' and not start or end with '@'
        if "@" not in email or email.startswith("@") or email.endswith("@"):
            error_reason = "Invalid email"

    # -------------------------------
    # Validate department
    # -------------------------------
    if not error_reason:
        if emp["department"].strip() == "":
            error_reason = "Invalid department"

    # -------------------------------
    # Final decision: valid or error
    # -------------------------------
    if error_reason:
        error.append({"emp_id": emp_id, "error_reason": error_reason})
        error_count += 1
    else:
        clear_data.append(emp)
        clear_count += 1

# -------------------------------
# Save results to output JSON files
# -------------------------------
with open("employees_cleaned.json", "w", encoding="utf-8") as file1:
    json.dump(clear_data, file1, indent=2)   # Save valid employees

with open("employees_error.json", "w", encoding="utf-8") as file2:
    json.dump(error, file2, indent=2)        # Save invalid employees with reasons

# Print summary counts
print(f"Valid employees: {clear_count}")
print(f"Invalid employees: {error_count}")