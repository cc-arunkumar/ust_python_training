from fastapi import FastAPI,HTTPException
from employee_model import Employee
import employee_crud

app=FastAPI(title="Employee Management System")

@app.get("/employees/{employee_id}", response_model=Employee)
def get_employee_by_id(employee_id:int):
    x = employee_crud.read_employee_by_id(employee_id)
    if x is not None:
        return x
    raise HTTPException(status_code=404, detail="Id Not Found")

@app.post("/employees", response_model=Employee)
def create_employee(emp:Employee):
    x = employee_crud.create_employee(emp)
    if x is not None:
        return x
    raise HTTPException(status_code=409, detail="Error in employee Fields")

@app.put("/employees/{employee_id}", response_model=Employee)
def update_by_id(employee_id:int, emp:Employee):
    success = employee_crud.update_employee_by_id(employee_id, emp)
    if success:
        return employee_crud.read_employee_by_id(employee_id)  # ✅ return updated record
    raise HTTPException(status_code=404, detail="Id Not Found")

@app.delete("/employees/{employee_id}")
def delete_by_id(employee_id:int):
    success = employee_crud.delete_employee_by_id(employee_id)
    if success:
        return {"detail":"Employee Deleted"}
    raise HTTPException(status_code=404, detail="Employee Not Found")
