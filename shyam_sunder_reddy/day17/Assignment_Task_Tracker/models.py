# Import required libraries
from pydantic import BaseModel, Field   # BaseModel for data validation, Field for metadata
from typing import Optional, List       # Optional for nullable fields, List for collections

# Global variable to keep track of auto-incrementing task IDs
next_id = 1

# ---------------- TASK MODEL ----------------
class Task(BaseModel):
    """
    Represents a task in the system.
    """
    id: Optional[int] = None   # Task ID (auto-assigned when created)
    title: str = Field(..., description="Enter proper title")   # Task title (required)
    description: str = Field(..., description="Enter proper description for the task")  # Task description (required)
    completed: bool = Field(False, description="Mark it as true or false")  # Task status (default: False)

# In-memory storage for tasks (acts like a database table)
tasks: List[Task] = []

# ✅ Example Task Output:
# {
#   "id": 1,
#   "title": "Finish FastAPI project",
#   "description": "Add comments and outputs to endpoints",
#   "completed": false
# }

# ---------------- LOGIN REQUEST MODEL ----------------
class LoginRequest(BaseModel):
    """
    Represents login request payload.
    """
    username: str   # Username provided by user
    password: str   # Password provided by user

# ✅ Example LoginRequest Output:
# {
#   "username": "admin",
#   "password": "secret123"
# }

# ---------------- TOKEN MODEL ----------------
class Token(BaseModel):
    """
    Represents authentication token returned after login.
    """
    access_token: str   # JWT access token
    token_type: str     # Token type (usually "bearer")

# ✅ Example Token Output:
# {
#   "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
#   "token_type": "bearer"
# }

# ---------------- USER MODEL ----------------
class User(BaseModel):
    """
    Represents a user in the system.
    """
    username: str   # Username of the user
    password: str   # Password of the user

# ✅ Example User Output:
# {
#   "username": "admin",
#   "password": "secret123"
# }
