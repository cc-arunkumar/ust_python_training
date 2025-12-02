from models.training_model import TrainingRequest
from datetime import date
from fastapi import HTTPException
from config.db_connection import get_connection
def get_all_training():
    try:
        conn=get_connection()
        cursor=conn.cursor()
        
        query="""SELECT * FROM training_request
        """
        cursor.execute(query)  
        result = cursor.fetchall() 

        return result

    except Exception as e:
        print("Error:", e)
        raise HTTPException(status_code=500, detail="Error getting training")
    finally:
        cursor.close()
        conn.close()
        
def get_by_id(id:int):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        query = "SELECT * FROM training_request WHERE id = %s"
        cursor.execute(query, (id,))
        result = cursor.fetchone()
        
        if not result:
            raise HTTPException(status_code=404, detail="training not found")
        
        return result
    except Exception as e:
        print("Error:", e)
        raise HTTPException(status_code=500, detail="Error fetching training")
    finally:
        cursor.close()
        conn.close()
        
def create_training(trn: TrainingRequest):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        query = """
        INSERT INTO training_request (
            employee_id,
            employee_name,
            training_title,
            training_description,
            requested_date,
            status,
            manager_id,
            last_updated
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, NOW())
        """
        data = (
            trn.employee_id,
            trn.employee_name,
            trn.training_title,
            trn.training_description,
            trn.requested_date,   
            trn.status,           
            trn.manager_id
        )

        cursor.execute(query, data)
        conn.commit()
        return {"message": "Training request created successfully"}

    except Exception as e:
        print("Error:", e)
        raise HTTPException(status_code=500, detail="Error adding training request")

    finally:
        cursor.close()
        conn.close()
        
def delete_training(id: int):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        query = "DELETE FROM training_request WHERE id = %s"
        cursor.execute(query, (id,))
        conn.commit()
        
        return {"message": f"Training with id {id} deleted successfully"}
    except Exception as e:
        print("Error:", e)
        raise HTTPException(status_code=500, detail="Error deleting Training")
    finally:
        cursor.close()
        conn.close()
        
def update_trainig(id:int,new_trng:TrainingRequest):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        query = """
        UPDATE training_request SET
            employee_id=%s,
            employee_name=%s,
            training_title=%s,
            training_description=%s,
            requested_date=%s,
            status=%s,
            manager_id=%s,
            last_updated=NOW()
        WHERE id=%s
        """
        data = (
            new_trng.employee_id,
            new_trng.employee_name,
            new_trng.training_title,
            new_trng.training_description,
            new_trng.requested_date,
            new_trng.status,
            new_trng.manager_id,
            id
        )

        cursor.execute(query, data)
        conn.commit()
        return {"message": "Training request updated successfully"}

    except Exception as e:
        print("Error:", e)
        raise HTTPException(status_code=500, detail="Error updating training request")

    finally:
        cursor.close()
        conn.close()
        
def partial_update(id:int,trng_title:str):
    try:
        conn=get_connection()
        cursor=conn.cursor()
        query = """
        UPDATE training_request
        SET training_title=%s
        WHERE id=%s
        """
        data = (trng_title,  id)

        cursor.execute(query, data)
        conn.commit()

        if cursor.rowcount == 0:
            raise HTTPException(status_code=404, detail="Training request not found")

        return {"message": "Training title updated successfully"}

    except Exception as e:
        print("Error:", e)
        raise HTTPException(status_code=500, detail="Error updating training request")

    finally:
        cursor.close()
        conn.close()

