import json   # Import JSON module

def validate(row):
    required = ["emp_id","name","age","salary","department","phone","email"]   # Required fields
    try:
        for i in row:   # Loop through each field in employee record
            if str(row[i]).strip()=="" or row[i]==None:   # Check for empty or None values
                return False,"Field is empty"
            if i == required[2]:   # Validate age
                if (row[i]<18 or row[i]>65):
                    return False,"Invalid age"
            if i == required[3] and int(row[i])<0:   # Validate salary (non-negative)
                return False,"Invalid Salary"
            if i == required[5] and int(row[i]):   # Validate phone number
                if len(str(row[i])) != 10:
                    return False,"Invalid Phone number"
            if i == required[6]:   # Validate email format
                e_list = row[i].split("@")
                if len(e_list)!=2:
                    # print(f"{row["emp_id"]}")   # Debug line (commented out)
                    return False,"Invalid email"
        return True,"validation complete"   # If all validations pass

    except Exception as e:   # Catch unexpected errors
        return False,str(e)


error = []    # List to store invalid employee records
cleaned = []  # List to store valid employee records

# Open raw employee JSON file
with open("C:/Users/303394/Desktop/ust_python_training/akhil_praveen/day12/ust_employee_data_processing/employees_raw.json","r") as employees_json_data:
    data = json.load(employees_json_data)   # Load JSON data into Python dict
    employees = data["employees"]           # Extract employees list
    # print(employees)   # Debug line (commented out)
    print("Total: ",len(employees))         # Print total employees
    
    for row in employees:   # Validate each employee record
        condition, reason = validate(row)
        if condition:
            # Remove extra spaces in names
            name_list = row["name"].split()
            row["name"] = " ".join(name_list)
            # Append valid record to cleaned list
            cleaned.append(row)
        else:
            # Append error message with employee ID
            error.append(f"Error {row["emp_id"]}: {reason}")
    
    # Save cleaned employee records to JSON file
    with open("C:/Users/303394/Desktop/ust_python_training/akhil_praveen/day12/ust_employee_data_processing/employees_cleaned.json","w") as cleaned_json_data:
        json.dump(cleaned,cleaned_json_data,indent=2)
    
    # Save error messages to JSON file
    with open("C:/Users/303394/Desktop/ust_python_training/akhil_praveen/day12/ust_employee_data_processing/employees_error.json","w") as error_json_data:
        json.dump(error,error_json_data,indent=2)
    
    # Print summary
    print("Total cleaned: ",len(cleaned))
    print("Total skipped: ",len(error))

# ===========================
# Expected Output (example):
# ===========================
# Total:  5
# Total cleaned:  3
# Total skipped:  2
