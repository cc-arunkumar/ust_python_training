# CRUD API Development
# UST Employee Laptop Inventory

# 1. Context
# UST maintains an internal inventory of company laptops assigned to employees.
# The IT department needs a small internal API to:
# Register laptops
# View laptop details
# Update laptop records
# Remove laptops that are retired or disposed
# All data will be stored in memory for this exercise

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from typing import Optional, List

# Create a FastAPI instance with a title for Swagger documentation
app = FastAPI(title="UST Employee Laptop Inventory")

# Define a Pydantic model for LaptopAsset to validate data
class LaptopAsset(BaseModel):
    asset_id: int = Field(
        ..., ge=1, le=999999,
        description="Asset id must be in between 1 abd 999999"
    )
    serial_number: str = Field(
        ..., pattern=r"^[A-Za-z0-9]{8,20}$",
        description="serial number patters not matching"
    )
    model_name: str = Field(
        ..., min_length=3, max_length=50,
        description="model name length is between 3 and 50"
    )
    assigned_to_emp_id: Optional[int] = Field(
        None, ge=1000, le=999999,
        description="Optional employee ID the laptop is assigned to"
    )
    status: str = Field(
        ..., pattern=r"^(in_stock|assigned|retired)$",
        description="status does not match"
    )
    purchase_year: int = Field(
        ..., ge=2015, le=2025,
        description="invalid puchase year"
    )
    location: Optional[str] = Field("Bangaluru", description="Laptop location")

# In-memory list to store laptop records
laptops = []

# Endpoint to retrieve all laptops
@app.get("/laptops")
def get_laptops():
    # Return the list of all laptops
    return laptops

# Endpoint to retrieve a laptop by its asset_id
@app.get("/laptops/{asset_id}")
def get_laptop_by_id(asset_id: int):
    # Iterate through the list to find the laptop
    for i in laptops:
        if i.asset_id == asset_id:
            return i
    # Raise HTTP 404 if the laptop is not found
    raise HTTPException(status_code=404, detail="No laptop found")

# Endpoint to create a new laptop record
@app.post("/laptops")
def create_new_laptop(laptop: LaptopAsset):
    # Append the new laptop to the in-memory list
    laptops.append(laptop)
    return {"Laptop added": laptop}

# Endpoint to update an existing laptop by asset_id
@app.put("/laptops/{asset_id}")
def update_laptop(asset_id: int, laptop: LaptopAsset):
    # Search for the laptop and update it
    for i in range(len(laptops)):
        if laptops[i].asset_id == asset_id:
            laptops[i] = laptop
            return {"laptop updated": laptop}
    # Raise HTTP 404 if laptop not found
    raise HTTPException(status_code=404, detail="No laptop found")

# Endpoint to delete a laptop by asset_id
@app.delete("/laptops.{asset_id}")
def delete_laptop(asset_id: int):
    # Search for the laptop and remove it from the list
    for i in range(len(laptops)):
        if laptops[i].asset_id == asset_id:
            return {"laptop data deleted": laptops.pop(i)}
    # Raise HTTP 404 if laptop not found
    raise HTTPException(status_code=404, detail="No laptop found")
