from fastapi import FastAPI
from validation import Validation
from crud import create_employee,get_employee,update_employee,delete_employee
app=FastAPI(description="Employeee management system")


# 1. POST /employees/ - Add a new employee.
# Request Body: first_name , last_name , email , position , salary , hire_date
# Validation:
# Ensure all required fields are provided.
# Validate email format.
# Ensure salary is a positive value.
# Response: employee_id of the created employee.

@app.post("/employees")
def create_emp_api(employee:Validation):
    result =create_employee(employee)
    return result

@app.get("/employees")
def get_all_emp():
    result=get_employee()
    return result
    

@app.put("/employees/{emp_id}")
def update_employee_api(employee:Validation,emp_id:int):
    result=update_employee(employee,emp_id)
    return result


@app.delete("/employees/employee/{emp_id}")
def delete_employee_api(emp_id:int):
    result=delete_employee(emp_id)
    return result