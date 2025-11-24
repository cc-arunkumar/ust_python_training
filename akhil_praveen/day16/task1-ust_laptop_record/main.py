from typing import List, Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import re

app = FastAPI(title="Ust Laptop Inventory")

class LaptopAsset(BaseModel):
    asset_id: int = Field(..., ge=1, le=999999, description="Asset id should be in between 1 and 999999 ")
    seriel_number: str = Field(..., pattern=r"^[A-Za-z0-9]{8,20}$", description="Should be alphanumeric and character should be in between 8-20")
    model_name: str = Field(..., min_length=3, max_length=50, description="Model name length should be in between 3 and 50")
    assigned_to_emp_id: Optional[int] = Field(..., ge=1000, le=999999, description="Employee id if assigned should be in between 1000-999999 ")
    status: str = Field(..., pattern=r"^(in_stock|assigned|retired)$", description="Status should be one of [in_stock|assigned|retired]")
    purchase_year: int = Field(..., ge=2015, le=2025, description="Purchase year should be in between 2015-2025")
    location: Optional[str] = Field("Bangaluru")

laptop_store = []
asset_list = []

# Add laptop asset
@app.post("/laptops")
def add_laptop(laptop: LaptopAsset):
    if laptop.asset_id in asset_list:
        raise HTTPException(status_code=409, detail="Asset already exists!")
    laptop_store.append(laptop)
    asset_list.append(laptop.asset_id)
    return laptop

# Get all laptop assets
@app.get("/laptops")
def get_all_assets():
    return laptop_store

# Get laptop by asset_id
@app.get("/laptops/{asset_id}")
def get_assets_by_id(asset_id: int):
    if asset_id not in asset_list:
        raise HTTPException(status_code=404, detail="Asset doesn't exist!")
    for asset in laptop_store:
        if asset.asset_id == asset_id:
            return asset

# Update laptop asset
@app.put("/laptops/{asset_id}")
def update_laptop(asset_id: int, laptop: LaptopAsset):
    if asset_id not in asset_list:
        raise HTTPException(status_code=404, detail="Asset doesn't exist!")
    for i in range(len(laptop_store)):
        if laptop_store[i].asset_id == asset_id:
            if asset_id != laptop.asset_id:
                raise HTTPException(status_code=400, detail="Asset ID can't be changed!")
            laptop_store[i] = laptop
            return laptop

# Delete laptop asset
@app.delete("/laptops/{asset_id}")
def delete_profile(asset_id: int):
    if asset_id not in asset_list:
        raise HTTPException(status_code=404, detail="Asset Not Found")
    for i in range(len(laptop_store)):
        if laptop_store[i].asset_id == asset_id:
            removed = laptop_store.pop(i)
            asset_list.remove(asset_id)
            return removed

# Sample Output

"""
Sample Output for /laptops (POST):
Input: 
{
    "asset_id": 1,
    "seriel_number": "ABC12345",
    "model_name": "Dell XPS 13",
    "assigned_to_emp_id": 12345,
    "status": "in_stock",
    "purchase_year": 2022,
    "location": "Bangaluru"
}
Output:
{
    "asset_id": 1,
    "seriel_number": "ABC12345",
    "model_name": "Dell XPS 13",
    "assigned_to_emp_id": 12345,
    "status": "in_stock",
    "purchase_year": 2022,
    "location": "Bangaluru"
}

Sample Output for /laptops (GET):
Input: /laptops
Output:
[
    {
        "asset_id": 1,
        "seriel_number": "ABC12345",
        "model_name": "Dell XPS 13",
        "assigned_to_emp_id": 12345,
        "status": "in_stock",
        "purchase_year": 2022,
        "location": "Bangaluru"
    }
]

Sample Output for /laptops/{asset_id} (GET):
Input: /laptops/1
Output:
{
    "asset_id": 1,
    "seriel_number": "ABC12345",
    "model_name": "Dell XPS 13",
    "assigned_to_emp_id": 12345,
    "status": "in_stock",
    "purchase_year": 2022,
    "location": "Bangaluru"
}

Sample Output for /laptops/{asset_id} (GET) - Error:
Input: /laptops/999
Output:
{
    "detail": "Asset doesn't exist!"
}

Sample Output for /laptops/{asset_id} (PUT):
Input:
{
    "asset_id": 1,
    "seriel_number": "ABC12345",
    "model_name": "Dell XPS 15",
    "assigned_to_emp_id": 12345,
    "status": "assigned",
    "purchase_year": 2022,
    "location": "Bangaluru"
}
Output:
{
    "asset_id": 1,
    "seriel_number": "ABC12345",
    "model_name": "Dell XPS 15",
    "assigned_to_emp_id": 12345,
    "status": "assigned",
    "purchase_year": 2022,
    "location": "Bangaluru"
}

Sample Output for /laptops/{asset_id} (DELETE):
Input: /laptops/1
Output:
{
    "asset_id": 1,
    "seriel_number": "ABC12345",
    "model_name": "Dell XPS 13",
    "assigned_to_emp_id": 12345,
    "status": "in_stock",
    "purchase_year": 2022,
    "location": "Bangaluru"
}

Sample Output for /laptops/{asset_id} (DELETE) - Error:
Input: /laptops/999
Output:
{
    "detail": "Asset Not Found"
}
"""
