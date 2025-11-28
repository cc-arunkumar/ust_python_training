import csv
import re
from datetime import datetime, date
from pydantic import BaseModel, Field, field_validator
from typing import Optional

# -------------------------------
# Maintenance Log Model with Validations
# -------------------------------
class MaintenanceLogModel(BaseModel):
    log_id: Optional[int] = 0
    asset_tag: str = Field(..., description="Asset tag must start with 'UST-'")
    maintenance_type: str = Field(..., description="Must be 'Repair', 'Service', or 'Upgrade'")
    vendor_name: str = Field(..., description="Vendor name must only contain alphabets and spaces")
    description: str = Field(..., min_length=10, description="Description must have at least 10 characters")
    cost: float = Field(..., gt=0, description="Cost must be a positive number")
    maintenance_date: date = Field(..., description="Maintenance date cannot be in the future")
    technician_name: str = Field(..., description="Technician name must only contain alphabets and spaces")
    status: str = Field(..., description="Status must be 'Completed' or 'Pending'")

    @field_validator("asset_tag")
    def validate_asset_tag(cls, val):
        if not val.startswith("UST-"):
            raise ValueError("asset_tag must start with 'UST-'")
        return val

    @field_validator("maintenance_type")
    def validate_maintenance_type(cls, val):
        valid_types = ["Repair", "Service", "Upgrade"]
        if val not in valid_types:
            raise ValueError(f"maintenance_type must be one of {', '.join(valid_types)}")
        return val

    @field_validator("vendor_name")
    def validate_vendor_name(cls, val):
        if any(char.isdigit() for char in val) or not all(char.isalpha() or char.isspace() for char in val):
            raise ValueError("vendor_name must only contain alphabets and spaces")
        return val

    @field_validator("cost")
    def validate_cost(cls, val):
        if val <= 0:
            raise ValueError("cost must be greater than 0")
        return val

    @field_validator("maintenance_date")
    def validate_maintenance_date(cls, val):
        if val > date.today():
            raise ValueError("maintenance_date cannot be a future date")
        return val

    @field_validator("technician_name")
    def validate_technician_name(cls, val):
        if any(char.isdigit() for char in val) or not all(char.isalpha() or char.isspace() for char in val):
            raise ValueError("technician_name must only contain alphabets and spaces")
        return val

    @field_validator("status")
    def validate_status(cls, val):
        if val not in ["Completed", "Pending"]:
            raise ValueError("status must be either 'Completed' or 'Pending'")
        return val

# -------------------------------
# CSV Processing Logic
# -------------------------------
def process_maintenance_logs(input_file: str, output_file: str):
    processedlist = []
    invalidlist = []

    # Corrected path formatting
    input_file = input_file.replace("\\", "/")  # Convert backslashes to forward slashes
    output_file = output_file.replace("\\", "/")

    with open(input_file, "r") as file:
        content = csv.DictReader(file)
        for row in content:
            try:
                # Validate with Pydantic model
                maintenance_log = MaintenanceLogModel(**row)
                processedlist.append(maintenance_log)
            except Exception as e:
                invalidlist.append({"row": row, "error": str(e)})

    print("Valid rows:", len(processedlist))
    print("Invalid rows:", len(invalidlist))

    with open(output_file, "w", newline="") as file:
        headers = [
            "log_id", "asset_tag", "maintenance_type", "vendor_name", "description",
            "cost", "maintenance_date", "technician_name", "status"
        ]
        writer = csv.DictWriter(file, fieldnames=headers)
        writer.writeheader()
        for log in processedlist:
            log_data = log.model_dump()  # Use model_dump() instead of dict() (for Pydantic V2)
            writer.writerow(log_data)

if __name__ == "__main__":
    # Use raw string format for file paths or double backslashes
    process_maintenance_logs(
        r"C:\Users\Administrator\Desktop\Training\ust_python_training\vinutha\day13\day19\AIMS_PLUS\database\sample_data\maintenance_log.csv",
        r"C:\Users\Administrator\Desktop\Training\ust_python_training\vinutha\day13\day19\AIMS_PLUS\database\sample_data\validated_maintenance_log.csv"
    )
