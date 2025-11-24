import json

# List of required fields that should be present in each employee dictionary
required_fields_list = ["emp_id", "name", "age", "salary", "department", "phone", "email"]
error_list = []  # List to store invalid employee data

# Function to check if all required fields are present and non-empty
def required_fields(emp_dict):
    for field in required_fields_list:
        # Check if the field is missing in the dictionary
        if field not in emp_dict:
            return False

        value = emp_dict[field]

        # Check if the field is None or an empty string
        if value is None or str(value).strip() == "":
            return False
    return True

# Function to clean the 'name' field by removing extra spaces
def name_cleaning(emp_dict):
    emp_name = emp_dict['name']
    clean_name = " ".join(emp_name.split())  # Split by spaces and join again to remove extra spaces
    emp_dict['name'] = clean_name

# Function to validate the 'age' field to ensure it's an integer within a valid range (18-65)
def age_validation(emp_dict):
    try:
        emp_age = int(emp_dict['age'])  # Convert age to integer
        emp_dict['age'] = emp_age
        # Check if age is between 18 and 65
        if emp_dict['age'] > 18 and emp_dict['age'] < 65:
            return True
    except TypeError:
        print(f"The value should be in int format: {emp_dict['age']}")
        return False
    except ValueError:
        print(f"The value should be in int format: {emp_dict['age']}")
        return False

# Function to validate the 'salary' field to ensure it's a positive integer
def salary_validation(emp_dict):
    try:
        emp_salary = int(emp_dict['salary'])  # Convert salary to integer
        # Check if salary is greater than 0
        if emp_salary > 0:
            return True
        else:
            return False
    except ValueError:
        print(f"Not in a proper format: {emp_dict['salary']}")
        return False

# Function to validate the 'phone' field to ensure it's a 10-digit number
def phone_number_validation(emp_dict):
    try:
        emp_phone_number = int(emp_dict['phone'])  # Convert phone to integer
        temp = emp_phone_number
        flag = 0
        while(temp > 0):  # Count the digits in the phone number
            flag += 1
            temp = temp // 10

        # Check if the phone number has exactly 10 digits
        if flag == 10:
            return True
        else:
            return False
    except ValueError:
        print(f"The format is not proper: {emp_dict['phone']}")
        return False

# Function to validate the 'email' field to ensure it has an "@" symbol and proper format
def email_validation(emp_dict):
    email = emp_dict['email']
    # Check if email contains "@" symbol
    if "@" not in email:
        return False

    username, domain = email.split("@", 1)  # Split the email at the first "@"
    # Ensure both username and domain are non-empty
    if username.strip() == "" or domain.strip() == "":
        return False
    return True

# Load employee data from a JSON file
with open("task_2_ust_india_employee_data_processing/employee.json", "r") as emp_file:
    employee_file_json = json.load(emp_file)

# Extract employee list from the loaded JSON data
employees_list = employee_file_json["employees"]

# Print the total number of employees found
print(f"Total employees found: {len(employees_list)}")

count = 0  # Counter for valid employees
validated_list = []  # List to store valid employee data
error_list = []  # List to store employees with errors

# Iterate over each employee to validate their data
for emp in employees_list:
    # Check each validation function
    is_valid = required_fields(emp)
    is_age_valid = age_validation(emp)
    is_salary_valid = salary_validation(emp)
    is_phone_valid = phone_number_validation(emp)
    is_email_valid = email_validation(emp)
    name_cleaning(emp)  # Clean the name field by removing extra spaces
    
    # If all validations pass, append the employee to validated_list
    if is_valid and is_age_valid and is_salary_valid and is_phone_valid and is_email_valid:
        validated_list.append(emp)
        count += 1
    else:
        # If validation fails, add the employee to error_list
        error_list.append(emp)

# Print the total number of valid employees
print(f"Total number of valid employees: {count}")
print(validated_list)

# Prepare the output data with valid and invalid employee records
output_data = {"employees": validated_list}
error_data = {"employees": error_list}

# Write the validated data to a new JSON file
with open("employee_cleaned.json", "w") as f:
    json.dump(output_data, f, indent=4)

# Write the errors to a separate JSON file
with open("employees_errors.json", "w") as f:
    json.dump(error_data, f, indent=4)
