from pydantic import BaseModel, Field  
from typing import List, Optional 
from fastapi import FastAPI, HTTPException  

# Initialize the FastAPI app with a custom title
app = FastAPI(title="Employee Laptop Inventory")

# Define the LaptopAssets model using Pydantic for validation
class LaptopAssets(BaseModel):
    # Asset ID must be an integer between 1 and 999999
    asset_id: int = Field(..., ge=1, le=999999)
    
    # Serial number must be a string with 8 to 20 alphanumeric characters
    serial_number: str = Field(..., pattern=r"^[A-Za-z0-9]{8,20}$")
    
    # Model name must be a string between 3 and 50 characters long
    model_name: str = Field(..., min_length=3, max_length=50)
    
    # Employee ID to whom the laptop is assigned (must be an integer between 1000 and 999999)
    assigned_to_emp_id: int = Field(..., ge=1000, le=999999)
    
    # Status must be one of the predefined values: 'in_stock', 'assigned', 'retired'
    status: str = Field(..., pattern=r"^(in_stock|assigned|retired)$")
    
    # Purchase year must be between 2015 and 2025
    purchase_year: int = Field(..., ge=2015, le=2025)
    
    # Location is defaulted to 'Bengaluru'
    location: str = "Bengaluru"

# List to store laptop asset details (in-memory database)
laptop_specs: List[dict] = []

# Endpoint to add a new laptop asset
@app.post("/laptops", response_model=LaptopAssets)
def add_lap(lap: LaptopAssets):
    for a in laptop_specs:
        if a['asset_id'] == lap.asset_id:
            raise HTTPException(status_code=409, detail="Asset id already exists")  # Conflict error if ID exists
    
    laptop_specs.append(lap.model_dump())
    
    # Return the added laptop asset
    return lap

# Endpoint to get all laptop assets
@app.get("/laptops", response_model=List[LaptopAssets])
def get_all():
    return laptop_specs  

# Endpoint to get a specific laptop by its asset_id
@app.get("/laptops/{asset_id}", response_model=LaptopAssets)
def get(asset_id: int):
    for a in laptop_specs:
        if a['asset_id'] == asset_id:
            return a  
    
    # If not found, raise a 404 error (Laptop not found)
    raise HTTPException(status_code=404, detail="Laptop not found")

# Endpoint to edit an existing laptop asset by asset_id
@app.put("/laptops/{asset_id}", response_model=LaptopAssets)
def edit(asset_id: int, lap: LaptopAssets):
    existing = None  
    
    # Search for the laptop asset to edit by asset_id
    for a in laptop_specs:
        if a['asset_id'] == asset_id:
            existing = a
            break
    
    # If the asset doesn't exist, raise a 404 error (Laptop not found)
    if existing is None:
        raise HTTPException(status_code=404, detail="Laptop not Found")
    
    # Ensure that the asset_id in the path matches the asset_id in the body
    if asset_id != lap.asset_id:
        raise HTTPException(status_code=400, detail="Asset ID and Body must match")  # Bad request error if IDs don't match
    
    # Remove the existing laptop asset and append the updated one
    laptop_specs.remove(existing)
    laptop_specs.append(lap.model_dump())
    
    return lap

# Endpoint to delete a laptop asset by its asset_id
@app.delete("/laptops/{asset_id}")
def delete(asset_id: int):
    for a in laptop_specs:
        if a['asset_id'] == asset_id:
            laptop_specs.remove(a) 
            return {"detail": "Laptop deleted successfully"}  
    
    raise HTTPException(status_code=404, detail="Laptop not found")


