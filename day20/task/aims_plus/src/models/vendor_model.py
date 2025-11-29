from pydantic import BaseModel

class VendorCreate(BaseModel):
    vendor_name: str
    contact_person: str
    contact_phone: str
    gst_number: str
    email: str
    address: str
    city: str
    active_status: str


class VendorUpdate(BaseModel):
    vendor_name: str
    contact_person: str
    contact_phone: str
    gst_number: str
    email: str
    address: str
    city: str
    active_status: str


class VendorStatusUpdate(BaseModel):
    active_status: str
