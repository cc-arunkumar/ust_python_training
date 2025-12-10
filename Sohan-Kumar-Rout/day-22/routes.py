from fastapi import APIRouter, Depends, HTTPException, status
from db_connection import get_connection
from models import TrainingRequest, TrainingUpdate
from jwt import require_auth

router = APIRouter(prefix="/SOHAN", tags=["training-requests"])

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_request(body: TrainingRequest,user=Depends(require_auth)):
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            sql = """
            INSERT INTO training_request (
                employee_id, employee_name, training_title, training_description,
                requested_date, status, manager_id
            ) VALUES (%s,%s,%s,%s,%s,%s,%s)
            """
            cur.execute(sql, (
                body.employee_id,
                body.employee_name,
                body.training_title,
                body.training_description,
                body.requested_date.strftime("%Y-%m-%d"),
                body.status,
                body.manager_id
            ))
            conn.commit()
            new_id = cur.lastrowid
            cur.execute("SELECT * FROM training_request WHERE id=%s", (new_id,))
            return cur.fetchone()
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=f"Server error: {e}")
    finally:
        conn.close()

@router.get("/", status_code=status.HTTP_200_OK)
def list_requests(user=Depends(require_auth)):
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM training_request ORDER BY id DESC")
            return cur.fetchall()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Server error: {e}")
    finally:
        conn.close()

@router.get("/{id}", status_code=status.HTTP_200_OK)
def get_request(id: int,user=Depends(require_auth)):
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM training_request WHERE id=%s", (id,))
            row = cur.fetchone()
            if not row:
                raise HTTPException(status_code=404, detail="Request not found")
            return row
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Server error: {e}")
    finally:
        conn.close()

@router.put("/{id}", status_code=status.HTTP_200_OK)
def update_request(id: int, body: TrainingRequest,user=Depends(require_auth)):
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            sql = """
            UPDATE training_request
            SET employee_id=%s, employee_name=%s, training_title=%s,
                training_description=%s, requested_date=%s, status=%s, manager_id=%s
            WHERE id=%s
            """
            cur.execute(sql, (
                body.employee_id,
                body.employee_name,
                body.training_title,
                body.training_description,
                body.requested_date.strftime("%Y-%m-%d"),
                body.status,
                body.manager_id,
                id
            ))
            conn.commit()
            if cur.rowcount == 0:
                raise HTTPException(status_code=404, detail="Request not found")
            cur.execute("SELECT * FROM training_request WHERE id=%s", (id,))
            return cur.fetchone()
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=f"Server error: {e}")
    finally:
        conn.close()

@router.patch("/{id}", status_code=status.HTTP_200_OK)
def patch_request(id: int, body: TrainingUpdate,user=Depends(require_auth)):
    conn = get_connection()
    try:
        data = body.dict(exclude_unset=True)
        if not data:
            raise HTTPException(status_code=400, detail="No fields to update")

        if "requested_date" in data and data["requested_date"] is not None:
            data["requested_date"] = data["requested_date"].strftime("%Y-%m-%d")

        fields = [f"{k}=%s" for k in data.keys()]
        values = list(data.values()) + [id]

        with conn.cursor() as cur:
            cur.execute(f"UPDATE training_request SET {', '.join(fields)} WHERE id=%s", tuple(values))
            conn.commit()
            if cur.rowcount == 0:
                raise HTTPException(status_code=404, detail="Request not found")
            cur.execute("SELECT * FROM training_requests WHERE id=%s", (id,))
            return cur.fetchone()
    except HTTPException:
        raise
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=f"Server error: {e}")
    finally:
        conn.close()

@router.delete("/{id}", status_code=status.HTTP_200_OK)
def delete_request(id: int,user=Depends(require_auth)):
    conn = get_connection()
    try:
        with conn.cursor() as cur:
            cur.execute("DELETE FROM training_request WHERE id=%s", (id,))
            conn.commit()
            if cur.rowcount == 0:
                raise HTTPException(status_code=404, detail="Request not found")
            return {"message": "Deleted successfully", "id": id}
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=f"Server error: {e}")
    finally:
        conn.close()
