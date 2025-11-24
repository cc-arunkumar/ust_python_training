from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from typing import List, Optional

# Defining the LaptopAsset model using Pydantic for validation
class LaptopAsset(BaseModel):
    # Asset ID: Must be an integer between 1 and 999999
    asset_id: int = Field(..., ge=1, le=999999, description="Unique Asset Identifier.")
    
    # Serial number: Must be alphanumeric with 8 to 20 characters
    serial_number: str = Field(..., pattern=r"[a-zA-Z0-9]{8,20}$", description="Must be alphanumeric, 8-20 characters.")
    
    # Model name: Must be between 3 and 50 characters
    model_name: str = Field(..., min_length=3, max_length=50, description="Laptop Model Name")
    
    # Assigned employee ID: Must be between 1000 and 999999
    assigned_to_emp_id: int = Field(ge=1000, le=999999, description="Employee ID if Assigned.")
    
    # Status: Can only be 'in_stock', 'assigned', or 'retired'
    status: str = Field(..., pattern=r"^(in_stock|assigned|retired)$")
    
    # Purchase year: Must be between 2015 and 2025
    purchase_year: int = Field(..., ge=2015, le=2025, description="Purchase Year.")
    
    # Location: Default is 'Bengaluru'
    location: str = Field("Bengaluru")


# A list to store laptop asset data
laptops: List[LaptopAsset] = []

# Initialize FastAPI app
app = FastAPI(title="UST Employee Laptop Inventory")

# Endpoint to get all laptops
@app.get("/laptops", status_code=200)
def get_laptops():
    # Return the list of all laptops
    return laptops

# Endpoint to get laptop by asset_id
@app.get("/laptops/{asset_id}", status_code=200)
def get_laptops_by_asset_id(asset_id: int):
    # Search for the laptop with the given asset_id
    for lap in laptops:
        if lap.asset_id == asset_id:
            return lap
    # If laptop is not found, raise an HTTPException
    raise HTTPException(status_code=400, detail="Laptop not found.")

# Endpoint to create a new laptop entry
@app.post("/laptops", status_code=201)
def create_laptops(new_laptop: LaptopAsset):
    # Check if the asset_id already exists
    for laptop in laptops:
        if laptop.asset_id == new_laptop.asset_id:
            raise HTTPException(status_code=409, detail="Asset_id already exists.")
    # Add the new laptop to the list
    laptops.append(new_laptop)
    return new_laptop

# Endpoint to update an existing laptop entry
@app.put("/laptops/{asset_id}", status_code=200)
def update_laptop(asset_id: int, details: LaptopAsset):
    # Ensure that the asset_id in the URL matches the asset_id in the request body
    if asset_id != details.asset_id:
        raise HTTPException(status_code=400, detail="Asset id in path and body does not match.")
    
    # Search for the laptop by asset_id
    for laptop in laptops:
        if laptop.asset_id == asset_id:
            # Remove the old laptop and add the updated laptop details
            laptops.remove(laptop)
            laptops.append(details)
            return details
    
    # If laptop not found, raise an HTTPException
    raise HTTPException(status_code=404, detail="Laptop not found.")

# Endpoint to delete a laptop by asset_id
@app.delete("/laptops/{asset_id}", status_code=200)
def delete_laptop(asset_id: int):
    # Search for the laptop by asset_id
    for l in laptops:
        if l.asset_id == asset_id:
            laptops.remove(l)  # Remove the laptop from the list
            return l
    # If laptop not found, raise an HTTPException
    raise HTTPException(status_code=404, detail="Laptop not found.")
