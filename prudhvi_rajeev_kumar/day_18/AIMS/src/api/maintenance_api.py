from fastapi import HTTPException
from src.models.maintainance_model import MaintenanceLog
from src.crud.maintainance_crud import (
    create_log,
    get_log_by_id as crud_get_log_by_id,
    get_all_logs,
    delete_log
)

def register_maintenance_api(app):
    @app.post("/maintenance")
    def add_log(log: MaintenanceLog):
        log_id = create_log(log)
        return {"message": "Maintenance log created successfully", "log_id": log_id}

    @app.get("/maintenance")
    def list_logs():
        return get_all_logs()

    @app.get("/maintenance/{log_id}")
    def read_log(log_id: int):
        log = crud_get_log_by_id(log_id)
        if not log:
            raise HTTPException(status_code=404, detail="Log not found")
        return log

    @app.delete("/maintenance/{log_id}")
    def remove_log(log_id: int):
        deleted = delete_log(log_id)
        if deleted == 0:
            raise HTTPException(status_code=404, detail="Log not found")
        return {"message": "Log deleted"}
