from config.db_connection import get_db_connection

def create_training(training_id,training_name,training_title,training_description,requested_date,status,manager_id):
    conn=get_db_connection()
    cursor=conn.cursor()
    
    try:
        query="""
        INSERT INTO training_requests (training_id,training_name,training_title,training_description,requested_date,status,manager_id)
        VALUES (%s,%s,%s,%s,%s,%s,%s)
        """
        cursor.execute(query,(training_id,training_name,training_title,training_description,requested_date,status,manager_id))
        conn.commit()
        return {"message": "Training Created Sucessfully"}
    
    except Exception as e:
        print ("Error in Adding :",e)
    finally:
        cursor.close()
        conn.close()
        print("Connection Closed Sucessully - Add")
        
def get_all_training():
    conn=get_db_connection()
    cursor=conn.cursor()
    try:
        cursor.execute("SELECT * FROM training_requests ORDER BY id")
        rows=cursor.fetchall()
        if not rows:
            return {"message":"No details Found"}
        return rows
    except Exception as e:
        print("Error :",e)
    finally:
        cursor.close()
        conn.close()
        print("Connection Closed Sucessfully - GEt all")

def get_training_by_id(id):
    conn=get_db_connection()
    cursor=conn.cursor()
    
    try:
        cursor.execute("SELECT * FROM training_requests where id = %s",(id,))
        row=cursor.fetchone()
        if row:
            return {"Details":row}
        else: return {"No Details Found"}
    except Exception as e:
        print("Error :",e)
    finally:
        cursor.close()
        conn.close()
        print("Connection Closed - GET by id")
        
        
def update_training_by_id(id,training_id,training_name,training_title,training_description,requested_date,status,manager_id):
    conn = get_db_connection()
    cursor = conn.cursor()

    try:
        cursor.execute("SELECT 1 FROM training_requests WHERE id=%s", (id,))
        row = cursor.fetchone()
        if not row:
            return "Training not found"  

        query = """
        UPDATE training_requests SET
        training_id=%s, training_name=%s, training_title=%s, training_description=%s, requested_date=%s,
        status=%s,manager_id=%s
        WHERE id=%s
        """
        cursor.execute(query, (training_id, training_name,training_title,training_description,requested_date,status,manager_id,id))
        conn.commit()

        return "Training updated successfully"

    except Exception as e:
        print("Error in Updating:", e)

    finally:
        cursor.close()
        conn.close()
        print("Connection Closed Successfully! - Update")

        
def delete_training_by_id(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        cursor.execute("DELETE FROM training_requests WHERE id=%s", (id,))
        conn.commit()
        
        if cursor.rowcount > 0:
            return "Training deleted successfully"  
        else:
            return "Training not found"  
    except Exception as e:
        print("Error in Deleting:", e)  
    finally:
        cursor.close()
        conn.close()
        print("Connection closed successfully - Delete")




def update_training_status(id,new_status):
    conn=get_db_connection()
    cursor=conn.cursor()
    
    try:
        cursor.execute("UPDATE training_requests SET status=%s WHERE id=%s",(new_status,id))
        conn.commit()
        if cursor.rowcount>0:
            return {"message":"Updated Status Sucessfully"}
        else:
            return "No Training Found"
    
    except Exception as e:
        print("Error in Updating Status :",e)
    
    finally:
        cursor.close()
        conn.close()
        print("Connection Closed Sucessfuly - Patch")