import json

# Custom exception for age-related validation errors
class InvalidAgeError(Exception):
    pass

processed_fields = 0   # Count how many employee entries were processed
skipped = 0            # Count how many employee entries were rejected

# Required fields that must be present in each employee dictionary
required_fields = ['emp_id','name','age','salary','department','phone','email']

# Load the beautified raw employee file
with open(r"C:\Users\303372\Desktop\ust_python_training\Arumukesh\day_12\task_4_HR\employees_raw_beautified.json", "r") as file:
    data = json.load(file)

    valid_emp = []      # List to store valid employee records
    invalid_emp = []    # List to store invalid employee records

    # Process each employee in the dataset
    for emp in data["employees"]:
        try:
            # 1️⃣ Check if all required fields exist and are not empty
            if all(field in emp and emp[field] not in ("", None) for field in required_fields):

                # 2️⃣ Clean each field (remove extra spaces between words)
                for key in emp.keys():
                    emp[key] = " ".join(str(emp[key]).split())

                # 3️⃣ Validate age (must be between 18 and 65)
                emp["age"] = int(emp["age"])
                if emp["age"] < 18 or emp["age"] > 65:
                    raise InvalidAgeError("Invalid age found")

                # 4️⃣ Validate salary (must be a number)
                if not emp["salary"].isdigit():
                    raise ValueError("Invalid salary value")
                emp["salary"] = int(emp["salary"])

                # 5️⃣ Validate phone number (must be 10 digits)
                if not (emp["phone"].isdigit() and len(emp["phone"]) == 10):
                    raise ValueError("Invalid phone number")

                # 6️⃣ Validate email (must contain @ and .)
                if "@" not in emp["email"] or "." not in emp["email"]:
                    raise ValueError("Invalid email address")

                # 7️⃣ All validations passed → record is valid
                valid_emp.append(emp)

            else:
                # Missing required fields
                raise KeyError("Missing required field")

        except Exception as e:
            # If any validation failed, record the employee as invalid
            print(f"Skipping employee {emp.get('emp_id','Unknown')} due to unexpected error: {e}")
            skipped += 1
            invalid_emp.append(emp)

        finally:
            # Count every processed employee (valid + invalid)
            processed_fields += 1

    # 🟩 Summary Output
    print(f"Total valid employees: {len(valid_emp)}")
    print(f"Total skipped employees: {len(invalid_emp)}")
    print(f"Processed employees: {processed_fields}")

    # Prepare final JSON files
    valid_emp_data = {"employees": valid_emp}
    invalid_emp_data = {"employees": invalid_emp}

    # Save cleaned valid employee list
    with open(r"C:\Users\303372\Desktop\ust_python_training\Arumukesh\day_12\task_4_HR\cleaned_employees.json", "w") as file:
        json.dump(valid_emp_data, file, indent=2)

    # Save invalid employee records separately
    with open(r"C:\Users\303372\Desktop\ust_python_training\Arumukesh\day_12\task_4_HR\error_employees.json", "w") as file:
        json.dump(invalid_emp_data, file, indent=2)

# =============output=================


# -3.14-64\python.exe c:/Users/303372/Desktop/ust_python_training/Arumukesh/day_12/task_4_HR/hr_val.py
# Skipping employee UST003 due to unexpected error:'MIssing required field'
# Skipping employee UST004 due to unexpected error:Invalid salary value
# Skipping employee UST006 due to unexpected error:'MIssing required field'
# Skipping employee UST007 due to unexpected error:Invalid salary value
# Skipping employee UST010 due to unexpected error:Invalid phone number
# Skipping employee UST012 due to unexpected error:Invalid age found
# Skipping employee UST014 due to unexpected error:Invalid phone number
# Skipping employee UST016 due to unexpected error:'MIssing required field'
# Skipping employee UST018 due to unexpected error:Invalid phone number
# Skipping employee UST022 due to unexpected error:'MIssing required field'
# Skipping employee UST025 due to unexpected error:Invalid age found
# Skipping employee UST026 due to unexpected error:Invalid salary value
# Skipping employee UST029 due to unexpected error:'MIssing required field'
# Skipping employee UST030 due to unexpected error:Invalid phone number
# Skipping employee UST032 due to unexpected error:Invalid phone number
# Skipping employee UST033 due to unexpected error:Invalid email address
# Skipping employee UST035 due to unexpected error:'MIssing required field'
# Skipping employee UST037 due to unexpected error:Invalid phone number
# Skipping employee UST040 due to unexpected error:Invalid salary value
# Skipping employee UST042 due to unexpected error:Invalid phone number
# Skipping employee UST044 due to unexpected error:'MIssing required field'
# Skipping employee UST046 due to unexpected error:'MIssing required field'
# Skipping employee UST049 due to unexpected error:Invalid email address
# Skipping employee UST050 due to unexpected error:Invalid phone number
# totalvalid employees:26
# total skipped employees:24
# processed employees:50