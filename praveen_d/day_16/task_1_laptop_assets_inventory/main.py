from pydantic import BaseModel, Field
from typing import Optional, List
from fastapi import FastAPI, HTTPException

# Initialize the FastAPI application with a description
app = FastAPI(description="Laptop assets inventory")

# In-memory storage for laptops
laptops_list = [
    {
        "asset_id": 1,
        "serial_number": "ABC12345",
        "model_name": "Dell Latitude 5420",
        "assigned_to_emp_id": 12345,
        "status": "assigned",
        "purchase_year": 2022,
        "location": "Bengaluru"
    }
]

# Define the Pydantic model for laptop asset
class LaptopAsset(BaseModel):
    # Unique asset identifier, must be between 1 and 999999
    asset_id: int = Field(..., ge=1, le=999999, description="Unique asset identifier between 1 and 999999")
    
    # Serial number (alphanumeric, 8–20 characters long)
    serial_number: str = Field(..., min_length=8, max_length=20, pattern=r"^[A-Za-z0-9]{8,20}$", description="Serial number must be alphanumeric, 8–20 characters long.")
    
    # Laptop model name (between 3 and 50 characters)
    model_name: str = Field(..., min_length=3, max_length=50, description="Laptop model name.")
    
    # Employee ID (optional)
    assigned_to_emp_id: Optional[int] = Field(None, ge=1000, le=999999, description="Employee ID if assigned.")
    
    # Laptop status (valid values: in_stock, assigned, retired)
    status: str = Field(..., pattern=r"^(in_stock|assigned|retired)$", description='Status of the laptop: "in_stock", "assigned", or "retired".')
    
    # Purchase year (between 2015 and 2025)
    purchase_year: int = Field(..., ge=2015, le=2025, description="Purchase year of the laptop.")
    
    # Location (default "Bengaluru")
    location: str = Field("Bengaluru", description="Location of the laptop.")


# Endpoint 1: Get all laptops
@app.get("/laptops")
def display_laptops():

    return laptops_list


# Endpoint 2: Get laptop by asset_id
@app.get("/laptops/{asset_id}")
def disp_specific_id(id: int):

    for lap in laptops_list:
        if lap["asset_id"] == id:
            return lap
    raise HTTPException(status_code=404, detail="Laptop not found")


# Endpoint 3: Create a new laptop record
@app.post("/laptops")
def create_laptop(laptopasset: LaptopAsset):

    # Check if asset_id already exists
    for lap in laptops_list:
        if lap["asset_id"] == laptopasset.asset_id:
            raise HTTPException(status_code=400, detail="Asset ID already exists")
    
    # Append the new laptop asset to the list
    laptops_list.append(laptopasset.dict())
    return laptopasset


# Endpoint 4: Update an existing laptop record by asset_id
@app.put("/laptops/{asset_id}")
def update_laptop(asset_id: int, laptopasset: LaptopAsset):

    for idx, lap in enumerate(laptops_list):
        if lap["asset_id"] == asset_id:
            # Update the laptop record with new values
            laptops_list[idx] = laptopasset.dict()  # Replace the old record with the new one
            return laptopasset
    raise HTTPException(status_code=404, detail="Laptop not found")


# Endpoint 5: Delete an existing laptop record by asset_id
@app.delete("/laptops/{asset_id}")
def delete_laptop(asset_id: int):
    for idx, lap in enumerate(laptops_list):
        if lap["asset_id"] == asset_id:
            # Remove the laptop from the list
            removed_laptop = laptops_list.pop(idx)
            return removed_laptop
    raise HTTPException(status_code=404, detail="Laptop not found")
