from pydantic import BaseModel, Field
from datetime import date

class EmployeeMaster(BaseModel):
    emp_id: int | None = None   # Auto-increment PK, optional on create
    emp_code: str = Field(..., max_length=20, description="Must start with USTEMP")
    full_name: str = Field(..., max_length=100, description="Alphabets + spaces only")
    email: str = Field(..., max_length=100, description="Must end with @ust.com")
    phone: str = Field(..., max_length=15, description="10-digit Indian mobile")
    department: str = Field(..., max_length=50, description="HR/IT/Admin/Finance/etc.")
    location: str = Field(..., max_length=100, description="Indian UST locations")
    join_date: date = Field(..., description="Cannot be future date")
    status: str = Field(..., max_length=20, description="Active/Inactive/Resigned")

    