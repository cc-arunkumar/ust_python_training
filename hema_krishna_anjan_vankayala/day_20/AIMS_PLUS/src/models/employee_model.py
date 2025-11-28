from pydantic import BaseModel, Field
from datetime import date

class EmployeeDirectory(BaseModel):
    # Core employee fields
    emp_id: int
    emp_code: str = Field(..., pattern=r'^USTEMP-')   # Must start with USTEMP-
    full_name: str = Field(...)
    email: str = Field(..., pattern=r'^[A-Za-z0-9._%+-]+@ust\.com$')  # Must be UST domain
    phone: str = Field(..., pattern=r'^[6-9]\d{9}')   # Valid Indian mobile number
    department: str = Field(...)                      # HR/IT/Admin/Finance/Support
    location: str = Field(...)                        # Trivandrum/Bangalore/Chennai/Hyderabad
    join_date: date = Field(...)                      # Cannot be in the future
    status: str = Field(...)                          # Active/Inactive/Resigned

    # Validation methods
    def validation_department(self):
        if self.department not in ['HR', 'IT', 'Admin', 'Finance', 'Support']:
            raise ValueError("Invalid Department")

    def validation_location(self):
        if self.location not in ['Trivandrum', 'Bangalore', 'Chennai', 'Hyderabad']:
            raise ValueError("Invalid Location")

    def validation_joindate(self):
        if self.join_date > date.today():
            raise ValueError("Join Date cannot be in the future")

    def validation_status(self):
        if self.status not in ['Active', 'Inactive', 'Resigned']:
            raise ValueError("Invalid Status")

    # Run validations on initialization
    def __init__(self, **data):
        super().__init__(**data)
        self.validation_department()
        self.validation_joindate()
        self.validation_location()
        self.validation_status()
