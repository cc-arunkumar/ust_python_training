from pydantic import BaseModel, Field, field_validator
from typing import Optional
from datetime import date
import csv

# -----------------------------
# MaintenanceLogModel
# -----------------------------
class MaintenanceLogModel(BaseModel):
    """
    Pydantic model for validating maintenance log records.
    Each field is validated against business rules.
    """
    log_id: Optional[int] = Field(default=None, description="Auto-increment integer primary key")
    asset_tag: str = Field(..., description="Must follow UST- pattern")
    maintenance_type: str = Field(..., description="Only 'Repair', 'Service', or 'Upgrade' allowed")
    vendor_name: str = Field(..., description="Alphabets only (no digits or special characters)")
    description: str = Field(..., min_length=10, description="Minimum 10 characters for description")
    cost: float = Field(..., gt=0, description="Must be greater than 0")
    maintenance_date: date = Field(..., description="Date, cannot be a future date")
    technician_name: str = Field(..., description="Alphabets only (no digits or special characters)")
    status: str = Field(..., description="Only 'Completed' or 'Pending' allowed")

    # -----------------------------
    # Field-level validators
    # -----------------------------
    @field_validator("asset_tag")
    def validate_asset_tag(cls, val):
        # Asset tag must start with "UST-"
        if not val.startswith("UST-"):
            raise ValueError("asset_tag must start with 'UST-'")
        return val

    @field_validator("maintenance_type")
    def validate_maintenance_type(cls, val):
        # Maintenance type must be one of the allowed values
        valid_types = ["Repair", "Service", "Upgrade"]
        if val not in valid_types:
            raise ValueError(f"maintenance_type must be one of {', '.join(valid_types)}")
        return val

    @field_validator("vendor_name")
    def validate_vendor_name(cls, val):
        # Vendor name must contain only alphabets and spaces
        if any(char.isdigit() for char in val) or not all(char.isalpha() or char.isspace() for char in val):
            raise ValueError("vendor_name must only contain alphabets and spaces, no digits or special characters")
        return val

    @field_validator("cost")
    def validate_cost(cls, val):
        # Cost must be greater than 0
        if val <= 0:
            raise ValueError("cost must be greater than 0")
        return val

    @field_validator("maintenance_date")
    def validate_maintenance_date(cls, val):
        # Maintenance date cannot be in the future
        if val > date.today():
            raise ValueError("maintenance_date cannot be a future date")
        return val

    @field_validator("technician_name")
    def validate_technician_name(cls, val):
        # Technician name must contain only alphabets and spaces
        if any(char.isdigit() for char in val) or not all(char.isalpha() or char.isspace() for char in val):
            raise ValueError("technician_name must only contain alphabets and spaces, no digits or special characters")
        return val

    @field_validator("status")
    def validate_status(cls, val):
        # Status must be either "Completed" or "Pending"
        if val not in ["Completed", "Pending"]:
            raise ValueError("status must be either 'Completed' or 'Pending'")
        return val

    # -----------------------------
    # Class method: Process CSV
    # -----------------------------
    @classmethod
    def from_csv(cls, input_file_path: str, output_file_path: str):
        """
        Parse the CSV file, validate each row using MaintenanceLogModel,
        and write valid rows to the processed CSV file.
        """
        valid_logs = []
        try:
            # Step 1: Read input CSV
            with open(input_file_path, mode='r', newline='', encoding='utf-8') as infile:
                reader = csv.DictReader(infile)
                for row in reader:
                    try:
                        # Validate and parse row into MaintenanceLogModel
                        log = cls(**row)
                        valid_logs.append(log.dict())  # Add valid log to list
                    except ValueError as e:
                        # Skip invalid rows and print error
                        print(f"Skipping row due to validation error: {e}")

            # Step 2: Write valid rows to output CSV
            with open(output_file_path, mode='w', newline='', encoding='utf-8') as outfile:
                fieldnames = valid_logs[0].keys() if valid_logs else []  # Use keys from first valid log
                writer = csv.DictWriter(outfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(valid_logs)

        except FileNotFoundError:
            print(f"File not found: {input_file_path}")


# -----------------------------
# Example usage
# -----------------------------
input_file_path = r"C:\Users\Administrator\Documents\Himavarsha\ust_python_training\himavarsha\day20\AIMS_Plus\database\sampledata\raw_csv\maintenance_log.csv"
output_file_path = r"C:\Users\Administrator\Documents\Himavarsha\ust_python_training\himavarsha\day20\AIMS_Plus\database\sampledata\final_csv\valid_maintenance.csv"

# Run the CSV processing
MaintenanceLogModel.from_csv(input_file_path, output_file_path)
