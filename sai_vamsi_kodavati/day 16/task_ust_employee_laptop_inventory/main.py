# CRUD API Development
# UST Employee Laptop Inventory
# 1. Context
# UST maintains an internal inventory of company laptops assigned to employees.
# The IT department needs a small internal API to:
# Register laptops
# View laptop details
# Update laptop records
# Remove laptops that are retired or disposed
# All data will be stored in memory for this exercise.


from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from typing import Optional, List

# Initialize the FastAPI app
app = FastAPI(title="UST Employee Laptop Inventory")

# Define Pydantic model for LaptopAsset
class LaptopAsset(BaseModel):
    asset_id: int = Field(..., ge=1, le=999999) 
    serial_number: str = Field(..., pattern=r'^[A-Za-z0-9]{8,20}$')  
    model_name: str = Field(..., min_length=3, max_length=50) 
    assigned_to_emp_id: int = Field(ge=1000, le=999999) 
    status: str = Field(..., pattern=r'^(in_stock|assigned|retired)$')  
    purchase_year: int = Field(..., ge=2015, le=2025)  
    location: str = "Bengaluru"  

# In-memory list to store laptop assets
laptop: List[LaptopAsset] = []

# Endpoint to get details of all laptops
@app.get("/laptops", response_model=List[LaptopAsset])
def get_details():
    return laptop 


# Endpoint to add a new laptop to the inventory
@app.post("/laptops", response_model=LaptopAsset)
def add_details(product: LaptopAsset):
    # Check if asset_id already exists in the inventory
    for row in laptop:
        if row.asset_id == product.asset_id:
            raise HTTPException(status_code=409, detail="Asset ID already exists")  # Conflict error
    laptop.append(product)  # Add the new laptop to the list
    return product  # Return the newly added laptop details


# Endpoint to get laptop details by asset_id
@app.get("/laptops/{asset_id}")
def get_details_by_asset_id(asset_id: int):
    try:
        # Return laptop at the specified asset_id
        return laptop[asset_id]
    except IndexError:
        # Handle case when asset_id is out of range in the list
        raise HTTPException(status_code=404, detail="Laptop not found")  # Not found error


# Endpoint to update the details of a laptop
@app.put("/laptops/{asset_id}", response_model=LaptopAsset)
def update_details(asset_id: int, product: LaptopAsset):
    # Ensure that the asset_id in the URL matches the asset_id in the body
    if asset_id != product.asset_id:
        raise HTTPException(status_code=400, detail="Asset ID in path and body must match")  # Bad request if IDs don't match

    for i, row in enumerate(laptop):
        if row.asset_id == asset_id:
            laptop[i] = product  
            return product  
    # If asset_id is not found, raise error
    raise HTTPException(status_code=404, detail="Laptop not found")  # Not found error


# Endpoint to delete a laptop by asset_id
@app.delete("/laptops/{asset_id}")
def delete_data(asset_id: int):
    for i, row in enumerate(laptop):
        if row.asset_id == asset_id:
            del laptop[i]  
            return {"detail": "Laptop deleted"}  
    # If asset_id is not found, raise error
    raise HTTPException(status_code=404, detail="Laptop not found") 

# -------------------------------------------------------------------------------

# Sample Output

# **Output for GET /laptops**
# Example: If there are two laptops in the list:
# [
#     {"asset_id": 1, "serial_number": "ABC12345", "model_name": "Dell XPS 13", "assigned_to_emp_id": 1001, "status": "assigned", "purchase_year": 2021, "location": "Bengaluru"},
#     {"asset_id": 2, "serial_number": "XYZ98765", "model_name": "HP Spectre x360", "assigned_to_emp_id": 1002, "status": "in_stock", "purchase_year": 2022, "location": "Bengaluru"}
# ]


# **Output for POST /laptops**
# Input:
# {
#     "asset_id": 3,
#     "serial_number": "LMN45678",
#     "model_name": "MacBook Pro",
#     "assigned_to_emp_id": 1003,
#     "status": "in_stock",
#     "purchase_year": 2023
# }
# Output:
# {
#     "asset_id": 3,
#     "serial_number": "LMN45678",
#     "model_name": "MacBook Pro",
#     "assigned_to_emp_id": 1003,
#     "status": "in_stock",
#     "purchase_year": 2023,
#     "location": "Bengaluru"
# }

# **Output for DELETE /laptops/{asset_id}**
# If `asset_id=1` exists:
# Output:
# {"detail": "Laptop deleted"}
# If `asset_id=5` (nonexistent):
# HTTPException: 404 Not Found - Laptop not found


# **Output for PUT /laptops/{asset_id}**
# Input:
# {
#     "asset_id": 1,
#     "serial_number": "ABC12345",
#     "model_name": "Dell XPS 13",
#     "assigned_to_emp_id": 1001,
#     "status": "assigned",
#     "purchase_year": 2022
# }
# Output (if asset_id=1 exists):
# {
#     "asset_id": 1,
#     "serial_number": "ABC12345",
#     "model_name": "Dell XPS 13",
#     "assigned_to_emp_id": 1001,
#     "status": "assigned",
#     "purchase_year": 2022,
#     "location": "Bengaluru"
# }


# **Output for GET /laptops/{asset_id}**
# If `asset_id=1`, output:
# {
#     "asset_id": 1,
#     "serial_number": "ABC12345",
#     "model_name": "Dell XPS 13",
#     "assigned_to_emp_id": 1001,
#     "status": "assigned",
#     "purchase_year": 2021,
#     "location": "Bengaluru"
# }
# If `asset_id=5` (nonexistent):
# HTTPException: 404 Not Found - Laptop not found
