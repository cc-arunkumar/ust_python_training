import csv
from datetime import datetime
from pydantic import BaseModel, field_validator, model_validator
from typing import List

# -----------------------------
# Allowed values for employee status
# -----------------------------
allowed_status = {"Active", "Inactive", "Resigned"}


# -----------------------------
# EmployeeDirectory Model
# -----------------------------
class EmployeeDirectory(BaseModel):
    """
    Pydantic model for validating employee directory records.
    Each field is validated against business rules.
    """
    emp_code: str
    full_name: str
    email: str
    phone: str
    department: str
    location: str
    join_date: datetime
    status: str

    # -----------------------------
    # Field-level validators
    # -----------------------------
    @field_validator('emp_code')
    def validate_emp_code(cls, v):
        # Employee code must start with "USTEMP-"
        if not v.startswith("USTEMP-"):
            raise ValueError(f"Invalid emp_code: {v}. Must start with 'USTEMP-'")
        return v

    @field_validator('email')
    def validate_email(cls, v):
        # Email must end with "@ust.com"
        if not v.endswith("@ust.com"):
            raise ValueError(f"Invalid email: {v}. Must end with @ust.com")
        return v

    @field_validator('phone')
    def validate_phone(cls, v):
        # Phone must be exactly 10 digits and numeric
        if len(v) != 10 or not v.isdigit():
            raise ValueError(f"Invalid phone: {v}. Must be a 10-digit number.")
        return v

    @field_validator('join_date')
    def validate_join_date(cls, v):
        # Join date cannot be in the future
        if v > datetime.today():
            raise ValueError(f"Invalid join_date: {v}. Cannot be a future date.")
        return v

    @field_validator('status')
    def validate_status(cls, v):
        # Status must be one of the allowed values
        if v not in allowed_status:
            raise ValueError(f"Invalid status: {v}. Must be one of {allowed_status}.")
        return v

    # -----------------------------
    # Model-level validator (runs before field validators)
    # -----------------------------
    @model_validator(mode='before')
    def validate_all_fields(cls, values):
        # Currently just returns values, but can be used for cross-field validation
        return values


# -----------------------------
# Function: Process employees from CSV
# -----------------------------
def process_employees(input_file: str, output_file: str):
    """
    Reads raw employee data from a CSV file, validates each row using EmployeeDirectory,
    separates valid and invalid rows, and writes valid rows to a new CSV file.
    """
    processedlist = []  # Valid employees
    invalidlist = []    # Invalid employees with error details

    try:
        # Step 1: Read input CSV
        with open(input_file, "r") as file:
            content = csv.DictReader(file)
            for row in content:
                try:
                    # Convert join_date string to datetime object
                    row['join_date'] = datetime.strptime(row['join_date'], "%Y-%m-%d")
                    
                    # Validate row using EmployeeDirectory model
                    employee = EmployeeDirectory(**row)  
                    processedlist.append(employee)
                except Exception as e:
                    # Capture invalid rows with error message
                    invalidlist.append({"row": row, "error": str(e)})
        
        # Step 2: Print summary
        print("Valid rows:", len(processedlist))
        print("Invalid rows:", len(invalidlist))

        # Step 3: Write valid rows to output CSV
        with open(output_file, "w", newline="") as file:
            headers = [
                "emp_code", "full_name", "email", "phone", "department", "location", "join_date", "status"
            ]
            writer = csv.DictWriter(file, fieldnames=headers)
            writer.writeheader()
            for employee in processedlist:
                writer.writerow(employee.dict())

    except FileNotFoundError:
        # Handle case where input file is missing
        print(f"Error: The file {input_file} was not found.")
    except Exception as e:
        # Handle other unexpected errors
        print(f"An error occurred: {str(e)}")


# -----------------------------
# Run the script
# -----------------------------
if __name__ == "__main__":
    process_employees(
        "C:/Users/Administrator/Documents/Himavarsha/ust_python_training/himavarsha/day20/AIMS_Plus/database/sampledata/raw_csv/employee_directory.csv",
        "C:/Users/Administrator/Documents/Himavarsha/ust_python_training/himavarsha/day20/AIMS_Plus/database/sampledata/final_csv/employee_output.csv"
    )
