from fastapi import FastAPI,HTTPException
from pydantic import BaseModel,Field
from typing import List,Optional

app=FastAPI(title=" UST Employee Laptop Inventory")

# Laptop model (like a blueprint)
class LaptopAsset(BaseModel):
    asset_id: int = Field(..., ge=1, le=999999)
    serial_number: str = Field(..., min_length=8, max_length=20, pattern=r"^[A-Za-z0-9]+$")
    model_name: str = Field(..., min_length=3, max_length=50)
    assigned_to_emp_id: Optional[int] = Field(None, ge=1000, le=999999)
    status: str = Field(..., pattern=r"^(in_stock|assigned|retired)$")
    purchase_year: int = Field(..., ge=2015, le=2025)
    location: Optional[str] = "Bengaluru"

# In-memory list (like a temporary database)
laptops: List[LaptopAsset] = []

@app.get("/laptops")
def getall():
    return laptops

#get laptops by id
@app.get("/laptops/{asset_id}")
def getbyid(asset_id:int):
    for laptop in laptops:
        if laptop.asset_id==asset_id:
            return laptop
    raise HTTPException(status_code=404,detail="Laptop not found")

# 3. Create new laptop
@app.post("/laptops",status_code=201)
def create(asset: LaptopAsset):
    for laptop in laptops:
        if laptop.asset_id == asset.asset_id:
            raise HTTPException(status_code=409, detail="Asset ID already exists")
    laptops.append(asset)
    return asset

# 4. Update laptop (replace object directly)
@app.put("/laptops/{asset_id}")
def update(asset_id: int, asset: LaptopAsset):
    if asset_id != asset.asset_id:
        raise HTTPException(status_code=400, detail="ID mismatch")
    for laptop in laptops:
        if laptop.asset_id == asset_id:
            # remove old object, add new one
            laptops.remove(laptop)
            laptops.append(asset)
            return asset
    raise HTTPException(status_code=404, detail="Laptop not found")

# 5. Delete laptop (remove object directly)
@app.delete("/laptops/{asset_id}")
def delete(asset_id: int):
    for laptop in laptops:
        if laptop.asset_id == asset_id:
            laptops.remove(laptop)
            return {"detail": "Laptop deleted"}
    raise HTTPException(status_code=404, detail="Laptop not found")
    
# -------------------------------
# SAMPLE INPUT AND OUTPUT
# -------------------------------

# """
# 1. Create a new laptop (POST /laptops)
# --------------------------------------
# Sample Input (JSON body):
# {
#     "asset_id": 101,
#     "serial_number": "ABC12345XYZ",
#     "model_name": "Dell Latitude 5420",
#     "assigned_to_emp_id": 2001,
#     "status": "assigned",
#     "purchase_year": 2022,
#     "location": "Bengaluru"
# }

# Sample Output (201 Created):
# {
#     "asset_id": 101,
#     "serial_number": "ABC12345XYZ",
#     "model_name": "Dell Latitude 5420",
#     "assigned_to_emp_id": 2001,
#     "status": "assigned",
#     "purchase_year": 2022,
#     "location": "Bengaluru"
# }


# 2. Get all laptops (GET /laptops)
# ---------------------------------
# Sample Output (200 OK):
# [
#     {
#         "asset_id": 101,
#         "serial_number": "ABC12345XYZ",
#         "model_name": "Dell Latitude 5420",
#         "assigned_to_emp_id": 2001,
#         "status": "assigned",
#         "purchase_year": 2022,
#         "location": "Bengaluru"
#     }
# ]


# 3. Get laptop by ID (GET /laptops/101)
# --------------------------------------
# Sample Output (200 OK):
# {
#     "asset_id": 101,
#     "serial_number": "ABC12345XYZ",
#     "model_name": "Dell Latitude 5420",
#     "assigned_to_emp_id": 2001,
#     "status": "assigned",
#     "purchase_year": 2022,
#     "location": "Bengaluru"
# }

# If not found:
# {
#     "detail": "Laptop not found"
# }


# 4. Update laptop (PUT /laptops/101)
# -----------------------------------
# Sample Input (JSON body):
# {
#     "asset_id": 101,
#     "serial_number": "ABC12345XYZ",
#     "model_name": "Dell Latitude 5430",
#     "assigned_to_emp_id": 2001,
#     "status": "in_stock",
#     "purchase_year": 2023,
#     "location": "Chennai"
# }

# Sample Output (200 OK):
# {
#     "asset_id": 101,
#     "serial_number": "ABC12345XYZ",
#     "model_name": "Dell Latitude 5430",
#     "assigned_to_emp_id": 2001,
#     "status": "in_stock",
#     "purchase_year": 2023,
#     "location": "Chennai"
# }


# 5. Delete laptop (DELETE /laptops/101)
# --------------------------------------
# Sample Output (200 OK):
# {
#     "detail": "Laptop deleted"
# }

# If not found:
# {
#     "detail": "Laptop not found"
# }
# """
