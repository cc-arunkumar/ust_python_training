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

# Initialize FastAPI application with a title
app = FastAPI(title="UST Employee Laptop Inventory")

# Define LaptopAsset model using Pydantic for validation
class LaptopAsset(BaseModel):
    asset_id : int = Field(..., ge=1, le=999999)  # Unique ID for laptop, must be between 1 and 999999
    serial_number : str = Field(..., pattern=r"^[A-Za-z0-9]{8,20}$")  # Alphanumeric serial number, 8-20 chars
    model_name : str = Field(..., min_length=3, max_length=50)  # Model name with length constraints
    assigned_to_emp_id : int = Field(ge=1, le=999999)  # Employee ID to whom laptop is assigned
    status : str = Field(..., pattern=r"^(in_stock|assigned|retired)$")  # Status must be one of these values
    purchase_year : int = Field(..., ge=2015, le=2025)  # Purchase year between 2015 and 2025
    location : str = Field(default="Bengaluru")  # Default location is Bengaluru

# In-memory list to store laptop assets
laptop_list : List[LaptopAsset] = []

# GET endpoint: Retrieve all laptops
@app.get("/laptops", response_model=List[LaptopAsset])
def get_all_laptops():
    return laptop_list

# GET endpoint: Retrieve a laptop by asset_id
@app.get("/laptops/{asset_id}", response_model=LaptopAsset)
def get_laptop_by_asset_id(asset_id: int):
    for data in laptop_list:
        if data.asset_id == asset_id:
            return data
    raise HTTPException(status_code=404, detail="Laptop with given asset_id not found")

# POST endpoint: Add a new laptop
@app.post("/laptops", response_model=LaptopAsset)
def add_laptop(laptop: LaptopAsset):
    # Check for duplicate asset_id
    for data in laptop_list:
        if data.asset_id == laptop.asset_id:
            raise HTTPException(status_code=409, detail="Asset ID already exists")
    laptop_list.append(laptop)
    return laptop

# PUT endpoint: Update an existing laptop by asset_id
@app.put("/laptops/{asset_id}", response_model=LaptopAsset)
def update_laptop(asset_id: int, laptop: LaptopAsset):
    for id, data in enumerate(laptop_list):
        if data.asset_id == asset_id:
            laptop_list[id] = laptop
            return laptop
    raise HTTPException(status_code=404, detail="Laptop with given asset_id not found")

# DELETE endpoint: Remove a laptop by asset_id
@app.delete("/laptops/{asset_id}", response_model=LaptopAsset)
def delete_laptop(asset_id: int):
    for id, data in enumerate(laptop_list):
        if data.asset_id == asset_id:
            return laptop_list.pop(id)
    raise HTTPException(status_code=404, detail="Laptop with given asset_id not found")


# ---------------- SAMPLE INPUT & OUTPUT ----------------

"""
Sample Input (POST /laptops):
{
  "asset_id": 101,
  "serial_number": "ABC12345XY",
  "model_name": "Dell Latitude 5420",
  "assigned_to_emp_id": 2001,
  "status": "assigned",
  "purchase_year": 2021,
  "location": "Chennai"
}

Sample Output (Response for POST /laptops):
{
  "asset_id": 101,
  "serial_number": "ABC12345XY",
  "model_name": "Dell Latitude 5420",
  "assigned_to_emp_id": 2001,
  "status": "assigned",
  "purchase_year": 2021,
  "location": "Chennai"
}

Sample Input (GET /laptops/101):
No body required

Sample Output:
{
  "asset_id": 101,
  "serial_number": "ABC12345XY",
  "model_name": "Dell Latitude 5420",
  "assigned_to_emp_id": 2001,
  "status": "assigned",
  "purchase_year": 2021,
  "location": "Chennai"
}

Sample Input (PUT /laptops/101):
{
  "asset_id": 101,
  "serial_number": "ABC12345XY",
  "model_name": "Dell Latitude 5420",
  "assigned_to_emp_id": 2002,
  "status": "assigned",
  "purchase_year": 2021,
  "location": "Bengaluru"
}

Sample Output:
{
  "asset_id": 101,
  "serial_number": "ABC12345XY",
  "model_name": "Dell Latitude 5420",
  "assigned_to_emp_id": 2002,
  "status": "assigned",
  "purchase_year": 2021,
  "location": "Bengaluru"
}

Sample Input (DELETE /laptops/101):
No body required

Sample Output:
{
  "asset_id": 101,
  "serial_number": "ABC12345XY",
  "model_name": "Dell Latitude 5420",
  "assigned_to_emp_id": 2002,
  "status": "assigned",
  "purchase_year": 2021,
  "location": "Bengaluru"
}
"""