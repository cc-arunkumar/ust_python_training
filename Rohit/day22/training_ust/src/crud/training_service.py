from fastapi import HTTPException
from src.models.training_pydentic import TrainingPydantic
from src.config.db_connecion import get_connection

def create_training_request(training: TrainingPydantic):
    try:
        conn = get_connection()
        with conn.cursor() as cursor:
            sql = """
            INSERT INTO training_requests 
            (employee_id, employee_name, training_title, training_description, requested_date, status, manager_id)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            """
            cursor.execute(sql, (
                training.employee_id,
                training.employee_name,
                training.training_title,
                training.training_description,
                training.requested_date,
                training.status.value,
                training.manager_id
            ))
            conn.commit()
            training.id = cursor.lastrowid
        conn.close()
        return training
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def get_training_data():
    try:
        conn = get_connection()
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM training_requests")
            rows = cursor.fetchall()
        conn.close()
        return rows
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def get_training_by_id(id: int):
    try:
        conn = get_connection()
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM training_requests WHERE id=%s", (id,))
            row = cursor.fetchone()
        conn.close()
        if not row:
            raise HTTPException(status_code=404, detail="Training request not found")
        return row
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def update_patch_by_training(id: int, field: str, value: str):
    allowed_fields = {"employee_id","employee_name","training_title","training_description","requested_date","status","manager_id"}
    if field not in allowed_fields:
        raise HTTPException(status_code=400, detail=f"Field '{field}' not allowed")
    try:
        conn = get_connection()
        with conn.cursor() as cursor:
            sql = f"UPDATE training_requests SET {field}=%s WHERE id=%s"
            cursor.execute(sql, (value, id))
            conn.commit()
            cursor.execute("SELECT * FROM training_requests WHERE id=%s", (id,))
            row = cursor.fetchone()
        conn.close()
        if not row:
            raise HTTPException(status_code=404, detail="Training request not found")
        return row
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def update_put_by_training(id: int, training: TrainingPydantic):
    try:
        conn = get_connection()
        with conn.cursor() as cursor:
            sql = """
            UPDATE training_requests 
            SET employee_id=%s, employee_name=%s, training_title=%s, training_description=%s,
                requested_date=%s, status=%s, manager_id=%s
            WHERE id=%s
            """
            cursor.execute(sql, (
                training.employee_id,
                training.employee_name,
                training.training_title,
                training.training_description,
                training.requested_date,
                training.status.value,
                training.manager_id,
                id
            ))
            conn.commit()
            cursor.execute("SELECT * FROM training_requests WHERE id=%s", (id,))
            row = cursor.fetchone()
        conn.close()
        if not row:
            raise HTTPException(status_code=404, detail="Training request not found")
        return row
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def delete_by_training(id: int):
    try:
        conn = get_connection()
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM training_requests WHERE id=%s", (id,))
            conn.commit()
        conn.close()
        return {"message": "Deleted successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
