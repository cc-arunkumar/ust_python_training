from pydantic import BaseModel, Field

class UserCreate(BaseModel):
    user_id: str = Field(min_length=3, max_length=64)
    password: str = Field(min_length=8, max_length=128)
    role: str = Field(pattern="^(admin|manager|employee)$")
    status: str = Field(pattern="^(active|inactive)$")

class UserLogin(BaseModel):
    user_id: str
    password: str

class UserUpdate(BaseModel):
    role: str | None = Field(default=None, pattern="^(admin|manager|employee)$")
    status: str | None = Field(default=None, pattern="^(active|inactive)$")

class UserOut(BaseModel):
    user_id: str
    role: str
    status: str
