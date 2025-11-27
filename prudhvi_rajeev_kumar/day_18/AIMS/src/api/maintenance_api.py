from fastapi import HTTPException
from src.models.maintainance_model import MaintenanceLog
from src.crud.maintainance_crud import (
    create_log,
    get_log_by_id as crud_get_log_by_id,
    get_all_logs,
    get_log_by_status,
    update_log,
    search_assets,
    update_asset_status,
    count_total,
    delete_log
)

def register_maintenance_api(app):
    @app.post("/maintenance")
    def add_log(log: MaintenanceLog):
        log_id = create_log(log)
        return {"message": "Maintenance log created successfully", "log_id": log_id}

    @app.get("/maintenance/list")
    def list_logs():
        return get_all_logs()
    
    @app.get("/assets/search_keyword")
    def search_by_column(column_name: str, value: str):
        try:
            results = search_assets(column_name, value)
            if not results:
                raise HTTPException(status_code=404, detail="No matching assets found")
            return results
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))
    
    @app.get("/maintenance/status")
    def list_by_status(status : str):
        return get_log_by_status(status)

    @app.get("/maintenance/{log_id}")
    def read_log(log_id: int):
        log = crud_get_log_by_id(log_id)
        if not log:
            raise HTTPException(status_code=404, detail="Log not found")
        return log
    
    @app.put("/maintenance/{log_id}")
    def update_log_record(log_id: int, maintenance: MaintenanceLog):
        updated = update_log(log_id, maintenance)
        if updated == 0:
            raise HTTPException(status_code=404, detail="Maintenance log not found")
        return {"message": "Maintenance log updated successfully"}
    
    @app.patch("/maintenance/{log_id}/status")
    def change_asset_status(log_id: int, new_status: str):
        updated = update_asset_status(log_id, new_status)
        if updated == 0:
            raise HTTPException(status_code=404, detail="Asset not found")
        return {"message": "Asset status updated"}
    
    @app.get("/maintenance")
    def get_count():
        return count_total()

    @app.delete("/maintenance/{log_id}")
    def remove_log(log_id: int):
        deleted = delete_log(log_id)
        if deleted == 0:
            raise HTTPException(status_code=404, detail="Log not found")
        return {"message": "Log deleted"}
