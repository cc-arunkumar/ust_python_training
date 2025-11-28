from fastapi import APIRouter, HTTPException, Depends
from src.models.employee_model import Employee, validate_employee
from src.crud import employee_crud
from src.auth.jwt_auth import User,get_current_user
router = APIRouter()

@router.post("/create", response_model=Employee)
def create(emp: Employee, current_user:User=Depends(get_current_user)):
    validate_employee(emp)
    new_id = employee_crud.create_employee(emp)
    return {**emp.model_dump(), "emp_id": new_id}

@router.get("/list")
def list_employees(status: str = None, current_user:User=Depends(get_current_user)):
    rows = employee_crud.list_employees(status)
    if not rows:
        raise HTTPException(status_code=404, detail="No employees found")
    return {"status": "success", "data": rows}
@router.get("/count")
def count_employees(current_user:User=Depends(get_current_user)):
    row = employee_crud.count_employees()
    return {"status": "success", "count": row["total"]}

@router.get("/{emp_id}", response_model=Employee)
def get_employee(emp_id: int, current_user:User=Depends(get_current_user)):
    row = employee_crud.get_employee(emp_id)
    if not row:
        raise HTTPException(status_code=404, detail="Employee not found")
    return Employee(**row)

@router.put("/{emp_id}", response_model=Employee)
def update_employee(emp_id: int, emp: Employee, current_user:User=Depends(get_current_user)):
    validate_employee(emp)
    employee_crud.update_employee(emp_id, emp)
    row = employee_crud.get_employee(emp_id)
    return Employee(**row)

@router.patch("/{emp_id}/status")
def update_status(emp_id: int, status: str, current_user:User=Depends(get_current_user)):
    if status not in {"Active", "Inactive", "Resigned"}:
        raise HTTPException(status_code=422, detail="Invalid status")
    employee_crud.update_status(emp_id, status)
    return {"status": "success", "message": f"Employee {emp_id} status updated to {status}"}

@router.delete("/{emp_id}")
def delete_employee(emp_id: int, current_user:User=Depends(get_current_user)):
    employee_crud.delete_employee(emp_id)
    return {"status": "success", "message": "Employee deleted"}

@router.get("/search")
def search_employees(keyword: str, current_user:User=Depends(get_current_user)):
    rows = employee_crud.search_employees(keyword)
    if not rows:
        raise HTTPException(status_code=404, detail="No matching employees found")
    return {"status": "success", "data": rows}

@router.get("/count")
def count_employees(current_user:User=Depends(get_current_user)):
    row = employee_crud.count_employees()
    return {"status": "success", "count": row["total"]}
