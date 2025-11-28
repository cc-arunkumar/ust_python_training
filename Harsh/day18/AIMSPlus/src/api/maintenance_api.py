from fastapi import HTTPException
from typing import List
from src.models.maintainance_model import MaintenanceLog
from src.crud.maintainance_crud import (
    create_maintenance,
    get_all_maintenance,
    get_maintenance_by_id,
    update_maintenance_by_id,
    update_maintenance_status,
    delete_maintenance,
    search_maintenance,
    count_maintenance,
    bulk_upload_maintenance,
)

def register_maintenance_api(app):
    @app.post("/maintenance/create")
    def add_maintenance(log: MaintenanceLog):
        try:
            return create_maintenance(log)
        except Exception as e:
            print(f"Error in create_maintenance: {e}")
            raise HTTPException(status_code=500, detail="Internal Server Error")

    @app.get("/maintenance/list")
    def list_maintenance(status: str | None = None):
        return get_all_maintenance(status)
    
    @app.get("/maintenance/count")
    def count():
        return count_maintenance()

    
    @app.get("/maintenance/search")
    def search(column_name: str,keyword: str):
        return search_maintenance(column_name,keyword)

   
    @app.get("/maintenance/{id}")
    def read_maintenance(id: int):
        result = get_maintenance_by_id(id)
        if not result:
            raise HTTPException(status_code=404, detail="Maintenance log not found")
        return result

    @app.put("/maintenance/{id}")
    def update_maintenance(id: int, log: MaintenanceLog):
        result = update_maintenance_by_id(id, log)
        if not result:
            raise HTTPException(status_code=404, detail="Maintenance log not found")
        return result

    @app.patch("/maintenance/{id}/status")
    def update_status(id: int, new_status: str):
        result = update_maintenance_status(id, new_status)
        if not result:
            raise HTTPException(status_code=404, detail="Maintenance log not found")
        return result

    @app.delete("/maintenance/{id}")
    def remove_maintenance(id: int):
        result = delete_maintenance(id)
        if not result:
            raise HTTPException(status_code=404, detail="Maintenance log not found")
        return result

    @app.post("/maintenance/bulk-upload")
    def bulk_upload(logs: List[MaintenanceLog]):
        return bulk_upload_maintenance(logs)
