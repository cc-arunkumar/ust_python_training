from config.db_connection import get_db_connection

def create_employee(first_name,last_name,email,position,salary,hire_date):
    
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute("SELECT email FROM employees WHERE email = %s",(email,))
        if cursor.fetchone():
            return {"error" : "Email already exist"}
        
        query = """
        INSERT INTO employees (first_name,last_name,email,position,salary,hire_date)
        VALUES (%s,%s,%s,%s,%s)
        """
        
        conn.commit()
        return "Data added successfully"
    except Exception as e:
        raise e
    finally:
        if conn and conn.open:
            cursor.close()
            conn.close()
        print("connection closed")
        
        
def get_employee_by_id(employee_id):
    conn = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM employees WHERE employee_id = %s", (employee_id,))
        row = cursor.fetchone()
        if row:
            return {"Details":row}
        else:
            return {"No row found"}
    except Exception as e:
        print("Error",e)
    finally:
            if conn and conn.open:
                cursor.close()
                conn.close()
            print("Connection Closed")
            
def update_employee_by_id(first_name,last_name,email,position,salary,hire_date):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT email FROM employees WHERE email = %s",(email,))
            if cursor.fetchone():
                return {"error" : "Email already exist"}
            query = """
                INSERT INTO employees (first_name,last_name,email,position,salary,hire_date)
                VALUES (%s,%s,%s,%s,%s)
                """
            conn.commit()
            return "Data added successfully"
            
        except Exception as e:
            raise e
        finally:
            if conn.open:
                cursor.close()
                conn.close()
            print("Connection Closed")
            
def delete_employee_by_id(employee_id):
    conn = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE employee_id FROM employees WHERE employee_id = %s",(employee_id,))
        conn.commit()
        
        if cursor:
            return "Data deleted successfully"
        else:
            return "Data not found"
    except Exception as e:
        raise e
    finally:
            if conn.open:
                cursor.close()
                conn.close()
            print("Connection Closed")