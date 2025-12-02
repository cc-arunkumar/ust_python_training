from fastapi import APIRouter, Depends, HTTPException, status
from models.emp_model import Employee
from models.emp_model import StatusModel
from crud.employee_crud import create_emp, get_all, get_by_id, update_by_id, delete_by_id, update_partial
from auth_jwt import get_current_user, User

# Router for Employee Training Requests
emp_router = APIRouter(prefix="/employee")

# -----------------------------
# CREATE Employee Training Request
# -----------------------------
@emp_router.post("", status_code=status.HTTP_201_CREATED)
def create_one(emp: Employee, current_user: User = Depends(get_current_user)):
    try:
        return create_emp(emp)
    except Exception as e:
        # 400 Bad Request if creation fails
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Error creating employee request: {str(e)}"
        )

# -----------------------------
# READ All Employee Training Requests
# -----------------------------
@emp_router.get("", status_code=status.HTTP_200_OK)
def get_all_emp(current_user: User = Depends(get_current_user)):
    try:
        return get_all()
    except Exception as e:
        # 500 Internal Server Error if unexpected issue
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error fetching records: {str(e)}"
        )

# -----------------------------
# READ Employee Training Request by ID
# -----------------------------
@emp_router.get("/{employee_id}", status_code=status.HTTP_200_OK)
def get_id(id: int, current_user: User = Depends(get_current_user)):
    try:
        return get_by_id(id)
    except Exception as e:
        # 404 Not Found if record missing
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Employee request with ID {id} not found. Error: {str(e)}"
        )

# -----------------------------
# UPDATE Employee Training Request by ID
# -----------------------------
@emp_router.put("/{employee_id}", status_code=status.HTTP_200_OK)
def update_id(id: int, emp: Employee, current_user: User = Depends(get_current_user)):
    try:
        return update_by_id(id, emp)
    except Exception as e:
        # 400 Bad Request if update fails
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Error updating employee request with ID {id}: {str(e)}"
        )

# -----------------------------
# PARTIAL UPDATE (Status only)
# -----------------------------
@emp_router.patch("/{employee_id}", status_code=status.HTTP_200_OK)
def update_partial_by_id(id: int, status: StatusModel, current_user: User = Depends(get_current_user)):
    try:
        return update_partial(id, status)
    except Exception as e:
        # 400 Bad Request if partial update fails
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Error updating status for employee request with ID {id}: {str(e)}"
        )

# -----------------------------
# DELETE Employee Training Request by ID
# -----------------------------
@emp_router.delete("/{employee_id}", status_code=status.HTTP_200_OK)
def delete_id(id: int, current_user: User = Depends(get_current_user)):
    try:
        return delete_by_id(id)
    except Exception as e:
        # 404 Not Found if record missing or 500 if unexpected
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Error deleting employee request with ID {id}: {str(e)}"
        )
