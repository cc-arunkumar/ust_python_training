# UST EMPLOYEE LAPTOP INVENTORY SYSTEM
# FastAPI application to manage laptop assets with CRUD operations

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List

# Initialize FastAPI app with a title
app = FastAPI(title="Employee Laptop Inventory (CRUD)")

# Define LaptopAsset model using Pydantic for validation
class LaptopAsset(BaseModel):
    asset_id: int = Field(..., ge=1, le=999999)  # Unique ID for each laptop (1–999999)
    serial_number: str = Field(..., pattern=r"^[A-Za-z0-9]{8,20}$", description="Must be alphanumeric (8-20)")  
    model_name: str = Field(..., min_length=3, max_length=50, description="Laptop model name")  
    assigned_to_emp_id: int = Field(..., ge=1000, le=999999, description="Employee ID if assigned")  
    status: str = Field(..., pattern=r"^(in_stock|assigned|retired)$")  # Laptop status must be one of these values
    purchase_year: int = Field(..., ge=2015, le=2025, description="Purchase year")  
    location: str = Field(default="Bengaluru")  # Default location if not provided

# In-memory storage for laptops (acts like a temporary database)
laptops: List[LaptopAsset] = []

# ------------------- CRUD Endpoints -------------------

# GET all laptops
@app.get("/laptops", response_model=List[LaptopAsset], status_code=200)
def get_all_laptops():
    """
    Retrieve all laptops in the inventory.
    Returns a list of LaptopAsset objects.
    """
    return laptops

# GET a single laptop by asset_id
@app.get("/laptops/{asset_id}", response_model=LaptopAsset)
def get_laptop(asset_id: int):
    """
    Retrieve a laptop by its asset_id.
    Raises 404 if not found.
    """
    for lap in laptops:
        if lap.asset_id == asset_id:
            return lap
    raise HTTPException(status_code=404, detail="Laptop not found")

# POST a new laptop
@app.post("/laptops", status_code=201)
def create_new_laptop(laptop: LaptopAsset):
    """
    Add a new laptop to the inventory.
    Raises 409 if asset_id already exists.
    """
    for existinglaptop in laptops:
        if existinglaptop.asset_id == laptop.asset_id:
            raise HTTPException(status_code=409, detail="Laptop already exists")
    laptops.append(laptop)
    return laptop

# PUT update an existing laptop
@app.put("/laptops/{asset_id}")
def update_laptop(asset_id: int, updated_laptop: LaptopAsset):
    """
    Update details of an existing laptop by asset_id.
    Raises 404 if laptop not found.
    """
    for idx, lap in enumerate(laptops):
        if lap.asset_id == asset_id:
            laptops[idx] = updated_laptop
            return updated_laptop
    raise HTTPException(status_code=404, detail="Laptop not found for updation")

# DELETE a laptop by asset_id
@app.delete("/laptops/{asset_id}")
def delete_laptop(asset_id: int):
    """
    Delete a laptop from the inventory by asset_id.
    Raises 404 if laptop not found.
    """
    for idx, lap in enumerate(laptops):
        if lap.asset_id == asset_id:
            laptops.pop(idx)
            return {"detail": "Laptop removed"}
    raise HTTPException(status_code=404, detail="Laptop not found")
