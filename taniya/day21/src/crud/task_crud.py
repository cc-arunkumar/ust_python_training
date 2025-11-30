import pymysql
from fastapi import HTTPException
from src.config.db_connection import get_connection
from src.models.employee_management import Employee

def create_employees(emp:Employee):
    try:
        conn=get_connection()
        cursor=conn.cursor(pymysql.cursors.DictCursor)
        sql="""
        INSERT INTO employees(first_name,last_name,email,position,salary,hire_date)
        VALUES(%s,%s,%s,%s,%s,%s)
        """
        values=(emp.first_name,
                emp.last_name,
                emp.email,
                emp.position,
                emp.salary,
                emp.hire_date.strftime("%Y-%m-%d")
                )
        cursor.execute(sql,values)
        conn.commit()
        
        return {"message":"employee inserted successfully"}
    except Exception as e:
        if conn:
            conn.rollback()
        raise HTTPException(status_code=500,detail=f"Error inserting employee {str(e)}")
    finally:
        if conn:
            cursor.close()
            conn.close()
            
def get_emp_by_id(employee_id:int):
    try:
        conn=get_connection()
        cursor=conn.cursor(pymysql.cursors.DictCursor)
        
        sql="""
        SELECT * FROM employees WHERE employee_id=%s
        """
        cursor.execute(sql,(employee_id),)
        row=cursor.fetchone
        if not row:
            return HTTPException(status_code=404,detail=f"error in fetching employee id {employee_id}")
        return row
    except Exception as e:
        raise HTTPException(status_code=500,detail=f"error in employee id {str(e)}")
    finally:
        if conn:
            cursor.close()
            conn.close()
def get_all_employees():
    try:
        conn=get_connection()
        cursor=conn.cursor(pymysql.cursors.DictCursor)
        sql="""
        SELECT * FROM employees
        """
        cursor.execute(sql)
        row= cursor.fetchall
        return row
    except Exception as e:
        raise HTTPException(status_code=500,detail=f"error in employee {str(e)}")
    finally:
        if conn:
            cursor.close()
            conn.close()
            
def update_employee(employee_id:int,emp:Employee):
    try:
        conn=get_connection()
        cursor=conn.cursor()
        sql = "UPDATE employees SET first_name=%s,Last_name=%s,email=%s,position=%s,salary=%s,hire_date=%s WHERE employee_id=%s"
        values=(
            emp.first_name,
            emp.last_name,
            emp.email,
            emp.position,
            emp.salary,
            emp.hire_date.strftime("%Y-%m-%d"),
            employee_id
        )   
        cursor.execute(sql,values)
        conn.commit()
        if cursor.rowcount==0:
            raise HTTPException(status_code=404,detail=f"employee_id {employee_id} not found")
        return {"message":"employee updated successfully","employee_id":employee_id}
    except Exception as e:
        if conn:
            conn.rollback()
        raise HTTPException(status_code=500,detail=f"Error in updating employee {str(e)}")
    finally:
        if conn:
            cursor.close()
            conn.close()    
            
def delete_employee(employee_id:int):
    try:
        conn=get_connection()
        cursor=conn.cursor()
        sql="DELETE FROM employees WHERE employee_id=%s"
        cursor.execute(sql,(employee_id),)
        conn.commit()
        if cursor.rowcount==0:
            raise HTTPException(status_code=404,detail=f"employee id {employee_id} not found")
        return {"message":"employee deleted successfully","employee id":employee_id}
    except Exception as e:
        if conn:
            conn.rollback()
        raise HTTPException(status_code=500,detail=f"Error in deleting employee {str(e)}")
    finally:
        if conn:
            cursor.close()
            conn.close()
        