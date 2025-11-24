# crud_api_development
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from typing import Optional, List

# Initialize the FastAPI app
app = FastAPI(title="UST Employee Laptop Inventory")

# Define the LaptopAsset model with validation rules using Pydantic
class LaptopAsset(BaseModel):
    asset_id: int = Field(..., ge=1, le=999999)  # Asset ID must be between 1 and 999999
    serial_number: str = Field(..., pattern=r"^[A-Za-z0-9]{8,20}$")  # Serial number pattern validation (8-20 alphanumeric characters)
    model_name: str = Field(..., min_length=3, max_length=50)  # Model name must be between 3 and 50 characters
    assigned_to_emp_id: Optional[int] = Field(None, ge=1000, le=999999)  # Optional employee ID, must be within valid range
    status: str = Field(..., pattern=r"^(in_stock|assigned|retired)$")  # Valid status values: "in_stock", "assigned", or "retired"
    purchase_year: int = Field(..., ge=2015, le=2025)  # Purchase year must be between 2015 and 2025
    location: str = Field("Bengaluru")  # Default location is "Bengaluru"

# In-memory storage for laptops, simulating a database for now
laptops: List[LaptopAsset] = []

# Endpoint to retrieve all laptops
@app.get("/laptops", response_model=List[LaptopAsset])
def get_laptops():
    """
    Retrieves a list of all laptops in the inventory.
    This would typically be paginated in a production environment to improve performance.
    """
    return laptops

# Endpoint to retrieve a laptop by its asset ID
@app.get("/laptops/{asset_id}", response_model=LaptopAsset)
def get_lap_by_id(asset_id: int):
    """
    Retrieves a laptop by its asset ID. Raises a 404 error if the laptop is not found.
    """
    for lap in laptops:
        if lap.asset_id == asset_id:
            return lap
    raise HTTPException(status_code=404, detail="Laptop not found")

# Endpoint to create a new laptop entry in the inventory
@app.post("/laptops", response_model=LaptopAsset, status_code=status.HTTP_201_CREATED)
def create_laptop(lap: LaptopAsset):
    """
    Creates a new laptop entry. Raises a 409 error if the asset ID already exists.
    In production, we'd likely validate the uniqueness of asset IDs at the database level.
    """
    for existing_laptop in laptops:
        if existing_laptop.asset_id == lap.asset_id:
            raise HTTPException(status_code=409, detail="Asset ID already exists")
    laptops.append(lap)
    return lap

# Endpoint to update the details of an existing laptop
@app.put("/laptops/{asset_id}", response_model=LaptopAsset)
def update_laptop(asset_id: int, updated_lap: LaptopAsset):
    """
    Updates an existing laptop's information. 
    Ensures that the asset ID in the path matches the asset ID in the request body.
    """
    if updated_lap.asset_id != asset_id:
        raise HTTPException(status_code=400, detail="Asset ID in path and body must match")
    for index, lap in enumerate(laptops):
        if lap.asset_id == asset_id:
            laptops[index] = updated_lap
            return updated_lap
    raise HTTPException(status_code=404, detail="Laptop not found")

# Endpoint to delete a laptop entry by its asset ID
@app.delete("/laptops/{asset_id}")
def delete_laptop(asset_id: int):
    """
    Deletes a laptop by its asset ID. Raises a 404 error if the laptop is not found.
    In a production environment, this could trigger other actions like audit logs or updates to related records.
    """
    for index, lap in enumerate(laptops):
        if lap.asset_id == asset_id:
            del laptops[index]
            return {"detail": "Laptop deleted"}
    raise HTTPException(status_code=404, detail="Laptop not found")
