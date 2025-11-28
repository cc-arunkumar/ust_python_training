from pydantic import BaseModel, Field, field_validator
from datetime import date, datetime
from typing import Optional
from enum import Enum
import csv
import os

# ---------------------------------------------------------
# Static City List
# ---------------------------------------------------------
CITIES = [
    "Delhi", "Mumbai", "Kolkata", "Bengaluru", "Chennai",
    "Hyderabad", "Ahmedabad", "Surat", "Pune", "Jaipur"
]


# ---------------------------------------------------------
# Enum Class for Active Status
# ---------------------------------------------------------
class ActiveStatus(str, Enum):
    active = "Active"
    inactive = "Inactive"


# ---------------------------------------------------------
# Vendor Master Validation Model Using Pydantic
# ---------------------------------------------------------
class VendorMaster(BaseModel):
    """
    Validation schema for Vendor Master records.
    Enforces formatting rules like GST, email format,
    valid city mapping, and contact conventions.
    """

    vendor_name: str = Field(..., max_length=100, pattern=r"^[A-Za-z ]+$")
    contact_person: str = Field(..., max_length=100, pattern=r"^[^0-9]+$")
    contact_phone: str = Field(..., pattern=r"^[6-9][0-9]{9}$")
    gst_number: str = Field(..., pattern=r"^[0-9]{2}[A-Za-z0-9]{10}[A-Za-z0-9]{3}$")
    email: str = Field(..., pattern=r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$")
    address: str = Field(..., max_length=200)
    city: str
    active_status: ActiveStatus

    @field_validator("city")
    def validate_city(cls, value):
        """
        Normalize city name and enforce allowed list.
        Also corrects common spelling variations.
        """
        value = value.strip().title()

        # Auto-correct spelling variations
        if value in ["Bangalore", "Banglore"]:
            value = "Bengaluru"

        if value in CITIES:
            return value

        raise ValueError(f"Invalid city '{value}'. Allowed cities: {CITIES}")


# ---------------------------------------------------------
# File Paths
# ---------------------------------------------------------
input_file = r"C:\Users\Administrator\Desktop\ust_python_training\arumukesh\day_18\aims_plus\vendor_master.csv"
clean_output = r"C:\Users\Administrator\Desktop\ust_python_training\arumukesh\day_18\aims_plus\cleaned_vendor_master.csv"
error_output = r"C:\Users\Administrator\Desktop\ust_python_training\arumukesh\day_18\aims_plus\vendor_master_error_data.csv"

valid_rows = []
error_rows = []


# ---------------------------------------------------------
# Validate CSV Records
# ---------------------------------------------------------

if not os.path.exists(input_file):
    print(f" ERROR: Input file not found: {input_file}")
else:
    with open(input_file, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            try:
                model = VendorMaster(**row)
                valid_rows.append(model.model_dump())
            except Exception as e:
                print("\n ERROR PROCESSING ROW:", row)
                print("   Reason:", e)
                error_rows.append(row)


# ---------------------------------------------------------
# Write Cleaned Data to File
# ---------------------------------------------------------

if valid_rows:
    with open(clean_output, "w", newline='') as file:
        writer = csv.DictWriter(file, fieldnames=valid_rows[0].keys())
        writer.writeheader()
        writer.writerows(valid_rows)
    print(f"\nCLEAN DATA SAVED → {clean_output}")


# ---------------------------------------------------------
# Write Error Data to File
# ---------------------------------------------------------

if error_rows:
    with open(error_output, "w", newline='') as file:
        writer = csv.DictWriter(file, fieldnames=error_rows[0].keys())
        writer.writeheader()
        writer.writerows(error_rows)
    print(f" ERROR DATA SAVED → {error_output}")


# ---------------------------------------------------------
# Summary Output
# ---------------------------------------------------------
print("\n----------------------------------------------")
print(f" Total rows processed : {len(valid_rows) + len(error_rows)}")
print(f" Valid rows         : {len(valid_rows)}")
print(f" Invalid rows       : {len(error_rows)}")
print("----------------------------------------------\n")
