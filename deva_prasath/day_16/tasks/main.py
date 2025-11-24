# CRUD API Development
#  UST Employee Laptop Inventory 
#  UST maintains an internal inventory of company laptops assigned to employees.
#  The IT department needs a small internal API to:
#  Register laptops
#  View laptop details
#  Update laptop records
#  Remove laptops that are retired or disposed
#  All data will be stored in memory for this exercise.

from pydantic import BaseModel, Field
from typing import List, Optional
from fastapi import FastAPI, HTTPException

app = FastAPI(title="Employee Laptop Inventory")

# Pydantic model for Laptop Assets
class LaptopAssets(BaseModel):
    asset_id: int = Field(..., ge=1, le=999999)  # Asset ID should be between 1 and 999999
    serial_number: str = Field(..., pattern=r"^[A-Za-z0-9]{8,20}$")  # Serial number should be alphanumeric, 8 to 20 characters
    model_name: str = Field(..., min_length=3, max_length=50)  # Model name should be between 3 and 50 characters
    assigned_to_emp_id: int = Field(..., ge=1000, le=999999)  # Employee ID should be between 1000 and 999999
    status: str = Field(..., pattern=r"^(in_stock|assigned|retired)$")  # Status should be one of 'in_stock', 'assigned', or 'retired'
    purchase_year: int = Field(..., ge=2015, le=2025)  # Purchase year should be between 2015 and 2025
    location: str = "Bengaluru"  # Default location is Bengaluru


laptop_specs: List[dict] = []  # In-memory storage for laptop assets

# Endpoint to add a new laptop asset
@app.post("/laptops", response_model=LaptopAssets)
def add_lap(lap: LaptopAssets):
    # Check if asset ID already exists
    for a in laptop_specs:
        if a['asset_id'] == lap.asset_id:
            raise HTTPException(status_code=409, detail="Asset id already exists")
    
    # Add new laptop asset to the in-memory list
    laptop_specs.append(lap.model_dump())
    return lap

# Endpoint to get all laptop assets
@app.get("/laptops", response_model=List[LaptopAssets])
def get_all():
    return laptop_specs  # Return all laptop assets

# Endpoint to get a specific laptop asset by asset_id
@app.get("/laptops/{asset_id}", response_model=LaptopAssets)
def get(asset_id: int):
    for a in laptop_specs:
        if a['asset_id'] == asset_id:
            return a  # Return the laptop asset if found
        
    raise HTTPException(status_code=404, detail="Laptop not found")  # Return error if laptop not found

# Endpoint to update a laptop asset by asset_id
@app.put("/laptops/{asset_id}", response_model=LaptopAssets)
def edit(asset_id: int, lap: LaptopAssets):
    existing = None
    for a in laptop_specs:
        if a['asset_id'] == asset_id:
            existing = a
            break
    
    if existing is None:
        raise HTTPException(status_code=404, detail="Laptop not Found")  # Return error if laptop not found
    
    if asset_id != lap.asset_id:
        raise HTTPException(status_code=400, detail="Asset ID and Body must match")  # Ensure the asset ID in the URL matches the body
    
    # Update the laptop asset
    laptop_specs.remove(existing)
    laptop_specs.append(lap.model_dump())
    return lap

# Endpoint to delete a laptop asset by asset_id
@app.delete("/laptops/{asset_id}")
def delete(asset_id: int):
    for a in laptop_specs:
        if a['asset_id'] == asset_id:
            laptop_specs.remove(a)  # Remove the laptop asset from the list
            return {"detail": "Laptop deleted successfully"}  # Return success message
        
    raise HTTPException(status_code=404, detail="Laptop not found")  # Return error if laptop not found

#Sample output


#1. Post laptop

#Request

#  {
#  "asset_id": 2,
#  "serial_number": "XYZ98765",
#  "model_name": "HP EliteBook 840",
#  "assigned_to_emp_id" 54321,
#  "status": "assigned",
#  "purchase_year": 2021,
#  "location": "Chennai"
#}

#Response # 200

# {
#   "asset_id": 2,
#   "serial_number": "XYZ98765",
#   "model_name": "HP EliteBook 840",
#   "assigned_to_emp_id": 54321,
#   "status": "assigned",
#   "purchase_year": 2021,
#   "location": "Chennai"
# }

# Response headers
#  content-length: 162 
#  content-type: application/json 
#  date: Mon,24 Nov 2025 11:06:09 GMT 
#  server: uvicorn 


# 2. Get all 

# Request

# curl -X 'GET' \
#   'http://127.0.0.1:8000/laptops' \
#   -H 'accept: application/json'

	
# Response body
# Download
# [
#   {
#     "asset_id": 2,
#     "serial_number": "XYZ98765",
#     "model_name": "HP EliteBook 840",
#     "assigned_to_emp_id": 54321,
#     "status": "assigned",
#     "purchase_year": 2021,
#     "location": "Chennai"
#   }
# ]
# Response headers
#  content-length: 164 
#  content-type: application/json 
#  date: Mon,24 Nov 2025 11:41:54 GMT 
#  server: uvicorn


#3. Get by id

# curl -X 'GET' \
#   'http://127.0.0.1:8000/laptops/2' \
#   -H 'accept: application/json'


# Response body
# 200	
# {
#   "asset_id": 2,
#   "serial_number": "XYZ98765",
#   "model_name": "HP EliteBook 840",
#   "assigned_to_emp_id": 54321,
#   "status": "assigned",
#   "purchase_year": 2021,
#   "location": "Chennai"
# }


#4. Put command

#Request

# curl -X 'PUT' \
#   'http://127.0.0.1:8000/laptops/2' \
#   -H 'accept: application/json' \
#   -H 'Content-Type: application/json' \
#   -d '{
#     "asset_id": 2,
#     "serial_number": "XYZ98765",
#     "model_name": "Macbook m1pro",
#     "assigned_to_emp_id": 12345,
#     "status": "assigned",
#     "purchase_year": 2020,
#     "location": "Ranchi"
#   }'


#Response
	
# 200
# {
#   "asset_id": 2,
#   "serial_number": "XYZ98765",
#   "model_name": "Macbook m1pro",
#   "assigned_to_emp_id": 12345,
#   "status": "assigned",
#   "purchase_year": 2020,
#   "location": "Ranchi"
# }

#5. Delete api by emp_id

#Request
# curl -X 'DELETE' \
#   'http://127.0.0.1:8000/laptops/2' \
#   -H 'accept: application/json'

#Response
#200
# {
#   "detail": "Laptop deleted successfully"
# }