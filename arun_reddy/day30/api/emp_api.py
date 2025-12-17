from fastapi import APIRouter, Depends
from crud.emp_crud import (
    create_emp,
    get_employees_by_manager_id,
    get_employee_by_id,
    update_employee_by_id,
    delete_emp_byid
)
from Models.employee_model import Employee
from authorise.authorisation import role_guard

emp_router = APIRouter(
    prefix="/employee",
    tags=["Employee"]
)

# ---------------- CREATE EMPLOYEE ----------------
@emp_router.post("", dependencies=[Depends(role_guard(["admin"]))])
def create_employee(emp: Employee):
    return create_emp(emp)

# ---------------- GET EMPLOYEES BY MANAGER ----------------
@emp_router.get("/manager/{manager_id}", dependencies=[Depends(role_guard(["admin","manager"]))])
def get_employees_by_manager(manager_id: int):
    return get_employees_by_manager_id(manager_id)

# ---------------- GET EMPLOYEE BY ID ----------------
@emp_router.get("/{employee_id}", dependencies=[Depends(role_guard(["admin","manager"]))])
def get_employee(employee_id: int):
    return get_employee_by_id(employee_id)

# ---------------- UPDATE EMPLOYEE ----------------
@emp_router.put("/{employee_id}", dependencies=[Depends(role_guard(["admin"]))])
def update_employee(employee_id: int, emp: Employee):
    return update_employee_by_id(employee_id, emp)

# ---------------- DELETE EMPLOYEE ----------------
@emp_router.delete("/{employee_id}", dependencies=[Depends(role_guard(["admin"]))])
def delete_employee(employee_id: int):
    return delete_emp_byid(employee_id)
