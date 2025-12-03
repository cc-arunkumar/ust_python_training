import csv
import re
from pydantic import BaseModel, Field, ValidationError, model_validator

class Vendor(BaseModel):
    vendor_id: int
    vendor_name: str = Field(..., max_length=100)
    contact_person: str = Field(..., max_length=100)
    contact_phone: str
    gst_number: str = Field(..., min_length=15, max_length=15)
    email: str
    address: str = Field(..., max_length=200)
    city: str
    active_status: str

    @model_validator(mode="after")
    def check_rules(self) -> "Vendor":
        if not re.match(r"^[A-Za-z ]+$", self.vendor_name):
            raise ValueError("Vendor name must contain only alphabets and spaces")
        if not re.match(r"^[A-Za-z ]+$", self.contact_person):
            raise ValueError("Contact person must contain only alphabets")
        if not re.match(r"^[6-9]\d{9}$", self.contact_phone):
            raise ValueError("Contact phone must be a valid Indian mobile number starting with 6/7/8/9")
        if not re.match(r"^[A-Za-z0-9]+$", self.gst_number) or len(self.gst_number) != 15:
            raise ValueError("GST number must be exactly 15 alphanumeric characters")
        if not re.match(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$", self.email):
            raise ValueError("Invalid email format")
        if self.active_status not in ["Active", "Inactive"]:
            raise ValueError("Active status must be either 'Active' or 'Inactive'")
        return self


valid_vendors = []
invalid_vendors = []

with open(r"C:\Users\Administrator\Desktop\Training\ust_python_training\taniya\day18\task\vendor_master.csv",
          mode="r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    all_fields = reader.fieldnames

    for row in reader:
        try:
            obj = Vendor(
                vendor_id=int(row["vendor_id"]),
                vendor_name=row["vendor_name"],
                contact_person=row["contact_person"],
                contact_phone=row["contact_phone"],
                gst_number=row["gst_number"],
                email=row["email"],
                address=row["address"],
                city=row["city"],
                active_status=row["active_status"]
            )
            valid_vendors.append(obj)
        except (ValidationError, ValueError) as e:
            # print("Row failed:", row)
            # print("Error:", str(e))
            invalid_vendors.append({"row": row, "error": str(e)})

with open(r"C:\Users\Administrator\Desktop\Training\ust_python_training\taniya\day18\task\vendor_master_validated.csv",
          mode="w", newline="", encoding="utf-8") as file1:
    writer = csv.DictWriter(file1, fieldnames=all_fields)
    writer.writeheader()
    for vendor in valid_vendors:
        writer.writerow(vendor.dict())

print(f"Wrote {len(valid_vendors)} valid rows")
print(f"Skipped {len(invalid_vendors)} invalid rows")

