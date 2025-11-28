from fastapi import APIRouter, HTTPException, Depends
from src.models.maintainance_model import MaintenanceLog, validate_log
from src.crud import maintainance_crud
from src.auth.jwt_auth import User,get_current_user
router = APIRouter()

@router.post("/create", response_model=MaintenanceLog)
def create(log: MaintenanceLog, current_user:User=Depends(get_current_user)):
    validate_log(log)
    new_id = maintainance_crud.create_log(log)
    return {**log.model_dump(), "log_id": new_id}

@router.get("/list")
def list_logs(status: str = None, current_user:User=Depends(get_current_user)):
    rows = maintainance_crud.list_logs(status)
    if not rows:
        raise HTTPException(status_code=404, detail="No logs found")
    return {"status": "success", "data": rows}
@router.get("/count")
def count_logs(current_user:User=Depends(get_current_user)):
    row = maintainance_crud.count_logs()
    return {"status": "success", "count": row["total"]}


@router.get("/{log_id}", response_model=MaintenanceLog)
def get_log(log_id: int, current_user:User=Depends(get_current_user)):
    row = maintainance_crud.get_log(log_id)
    if not row:
        raise HTTPException(status_code=404, detail="Log not found")
    return MaintenanceLog(**row)

@router.put("/{log_id}", response_model=MaintenanceLog)
def update_log(log_id: int, log: MaintenanceLog, current_user:User=Depends(get_current_user)):
    validate_log(log)
    maintainance_crud.update_log(log_id, log)
    row = maintainance_crud.get_log(log_id)
    return MaintenanceLog(**row)

@router.patch("/{log_id}/status")
def update_status(log_id: int, status: str, current_user:User=Depends(get_current_user)):
    if status not in {"Completed", "Pending"}:
        raise HTTPException(status_code=422, detail="Invalid status")
    maintainance_crud.update_status(log_id, status)
    return {"status": "success", "message": f"Log {log_id} status updated to {status}"}

@router.delete("/{log_id}")
def delete_log(log_id: int, current_user:User=Depends(get_current_user)):
    maintainance_crud.delete_log(log_id)
    return {"status": "success", "message": "Log deleted"}

@router.get("/search")
def search_logs(keyword: str, current_user:User=Depends(get_current_user)):
    rows = maintainance_crud.search_logs(keyword)
    if not rows:
        raise HTTPException(status_code=404, detail="No matching logs found")
    return {"status": "success", "data": rows}

