from employee_crud import read_all_employees, read_emp_by_id, create_employee_crud, update_employee_crud, delete_employee_by_id
from fastapi import FastAPI, HTTPException,status
from employee_model import Employee

# FastAPI app instance for the Employee Management System
app = FastAPI(title="Employee Management System")


@app.get('/employees/{employee_id}',response_model=Employee)
# API endpoint to fetch an employee by ID
def get_emp_id(employee_id : int):
    try:
        data = read_emp_by_id(employee_id)
        if not data:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="ID Not Found")
        return data 
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"ID not Found or Unable to fetch the Record : {e}")
    
@app.post('/employees/', response_model=Employee)
# API endpoint to create a new employee
def create_employee_endpoint(new_emp: Employee):
    try:
        data = create_employee_crud(new_emp)
        return new_emp
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Error: {e}")


@app.put('/employees/', response_model=Employee)
# API endpoint to update an existing employee
def update_employee_endpoint(emp_id: int,updated_emp : Employee):
    try:
        data = update_employee_crud(emp_id,updated_emp)
        return get_emp_id(emp_id)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"Error: {e}")
    
    
@app.delete('/employees/{employee_id}')
# API endpoint to delete an employee by ID
def delete_employee_endpoint(employee_id:int):
    try:
        data = delete_employee_by_id(employee_id)
        return {'details':'Employee Deleted Successfully!'}
    
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Error: {e}")
    