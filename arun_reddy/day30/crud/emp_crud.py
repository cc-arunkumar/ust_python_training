from fastapi import HTTPException, status
from database.mysql_connection import SessionLocal, Employee

# Create a new employee
def create_emp(emp: Employee):
    session = SessionLocal()
    try:
        # Check if manager_id is invalid (manager_id cannot equal an employee id)
        not_valid = session.query(Employee).filter(Employee.id == emp.manager_id).first()
        if not_valid is None:
            new_emp = Employee(
                name=emp.name,
                email=emp.email,
                designation=emp.designation,
                manager_id=emp.manager_id
            )
        else:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Manager_id cannot be an existing employee id"
            )

        session.add(new_emp)
        session.commit()
        session.refresh(new_emp)
        return new_emp

    except HTTPException as e:
        session.rollback()
        raise e  # re-raise HTTPException for FastAPI to handle
    except Exception as e:
        session.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error creating employee: {str(e)}"
        )
    finally:
        session.close()


# Get employee by ID
def get_employee_by_id(id: int):
    session = SessionLocal()
    try:
        employee = session.query(Employee).filter(Employee.id == id).first()
        if employee is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Employee not found"
            )
        return employee

    except Exception as e:
        session.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error fetching employee: {str(e)}"
        )
    finally:
        session.close()


# Get employees by manager ID
def get_employees_by_manager_id(manager_id: int):
    session = SessionLocal()
    try:
        employees = session.query(Employee).filter(Employee.manager_id == manager_id).all()
        if not employees:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="No employees found for this manager"
            )
        return employees

    except Exception as e:
        session.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error fetching employees: {str(e)}"
        )
    finally:
        session.close()


# Update employee by ID
def update_employee_by_id(id: int, emp: Employee):
    session = SessionLocal()
    try:
        employee = session.query(Employee).filter(Employee.id == id).first()
        if employee is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Employee not found"
            )

        # Update fields
        employee.name = emp.name
        employee.designation = emp.designation
        employee.manager_id = emp.manager_id
        employee.email = emp.email

        session.commit()
        session.refresh(employee)
        return {"message": "Updated successfully"}

    except Exception as e:
        session.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error updating employee: {str(e)}"
        )
    finally:
        session.close()


# Delete employee by ID
def delete_emp_byid(id: int):
    session = SessionLocal()
    try:
        employee = session.query(Employee).filter(Employee.id == id).first()
        if employee is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Employee not found"
            )

        session.delete(employee)
        session.commit()
        return {"message": "Deleted successfully"}

    except Exception as e:
        session.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error deleting employee: {str(e)}"
        )
    finally:
        session.close()
        
        
        


