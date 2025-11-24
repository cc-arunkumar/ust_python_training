# Task UST Employee Laptop Inventory

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List

app = FastAPI(title="UST Employee Laptop Inventory")

# LaptopAsset model with validation
class LaptopAsset(BaseModel):
    asset_id: int = Field(..., ge=1, le=999999)
    serial_number: str = Field(..., pattern=r"^[A-Za-z0-9]{8,20}$")
    model_number: str = Field(..., min_length=3, max_length=50)
    assigned_to_emp_id: int = Field(..., ge=1000, le=999999)
    status: str = Field(..., pattern=r"^(in_stock|assigned|retired)$")
    purchase_year: int = Field(..., ge=2015, le=2025)
    location: str = "Bengaluru"

# In-memory storage
laptops: List[LaptopAsset] = []

# Helper to find index by asset_id
def find_profile_index(asset_id: int) -> int:
    for idx, p in enumerate(laptops):
        if p.asset_id == asset_id:
            return idx
    return -1

@app.get("/laptops", response_model=List[LaptopAsset])
def get_all_laptops():
    # Return all laptops
    return laptops

@app.get("/laptops/{asset_id}", response_model=LaptopAsset)
def get_laptop_by_id(asset_id: int):
    # Get laptop by asset_id
    idx = find_profile_index(asset_id)
    if idx == -1:
        raise HTTPException(status_code=404, detail="Laptop not found")
    return laptops[idx]

@app.post("/laptops", response_model=LaptopAsset, status_code=201)
def create_laptops(laptop: LaptopAsset):
    # Create new laptop asset
    asset_id = laptop.asset_id
    if find_profile_index(asset_id) != -1:
        raise HTTPException(status_code=409, detail="Laptop with asset_id already exists")
    laptops.append(laptop)
    return laptop

@app.put("/laptops/{asset_id}", response_model=LaptopAsset)
def update_laptop(asset_id: int, laptop: LaptopAsset):
    # Update laptop details
    if laptop.asset_id != asset_id:
        raise HTTPException(status_code=400, detail="Path asset_id and body asset_id must match")
    idx = find_profile_index(asset_id)
    if idx == -1:
        raise HTTPException(status_code=404, detail="Laptop not found")
    laptops[idx] = laptop
    return laptop

@app.delete("/laptops/{asset_id}", response_model=LaptopAsset)
def delete_laptop(asset_id: int):
    # Delete laptop by asset_id
    idx = find_profile_index(asset_id)
    if idx == -1:
        raise HTTPException(status_code=404, detail="Laptop not found")
    removed = laptops.pop(idx)
    return removed

#Sample Executions

# Create a new laptop
# {
#   "asset_id": 101,
#   "serial_number": "ABC12345XY",
#   "model_number": "Dell-Latitude-5420",
#   "assigned_to_emp_id": 2001,
#   "status": "assigned",
#   "purchase_year": 2022,
#   "location": "Bengaluru"
# }

# Get all laptops

# [
#   {
#     "asset_id": 101,
#     "serial_number": "ABC12345XY",
#     "model_number": "Dell-Latitude-5420",
#     "assigned_to_emp_id": 2001,
#     "status": "assigned",
#     "purchase_year": 2022,
#     "location": "Bengaluru"
#   }
# ]

# 
# Update laptop details
# Request: /laptops/101
# {
#   "asset_id": 101,
#   "serial_number": "XYZ98765PQ",
#   "model_number": "HP-EliteBook-840",
#   "assigned_to_emp_id": 2002,
#   "status": "in_stock",
#   "purchase_year": 2023,
#   "location": "Bengaluru"
# }

# Delete laptop
# Request: /laptops/101

# []