from fastapi import FastAPI, HTTPException
from src.crud.employee_crud import (
    create_employee,
    get_all_employees,
    get_employee_by_id,
    update_employee,
    update_employee_status,
    delete_employee,
    search_employees,
    count_employees
)

def register_employee_api(app: FastAPI):
    # POST /employees/create
    @app.post("/employees/create")
    def api_create_employee(emp_code: str, full_name: str, email: str, phone: str,
                            department: str, location: str, join_date: str, status: str):
        emp_id = create_employee(emp_code, full_name, email, phone,
                                 department, location, join_date, status)
        return {"message": "Employee created successfully", "emp_id": emp_id}

    # GET /employees/list
    @app.get("/employees/list")
    def api_list_employees(status: str = None):
        employees = get_all_employees(status)
        return employees

    # GET /employees/{id}
    @app.get("/employees/{id}")
    def api_get_employee(id: int):
        emp = get_employee_by_id(id)
        if not emp:
            raise HTTPException(status_code=404, detail="Employee not found")
        return emp

    # PUT /employees/{id}
    @app.put("/employees/{id}")
    def api_update_employee(id: int, emp_code: str, full_name: str, email: str, phone: str,
                            department: str, location: str, join_date: str, status: str):
        ok = update_employee(id, emp_code, full_name, email, phone,
                             department, location, join_date, status)
        if not ok:
            raise HTTPException(status_code=404, detail="Employee not found")
        return {"message": "Employee updated successfully"}

    # PATCH /employees/{id}/status
    @app.patch("/employees/{id}/status")
    def api_update_status(id: int, status: str):
        ok = update_employee_status(id, status)
        if not ok:
            raise HTTPException(status_code=404, detail="Employee not found")
        return {"message": "Status updated successfully"}

    # DELETE /employees/{id}
    @app.delete("/employees/{id}")
    def api_delete_employee(id: int):
        ok = delete_employee(id)
        if not ok:
            raise HTTPException(status_code=404, detail="Employee not found")
        return {"message": "Employee deleted successfully"}

    # GET /employees/search?keyword=
    @app.get("/employees/search")
    def api_search_employees(keyword: str):
        results = search_employees(keyword)
        return results

    # GET /employees/count
    @app.get("/employees/count")
    def api_count_employees():
        count = count_employees()
        return {"count": count}
