from pydantic import BaseModel, EmailStr, Field, field_validator
from typing import Optional
from datetime import datetime

# ==================== User Models ====================

class UserBase(BaseModel):
    emp_id: int = Field(..., description="Employee ID")
    role: str = Field(..., min_length=1, max_length=100, description="User roles (comma-separated)")

class UserCreate(UserBase):
    password: str = Field(..., min_length=6, max_length=50, description="User password")

class UserUpdate(BaseModel):
    password: Optional[str] = Field(None, min_length=6, max_length=50)
    role: Optional[str] = Field(None, min_length=1, max_length=100)

class UserResponse(UserBase):
    """Response model without password"""
    class Config:
        from_attributes = True

class UserInDB(UserBase):
    password: str
    
    class Config:
        from_attributes = True


# ==================== Employee Models ====================

class EmployeeBase(BaseModel):
    emp_id: str = Field(..., min_length=1, max_length=20, description="Employee ID")
    name: str = Field(..., min_length=1, max_length=50, description="Employee name")
    email: EmailStr = Field(..., description="Employee email")
    designation: str = Field(..., min_length=1, max_length=50, description="Employee designation")
    mgr_id: Optional[str] = Field(None, max_length=20, description="Manager ID")

class EmployeeCreate(EmployeeBase):
    pass

class EmployeeUpdate(BaseModel):
    name: Optional[str] = Field(None, min_length=1, max_length=50)
    email: Optional[EmailStr] = None
    designation: Optional[str] = Field(None, min_length=1, max_length=50)
    mgr_id: Optional[str] = Field(None, max_length=20)

class EmployeeResponse(EmployeeBase):
    class Config:
        from_attributes = True


# ==================== Task Models ====================

class TaskBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=100, description="Task title")
    description: str = Field(..., min_length=1, max_length=200, description="Task description")
    created_by: str = Field(..., max_length=50, description="Creator employee ID")
    assigned_to: str = Field(..., max_length=50, description="Assignee employee ID")
    assigned_by: str = Field(..., max_length=50, description="Assigner employee ID")
    priority: str = Field(..., max_length=10, description="Priority: high, medium, low")
    status: str = Field(..., max_length=20, description="Status: pending, in_progress, completed")
    reviewer: str = Field(..., max_length=20, description="Reviewer employee ID")
    expected_closure: datetime = Field(..., description="Expected closure date")
    remarks: Optional[str] = Field(None, max_length=500, description="Task remarks")

    @field_validator('priority')
    @classmethod
    def validate_priority(cls, v: str) -> str:
        allowed = ['high', 'medium', 'low']
        if v.lower() not in allowed:
            raise ValueError(f'Priority must be one of {allowed}')
        return v.lower()

    @field_validator('status')
    @classmethod
    def validate_status(cls, v: str) -> str:
        allowed = ['pending', 'in_progress', 'completed', 'on_hold', 'cancelled']
        if v.lower() not in allowed:
            raise ValueError(f'Status must be one of {allowed}')
        return v.lower()

class TaskCreate(TaskBase):
    assigned_at: Optional[datetime] = Field(default_factory=datetime.now, description="Assignment timestamp")

class TaskUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=100)
    description: Optional[str] = Field(None, min_length=1, max_length=200)
    assigned_to: Optional[str] = Field(None, max_length=50)
    updated_by: Optional[str] = Field(None, max_length=20)
    updated_at: Optional[datetime] = Field(default_factory=datetime.now)
    priority: Optional[str] = Field(None, max_length=10)
    status: Optional[str] = Field(None, max_length=20)
    remarks: Optional[str] = Field(None, max_length=500)
    reviewer: Optional[str] = Field(None, max_length=20)
    expected_closure: Optional[datetime] = None
    actual_closure: Optional[datetime] = None

    @field_validator('priority')
    @classmethod
    def validate_priority(cls, v: Optional[str]) -> Optional[str]:
        if v is None:
            return v
        allowed = ['high', 'medium', 'low']
        if v.lower() not in allowed:
            raise ValueError(f'Priority must be one of {allowed}')
        return v.lower()

    @field_validator('status')
    @classmethod
    def validate_status(cls, v: Optional[str]) -> Optional[str]:
        if v is None:
            return v
        allowed = ['pending', 'in_progress', 'completed', 'on_hold', 'cancelled']
        if v.lower() not in allowed:
            raise ValueError(f'Status must be one of {allowed}')
        return v.lower()

class TaskResponse(TaskBase):
    t_id: int = Field(..., description="Task ID")
    assigned_at: datetime
    updated_by: Optional[str] = None
    updated_at: Optional[datetime] = None
    actual_closure: Optional[datetime] = None
    
    class Config:
        from_attributes = True


# ==================== Example Usage ====================

if __name__ == "__main__":
    # Example: Creating a user
    user_data = UserCreate(
        emp_id=1001,
        password="securepass123",
        role="admin,manager"
    )
    print("User created:", user_data.model_dump())
    
    # Example: Creating an employee
    employee_data = EmployeeCreate(
        emp_id="EMP001",
        name="John Doe",
        email="john.doe@example.com",
        designation="Senior Developer",
        mgr_id="EMP100"
    )
    print("\nEmployee created:", employee_data.model_dump())
    
    # Example: Creating a task
    task_data = TaskCreate(
        title="Implement user authentication",
        description="Add JWT-based authentication system",
        created_by="EMP001",
        assigned_to="EMP002",
        assigned_by="EMP001",
        priority="high",
        status="pending",
        reviewer="EMP100",
        expected_closure=datetime(2024, 12, 31),
        remarks="High priority task"
    )
    print("\nTask created:", task_data.model_dump())