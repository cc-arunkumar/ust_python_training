import pymysql
from db_connection import get_connection
from employee_model import Employee

def get_all_employees():
    try:
        conn=get_connection()
        cursor=conn.cursor()
        cursor.execute('''
                       SELECT * FROM ust_db.emp_training
                       '''
        )
        data=cursor.fetchall()
        return data
    except Exception:
        return False
    finally:
        if conn.open:
            cursor.close()
            conn.close()
            
def get_employee_by_id(id):
    try:
        conn=get_connection()
        cursor=conn.cursor()
        cursor.execute('''
                       SELECT * FROM ust_db.emp_training WHERE id=%s
                       ''',
                       (id,)
        )
        data=cursor.fetchone()
        return data
    except Exception:
        return False
    finally:
        if conn.open:
            cursor.close()
            conn.close()
            
def create_employee(emp:Employee):
    try:
        conn=get_connection()
        cursor=conn.cursor()
        cursor.execute('''
            INSERT INTO ust_db.emp_training
            (employee_id,employee_name,training_title,
            training_description,requested_date,status,
            manager_id) VALUES(
                %s,%s,%s,
                %s,%s,%s,
                %s
            )
            ''',
            (emp.employee_id,emp.employee_name,emp.training_title,
            emp.training_description,emp.requested_date,emp.status,
            emp.manager_id)
        )
        conn.commit()
        return emp
    except Exception:
        return False
    finally:
        if conn.open:
            cursor.close()
            conn.close()
            
def update_employee_by_Id(id,emp:Employee):
    try:
        conn=get_connection()
        cursor=conn.cursor()
        if get_employee_by_id(id):
            cursor.execute('''
                UPDATE ust_db.emp_training
                SET employee_id=%s,
                employee_name=%s,
                training_title=%s,
                training_description=%s,
                requested_date=%s,
                status=%s,
                manager_id=%s
                WHERE id = %s
                ''',
                (emp.employee_id,emp.employee_name,emp.training_title,
                emp.training_description,emp.requested_date,emp.status,
                emp.manager_id,id)
            )
            conn.commit()
            return emp
        return False
    except Exception:
        return False
    finally:
        if conn.open:
            cursor.close()
            conn.close()

def patch_by_id(id,field,value):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        if get_employee_by_id(id):
            query = f"UPDATE ust_db.emp_training SET {field}=%s WHERE id=%s"
            cursor.execute(query, (value, id))
            conn.commit()
            return True
        else:
            return False
    except Exception:
        return False
    finally:
        if conn.open:
            cursor.close()
            conn.close()

def delete_by_id(id):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        if get_employee_by_id(id):
            cursor.execute("DELETE FROM ust_db.emp_training WHERE id=%s", (id,))
            conn.commit()
            return True
        else:
            return False
    except Exception as e:
        return False
    finally:
        if conn.open:
            cursor.close()
            conn.close()