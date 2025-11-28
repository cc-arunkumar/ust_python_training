from fastapi import Depends, HTTPException
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
)
from src.auth.jwt_auth import get_current_user, User

def register_maintenance_api(app):
    """
    Register all maintenance-related API endpoints with the FastAPI app.
    Each endpoint interacts with the CRUD functions defined in maintainance_crud.
    """

    # 1. Create a new maintenance log
    @app.post("/maintenance/create")
    def add_maintenance(log: MaintenanceLog,current_user: User = Depends(get_current_user)):
        """
        Endpoint: POST /maintenance/create
        Input: MaintenanceLog object (validated by Pydantic model)
        Action: Calls create_maintenance() to insert a new maintenance record into DB
        Returns: Created maintenance log
        """
        try:
            return create_maintenance(log)
        except Exception as e:
            print(f"Error in create_maintenance: {e}")
            raise HTTPException(status_code=500, detail="Internal Server Error")

    # 2. List all maintenance logs (optionally filter by status)
    @app.get("/maintenance/list")
    def list_maintenance(status: str | None = None,current_user: User = Depends(get_current_user)):
        """
        Endpoint: GET /maintenance/list
        Query param: status (optional)
        Action: Fetch all maintenance logs, optionally filtered by status
        Returns: List of maintenance logs
        """
        return get_all_maintenance(status)
    
    # 3. Count total maintenance logs
    @app.get("/maintenance/count")
    def count(current_user: User = Depends(get_current_user)):
        """
        Endpoint: GET /maintenance/count
        Action: Returns total count of maintenance logs
        """
        return count_maintenance()

    # 4. Search maintenance logs by column and keyword
    @app.get("/maintenance/search")
    def search(column_name: str, keyword: str,current_user: User = Depends(get_current_user)):
        """
        Endpoint: GET /maintenance/search
        Query params: column_name, keyword
        Action: Search maintenance logs based on column and keyword
        Returns: Matching maintenance logs
        """
        return search_maintenance(column_name, keyword)

    # 5. Get maintenance log by ID
    @app.get("/maintenance/{id}")
    def read_maintenance(id: int,current_user: User = Depends(get_current_user)):
        """
        Endpoint: GET /maintenance/{id}
        Path param: id
        Action: Fetch maintenance log by ID
        Returns: Maintenance log record or 404 if not found
        """
        result = get_maintenance_by_id(id)
        if not result:
            raise HTTPException(status_code=404, detail="Maintenance log not found")
        return result

    # 6. Update full maintenance log record
    @app.put("/maintenance/{id}")
    def update_maintenance(id: int, log: MaintenanceLog,current_user: User = Depends(get_current_user)):
        """
        Endpoint: PUT /maintenance/{id}
        Path param: id
        Body: MaintenanceLog object
        Action: Replace maintenance log record with new data
        Returns: Updated maintenance log or 404 if not found
        """
        result = update_maintenance_by_id(id, log)
        if not result:
            raise HTTPException(status_code=404, detail="Maintenance log not found")
        return result

    # 7. Update only maintenance status
    @app.patch("/maintenance/{id}/status")
    def update_status(id: int, new_status: str,current_user: User = Depends(get_current_user)):
        """
        Endpoint: PATCH /maintenance/{id}/status
        Path param: id
        Body: new_status string
        Action: Update only the status field of a maintenance log
        Returns: Updated maintenance log or 404 if not found
        """
        result = update_maintenance_status(id, new_status)
        if not result:
            raise HTTPException(status_code=404, detail="Maintenance log not found")
        return result

    # 8. Delete maintenance log
    @app.delete("/maintenance/{id}")
    def remove_maintenance(id: int,current_user: User = Depends(get_current_user)):
        """
        Endpoint: DELETE /maintenance/{id}
        Path param: id
        Action: Delete maintenance log by ID
        Returns: Deleted maintenance log or 404 if not found
        """
        result = delete_maintenance(id)
        if not result:
            raise HTTPException(status_code=404, detail="Maintenance log not found")
        return result

