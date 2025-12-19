# routers/task_remarks.py
# Make sure this file is in your routers/ directory

from fastapi import APIRouter, Depends, HTTPException, status, UploadFile, File, Form
from sqlalchemy.orm import Session
from typing import Optional
from datetime import datetime
import os
import uuid

from services.database import SessionLocal
from services.task_service import get_task, TaskRemark
from utils.auth_dependency import get_current_user

# Create router
task_remarks_router = APIRouter(
    prefix="/tasks",
    tags=["Task Remarks"]
)

print("✅ Task Remarks Router loaded")  # Debug log

# Upload directory
UPLOAD_DIR = "uploads/task-files"
os.makedirs(UPLOAD_DIR, exist_ok=True)


# DB Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ---------------- ADD REMARK WITH FILE UPLOAD ----------------
@task_remarks_router.post("/{task_id}/remarks", status_code=status.HTTP_201_CREATED)
async def add_task_remark(
    task_id: str,
    remark: str = Form(""),
    file: Optional[UploadFile] = File(None),
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)  # Just get_current_user, no permission check
):
    """
    Add a remark to a task with optional file attachment
    """
    print(f"[DEBUG] Adding remark to task: {task_id}")
    print(f"[DEBUG] User: {current_user['emp_id']}")
    print(f"[DEBUG] Remark: {remark}")
    print(f"[DEBUG] File: {file.filename if file else 'None'}")
    
    # Check if task exists
    task = get_task(db, task_id)
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task {task_id} not found"
        )
    
    # Validate input
    if not remark.strip() and not file:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Remark text or file is required"
        )
    
    # Handle file upload
    file_url = None
    if file:
        # Validate file size (5MB)
        file_content = await file.read()
        if len(file_content) > 5 * 1024 * 1024:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="File size must be less than 5MB"
            )
        
        # Save file
        file_id = str(uuid.uuid4())
        file_extension = os.path.splitext(file.filename)[1]
        safe_filename = f"{file_id}_{file.filename}"
        file_path = os.path.join(UPLOAD_DIR, safe_filename)
        
        with open(file_path, "wb") as f:
            f.write(file_content)
        
        file_url = f"/uploads/task-files/{safe_filename}"
        print(f"[DEBUG] File saved to: {file_path}")
    
    # Create remark in database
    new_remark = TaskRemark(
        task_id=task_id,
        user_id=current_user["emp_id"],
        remark_text=remark.strip(),
        file_url=file_url,
        created_at=datetime.utcnow()
    )
    
    db.add(new_remark)
    db.commit()
    db.refresh(new_remark)
    
    print(f"[DEBUG] Remark created with ID: {new_remark.id}")
    
    return {
        "success": True,
        "remark": {
            "id": new_remark.id,
            "task_id": new_remark.task_id,
            "text": new_remark.remark_text,
            "file_url": new_remark.file_url,
            "created_at": new_remark.created_at,
            "user_id": new_remark.user_id
        }
    }


# ---------------- GET REMARKS FOR A TASK ----------------
@task_remarks_router.get("/{task_id}/remarks", status_code=status.HTTP_200_OK)
def get_task_remarks(
    task_id: str,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)
):
    """
    Get all remarks for a specific task
    """
    # Check if task exists
    task = get_task(db, task_id)
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task {task_id} not found"
        )
    
    # Query remarks
    remarks = db.query(TaskRemark).filter(
        TaskRemark.task_id == task_id
    ).order_by(
        TaskRemark.created_at.desc()
    ).all()
    
    return {
        "remarks": [
            {
                "id": r.id,
                "task_id": r.task_id,
                "text": r.remark_text,
                "file_url": r.file_url,
                "created_at": r.created_at,
                "user_id": r.user_id
            }
            for r in remarks
        ]
    }