import json

# Custom exception classes to handle different error type
class MissingFieldError(Exception):
    pass

class InvalidTypeError(Exception):
    pass

class InvalidDataError(Exception):
    pass

# Open the JSON file containing raw employee data
with open("ashutosh_samal\Day12\employees_raw.json","r") as raw_data:
    data = json.load(raw_data)

# Extract the employee list from the loaded data
employees = data["employees"]

# List of required fields that each employee record must contain
required_fields = ["emp_id","name","age","salary","department","phone","email"]
processed = []
errors = []

# Iterate through each employee record
for emp in employees:
    try:
        # Check for missing fields
        if not all(key in emp and emp[key] is not None for key in required_fields):
            raise MissingFieldError(f"Missing required field in emp: {emp}")
        
        # Validate age
        if not 18<=emp.get("age")<=65 and type(emp.get("age") == int):
            raise InvalidDataError(f"Invalid age : {emp["emp_id"]}")
        
        # Validate salary
        if not emp.get("salary")>0:
            raise InvalidDataError(f"Invalid salary : {emp["salary"]}")
        
        # Validate phone
        if not len(emp.get("phone"))==10 and (emp.get("phone")).isdigit():
            raise InvalidDataError(f"Invalid Mobile Number :{emp["phone"]}")
        
        # Validate email
        if not "@" in emp.get("email"):
            raise InvalidDataError(f"Invalid Email : {emp["email"]}")
        
        #validate department
        if not emp.get("department"):
            raise MissingFieldError(f"Department value missing :{emp["department"]}")
    
    # Handle specific exceptions and append error details to the 'errors' list    
    except MissingFieldError as e:
        errors.append({emp["emp_id"]:f"Missing field:{str(e)}"})
    except ValueError as e:
        errors.append({emp["emp_id"]:f"Invalid value:{str(e)}"})
    except Exception as e:
        errors.append({emp['emp_id']: f"Unexpected error for {str(e)}"})
    else:
        processed.append(emp)

# Write the valid employee records to a new JSON file
with open("employees_cleaned.json","w") as updated_file:
    updated_file.write(json.dumps(processed,indent=2))

# Write the error details records to a new JSON file    
with open("employees_errors.json","w") as updated_file:
    updated_file.write(json.dumps(errors,indent=2))

# Print the number of processed and skipped (invalid) records
print(f"Number of processed (valid) orders: {len(processed)}")
print(f"Number of skipped (invalid) orders: {len(errors)}")

#Sample Output
# Number of processed (valid) orders: 24
# Number of skipped (invalid) orders: 26