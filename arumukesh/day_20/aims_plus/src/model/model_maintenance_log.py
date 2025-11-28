from pydantic import BaseModel, Field, field_validator
from datetime import date, datetime
from typing import Optional
from enum import Enum
import csv
import os

# ---------------------------------------------------------
# ENUM CLASSES
# ---------------------------------------------------------

class MaintenanceType(str, Enum):
    """Allowed maintenance types."""
    repair = "Repair"
    service = "Service"
    upgrade = "Upgrade"


class Status(str, Enum):
    """Allowed status values for maintenance log."""
    completed = "Completed"
    pending = "Pending"


# ---------------------------------------------------------
# Pydantic Model: Maintenance Log Schema
# ---------------------------------------------------------

class MaintenanceLog(BaseModel):
    """
    Data validation model for maintenance entries.
    Ensures formatting rules for vendor, date, description,
    maintenance type and cost.
    """

    asset_tag: str = Field(..., pattern=r"^UST", description="Asset tag must start with UST")
    maintenance_type: MaintenanceType
    vendor_name: str = Field(..., pattern=r"^[A-Za-z ]+$", description="Vendor name should contain only alphabets and spaces")
    description: str = Field(..., min_length=10, description="Minimum 10 characters required")
    cost: float = Field(..., gt=0, description="Cost must be greater than zero")
    maintenance_date: date
    technician_name: str = Field(..., pattern=r"^[A-Za-z ]+$")
    status: Status

    @field_validator("maintenance_date")
    def validate_date(cls, value: date):
        """Ensures maintenance date is not in the future."""
        if value <= datetime.today().date():
            return value
        raise ValueError("Maintenance date cannot be in the future.")


# ---------------------------------------------------------
# CSV Processing Paths
# ---------------------------------------------------------

input_file = r"C:\Users\Administrator\Desktop\ust_python_training\arumukesh\day_18\aims_plus\maintenance_log.csv"
clean_output = r"C:\Users\Administrator\Desktop\ust_python_training\arumukesh\day_18\aims_plus\cleaned_maintenance_log.csv"
error_output = r"C:\Users\Administrator\Desktop\ust_python_training\arumukesh\day_18\aims_plus\maintenance_log_error_data.csv"

valid_rows = []
error_rows = []


# ---------------------------------------------------------
# CSV Processing Logic
# ---------------------------------------------------------

if not os.path.exists(input_file):
    print(f" ERROR: Input file not found: {input_file}")
else:
    with open(input_file, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            try:
                model = MaintenanceLog(**row)
                valid_rows.append(model.model_dump())
            except Exception as e:
                print("\nERROR PROCESSING ROW:", row)
                print("Reason:", e)
                error_rows.append(row)


# ---------------------------------------------------------
# WRITE CLEANED DATA
# ---------------------------------------------------------

if valid_rows:
    with open(clean_output, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=valid_rows[0].keys())
        writer.writeheader()
        writer.writerows(valid_rows)
    print(f"\n✔ Cleaned data saved at: {clean_output}")


# ---------------------------------------------------------
# WRITE ERROR DATA
# ---------------------------------------------------------

if error_rows:
    with open(error_output, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=error_rows[0].keys())
        writer.writeheader()
        writer.writerows(error_rows)
    print(f"Error data saved at: {error_output}")


# # ---------------------------------------------------------
# # SUMMARY OUTPUT
# # ---------------------------------------------------------

# print("\n-------------------------------------------------")
# print(f" Total rows processed: {len(valid_rows) + len(error_rows)}")
# print(f" Valid rows: {len(valid_rows)}")
# print(f" Invalid rows: {len(error_rows)}")
# print("-------------------------------------------------\n")