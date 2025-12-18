from pydantic import BaseModel ,EmailStr, Field
from typing import Optional, List


class LoginRequest(BaseModel):
    username: int
    password: str

# -----------------------
# Forgot Password Request
# -----------------------
class ForgotPasswordRequest(BaseModel):
    email: EmailStr

# -----------------------
# Verify Code Request
# -----------------------
class VerifyCodeRequest(BaseModel):
    email: EmailStr
    code: int=Field(min_length=6, max_length=6)  # 6-digit verification code

# -----------------------
# Reset Password Request
# -----------------------
class ResetPasswordRequest(BaseModel):
    email: EmailStr
    new_password: str =Field(min_length=6) # Minimum password length 6 characters
# -----------------------
# Reset Password Request
# -----------------------
class ResetPasswordRequest(BaseModel):
    email: EmailStr
    new_password: str = Field(min_length=6)  # Minimum password length 6 characters

class EmployeeInfo(BaseModel):
    e_id: Optional[str]
    name: Optional[str]
    email: Optional[str]
    designation: Optional[str]
    mgr_id: Optional[str]

class UserResponse(BaseModel):
    id: int
    username: str
    role: List[str]
    status: Optional[str]
    employee: Optional[EmployeeInfo]

class LoginResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str
    expires_in: int
    user: UserResponse
