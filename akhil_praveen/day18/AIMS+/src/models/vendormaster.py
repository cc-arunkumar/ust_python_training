from pydantic import BaseModel,Field,EmailStr
from typing import Literal
 
class StatusValidate(BaseModel):
    active_status: Literal['Active', 'Inactive']
    
class VendorMaster(BaseModel):
    vendor_name: str = Field(..., pattern=r"^[A-Za-z ]+$")
    contact_person: str = Field(..., pattern=r"^[A-Za-z ]+$")
    contact_phone: str = Field(..., pattern=r"^[6-9][0-9]{9}$")
    gst_number: str = Field(..., min_length=15, max_length=15)
    email: EmailStr
    address: str
    city: str = Literal[
    "Delhi", "Mumbai", "Bengaluru", "Chennai", "Hyderabad", "Kolkata",
    "Pune", "Ahmedabad", "Surat", "Jaipur", "Lucknow", "Kanpur",
    "Nagpur", "Indore", "Bhopal", "Patna", "Ranchi", "Chandigarh",
    "Thiruvananthapuram", "Kochi", "Coimbatore", "Madurai", "Visakhapatnam",
    "Vijayawada", "Mysuru", "Guwahati", "Shillong", "Gangtok", "Imphal"]
    active_status: Literal['Active', 'Inactive']
 