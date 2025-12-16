from pydantic import BaseModel, Field, EmailStr
from typing import Optional

def validate_ust_email(email: str) -> str:
    if not email.endswith("@ust.com"):
        raise ValueError("Email must end with @ust.com")
    return email

class EmployeeBase(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    email: EmailStr
    designation: str = Field(min_length=2, max_length=100)
    manager_id: Optional[int] = None

    def model_post_init(self, __context):
        # enforce UST email domain
        validate_ust_email(self.email)

class EmployeeCreate(EmployeeBase):
    pass

class EmployeeUpdate(BaseModel):
    name: Optional[str] = Field(default=None, min_length=2, max_length=100)
    email: Optional[EmailStr] = None
    designation: Optional[str] = Field(default=None, min_length=2, max_length=100)
    manager_id: Optional[int] = None

    def model_post_init(self, __context):
        if self.email is not None:
            validate_ust_email(self.email)

class EmployeeOut(BaseModel):
    emp_id: int
    name: str
    email: EmailStr
    designation: str
    manager_id: Optional[int]
