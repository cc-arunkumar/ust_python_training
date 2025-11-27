from pydantic import BaseModel, field_validator, EmailStr
import re

class VendorMaster(BaseModel):
    vendor_id: int
    vendor_name: str
    contact_person: str
    contact_phone: str
    gst_number: str
    email: EmailStr
    address: str
    city: str
    active_status: str

    @field_validator("vendor_name")
    def vendor_name_valid(cls, v):
        if not re.fullmatch(r"[A-Za-z ]{1,100}", v):
            raise ValueError("vendor_name must be alphabets only")
        return v

    @field_validator("contact_person")
    def contact_person_valid(cls, v):
        if not re.fullmatch(r"[A-Za-z ]{1,100}", v):
            raise ValueError("contact_person must be alphabets only")
        return v

    @field_validator("contact_phone")
    def phone_valid(cls, v):
        if not re.fullmatch(r"[6-9]\d{9}", v):
            raise ValueError("Invalid Indian mobile number")
        return v

    @field_validator("gst_number")
    def gst_valid(cls, v):
        if not re.fullmatch(r"[A-Za-z0-9]{15}", v):
            raise ValueError("Invalid GST number")
        return v

    @field_validator("address")
    def address_length(cls, v):
        if len(v) > 200:
            raise ValueError("Address too long")
        return v

    @field_validator("active_status")
    def status_valid(cls, v):
        if v not in {"Active", "Inactive"}:
            raise ValueError("active_status must be Active or Inactive")
        return v
