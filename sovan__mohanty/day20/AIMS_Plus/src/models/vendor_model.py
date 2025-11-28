from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime
import re
from fastapi import HTTPException

class Vendor(BaseModel):
    vendor_id: Optional[int] = None
    vendor_name: str = Field(..., max_length=100)
    contact_person: str = Field(..., max_length=100)
    contact_phone: str = Field(..., max_length=15)
    gst_number: str = Field(..., max_length=20)
    email: str = Field(..., max_length=100)
    address: str = Field(..., max_length=200)
    city: str = Field(..., max_length=100)
    active_status: str = Field(..., max_length=20)
    last_updated: Optional[datetime] = None

def validate_vendor(vendor: Vendor):
    if re.search(r"\d", vendor.vendor_name):
        raise HTTPException(status_code=422, detail="vendor_name must not contain digits")
    if not re.match(r"^[A-Za-z ]+$", vendor.contact_person):
        raise HTTPException(status_code=422, detail="contact_person must contain only alphabets and spaces")
    if not re.match(r"^[6-9]\d{9}$", vendor.contact_phone):
        raise HTTPException(status_code=422, detail="contact_phone must be a valid 10-digit Indian mobile number")
    if not re.match(r"^[A-Za-z0-9]{15}$", vendor.gst_number):
        raise HTTPException(status_code=422, detail="gst_number must be exactly 15 alphanumeric characters")
    if not re.match(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$", vendor.email):
        raise HTTPException(status_code=422, detail="Invalid email format")
    if vendor.city not in {"Bangalore", "Chennai", "Hyderabad", "Pune", "Trivandrum", "TVM"}:
        raise HTTPException(status_code=422, detail="Invalid city")
    if vendor.active_status not in {"Active", "Inactive"}:
        raise HTTPException(status_code=422, detail="active_status must be 'Active' or 'Inactive'")
