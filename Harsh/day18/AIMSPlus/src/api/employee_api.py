from fastapi import HTTPException
from typing import List
from src.models.employee_model import EmployeeDirectory
from src.crud.employee_crud import (
    create_employee,
    get_all_employees,
    get_employee_by_id,
    update_employee_by_id,
    update_employee_status,
    delete_employee,
    search_employees,
    count_employees,
    bulk_upload_employees,
)

def register_employee_api(app):
    @app.post("/employees/create")
    def add_employee(emp: EmployeeDirectory):
        try:
            return create_employee(emp)
        except Exception as e:
            print(f"Error in create_employee: {e}")
            raise HTTPException(status_code=500, detail="Internal Server Error")

    @app.get("/employees/list")
    def list_employees(status: str | None = None):
        return get_all_employees(status)

    @app.get("/employees/count")
    def count():
        return count_employees()

    @app.get("/employees/search")
    def search(column_name: str, keyword: str):
        return search_employees(column_name, keyword)

    @app.get("/employees/{id}")
    def read_employee(id: int):
        result = get_employee_by_id(id)
        if not result:
            raise HTTPException(status_code=404, detail="Employee not found")
        return result

    @app.put("/employees/{id}")
    def update_employee(id: int, emp: EmployeeDirectory):
        result = update_employee_by_id(id, emp)
        if not result:
            raise HTTPException(status_code=404, detail="Employee not found")
        return result

    @app.patch("/employees/{id}/status")
    def update_status(id: int, new_status: str):
        result = update_employee_status(id, new_status)
        if not result:
            raise HTTPException(status_code=404, detail="Employee not found")
        return result

    @app.delete("/employees/{id}")
    def remove_employee(id: int):
        result = delete_employee(id)
        if not result:
            raise HTTPException(status_code=404, detail="Employee not found")
        return result

    @app.post("/employees/bulk-upload")
    def bulk_upload(employees: List[EmployeeDirectory]):
        return bulk_upload_employees(employees)
