# Import FastAPI framework and HTTP utilities
from fastapi import FastAPI, HTTPException, status

# Import Pydantic for data validation
from pydantic import BaseModel, Field

# Typing for optional values and lists
from typing import Optional, List

# Regex for validating serial numbers
import re

# Create FastAPI app with a title
app = FastAPI(title="UST Employee Laptop Inventory")

# Regex pattern: serial number must be alphanumeric, 8–20 characters
SERIAL_NUMBER = re.compile(r"^[A-Za-z0-9]{8,20}$")

# ------------------ Data Model ------------------
class LaptopAsset(BaseModel):
    # Unique ID for laptop, must be between 1 and 999999
    asset_id: int = Field(..., ge=1, le=999999)
    # Serial number must match regex pattern
    serial_number: str = Field(..., pattern=SERIAL_NUMBER.pattern)
    # Model name must be 3–50 characters
    model_name: str = Field(..., min_length=3, max_length=50)
    # Employee ID assigned, optional, must be between 1000–999999
    assigned_to_emp_id: Optional[int] = Field(None, ge=1000, le=999999)
    # Status must be one of: in_stock, assigned, retired
    status: str = Field(..., pattern=r"^(in_stock|assigned|retired)$")
    # Purchase year must be between 2015–2025
    purchase_year: int = Field(..., ge=2015, le=2025)
    # Default location is Bengaluru
    location: str = Field(default="Bengaluru")

# In-memory list to store laptops
laptops: List[LaptopAsset] = []

# Helper function: find index of laptop by asset_id
def find_index(asset_id: int):
    for idx, laptop in enumerate(laptops):
        if laptop.asset_id == asset_id:
            return idx
    return None

# ------------------ CRUD Endpoints ------------------

# GET all laptops
@app.get("/laptops", response_model=List[LaptopAsset], status_code=status.HTTP_200_OK)
def get_all_laptops():
    return laptops
    # Output example: []
    # Output after adding laptops:
    # [
    #   {
    #     "asset_id": 101,
    #     "serial_number": "ABC12345XY",
    #     "model_name": "Dell Latitude 5420",
    #     "assigned_to_emp_id": 2001,
    #     "status": "in_stock",
    #     "purchase_year": 2022,
    #     "location": "Bengaluru"
    #   }
    # ]

# GET laptop by asset_id
@app.get("/laptops/{asset_id}", response_model=LaptopAsset, status_code=status.HTTP_200_OK)
def get_laptop(asset_id: int):
    idx = find_index(asset_id)
    if idx is None:
        # If not found, return 404 error
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Laptop not found")
    return laptops[idx]
    # Output example if found:
    # {
    #   "asset_id": 101,
    #   "serial_number": "ABC12345XY",
    #   "model_name": "Dell Latitude 5420",
    #   "assigned_to_emp_id": 2001,
    #   "status": "in_stock",
    #   "purchase_year": 2022,
    #   "location": "Bengaluru"
    # }

# POST create new laptop
@app.post("/laptops", response_model=LaptopAsset, status_code=status.HTTP_201_CREATED)
def create_laptop(new_laptop: LaptopAsset):
    if find_index(new_laptop.asset_id) is not None:
        # If asset_id already exists, return 409 conflict
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail="Asset ID already exists")
    laptops.append(new_laptop)
    return new_laptop
    # Output example:
    # {
    #   "asset_id": 102,
    #   "serial_number": "XYZ98765PQ",
    #   "model_name": "HP EliteBook",
    #   "assigned_to_emp_id": null,
    #   "status": "in_stock",
    #   "purchase_year": 2021,
    #   "location": "Bengaluru"
    # }

# PUT update existing laptop
@app.put("/laptops/{asset_id}", response_model=LaptopAsset, status_code=status.HTTP_200_OK)
def update_laptop(asset_id: int, updated_laptop: LaptopAsset):
    idx = find_index(asset_id)
    if idx is None:
        # If laptop not found, return 404
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Laptop not found")
    if updated_laptop.asset_id != asset_id:
        # Asset ID mismatch between path and body
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Asset ID in path and body must match")
    laptops[idx] = updated_laptop
    return updated_laptop
    # Output example:
    # {
    #   "asset_id": 102,
    #   "serial_number": "XYZ98765PQ",
    #   "model_name": "HP EliteBook Updated",
    #   "assigned_to_emp_id": 3002,
    #   "status": "assigned",
    #   "purchase_year": 2021,
    #   "location": "Bengaluru"
    # }

# DELETE laptop by asset_id
@app.delete("/laptops/{asset_id}", status_code=status.HTTP_200_OK)
def delete_laptop(asset_id: int):
    idx = find_index(asset_id)
    if idx is None:
        # If not found, return 404
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Laptop not found")
    laptops.pop(idx)
    return {"detail": "Laptop deleted"}
    # Output example:
    # {"detail": "Laptop deleted"}