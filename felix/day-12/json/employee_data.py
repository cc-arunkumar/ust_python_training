import json

# Lists to store valid and invalid employee records
cleaned = []
errors = []

# Open and read the raw employee JSON file
with open("employees_raw.json", "r") as employee_data:
    
    employee_raw_data = json.load(employee_data)
    employee = employee_raw_data["employees"]
    
    # Extract the list of required fields from the first employee record
    required_fields = list(employee[0].keys())
    
    # Iterate through each employee record
    for item in employee:
        flag = 0  # Flag to mark if the record contains missing fields
        
        # Check for missing or empty fields
        for key in required_fields:
            if item[key] is None or str(item[key]).strip() == "":
                flag = 1
                errors.append({
                    "id": item[required_fields[0]],
                    "error_reason": "Field is None"
                })
                break
        
        # Skip further validation if required fields are missing
        if flag == 1:
            continue
        
        # Clean up employee name (remove extra spaces)
        name = ""
        for i in item[required_fields[1]].split(" "):
            if i != "":
                name += i
                name += " "
                
        item[required_fields[1]] = name.strip()
            
        if int(item[required_fields[2]]) <18 or item[required_fields[2]]>65:
            errors.append({"id":item[required_fields[0]],"error_reason":"age is not valid"})
            continue
        
        # Validate email format (simple @ check)
        if len(item[required_fields[9]].split("@")) != 2:
            errors.append({
                "id": item[required_fields[0]],
                "error_reason": "Email is not valid"
            })
            continue
        
        # Validate salary and phone number
        try:
            # Salary must be positive
            if int(item[required_fields[7]]) <= 0:
                errors.append({
                    "id": item[required_fields[0]],
                    "error_reason": "Salary not valid"
                })
                continue
            
            # Phone number must be numeric and 10 digits
            if not int(item[required_fields[8]]):
                errors.append({
                    "id": item[required_fields[0]],
                    "error_reason": "Phone number not valid"
                })
                continue
            
            if len(str(item[required_fields[8]])) != 10:
                errors.append({
                    "id": item[required_fields[0]],
                    "error_reason": "Phone number not valid"
                })
                continue
        
        except Exception:
            # Any failure in converting phone/salary to int is an error
            errors.append({
                "id": item[required_fields[0]],
                "error_reason": "Phone number not valid"
            })
            continue
        
        # If all checks pass, add employee to the cleaned list
        cleaned.append(item)

# Print summary
print("Cleaned: ", len(cleaned))
print("Error: ", len(errors))

# Save errors to a JSON file
with open("employee_errors.json", "a") as cleaned_data:
    json.dump(errors, cleaned_data, indent=2)

# Save cleaned employee data to a JSON file
with open("employees_cleaned.json", "a") as cleaned_data:
    json.dump(cleaned, cleaned_data, indent=2)
