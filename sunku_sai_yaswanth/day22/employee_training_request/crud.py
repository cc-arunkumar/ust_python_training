import csv
from typing import Optional
from validations import EmployeeValidations
from db_connection import get_connection
from fastapi import HTTPException


def insert_employee(new_employee: EmployeeValidations):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT INTO ust_training_db.training_request(
                employee_id, employee_name, training_title, training_description, requested_date, status, manager_id, last_updated
            ) 
            VALUES (%s, %s, %s, %s, %s, %s,%s, NOW())
            """, (
                new_employee.employee_id,
                new_employee.employee_name,          
                new_employee.training_title,        
                new_employee.training_description,      
                new_employee.requested_date,      
                new_employee.status,  # Corrected this field
                new_employee.manager_id,      
            )
        )
        conn.commit()
    except Exception as e:
        print(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Error inserting employee")
    finally:
        if conn:
            cursor.close()
            conn.close()
            
def get_by_id(emp_id: int):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM ust_training_db.training_request WHERE employee_id = %s", (emp_id,))
        row = cursor.fetchone()
        
        return row if row else None
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching employee with ID {emp_id}")
    finally:
        if conn:
            cursor.close()
            conn.close()
            
def get_all_employees():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM ust_training_db.training_request")
        rows = cursor.fetchall()
        return rows
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching requests: {str(e)}")
    finally:
        if conn:
            cursor.close()
            conn.close()
            
def update_employee_by_id(employee_id: int, updated_employee: EmployeeValidations):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            """
            UPDATE ust_training_db.training_request  # Corrected the database name
            SET 
                employee_id=%s, employee_name = %s, training_title = %s, 
                training_description = %s,
                requested_date = %s, 
                status = %s,
                manager_id = %s,
                last_updated = NOW()
            WHERE employee_id = %s
            """, (
                updated_employee.employee_id,
                updated_employee.employee_name,          
                updated_employee.training_title,        
                updated_employee.training_description,      
                updated_employee.requested_date,      
                updated_employee.status,  # Corrected this field
                updated_employee.manager_id,      
                employee_id  
            )
        )
        conn.commit()
        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail=f"Employee training request with ID {employee_id} not found.")

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error updating employee training request: {str(e)}")
    finally:
        if conn.open:
            cursor.close()
            conn.close()
            
def delete_emp(emp_id: int):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        # Check if employee exists
        request = get_by_id(emp_id)
        if not request:
            raise HTTPException(status_code=404, detail=f"Employee with ID {emp_id} not found.")
        
        # Proceed with deletion
        cursor.execute("DELETE FROM ust_training_db.training_request WHERE employee_id = %s", (emp_id,))
        conn.commit()
        return {"detail": f"Training Request with ID {emp_id} has been deleted successfully."}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error deleting employee with ID {emp_id}")
    finally:
        if conn:
            cursor.close()
            conn.close()
