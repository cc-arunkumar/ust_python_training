from fastapi import APIRouter, HTTPException
from database.mongodb import user_collection
from utils.jwt_utils import create_access_token

auth_router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@auth_router.post("/login")
def login(emp_id: str, password: str):
    user = user_collection.find_one({"emp_id": emp_id})

    if not user or user["password"] != password:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_access_token({
        "emp_id": user["emp_id"],
        "role": user["role"]
    })

    return {
        "access_token": token,
        "token_type": "bearer"
    }

