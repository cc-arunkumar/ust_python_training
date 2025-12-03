import csv
import re
from pydantic import BaseModel, Field, ValidationError, model_validator
from datetime import date, datetime
from typing import Optional, Literal

class Asset(BaseModel):
    asset_id: int = 0
    asset_tag: str = Field(..., pattern=r'^UST.*$')
    asset_type: Literal["Laptop", "Monitor", "Keyboard", "Mouse"]
    serial_number: str
    manufacturer: Literal["Dell", "HP", "Lenovo", "Samsung"]
    model: str = Field(..., min_length=1)
    purchase_date: date
    warranty_years: int = Field(..., ge=1, le=5)
    condition_status: Literal["New", "Good", "Used", "Damaged"]
    assigned_to: Optional[str] = None
    location: Literal["Trivandrum","TVM", "Bangalore", "Chennai", "Hyderabad"]
    asset_status: Literal["Available", "Assigned", "Repair", "Retired"]

    @model_validator(mode="after")
    def check_rules(self):
        if self.purchase_date > date.today():
            raise ValueError("Purchase date cannot be in the future")
        if not re.match(r"^[A-Za-z0-9\-]+$", self.serial_number):
            raise ValueError("Serial number must be alphanumeric")
        if self.assigned_to and not re.match(r"^[A-Za-z ]+$", self.assigned_to):
            raise ValueError("Assigned_to must contain only alphabets and spaces")
        return self

seen_serials = set()
valid_assets = []
invalid_assets = []
asset_counter = 1

with open(r"C:\Users\Administrator\Desktop\Training\ust_python_training\taniya\day18\AIMS_Plus\database\asset_inventory.csv",
          mode="r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    all_fields = reader.fieldnames
    for row in reader:
        try:
            month, day, year = row["purchase_date"].split("/")
            purchase_date = date(int(year), int(month), int(day))
            
            obj = Asset(
                asset_id=asset_counter,
                asset_tag=row["asset_tag"],
                asset_type=row["asset_type"],
                serial_number=row["serial_number"],
                manufacturer=row["manufacturer"],
                model=row["model"],
                purchase_date=purchase_date,
                warranty_years=int(row["warranty_years"]),
                condition_status=row["condition_status"],
                assigned_to=row.get("assigned_to"),
                location=row["location"],
                asset_status=row["asset_status"]
            )
            asset_counter += 1
            if obj.serial_number in seen_serials:
                raise ValueError(f"Duplicate serial_number found: {obj.serial_number}")
            seen_serials.add(obj.serial_number)
            valid_assets.append(obj)
        except (ValidationError, ValueError) as e:
            invalid_assets.append({"row": row, "error": str(e)})

output_fields = ["asset_id"] + all_fields

with open(r"C:\Users\Administrator\Desktop\Training\ust_python_training\taniya\day18\AIMS_Plus\database\asset_inventory_validated.csv",
          mode="w", newline="", encoding="utf-8") as file1:
    writer = csv.DictWriter(file1, fieldnames=output_fields)
    writer.writeheader()
    for asset in valid_assets:
        writer.writerow(asset.dict())

print(f"Wrote {len(valid_assets)} valid rows")
print(f"Skipped {len(invalid_assets)} invalid rows")
