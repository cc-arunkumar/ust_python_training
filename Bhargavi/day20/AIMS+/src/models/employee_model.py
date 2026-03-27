import csv
from datetime import datetime
from pydantic import BaseModel, field_validator, model_validator
from typing import List

# -------------------------------
# Allowed lists for validation
# -------------------------------
allowed_status = {"Active", "Inactive", "Resigned"}  # Allowed status values for employees

# -------------------------------
# EmployeeDirectory Model
# -------------------------------
class EmployeeDirectory(BaseModel):
    emp_code: str  # Employee code
    full_name: str  # Full name of the employee
    email: str  # Employee's email address
    phone: str  # Employee's phone number
    department: str  # Department the employee belongs to
    location: str  # Location where the employee works
    join_date: datetime  # Join date of the employee
    status: str  # Status of the employee (Active, Inactive, Resigned)

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
    processedlist = []  # List to store valid employee records
    invalidlist = []  # List to store invalid rows

    try:
        # Open and read the CSV file
        with open(input_file, "r") as file:
            content = csv.DictReader(file)  # Read the CSV content as dictionary
            for row in content:
                try:
                    # Convert the 'join_date' from string to datetime object
                    row['join_date'] = datetime.strptime(row['join_date'], "%Y-%m-%d")
                    
                    # Create an EmployeeDirectory object, which automatically validates the fields
                    employee = EmployeeDirectory(**row)  
                    processedlist.append(employee)  # Add valid employees to the list
                except Exception as e:
                    # Capture invalid rows and the error message
                    invalidlist.append({"row": row, "error": str(e)})
        
        # Print the number of valid and invalid rows
        print("Valid rows:", len(processedlist))
        print("Invalid rows:", len(invalidlist))

        # Write the valid employees to the output CSV file
        with open(output_file, "w", newline="") as file:
            headers = [
                "emp_code", "full_name", "email", "phone", "department", "location", "join_date", "status"
            ]
            writer = csv.DictWriter(file, fieldnames=headers)  # Prepare the CSV writer
            writer.writeheader()  # Write the headers to the output file
            for employee in processedlist:
                # Convert the Pydantic model to dictionary for writing
                employee_data = employee.model_dump()  # Use model_dump() for Pydantic V2
                writer.writerow(employee_data)  # Write each employee to the file

    except FileNotFoundError:
        print(f"Error: The file {input_file} was not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# -------------------------------
# Run the processing function
# -------------------------------
if __name__ == "__main__":
    # Call the function to process the employee data from the input file and output to a new file
    process_employees(
        r"C:\Users\Administrator\Desktop\Training\ust_python_training\Bhargavi\day 19\AIMS_Plus\database\sample_data\employee_directory.csv",  # Input file path
        r"C:\Users\Administrator\Desktop\Training\ust_python_training\Bhargavi\day 19\AIMS_Plus\database\sample_data\validated_employee_directory.csv"  # Output file path
    )

#output
# Valid rows: 92
# Invalid rows: 8