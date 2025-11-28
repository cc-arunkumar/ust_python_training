from fastapi import HTTPException, Depends
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
# Import JWT auth dependency
from src.authentication.auth import get_current_user, User


def register_maintenance_api(app):
    # POST /maintenance
    @app.post("/maintenance")
    def add_log(log: MaintenanceLog, current_user: User = Depends(get_current_user)):
        log_id = create_log(log)
        return {"message": "Maintenance log created successfully", "log_id": log_id}

    # GET /maintenance/list
    @app.get("/maintenance/list")
    def list_logs(current_user: User = Depends(get_current_user)):
        return get_all_logs()

    # GET /assets/search_keyword
    @app.get("/assets/search_keyword")
    def search_by_column(column_name: str, value: str, current_user: User = Depends(get_current_user)):
        try:
            results = search_assets(column_name, value)
            if not results:
                raise HTTPException(status_code=404, detail="No matching assets found")
            return results
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))

    # GET /maintenance/status
    @app.get("/maintenance/status")
    def list_by_status(status: str, current_user: User = Depends(get_current_user)):
        return get_log_by_status(status)

    # GET /maintenance/{log_id}
    @app.get("/maintenance/{log_id}")
    def read_log(log_id: int, current_user: User = Depends(get_current_user)):
        log = crud_get_log_by_id(log_id)
        if not log:
            raise HTTPException(status_code=404, detail="Log not found")
        return log

    # PUT /maintenance/{log_id}
    @app.put("/maintenance/{log_id}")
    def update_log_record(log_id: int, maintenance: MaintenanceLog, current_user: User = Depends(get_current_user)):
        updated = update_log(log_id, maintenance)
        if updated == 0:
            raise HTTPException(status_code=404, detail="Maintenance log not found")
        return {"message": "Maintenance log updated successfully"}

    # PATCH /maintenance/{log_id}/status
    @app.patch("/maintenance/{log_id}/status")
    def change_asset_status(log_id: int, new_status: str, current_user: User = Depends(get_current_user)):
        updated = update_asset_status(log_id, new_status)
        if updated == 0:
            raise HTTPException(status_code=404, detail="Asset not found")
        return {"message": "Asset status updated"}

    # GET /maintenance
    @app.get("/maintenance")
    def get_count(current_user: User = Depends(get_current_user)):
        return count_total()

    # DELETE /maintenance/{log_id}
    @app.delete("/maintenance/{log_id}")
    def remove_log(log_id: int, current_user: User = Depends(get_current_user)):
        deleted = delete_log(log_id)
        if deleted == 0:
            raise HTTPException(status_code=404, detail="Log not found")
        return {"message": "Log deleted"}
