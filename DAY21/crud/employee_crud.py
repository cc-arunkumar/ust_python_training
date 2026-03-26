from config.db_connection import get_connection


def create_employee(first_name,last_name,email,position,salary,hire_date):
    conn=get_connection()
    cursor=conn.cursor()
    
    try:
        cursor.execute("SELECT 1 FROM employees WHERE email=%s",(email,))
        if cursor.fetchone():
            return {"error": "Email Already Exist"}
        query="""
        INSERT INTO employees
        (first_name,last_name,email,position,salary,hire_date)
        VALUES (%s, %s, %s, %s, %s, %s)
        """
        
        cursor.execute(query,(first_name,last_name,email,position,salary,hire_date))
        conn.commit()
        return {"message":"Employee Created Sucessfully"}
    
    except Exception as e:
        print("Error in Adding :",e)
    finally:
        cursor.close()
        conn.close()
        print("Connection Closed - Creating")
    
def get_employee_by_id(employee_id):
    conn=get_connection()
    cursor=conn.cursor()
    
    try:
        cursor.execute("SELECT * FROM employees where employee_id = %s",(employee_id,))
        row=cursor.fetchone()
        if row:
            return {"Details":row}
        else: return {"No Rows Found"}
    except Exception as e:
        print("Error :",e)
    finally:
        cursor.close()
        conn.close()
        print("Connection Closed - GET")


def update_employee_by_id(employee_id, first_name, last_name, email, position, salary, hire_date):
    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT 1 FROM employees WHERE employee_id=%s", (employee_id,))
        row = cursor.fetchone()
        if not row:
            return "Employee not found"  

        query = """
        UPDATE employees SET
        first_name=%s, last_name=%s, email=%s, position=%s, salary=%s,
        hire_date=%s
        WHERE employee_id=%s
        """
        cursor.execute(query, (first_name, last_name, email, position, salary, hire_date, employee_id))
        conn.commit()

        return "Employee updated successfully"

    except Exception as e:
        print("Error in Updating:", e)
        return "Internal Server Error"

    finally:
        cursor.close()
        conn.close()
        print("Connection Closed Successfully! - Update")

        
def delete_employee_by_id(employee_id: int):
    conn = get_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute("DELETE FROM employees WHERE employee_id=%s", (employee_id,))
        conn.commit()
        
        if cursor.rowcount > 0:
            return "Employee deleted successfully"  # Success message
        else:
            return "Employee not found"  # Failure message if no rows were affected
    except Exception as e:
        print("Error in Deleting:", e)
        return "Internal Server Error"  # Return error message if something goes wrong
    finally:
        cursor.close()
        conn.close()
        print("Connection closed successfully - Delete")
