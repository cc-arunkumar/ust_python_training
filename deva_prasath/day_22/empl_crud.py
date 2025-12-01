import pymysql
from empl_model import EntityRequest
def get_db_connection():
    conn=pymysql.connect(
        host="localhost",
        user="root",
        password="pass@word1",
        database="training"
    )
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
            )
        conn.commit()
    except Exception as e:
        raise e
    finally:
        cursor.close()
        conn.close()

def get_all():
    conn=get_db_connection()
    cursor=conn.cursor()
    try:
        cursor.execute("select * from training_requests")
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
        cursor.execute("select * from training_requests where id=%s",(id,))
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
    )
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
        cursor.execute("update training_requests set employee_name=%s where id=%s",(employee_name,id))
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
        cursor.execute("delete from training_requests where id=%s",(id,))
        conn.commit()
    except Exception as e:
        raise e
    finally:
        cursor.close()
        conn.close()