from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from typing import Optional, List

# -----------------------------------------------
# Pydantic Model for Laptop Asset
# -----------------------------------------------

class LaptopAsset(BaseModel):
    asset_id: int = Field(..., ge=1, le=999999, description="Asset ID must be between 1 and 999999")
    serial_number: str = Field(..., pattern=r"^[A-Za-z0-9]{8,20}$", description="Must be alphanumeric")
    model_name: str = Field(..., min_length=3, max_length=50)
    assigned_to_emp_id: Optional[int] = Field(None, ge=1000, le=999999, description="Correct employee ID")
    status: str = Field(..., pattern=r"^(in_stock|assigned|retired)$", description="Allowed: in_stock, assigned, retired")
    purchase_year: int = Field(..., ge=2015, le=2025)
    location: Optional[str] = "Bengaluru"


# -----------------------------------------------
# Initial In-Memory Database (List of Laptops)
# -----------------------------------------------

laptops: List[dict] = [
    {
        "asset_id": 1001,
        "serial_number": "ABC12345",
        "model_name": "Dell XPS 13",
        "assigned_to_emp_id": 1025,
        "status": "assigned",
        "purchase_year": 2021,
        "location": "Bengaluru"
    },
    {
        "asset_id": 1002,
        "serial_number": "XYZ98765",
        "model_name": "HP Spectre x360",
        "assigned_to_emp_id": 1050,
        "status": "assigned",
        "purchase_year": 2020,
        "location": "Mumbai"
    },
    {
        "asset_id": 1003,
        "serial_number": "EFG12345",
        "model_name": "MacBook Pro",
        "assigned_to_emp_id": 1101,
        "status": "in_stock",
        "purchase_year": 2022,
        "location": "Bengaluru"
    },
    {
        "asset_id": 1004,
        "serial_number": "LMN98765",
        "model_name": "Lenovo ThinkPad",
        "assigned_to_emp_id": None,
        "status": "in_stock",
        "purchase_year": 2023,
        "location": "Chennai"
    },
    {
        "asset_id": 1005,
        "serial_number": "JKL54321",
        "model_name": "Asus ROG Strix",
        "assigned_to_emp_id": 1032,
        "status": "assigned",
        "purchase_year": 2021,
        "location": "Delhi"
    },
    {
        "asset_id": 1006,
        "serial_number": "OPQ12345",
        "model_name": "Microsoft Surface Laptop",
        "assigned_to_emp_id": None,
        "status": "in_stock",
        "purchase_year": 2020,
        "location": "Bengaluru"
    },
    {
        "asset_id": 1007,
        "serial_number": "UVW98765",
        "model_name": "Acer Predator Helios",
        "assigned_to_emp_id": 1060,
        "status": "assigned",
        "purchase_year": 2021,
        "location": "Pune"
    },
    {
        "asset_id": 1008,
        "serial_number": "RST54321",
        "model_name": "Razer Blade 15",
        "assigned_to_emp_id": 1075,
        "status": "retired",
        "purchase_year": 2018,
        "location": "Bengaluru"
    },
    {
        "asset_id": 1009,
        "serial_number": "PQR12345",
        "model_name": "Dell Inspiron 15",
        "assigned_to_emp_id": None,
        "status": "in_stock",
        "purchase_year": 2022,
        "location": "Hyderabad"
    },
    {
        "asset_id": 1010,
        "serial_number": "TUV98765",
        "model_name": "MacBook Air",
        "assigned_to_emp_id": 1080,
        "status": "assigned",
        "purchase_year": 2023,
        "location": "Kolkata"
    }
]

# -----------------------------------------------
# FastAPI App Initialization
# -----------------------------------------------

app = FastAPI(title="Laptop Inventory Management")

# -----------------------------------------------
# Create New Laptop
# -----------------------------------------------

@app.post("/laptop", status_code=201)
def new_lap(laptop: LaptopAsset):
    # Check duplicate asset ID
    for lap in laptops:
        if laptop.asset_id == lap["asset_id"]:
            raise HTTPException(status_code=400, detail="Asset ID already exists")

    laptops.append(laptop.model_dump())   # Store as dictionary
    return {"message": "Laptop added successfully"}

# -----------------------------------------------
# List All Laptops
# -----------------------------------------------

@app.get("/laptops", response_model=List[LaptopAsset])
def list_laps():
    return laptops

# -----------------------------------------------
# Get Laptop by ID
# -----------------------------------------------

@app.get("/laptops/{asset_id}", response_model=LaptopAsset)
def get_by_id(asset_id: int):
    for lap in laptops:
        if lap["asset_id"] == asset_id:
            return lap  # Return laptop directly

    raise HTTPException(
        status_code=404,
        detail="Laptop with this Asset ID not found"
    )

# -----------------------------------------------
# Update Laptop by ID
# -----------------------------------------------

@app.put("/laptops/{asset_id}")
def update_lap(asset_id: int, laptop: LaptopAsset):
    for i, item in enumerate(laptops):
        if item["asset_id"] == asset_id:
            laptops[i] = laptop.model_dump()   # Replace existing entry
            return {"message": "Laptop updated successfully"}

    raise HTTPException(
        status_code=404,
        detail="Laptop with this Asset ID not found"
    )

# -----------------------------------------------
# Delete Laptop by ID
# -----------------------------------------------

@app.delete("/laptops/delete/{asset_id}")
def delete_lap(asset_id: int):
    for i, item in enumerate(laptops):
        if item["asset_id"] == asset_id:
            removed = laptops.pop(i)
            return {"message": "Laptop removed", "removed_item": removed}

    raise HTTPException(
        status_code=404,
        detail="Laptop with this Asset ID not found"
    )
"""
==========================================================
             SAMPLE INPUTS AND OUTPUTS
==========================================================

------------------ INITIAL DATA ------------------
[
  {
    "asset_id": 1,
    "name": "Dell Inspiron",
    "model": "3501",
    "ram": "8GB",
    "storage": "512GB SSD"
  },
  {
    "asset_id": 2,
    "name": "HP Pavilion",
    "model": "15-eg",
    "ram": "16GB",
    "storage": "1TB SSD"
  }
]

----------------------------------------------------------
1) POST /laptops/add
----------------------------------------------------------

INPUT:
{
  "asset_id": 3,
  "name": "Lenovo ThinkPad",
  "model": "E14",
  "ram": "16GB",
  "storage": "512GB SSD"
}

OUTPUT:
{
  "message": "Laptop added successfully",
  "data": {
    "asset_id": 3,
    "name": "Lenovo ThinkPad",
    "model": "E14",
    "ram": "16GB",
    "storage": "512GB SSD"
  }
}

----------------------------------------------------------
2) PUT /laptops/2
----------------------------------------------------------

INPUT:
{
  "asset_id": 2,
  "name": "HP Pavilion Updated",
  "model": "15-eg-2025",
  "ram": "32GB",
  "storage": "2TB SSD"
}

OUTPUT:
{
  "message": "Laptop updated successfully",
  "updated_data": {
    "asset_id": 2,
    "name": "HP Pavilion Updated",
    "model": "15-eg-2025",
    "ram": "32GB",
    "storage": "2TB SSD"
  }
}

If asset not found:
{
  "detail": "Laptop with id 10 not found"
}

----------------------------------------------------------
3) DELETE /laptops/delete/1
----------------------------------------------------------

OUTPUT:
{
  "message": "Laptop removed successfully",
  "removed_item": {
    "asset_id": 1,
    "name": "Dell Inspiron",
    "model": "3501",
    "ram": "8GB",
    "storage": "512GB SSD"
  }
}

If asset not found:
{
  "detail": "Laptop with id 50 not found"
}
==========================================================
"""