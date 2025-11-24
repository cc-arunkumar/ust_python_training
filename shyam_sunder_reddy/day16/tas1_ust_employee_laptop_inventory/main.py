from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List, Optional

# -----------------------------
# FastAPI Application
# -----------------------------
app = FastAPI(title="UST Employee Laptop Inventory")

# -----------------------------
# Data Model
# -----------------------------
class LaptopAsset(BaseModel):
    """
    Laptop asset schema:
    - asset_id: unique ID (1-999999)
    - serial_number: alphanumeric, 8-20 chars
    - model_name: 3-50 chars
    - assigned_to_emp_id: optional employee ID (1000-999999)
    - status: must be one of in_stock, assigned, retired
    - purchase_year: 2015-2025
    - location: optional, defaults to "Bengaluru"
    """
    asset_id: int = Field(..., ge=1, le=999999, description="the asset id must range between 1 to 999999",example=101)
    serial_number: str = Field(..., pattern=r"^[A-Za-z0-9]{8,20}$", description="Must be alphanumeric, 8-20 characters")
    model_name: str = Field(..., min_length=3, max_length=50, description="Laptop model name length must be greater than 3 and less than 50")
    assigned_to_emp_id: Optional[int] = Field(ge=1000, le=999999, description="The employee ID must be between 1000 and 999999")
    status: str = Field(..., pattern=r"^(in_stock|assigned|retired)$", description="The status must be in_stock,assigned,retired")
    purchase_year: int = Field(..., ge=2015, le=2025, description="Purchase year must be between 2015 and 2025")
    location: Optional[str] = Field("Benguluru", description="Enter valid location format")

# -----------------------------
# In-Memory Inventory
# -----------------------------
inventory: List[LaptopAsset] = []

# -----------------------------
# CRUD Endpoints
# -----------------------------

@app.get("/laptops", response_model=List[LaptopAsset])
def display_all():
    """
    Retrieve all laptops in inventory.

    Sample Output:
    GET /laptops
    [
      {"asset_id":1,"serial_number":"ABC12345","model_name":"Dell Latitude","assigned_to_emp_id":1234,
       "status":"in_stock","purchase_year":2020,"location":"Bengaluru"}
    ]
    """
    return inventory


@app.get("/laptops/{asset_id}", response_model=LaptopAsset)
def display_byid(asset_id: int):
    """
    Retrieve a laptop by asset ID.

    Sample Output:
    GET /laptops/1
    {"asset_id":1,"serial_number":"ABC12345","model_name":"Dell Latitude","assigned_to_emp_id":1234,
     "status":"in_stock","purchase_year":2020,"location":"Bengaluru"}

    Error Case:
    GET /laptops/99
    Response: 404 {"detail":"Laptop not found"}
    """
    for laptop in inventory:
        if laptop.asset_id == asset_id:
            return laptop
    raise HTTPException(status_code=404, detail="Laptop not found")


@app.post("/laptops", response_model=LaptopAsset)
def create_asset(new_asset: LaptopAsset):
    """
    Create a new laptop asset.
    Prevents duplicate asset IDs.

    Sample Output:
    POST /laptops
    Request:
    {"asset_id":1,"serial_number":"ABC12345","model_name":"Dell Latitude","assigned_to_emp_id":1234,
     "status":"in_stock","purchase_year":2020,"location":"Bengaluru"}

    Response:
    {"asset_id":1,"serial_number":"ABC12345","model_name":"Dell Latitude","assigned_to_emp_id":1234,
     "status":"in_stock","purchase_year":2020,"location":"Bengaluru"}

    Error Case:
    POST /laptops with duplicate asset_id
    Response: 409 {"detail":"asset id already exist"}
    """
    for asset in inventory:
        if asset.asset_id == new_asset.asset_id:
            raise HTTPException(status_code=409, detail="asset id already exist")
    inventory.append(new_asset)
    return new_asset


@app.put("/laptops/{asset_id}", response_model=LaptopAsset)
def update_asset_byid(asset_id: int, new_asset: LaptopAsset):
    """
    Update an existing laptop asset by ID.
    Ensures path ID matches body ID.

    Sample Output:
    PUT /laptops/1
    Request:
    {"asset_id":1,"serial_number":"XYZ98765","model_name":"HP Elitebook","assigned_to_emp_id":5678,
     "status":"assigned","purchase_year":2021,"location":"Chennai"}

    Response:
    {"asset_id":1,"serial_number":"XYZ98765","model_name":"HP Elitebook","assigned_to_emp_id":5678,
     "status":"assigned","purchase_year":2021,"location":"Chennai"}

    Error Case:
    PUT /laptops/99
    Response: 404 {"detail":"Laptop not found"}
    """
    if asset_id != new_asset.asset_id:
        raise HTTPException(status_code=400, detail="Asset ID in path and body must match")
    for asset in inventory:
        if asset.asset_id == new_asset.asset_id:
            asset.serial_number = new_asset.serial_number
            asset.model_name = new_asset.model_name
            asset.assigned_to_emp_id = new_asset.assigned_to_emp_id
            asset.status = new_asset.status
            asset.purchase_year = new_asset.purchase_year
            asset.location = new_asset.location
            return new_asset
    raise HTTPException(status_code=404, detail="Laptop not found")


@app.delete("/laptops/{asset_id}")
def delete_asset(asset_id: int):
    """
    Delete a laptop asset by ID.

    Sample Output:
    DELETE /laptops/1
    Response:
    {"detail":"Laptop deleted"}

    Error Case:
    DELETE /laptops/99
    Response: 404 {"detail":"Laptop not found"}
    """
    for asset in inventory:
        if asset.asset_id == asset_id:
            inventory.remove(asset)
            return {"detail": "Laptop deleted"}
    raise HTTPException(status_code=404, detail="Laptop not found")
