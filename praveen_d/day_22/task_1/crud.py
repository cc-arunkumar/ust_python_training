from database_connection import get_connection
from datetime import datetime

def get_all_data():
    try:
        conn=get_connection()
        cursor=conn.cursor()
        
        query="""
        SELECT * FROM ust_db.emp_training_request
        """
        
        cursor.execute(query)
        result=cursor.fetchall()
        # conn.commit()
        return result
    except Exception as e:
        print("Get api Exception:",e)
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

def get_by_id(id):
    try:
        conn=get_connection()
        cursor=conn.cursor()
        
        query="""
        SELECT * FROM ust_db.emp_training_request
        WHERE id=%s
        """
        
        cursor.execute(query,(id,))
        result=cursor.fetchone()
        return result
    except Exception as e:
        print("Get api Exception:",e)
    finally:
        cursor.close()
        conn.close()

def create_request(emp_request):
    conn=None
    cursor=None
    try:
        print("Try")
        conn=get_connection()
        print("conn")
        cursor=conn.cursor()
        last_updated=datetime.now()
        query="""
        INSERT INTO ust_db.emp_training_request(
            employee_id ,employee_name,training_title,
            training_description,requested_date,status,
            manager_id ,last_updated ) 
            VALUES(
                %s,%s,%s,
                %s,%s,%s,
                %s,%s
            ) 
        """
        values=(
            emp_request.employee_id,emp_request.employee_name,emp_request.training_title,
            emp_request.training_description,emp_request.requested_date,emp_request.status,
            emp_request.manager_id,last_updated
        )
        
        cursor.execute(query,values)
        print("cursor_executed")
        conn.commit()
        result=emp_request
        print("result returned")
        return result
    except Exception as e:
        print("Create api Exception:",e)
    finally:
        cursor.close()
        conn.close()
        
def update_request(id, emp_request):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        last_updated = datetime.now()
        # print(f"Last updated: {last_updated} - Type: {type(last_updated)}")
        
        # Corrected UPDATE query
        query = """
        UPDATE ust_db.emp_training_request
        SET 
            employee_id = %s,
            employee_name = %s,
            training_title = %s,
            training_description = %s,
            requested_date = %s,
            status = %s,
            manager_id = %s,
            last_updated = %s
        WHERE id = %s
        """
        
        values = (
            emp_request.employee_id,
            emp_request.employee_name,
            emp_request.training_title,
            emp_request.training_description,
            emp_request.requested_date,
            emp_request.status,
            emp_request.manager_id,
            last_updated,
            id
        )
        
        cursor.execute(query, values)
        conn.commit()  # Commit the changes to the database
        
        result = emp_request  # Return the updated request object (or any other data you need)
        return result
    
    except Exception as e:
        print("Update API Exception:", e)
        return None  # Or raise the exception based on how you want to handle it
    finally:
        cursor.close()
        conn.close()

def delete_request(id):
    try:
        conn=get_connection()
        cursor=conn.cursor()
        
        query="""
        DELETE FROM ust_db.emp_training_request
            WHERE id=%s
        """
        cursor.execute(query,(id,))
        conn.commit()
        result=f"Employee request {id} deleted sucessfully"
        return result
    except Exception as e:
        print("Delete api Exception:",e)
    finally:
        cursor.close()
        conn.close()

def patch_request(id, emp_request):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        last_updated = datetime.now()

        query = """
        UPDATE ust_db.emp_training_request
        SET
            employee_id = %s,
            employee_name = %s,
            training_title = %s,
            training_description = %s,
            requested_date = %s,
            status = %s,
            manager_id = %s,
            last_updated = %s
        WHERE id = %s
        """

        values = (
            emp_request.employee_id,
            emp_request.employee_name,
            emp_request.training_title,
            emp_request.training_description,
            emp_request.requested_date,
            emp_request.status,
            emp_request.manager_id,
            last_updated,
            id
        )

        cursor.execute(query, values)
        conn.commit()

        return f"Employee request {id} updated successfully"

    except Exception as e:
        print("Patch API Exception:", e)

    finally:
        cursor.close()
        conn.close()
