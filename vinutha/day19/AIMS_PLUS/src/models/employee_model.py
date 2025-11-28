import csv
from datetime import datetime
from pydantic import BaseModel, field_validator, model_validator
from typing import List

# -------------------------------
# Allowed lists for validation
# -------------------------------
allowed_status = {"Active", "Inactive", "Resigned"}

# -------------------------------
# EmployeeDirectory Model
# -------------------------------
class EmployeeDirectory(BaseModel):
    emp_code: str
    full_name: str
    email: str
    phone: str
    department: str
    location: str
    join_date: datetime
    status: str

    # Validator for emp_code: Must start with 'USTEMP-'
    @field_validator('emp_code')
    def validate_emp_code(cls, v):
        if not v.startswith("USTEMP-"):
            raise ValueError(f"Invalid emp_code: {v}. Must start with 'USTEMP-'")
        return v

    # Validator for email: Must end with '@ust.com'
    @field_validator('email')
    def validate_email(cls, v):
        if not v.endswith("@ust.com"):
            raise ValueError(f"Invalid email: {v}. Must end with @ust.com")
        return v

    # Validator for phone: Must be a 10-digit number
    @field_validator('phone')
    def validate_phone(cls, v):
        if len(v) != 10 or not v.isdigit():
            raise ValueError(f"Invalid phone: {v}. Must be a 10-digit number.")
        return v

    # Validator for join_date: Ensures it's not in the future
    @field_validator('join_date')
    def validate_join_date(cls, v):
        if v > datetime.today():
            raise ValueError(f"Invalid join_date: {v}. Cannot be a future date.")
        return v

    # Validator for status: Must be in allowed status list
    @field_validator('status')
    def validate_status(cls, v):
        if v not in allowed_status:
            raise ValueError(f"Invalid status: {v}. Must be one of {allowed_status}.")
        return v

    # Root validator to perform any cross-field validation if needed
    @model_validator(mode='before')
    def validate_all_fields(cls, values):
        # Additional root-level validation can go here if needed
        return values

# -------------------------------
# Process Employee Data
# -------------------------------
def process_employees(input_file: str, output_file: str):
    processedlist = []
    invalidlist = []

    try:
        with open(input_file, "r") as file:
            content = csv.DictReader(file)
            for row in content:
                try:
                    # Convert the join_date string to datetime object
                    row['join_date'] = datetime.strptime(row['join_date'], "%Y-%m-%d")
                    
                    # Create an EmployeeDirectory object and validate the fields
                    employee = EmployeeDirectory(**row)  
                    processedlist.append(employee)
                except Exception as e:
                    # Capture invalid rows and the error message
                    invalidlist.append({"row": row, "error": str(e)})
        
        print("Valid rows:", len(processedlist))
        print("Invalid rows:", len(invalidlist))

        with open(output_file, "w", newline="") as file:
            headers = [
                "emp_code", "full_name", "email", "phone", "department", "location", "join_date", "status"
            ]
            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writeheader()
            for employee in processedlist:
                # # Convert the Pydantic model to dictionary for writing
                # writer.writerow(employee.dict())
                employee_data = employee.model_dump()  # Use model_dump() instead of dict()
                writer.writerow(employee_data)

    except FileNotFoundError:
        print(f"Error: The file {input_file} was not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    # Use raw string format for file paths or double backslashes
    process_employees(
       r"C:\Users\Administrator\Desktop\Training\ust_python_training\vinutha\day13\day19\AIMS_PLUS\database\sample_data\employee_directory.csv", 
       r"C:\Users\Administrator\Desktop\Training\ust_python_training\vinutha\day13\day19\AIMS_PLUS\database\sample_data\validated_employee_directory.csv"
    )