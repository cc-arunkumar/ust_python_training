from fastapi import APIRouter, Depends, HTTPException, status
from typing import List, Dict, Any, Optional
from datetime import date, datetime
from pydantic import BaseModel, Field, field_validator
from db_connection import get_connection
from auth.auth import get_current_user

router = APIRouter(prefix="/api/v1/training-requests", tags=["Training Requests"])

UST_ID_PATTERN = r"^UST\d+$"

class TrainingRequest(BaseModel):
    employee_id: str = Field(..., max_length=20, pattern=UST_ID_PATTERN)
    employee_name: str = Field(..., max_length=100)
    training_title: str = Field(..., min_length=5, max_length=200)
    training_description: str = Field(..., min_length=10)
    requested_date: date
    status: str = Field(..., pattern=r"^(PENDING|APPROVED|REJECTED)$")
    manager_id: str = Field(..., max_length=20, pattern=UST_ID_PATTERN)

    @field_validator("employee_name")
    def validate_employee_name(cls, v):
        if not v.strip():
            raise ValueError("employee_name cannot be empty")
        if any(ch.isdigit() for ch in v):
            raise ValueError("employee_name cannot contain numbers")
        return v

    @field_validator("requested_date")
    def validate_requested_date(cls, v):
        if v > date.today():
            raise ValueError("requested_date cannot be a future date")
        return v


class TrainingRequestOut(TrainingRequest):
    id: int
    last_updated: datetime

class PartialTrainingRequest(BaseModel):
    employee_id: Optional[str] = Field(None, max_length=20, pattern=UST_ID_PATTERN)
    employee_name: Optional[str] = Field(None, max_length=100)
    training_title: Optional[str] = Field(None, min_length=5, max_length=200)
    training_description: Optional[str] = Field(None, min_length=10)
    requested_date: Optional[date]
    status: Optional[str] = Field(None, pattern=r"^(PENDING|APPROVED|REJECTED)$")
    manager_id: Optional[str] = Field(None, max_length=20, pattern=UST_ID_PATTERN)

    class Config:
        extra = "forbid"

# Create
@router.post("/", status_code=status.HTTP_201_CREATED)
def create_request(req: TrainingRequest, user: str = Depends(get_current_user)):
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute(
            """
            INSERT INTO training_requests
            (employee_id, employee_name, training_title, training_description, requested_date, status, manager_id)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            """,
            (req.employee_id, req.employee_name, req.training_title, req.training_description,
             req.requested_date, req.status, req.manager_id)
        )
        conn.commit()
        return {"id": cur.lastrowid}
    finally:
        cur.close()
        conn.close()

# List
@router.get("/", response_model=List[TrainingRequestOut])
def list_requests(user: str = Depends(get_current_user)):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM training_requests ORDER BY id DESC")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

# Get by ID
@router.get("/{id}", response_model=TrainingRequestOut)
def get_request(id: int, user: str = Depends(get_current_user)):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM training_requests WHERE id=%s", (id,))
    row = cur.fetchone()
    cur.close()
    conn.close()
    if not row:
        raise HTTPException(status_code=404, detail="Training request not found")
    return row

# Update full
@router.put("/{id}")
def update_request(id: int, req: TrainingRequest, user: str = Depends(get_current_user)):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id FROM training_requests WHERE id=%s", (id,))
    if not cur.fetchone():
        raise HTTPException(status_code=404, detail="Training request not found")
    cur.execute(
        """
        UPDATE training_requests
        SET employee_id=%s, employee_name=%s, training_title=%s, training_description=%s,
            requested_date=%s, status=%s, manager_id=%s
        WHERE id=%s
        """,
        (req.employee_id, req.employee_name, req.training_title, req.training_description,
         req.requested_date, req.status, req.manager_id, id)
    )
    conn.commit()
    cur.close()
    conn.close()
    return {"status": "success", "message": f"Request {id} updated"}

# Partial update
@router.patch("/{id}")
def partial_update_request(id: int, patch: PartialTrainingRequest, user: str = Depends(get_current_user)):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM training_requests WHERE id=%s", (id,))
    if not cur.fetchone():
        raise HTTPException(status_code=404, detail="Training request not found")

    updates: Dict[str, Any] = {k: v for k, v in patch.model_dump(exclude_unset=True).items()}
    if not updates:
        raise HTTPException(status_code=400, detail="No fields provided for update")

    set_clause = ", ".join([f"{k}=%s" for k in updates.keys()])
    values = list(updates.values()) + [id]
    sql = f"UPDATE training_requests SET {set_clause} WHERE id=%s"
    cur.execute(sql, values)
    conn.commit()
    cur.close()
    conn.close()
    return {"status": "success", "message": f"Request {id} partially updated", "updated_fields": list(updates.keys())}

# Delete
@router.delete("/{id}")
def delete_request(id: int, user: str = Depends(get_current_user)):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM training_requests WHERE id=%s", (id,))
    conn.commit()
    if cur.rowcount == 0:
        raise HTTPException(status_code=404, detail="Training request not found")
    cur.close()
    conn