from pydantic import BaseModel, field_validator, EmailStr
import re

class VendorMaster(BaseModel):
    vendor_id: int            # unique ID for vendor
    vendor_name: str          # vendor name, alphabets only
    contact_person: str       # contact person name, alphabets only
    contact_phone: str        # Indian mobile number (10 digits, starts with 6-9)
    gst_number: str           # GST number, exactly 15 alphanumeric characters
    email: EmailStr           # vendor email, validated format
    address: str              # vendor address, max 200 characters
    city: str                 # vendor city
    active_status: str        # must be Active or Inactive

    @field_validator("vendor_name")
    def vendor_name_valid(cls, v):
        # vendor_name must contain only alphabets and spaces (1–100 chars)
        if not re.fullmatch(r"[A-Za-z ]{1,100}", v):
            raise ValueError("vendor_name must be alphabets only")
        return v

    @field_validator("contact_person")
    def contact_person_valid(cls, v):
        # contact_person must contain only alphabets and spaces (1–100 chars)
        if not re.fullmatch(r"[A-Za-z ]{1,100}", v):
            raise ValueError("contact_person must be alphabets only")
        return v

    @field_validator("contact_phone")
    def phone_valid(cls, v):
        # contact_phone must be a valid Indian mobile number (10 digits, starts with 6–9)
        if not re.fullmatch(r"[6-9]\d{9}", v):
            raise ValueError("Invalid Indian mobile number")
        return v

    @field_validator("gst_number")
    def gst_valid(cls, v):
        # gst_number must be exactly 15 alphanumeric characters
        if not re.fullmatch(r"[A-Za-z0-9]{15}", v):
            raise ValueError("Invalid GST number")
        return v

    @field_validator("address")
    def address_length(cls, v):
        # address must not exceed 200 characters
        if len(v) > 200:
            raise ValueError("Address too long")
        return v

    @field_validator("active_status")
    def status_valid(cls, v):
        # active_status must be either Active or Inactive
        if v not in {"Active", "Inactive"}:
            raise ValueError("active_status must be Active or Inactive")
        return v
