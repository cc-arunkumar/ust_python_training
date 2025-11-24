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
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional, List

# Create the app
app = FastAPI()

# Define the Laptop model
class LaptopAsset(BaseModel):
    asset_id: int = Field(..., ge=1, le=999999)   # unique number
    serial_number: str = Field(..., pattern=r"^[A-Za-z0-9]{8,20}$")  # letters/numbers only
    model_name: str = Field(..., min_length=3, max_length=50)        # name of laptop
    assigned_to_emp_id: Optional[int] = Field(None, ge=1000, le=999999) # employee id
    status: str = Field(..., pattern=r"^(in_stock|assigned|retired)$")  # must be one of 3 values
    purchase_year: int = Field(..., ge=2015, le=2025)   # year bought
    location: str = "Bengaluru"   # default place

# Our "toy box" to store laptops
laptops: List[LaptopAsset] = []

# 1. GET all laptops
@app.get("/laptops")
def get_laptops():
    return laptops

# 2. GET one laptop by ID
@app.get("/laptops/{asset_id}")
def get_laptop(asset_id: int):
    for laptop in laptops:
        if laptop.asset_id == asset_id:
            return laptop
    raise HTTPException(status_code=404, detail="Laptop not found")

# 3. POST add a new laptop
@app.post("/laptops")
def add_laptop(laptop: LaptopAsset):
    for l in laptops:
        if l.asset_id == laptop.asset_id:
            raise HTTPException(status_code=409, detail="Asset ID already exists")
    laptops.append(laptop)
    return laptop

# 4. PUT update a laptop
@app.put("/laptops/{asset_id}")
def update_laptop(asset_id: int, laptop: LaptopAsset):
    for i, l in enumerate(laptops):
        if l.asset_id == asset_id:
            if asset_id != laptop.asset_id:
                raise HTTPException(status_code=400, detail="Asset ID in path and body must match")
            laptops[i] = laptop
            return laptop
    raise HTTPException(status_code=404, detail="Laptop not found")

# 5. DELETE remove a laptop
@app.delete("/laptops/{asset_id}")
def delete_laptop(asset_id: int):
    for i, l in enumerate(laptops):
        if l.asset_id == asset_id:
            laptops.pop(i)
            return {"detail": "Laptop deleted"}
    raise HTTPException(status_code=404, detail="Laptop not found")
# SAMPLE OUTPUT:
# GET /laptops → Get all laptops
# [
#   {
#     "asset_id": 1,
#     "serial_number": "ABC12345",
#     "model_name": "Dell Latitude 5420",
#     "assigned_to_emp_id": 12345,
#     "status": "assigned",
#     "purchase_year": 2022,
#     "location": "Bengaluru"
#   },
#   {
#     "asset_id": 2,
#     "serial_number": "XYZ98765",
#     "model_name": "HP EliteBook 840",
#     "assigned_to_emp_id": 54321,
#     "status": "in_stock",
#     "purchase_year": 2021,
#     "location": "Chennai"
#   }
# ]



# SAMPLE OUTPUT:
# GET /laptops/{asset_id} → Get laptop by ID

# {
#   "asset_id": 1,
#   "serial_number": "ABC12345",
#   "model_name": "Dell Latitude 5420",
#   "assigned_to_emp_id": 12345,
#   "status": "assigned",
#   "purchase_year": 2022,
#   "location": "Bengaluru"
# }



# SAMPLE OUTPUT:
# POST /laptops → Create a new laptop record

# {
#   "asset_id": 3,
#   "serial_number": "QWERTY12",
#   "model_name": "Lenovo ThinkPad X1",
#   "assigned_to_emp_id": null,
#   "status": "in_stock",
#   "purchase_year": 2023,
#   "location": "Bengaluru"
# }



# SAMPLE OUTPUT:
# PUT /laptops/{asset_id} → Update an existing laptop record

# {
#   "asset_id": 2,
#   "serial_number": "XYZ98765",
#   "model_name": "HP EliteBook 840 G9",
#   "assigned_to_emp_id": 54321,
#   "status": "assigned",
#   "purchase_year": 2022,
#   "location": "Pune"
# }



# SAMPLE OUTPUT:
# DELETE /laptops/{asset_id} → Delete a laptop record

# {
#   "detail": "Laptop Deleted"
# }


