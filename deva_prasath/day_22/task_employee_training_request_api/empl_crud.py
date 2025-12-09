import pymysql
from empl_model import EntityRequest

def get_db_connection():
    conn=pymysql.connect(
        host="localhost",
        user="root",
        password="pass@word1",
        database="training"
    )   # Create and return a database connection
    return conn

def create_rec(ob:EntityRequest):
    conn=get_db_connection()
    cursor=conn.cursor()
    try:
        cursor.execute(
            """
            insert into training_requests(employee_id,employee_name,training_title,training_description,requested_date,status,manager_id,last_updated)
            values(%s,%s,%s,%s,%s,%s,%s,%s)""",
            (
                ob.employee_id,
                ob.employee_name,
                ob.training_title,
                ob.training_description,
                ob.requested_date,
                ob.status,
                ob.manager_id,
                ob.last_updated
            )
            )   # Insert a new training request record
        conn.commit()     # Save changes
    except Exception as e:
        raise e          # Re-raise exception for API to handle
    finally:
        cursor.close()   # Cleanup cursor
        conn.close()     # Close connection

def get_all():
    conn=get_db_connection()
    cursor=conn.cursor()
    try:
        cursor.execute("select * from training_requests")   # Fetch all records
        return cursor.fetchall()
    except Exception as e:
        raise e
    finally:
        cursor.close()
        conn.close()

def get_by_id(id:int):
    conn=get_db_connection()
    cursor=conn.cursor()
    try:
        cursor.execute("select * from training_requests where id=%s",(id,))   # Fetch record by ID
        return cursor.fetchone()
    except Exception as e:
        raise e
    finally:
        cursor.close()
        conn.close()

def update_rec(id:int,ob:EntityRequest):
    conn=get_db_connection()
    cursor=conn.cursor()
    try:
        cursor.execute(
    """
    update training_requests
    set  employee_id=%s,employee_name=%s,training_title=%s,
    training_description=%s,requested_date=%s,status=%s,
    manager_id=%s,last_updated=%s
    
    where id=%s
    """,(
        ob.employee_id,
        ob.employee_name,
        ob.training_title,
        ob.training_description,
        ob.requested_date,
        ob.status,
        ob.manager_id,
        ob.last_updated,
        id
    )
    )   # Update full record based on ID
        conn.commit()
    except Exception as e:
        raise e
    finally:
        cursor.close()
        conn.close()
    
def update_patch(employee_name:str,id:int):
    conn=get_db_connection()
    cursor=conn.cursor()
    try:
        cursor.execute("update training_requests set employee_name=%s where id=%s",(employee_name,id))   # Update only name
        conn.commit()
    except Exception as e:
        raise e
    finally:
        cursor.close()
        conn.close()
        
def delete_rec(id:int):
    conn=get_db_connection()
    cursor=conn.cursor()
    try:
        cursor.execute("delete from training_requests where id=%s",(id,))   # Delete record by ID
        conn.commit()
    except Exception as e:
        raise e
    finally:
        cursor.close()
        conn.close()
