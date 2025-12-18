from datetime import datetime
from typing import Optional



def attachment_document(
    task_id: str,
    filename: str,
    file_type: str,
    file_path: str,
    uploaded_by: str,
    roles: list
):
    return {
        "task_id": task_id,
        "filename": filename,
        "file_type": file_type,
        "file_path": file_path,
        "uploaded_by": uploaded_by,
        "roles": roles,
        "uploaded_at": datetime.utcnow(),
        "is_active": True
    }

def task_document(
    task_id:str,
    title: str,
    description: str,
    priority: str,
    assigned_to: str,
    assigned_by: str,
    created_by: str,
    remarks: Optional[str] = None,
    reviewer: Optional[str] = None,
    expected_closure: Optional[datetime] = None
):
    return {
        "task_id":task_id,
        "title": title,
        "description": description,

        "status": "TO_DO",
        "priority": priority,

        "assigned_to": assigned_to,
        "assigned_by": assigned_by,
        "assigned_at": datetime.now(),

        "created_by": created_by,
        "created_at": datetime.now(),

        "updated_by": created_by,
        "updated_at": datetime.now(),

        "remarks": remarks,
        "reviewer": reviewer,
        "expected_closure": expected_closure,

        "actual_closure": None
    }



def log_document(
    emp_id: str,
    roles: list,
    module: str,
    action: str,
    description: str,
    status: str,
    resource_id: str | None = None,
    old_value: dict | None = None,
    new_value: dict | None = None
):
    return {
        "emp_id": emp_id,
        "roles": roles,
        "module": module,
        "action": action,
        "resource_id": resource_id,
        "description": description,
        "old_value": old_value,
        "new_value": new_value,
        "status": status,
        "timestamp": datetime.now()
    }

