import csv
from datetime import datetime, date
from pydantic import BaseModel, ValidationError
from typing import Literal

class Maintenance(BaseModel):
    log_id: int
    asset_tag: str
    maintenance_type: Literal["Repair", "Service", "Upgrade"]
    vendor_name: str
    description: str
    cost: float
    maintenance_date: date
    technician_name: str
    status: Literal["Completed", "Pending"]

    @classmethod
    def validate_row(cls, row, log_id):
        # Try parsing date in multiple formats
        date_str = row.get("maintenance_date", "").strip()
        for fmt in ("%Y-%m-%d", "%m/%d/%Y", "%d/%m/%Y"):
            try:
                parsed_date = datetime.strptime(date_str, fmt).date()
                break
            except ValueError:
                parsed_date = None
        if not parsed_date:
            raise ValueError("Invalid date format")

        return cls(
            log_id=log_id,
            asset_tag=row.get("asset_tag", "").strip(),
            maintenance_type=row.get("maintenance_type", "").strip().title(),
            vendor_name=row.get("vendor_name", "").strip(),
            description=row.get("description", "").strip(),
            cost=float(row.get("cost", "0")),
            maintenance_date=parsed_date,
            technician_name=row.get("technician_name", "").strip(),
            status=row.get("status", "").strip().title()
        )

valid_logs = []
invalid_logs = []

input_file = r"C:\Users\Administrator\Desktop\Training\ust_python_training\taniya\day18\task\maintenance_log.csv"
output_file = r"C:\Users\Administrator\Desktop\Training\ust_python_training\taniya\day18\task\maintenance_log_validated.csv"

with open(input_file, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    reader.fieldnames = [h.strip().lower() for h in reader.fieldnames]

    log_id = 1
    for row in reader:
        try:
            log = Maintenance.validate_row(row, log_id)
            valid_logs.append(log)
            log_id += 1
        except (ValidationError, ValueError) as e:
            invalid_logs.append({"row": row, "error": str(e)})

with open(output_file, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["log_id", "asset_tag", "maintenance_type", "vendor_name", "description", "cost", "maintenance_date", "technician_name", "status"])
    writer.writeheader()
    for log in valid_logs:
        writer.writerow(log.dict())

print(f"Wrote {len(valid_logs)} valid rows")
print(f"Skipped {len(invalid_logs)} invalid rows")


