import pymysql
from fastapi import HTTPException
from practice.config.db_connection import get_connection
from practice.models.training_models import Training

def Create_employee(request:Training):
    try:
        conn=get_connection()
        cursor=conn.cursor(pymysql.cursors.DictCursor)
        sql="""
        INSERT INTO training_requests(
            employee_id,employee_name,training_title,
            training_description,requested_date,
            status,manager_id,last_updated)
        VALUES (%s,%s,%s,%s,
                %s,%s,%s,%s) 
        """
        values =(
            request.employee_id,
            request.employee_name,
            request.training_title,
            request.training_description,
            request.requested_date.strftime("%Y-%m-%d"),
            request.status,
            request.manager_id,
            request.last_updated
        )
        cursor.execute(sql,values)
        conn.commit()
        return {"message":"employee inserted succesfully"}
    except Exception as e:
        if conn:
            conn.rollback()
        raise HTTPException(status_code=404,detail=f"error inserting employees {str(e)}")
    finally:
        if conn:
            cursor.close()
            conn.close()
            
def get_employees():
    try:
        conn=get_connection()
        cursor=conn.cursor(pymysql.cursors.DictCursor)
        sql="SELECT * FROM training_requests"
        cursor.execute(sql)
        return cursor.fetchall()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching employees: {str(e)}")
    finally:
        if conn:
            cursor.close()
            conn.close()

def get_employees_by_id(id:int):
    try:
        conn=get_connection()
        cursor=conn.cursor()
        sql="SELECT * FROM training_requests WHERE id=%s"
        cursor.execute(sql,(id,))
        row=cursor.fetchone()
        if not row:
            raise HTTPException(status_code=404, detail=f"Id {id} not found")
        return row
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching employee id: {str(e)}")
    finally:
        if conn:
            cursor.close()
            conn.close()
            
def update_employee(id:int,request:Training):
    try:
        conn=get_connection()
        cursor=conn.cursor(pymysql.cursors.DictCursor)
        sql="""UPDATE training_requests SET employee_id=%s,
             employee_name=%s, training_title=%s,
             training_description=%s, requested_date=%s,
             status=%s, manager_id=%s, last_updated=%s
         WHERE id=%s"""

        values=(
            request.employee_id,
            request.employee_name,
            request.training_title,
            request.training_description,
            request.requested_date.strftime("%Y-%m-%d"),
            request.status,
            request.manager_id,
            request.last_updated,
            id
        )
        cursor.execute(sql,values)
        conn.commit()
        
        if cursor.rowcount==0:
            raise HTTPException(status=404,detail=f"id {id} not found")
        return {"message":"employees updated successfully","id":id}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error updating employee: {str(e)}")
    finally:
        if conn:
            cursor.close()
            conn.close()
def update_training_title(id,training_title):
    try:
        conn=get_connection()
        cursor=conn.cursor()
        sql="UPDATE training_requests SET training_title=%s  WHERE id=%s"
        cursor.execute(sql,(str(training_title),id))
        conn.commit()
        
        if cursor.rowcount==0:
            raise HTTPException(sttaus=404,detail=f"id {id} not found")
        return {"message":"employees updated successfully","id":id,"training_title":training_title}
     
    except Exception as e:
        if conn:
            conn.rollback()
        raise HTTPException(status_code=500, detail=f"Error updating training_title: {str(e)}")
    finally:
        if conn:
            cursor.close()
            conn.close() 
            
def delete_training(id):
    try:
        conn=get_connection()
        cursor=conn.cursor()
        sql="DELETE FROM training_requests WHERE id=%s"
        cursor.execute(sql,(id,))
        conn.commit()
        if cursor.rowcount==0:
            raise HTTPException(sttaus=404,detail=f"id {id} not found")
        return {"message":"employees deleted successfully","id":id}
     
    except Exception as e:
        if conn:
            conn.rollback()
        raise HTTPException(status_code=500, detail=f"Error deleting employee: {str(e)}")
    finally:
        if conn:
            cursor.close()
            conn.close()     
