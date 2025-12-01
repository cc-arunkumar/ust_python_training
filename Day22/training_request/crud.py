from db_connection import get_db_connection
from model import TrainingRequestModel

def create_training_request(employee_id, employee_name, training_title, training_description, requested_date, status, manager_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute("SELECT employee_id FROM training_requests WHERE employee_id = %s", (employee_id,))
        if cursor.fetchone():
            return {"message": "Employee ID already present"}
        
        query = """
        INSERT INTO training_requests (employee_id, employee_name, training_title, training_description, requested_date, status, manager_id)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (employee_id, employee_name, training_title, training_description, requested_date, status, manager_id))
        conn.commit()
        return {"message": "Training request created successfully"}
    
    except Exception as e:
        return {"error": str(e)}
    
    finally:
        if conn:
            cursor.close()
            conn.close()
        print("Connection closed")
        
def get_all_employee(employee_id:int):
    try:
        conn = get_db_connection
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM employees WHERE employee_id = %s", (employee_id,))
        row = cursor.fetchone()
        if row:
            return {"Details":row}
        else:
            return {"No row found"}
    
    except Exception as e:
        raise e
    finally:
        if conn and conn.open:
            cursor.close()
            conn.close()
        print("connection closed")

def get_training_request_by_id(id):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM training_requests WHERE id = %s", (id,))
        row = cursor.fetchone()
        if row:
            return {"Details": row}
        else:
            return {"message": "ID not found"}
    except Exception as e:
        return {"error": str(e)}
    finally:
        if conn:
            cursor.close()
            conn.close()
        print("Connection closed")

def update_training_request_by_id(id, employee_id, employee_name, training_title, training_description, requested_date, status, manager_id):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM training_requests WHERE id = %s", (id,))
        if not cursor.fetchone():
            return {"message": "ID not found"}
        
        query = """
            UPDATE training_requests
            SET employee_id = %s, employee_name = %s, training_title = %s, training_description = %s,
                requested_date = %s, status = %s, manager_id = %s
            WHERE id = %s
        """
        cursor.execute(query, (employee_id, employee_name, training_title, training_description, requested_date, status, manager_id, id))
        conn.commit()
        return {"message": "Updated successfully"}
    
    except Exception as e:
        return {"error": str(e)}
    
    finally:
        if conn:
            cursor.close()
            conn.close()
        print("Connection closed")
        
def patch_by_employee(employee_id:int):
    conn = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        if cursor.rowcount>0:
            return {"updated status successfully"}
        else:
            return {"no data found"}
    except Exception as e:
        return {"error": str(e)}
    
    finally:
        if conn:
            cursor.close()
            conn.close()
        print("Connection closed")
    
        
        

def delete_training_request_by_id(id):
    conn = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM training_requests WHERE id = %s", (id,))
        if not cursor.fetchone():
            return {"message": "ID not found"}
        
        cursor.execute("DELETE FROM training_requests WHERE id = %s", (id,))
        conn.commit()
        return {"message": "Deleted successfully"}
    
    except Exception as e:
        return {"error": str(e)}
    
    finally:
        if conn:
            cursor.close()
            conn.close()
        print("Connection closed")
