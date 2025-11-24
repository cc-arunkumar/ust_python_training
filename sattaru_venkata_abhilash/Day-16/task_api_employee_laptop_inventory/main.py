from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from typing import Optional, List

app = FastAPI(title="UST Employee Laptop Inventory")

# Pydantic model to define laptop record
class LaptopAsset(BaseModel):
    asset_id: int = Field(..., ge=1, le=999999)  # asset_id with range
    serial_number: str = Field(..., pattern=r'^[A-Za-z0-9]{8,20}$')  # Alphanumeric serial number (8-20 characters)
    model_name: str = Field(..., min_length=3, max_length=50)  # Model name length (3-50 characters)
    assigned_to_emp_id: Optional[int] = Field(None, ge=1000, le=999999)  # Optional employee ID with validation
    status: str = Field(..., pattern=r'^(in_stock|assigned|retired)$')  # Status must be one of these values
    purchase_year: int = Field(..., ge=2015, le=2025)  # Purchase year validation
    location: str = Field("Bengaluru")  # Default location is Bengaluru

# In-memory database to store laptops
laptop: List[LaptopAsset] = []

# Endpoint to get all laptops
@app.get("/laptops", response_model=List[LaptopAsset])
def get_details():
    return laptop

# Endpoint to get a laptop by asset_id
@app.get("/laptop/{asset_id}", response_model=LaptopAsset)
def get_laptop_by_id(asset_id: int):
    for lap in laptop:
        if lap.asset_id == asset_id:
            return lap
    raise HTTPException(status_code=404, detail="Laptop not found")

# Endpoint to create a new laptop record
@app.post("/laptops", response_model=LaptopAsset, status_code=status.HTTP_201_CREATED)
def create_laptop(laptop_asset: LaptopAsset):
    for lap in laptop:
        if lap.asset_id == laptop_asset.asset_id:
            raise HTTPException(status_code=409, detail="Asset ID already exists")
    laptop.append(laptop_asset)  # Add the new laptop to the list
    return laptop_asset

# Endpoint to update an existing laptop record
@app.put("/laptop/{asset_id}", response_model=LaptopAsset)
def update_laptop(asset_id: int, laptop_asset: LaptopAsset):
    if asset_id != laptop_asset.asset_id:
        raise HTTPException(status_code=400, detail="Asset ID in path and body must match")
    for i, lap in enumerate(laptop):
        if lap.asset_id == asset_id:
            laptop[i] = laptop_asset  # Update the record
            return laptop_asset
    raise HTTPException(status_code=404, detail="Laptop not found")

# Endpoint to delete a laptop record
@app.delete("/laptops/{asset_id}")
def delete_laptop(asset_id: int):
    for i, lap in enumerate(laptop):
        if lap.asset_id == asset_id:
            del laptop[i]  # Remove from list
            return {"detail": "Laptop deleted"}
    raise HTTPException(status_code=404, detail="Laptop not found")

# Sample Output for each endpoint:

# 1. GET /laptops
# Sample Output:
"""
[
  {
    "asset_id": 1,
    "serial_number": "AB12345678",
    "model_name": "Dell XPS 13",
    "assigned_to_emp_id": 1001,
    "status": "in_stock",
    "purchase_year": 2022,
    "location": "Bengaluru"
  },
  {
    "asset_id": 2,
    "serial_number": "XY98765432",
    "model_name": "HP EliteBook",
    "assigned_to_emp_id": 1002,
    "status": "assigned",
    "purchase_year": 2023,
    "location": "Bengaluru"
  }
]
"""

# 2. GET /laptop/{asset_id} (GET a laptop by ID)
# Sample Output for asset_id = 1:
"""
{
  "asset_id": 1,
  "serial_number": "AB12345678",
  "model_name": "Dell XPS 13",
  "assigned_to_emp_id": 1001,
  "status": "in_stock",
  "purchase_year": 2022,
  "location": "Bengaluru"
}
"""

# Sample Output for asset_id = 999 (not found):
"""
{
  "detail": "Laptop not found"
}
"""

# 3. POST /laptops (Create a new laptop record)
# Sample Input:
"""
{
  "asset_id": 3,
  "serial_number": "LM98765432",
  "model_name": "MacBook Pro",
  "assigned_to_emp_id": 1003,
  "status": "in_stock",
  "purchase_year": 2024,
  "location": "Bengaluru"
}
"""
# Sample Output:
"""
{
  "asset_id": 3,
  "serial_number": "LM98765432",
  "model_name": "MacBook Pro",
  "assigned_to_emp_id": 1003,
  "status": "in_stock",
  "purchase_year": 2024,
  "location": "Bengaluru"
}
"""

# 4. PUT /laptop/{asset_id} (Update an existing laptop record)
# Sample Input for asset_id = 1:
"""
{
  "asset_id": 1,
  "serial_number": "AB12345678",
  "model_name": "Dell XPS 13 Updated",
  "assigned_to_emp_id": 1001,
  "status": "retired",
  "purchase_year": 2022,
  "location": "Bengaluru"
}
"""
# Sample Output for asset_id = 1 (updated):
"""
{
  "asset_id": 1,
  "serial_number": "AB12345678",
  "model_name": "Dell XPS 13 Updated",
  "assigned_to_emp_id": 1001,
  "status": "retired",
  "purchase_year": 2022,
  "location": "Bengaluru"
}
"""

# Sample Output for asset_id = 999 (not found):
"""
{
  "detail": "Laptop not found"
}
"""

# 5. DELETE /laptops/{asset_id} (Delete a laptop record)
# Sample Output for asset_id = 1 (deleted):
"""
{
  "detail": "Laptop deleted"
}
"""

# Sample Output for asset_id = 999 (not found):
"""
{
  "detail": "Laptop not found"
}
"""