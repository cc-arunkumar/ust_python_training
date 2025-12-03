import csv
import re
from datetime import date, datetime
from pydantic import BaseModel, Field, ValidationError, model_validator
from typing import Literal

class Employee(BaseModel):
    emp_id: int
    emp_code: str = Field(..., pattern=r'^USTEMP-?\d+$')
    full_name: str = Field(..., min_length=1)
    email: str
    phone: str
    department: Literal["HR", "IT", "Admin", "Finance"]
    location: Literal["TVM", "Bangalore", "Chennai", "Hyderabad"]
    join_date: date
    status: Literal["Active", "Inactive", "Resigned"]

    @model_validator(mode="after")
    def check_rules(self) -> "Employee":
        if not re.match(r"^[A-Za-z ]+$", self.full_name.strip()):
            raise ValueError("Full name must contain only alphabets and spaces")
        if not re.match(r"^[6-9]\d{9}$", self.phone.strip()):
            raise ValueError("Phone must be a valid 10-digit Indian mobile number starting with 6/7/8/9")
        if self.join_date > date.today():
            raise ValueError("Join date cannot be in the future")
        if not self.email.strip().lower().endswith("@ust.com"):
            raise ValueError("Email must end with @ust.com")
        return self

def parse_date_any(s: str) -> date:
    s = s.strip()
    for fmt in ("%Y-%m-%d", "%m/%d/%Y", "%d/%m/%Y"):
        try:
            return datetime.strptime(s, fmt).date()
        except ValueError:
            continue
    return date.fromisoformat(s.replace("/", "-"))

def clean_location(loc: str) -> str:
    loc = loc.strip()
    if loc.lower() == "trivandrum":
        return "TVM"
    return loc

def clean_status(st: str) -> str:
    s = st.strip()
    s_low = s.lower()
    if "resigned" in s_low:
        return "Resigned"
    if s_low in ("active", "activ"):
        return "Active"
    if s_low in ("inactive"):
        return "Inactive"
    return s

valid_employees = []
invalid_employees = []
emp_counter = 1

input_path = r"C:\Users\Administrator\Desktop\Training\ust_python_training\taniya\day18\task\employee_directory.csv"
output_path = r"C:\Users\Administrator\Desktop\Training\ust_python_training\taniya\day18\task\employee_directory_validated.csv"

with open(input_path, mode="r", encoding="utf-8") as file:
    reader = csv.DictReader(file, delimiter="\t")
    reader.fieldnames = [h.strip().lower() for h in reader.fieldnames]
    rows = list(reader)

    for row in rows:
        try:
            emp = Employee(
                emp_id=emp_counter,
                emp_code=row.get("emp_code", "").strip(),
                full_name=row.get("full_name", "").strip(),
                email=row.get("email", "").strip(),
                phone=row.get("phone", "").strip(),
                department=row.get("department", "").strip(),
                location=clean_location(row.get("location", "").strip()),
                join_date=parse_date_any(row.get("join_date", "").strip()),
                status=clean_status(row.get("status", "").strip())
            )
            emp_counter += 1
            valid_employees.append(emp)
        except (ValidationError, ValueError) as e:
            invalid_employees.append({"row": row, "error": str(e)})

with open(output_path, mode="w", newline="", encoding="utf-8") as file1:
    writer = csv.DictWriter(
        file1,
        fieldnames=["emp_id", "emp_code", "full_name", "email", "phone", "department", "location", "join_date", "status"],
        delimiter=","
    )
    writer.writeheader()
    for emp in valid_employees:
        writer.writerow(emp.model_dump())

print(f"Wrote {len(valid_employees)} valid rows")
print(f"Skipped {len(invalid_employees)} invalid rows")


