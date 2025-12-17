from datetime import date, datetime
from typing import Optional, List
from pydantic import BaseModel, EmailStr


# =========================================================
# EMPLOYEE SCHEMAS
# =========================================================

class EmployeeBase(BaseModel):
    name: str
    email: EmailStr
    designation: str
    manager_id: Optional[int] = None


class EmployeeCreate(EmployeeBase):
    pass


class EmployeeUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    designation: Optional[str] = None
    manager_id: Optional[int] = None


class EmployeeOut(EmployeeBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


# =========================================================
# TASK SCHEMAS
# =========================================================

class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    status: Optional[str] = "Pending"
    assigned_to: int
    assigned_by: int
    reviewer: Optional[int] = None
    priority: Optional[str] = "Medium"
    remarks: Optional[str] = None
    expected_closure: Optional[date] = None
    actual_closure: Optional[date] = None
    updated_by: Optional[int] = None


class TaskCreate(TaskBase):
    pass


class TaskUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[str] = None
    assigned_to: Optional[int] = None
    assigned_by: Optional[int] = None
    reviewer: Optional[int] = None
    priority: Optional[str] = None
    remarks: Optional[str] = None
    expected_closure: Optional[date] = None
    actual_closure: Optional[date] = None
    updated_by: Optional[int] = None


class TaskOut(TaskBase):
    task_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


# =========================================================
# ATTACHMENT SCHEMAS
# =========================================================

class AttachmentBase(BaseModel):
    task_id: int
    file_name: str
    file_path: str
    file_size: int
    uploaded_by: int


class AttachmentCreate(AttachmentBase):
    pass


class AttachmentOut(AttachmentBase):
    id: int
    uploaded_at: datetime

    class Config:
        orm_mode = True


# =========================================================
# USER SCHEMAS
# =========================================================

class UserBase(BaseModel):
    emp_id: int
    roles: str = "Employee"
    status: str = "Active"


class UserCreate(UserBase):
    password: str


class UserUpdate(BaseModel):
    emp_id: Optional[int] = None
    password: Optional[str] = None
    roles: Optional[str] = None
    status: Optional[str] = None


class UserOut(UserBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


# =========================================================
# LOGIN SCHEMA
# =========================================================

class UserLogin(BaseModel): 
    emp_id: int 
    password: str