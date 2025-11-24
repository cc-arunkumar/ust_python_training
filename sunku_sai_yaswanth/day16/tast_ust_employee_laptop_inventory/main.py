from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from typing import Optional, List
import re

# Pydantic model to define the structure and validation rules for a laptop asset
class LaptopAsset(BaseModel):
    # Unique asset identifier, must be an integer between 1 and 999999
    asset_id: int = Field(..., ge=1, le=999999, description="Unique asset identifier")
    
    # Serial number for the laptop, must be alphanumeric and between 8 to 20 characters
    serial_number: str = Field(..., pattern=r"^[A-Za-z0-9]{8,20}$", description="Alphanumeric serial number, 8-20 characters")
    
    # Laptop model name, must be between 3 and 50 characters
    model_name: str = Field(..., min_length=3, max_length=50, description="Laptop model name")
    
    # Employee ID to whom the laptop is assigned, optional and must be between 1000 and 999999 if provided
    assigned_to_emp_id: Optional[int] = Field(None, ge=1000, le=999999, description="Employee ID if assigned")
    
    # Status of the laptop, must be one of "in_stock", "assigned", or "retired"
    status: str = Field(..., pattern=r"^(in_stock|assigned|retired)$", description="Laptop status: in_stock, assigned, or retired")
    
    # Year the laptop was purchased, must be between 2015 and 2025
    purchase_year: int = Field(..., ge=2015, le=2025, description="Purchase year")
    
    # Location of the laptop, default is "Bengaluru"
    location: str = Field(default="Bengaluru", description="Location of the laptop")

# Initialize the FastAPI app
app = FastAPI(title="UST Employee Laptop Inventory")

# In-memory storage for laptop inventory
laptop_inventory = []

# Endpoint to get all laptops in the inventory
@app.get("/laptops", response_model=List[LaptopAsset])
def get_all_laptops():
    """
    Retrieve all laptops in the inventory.
    Returns a list of LaptopAsset objects.
    """
    return laptop_inventory

# Endpoint to get a laptop by its asset ID
@app.get("/laptops/{asset_id}", response_model=LaptopAsset)
def get_laptop_by_id(asset_id: int):
    """
    Retrieve a laptop by its asset_id.
    Returns the laptop details if found, otherwise raises a 404 error.
    """
    laptop = next((l for l in laptop_inventory if l.asset_id == asset_id), None)
    if laptop is None:
        raise HTTPException(status_code=404, detail="Laptop not found")
    return laptop

# Endpoint to create a new laptop record in the inventory
@app.post("/laptops", response_model=LaptopAsset, status_code=status.HTTP_201_CREATED)
def create_laptop(laptop: LaptopAsset):
    """
    Create a new laptop record.
    If the asset_id already exists, raises a 409 conflict error.
    Otherwise, the laptop is added to the inventory and returned.
    """
    # Check if the asset_id already exists in the inventory
    if any(l.asset_id == laptop.asset_id for l in laptop_inventory):
        raise HTTPException(status_code=409, detail="Asset ID already exists")
    
    # Add the new laptop to the inventory
    laptop_inventory.append(laptop)
    return laptop

# Endpoint to update an existing laptop's details
@app.put("/laptop/{asset_id}", response_model=LaptopAsset)
def update_laptop(asset_id: int, updated_laptop: LaptopAsset):
    """
    Update an existing laptop record.
    If the asset_id in the path and body do not match, raises a 400 error.
    If the laptop is found, it is updated and returned.
    """
    # Ensure the asset_id in the URL and the body match
    if asset_id != updated_laptop.asset_id:
        raise HTTPException(status_code=400, detail="Asset ID in path and body must match")
    
    # Find the existing laptop in the inventory
    laptop = next((l for l in laptop_inventory if l.asset_id == asset_id), None)
    
    # If laptop is not found, raise a 404 error
    if laptop is None:
        raise HTTPException(status_code=404, detail="Laptop not found")
    
    # Remove the old laptop and add the updated one
    laptop_inventory.remove(laptop)
    laptop_inventory.append(updated_laptop)
    
    return updated_laptop

# Endpoint to delete a laptop from the inventory by asset_id
@app.delete("/laptop/{asset_id}")
def delete_laptop(asset_id: int):
    """
    Delete a laptop by its asset_id.
    If the laptop is found, it is removed from the inventory and a confirmation message is returned.
    If the laptop is not found, a 404 error is raised.
    """
    # Find the laptop to delete
    laptop = next((l for l in laptop_inventory if l.asset_id == asset_id), None)
    
    # If laptop is not found, raise a 404 error
    if laptop is None:
        raise HTTPException(status_code=404, detail="Laptop not found")
    
    # Remove the laptop from the inventory
    laptop_inventory.remove(laptop)
    
    # Return a confirmation message
    return {"detail": "Laptop deleted"}


# output
# post
# {
#   "asset_id": 1,
#   "serial_number": "hSuVStvy",
#   "model_name": "HP model-1023",
#   "assigned_to_emp_id": 1000,
#   "status": "in_stock",
#   "purchase_year": 2015,
#   "location": "Bengaluru"
# }

# get_all_laptops
# {
#   "asset_id": 1,
#   "serial_number": "hSuVStvy",
#   "model_name": "HP model-1023",
#   "assigned_to_emp_id": 1000,
#   "status": "in_stock",
#   "purchase_year": 2015,
#   "location": "Bengaluru"
# }