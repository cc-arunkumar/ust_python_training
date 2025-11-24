from pydantic import BaseModel, Field  # Import Pydantic for data validation
from typing import Optional, List  # Import Optional and List for type annotations
from fastapi import FastAPI, HTTPException  # Import FastAPI and HTTPException for the API

# Define the LaptopAsset model with validation rules using Pydantic
class LaptopAsset(BaseModel):
    asset_id: int = Field(..., ge=1, le=999999)  # Asset ID should be between 1 and 999999
    serial_number: str = Field(..., pattern=r"^[A-Za-z0-9]{8,20}$")  # Serial number should be alphanumeric and 8-20 characters
    model_name: str = Field(..., min_length=3, max_length=50)  # Model name should be between 3 and 50 characters
    assigned_to_emp_id: Optional[int] = Field(None, ge=1000, le=999999)  # Optional employee ID between 1000 and 999999
    status: str = Field(..., pattern=r"^(in_stock|assigned|retired)$")  # Status can be 'in_stock', 'assigned', or 'retired'
    purchase_year: int = Field(..., ge=2015, le=2025)  # Purchase year between 2015 and 2025
    location: str = Field("Bengaluru")  # Default location is Bengaluru

app = FastAPI()  # Initialize the FastAPI app

# In-memory storage for laptops (using a dictionary)
laptops = {
    1: LaptopAsset(
        asset_id=1,
        serial_number="ABC12345",
        model_name="Dell Latitude 5420",
        assigned_to_emp_id=12345,
        status="assigned",
        purchase_year=2022,
        location="Bengaluru"
    ),
    2: LaptopAsset(
        asset_id=2,
        serial_number="XYZ98765",
        model_name="HP EliteBook 840",
        assigned_to_emp_id=54321,
        status="assigned",
        purchase_year=2021,
        location="Chennai"
    ),
    3: LaptopAsset(
        asset_id=3,
        serial_number="QWERTY12",
        model_name="Lenovo ThinkPad X1",
        assigned_to_emp_id=None,  # Not assigned
        status="in_stock",
        purchase_year=2023,
        location="Bengaluru"
    )
}

# Endpoint to get all laptops
@app.get("/laptops", response_model=List[LaptopAsset])
def get_laptops():
    return list(laptops.values())  # Return all laptop entries as a list

# Endpoint to get a specific laptop by asset ID
@app.get("/laptops/{asset_id}", response_model=LaptopAsset)
def get_laptop(asset_id: int):
    if asset_id not in laptops:  # Check if the laptop exists
        raise HTTPException(status_code=404, detail="Laptop not found")  # Raise 404 if not found
    return laptops[asset_id]  # Return the laptop details

# Endpoint to create a new laptop entry
@app.post("/laptops", response_model=LaptopAsset, status_code=201)
def create_laptop(laptop: LaptopAsset):
    if laptop.asset_id in laptops:  # Check if asset ID already exists
        raise HTTPException(status_code=409, detail="Asset ID already exists")  # Raise 409 if duplicate
    laptops[laptop.asset_id] = laptop  # Store the laptop in the dictionary
    return laptop  # Return the newly created laptop

# Endpoint to update an existing laptop entry
@app.put("/laptops/{asset_id}", response_model=LaptopAsset)
def update_laptop(asset_id: int, laptop: LaptopAsset):
    if asset_id != laptop.asset_id:  # Ensure asset ID in path matches the body
        raise HTTPException(status_code=400, detail="Asset ID in path and body must match")  # Raise 400 if mismatch
    if asset_id not in laptops:  # Check if the laptop exists
        raise HTTPException(status_code=404, detail="Laptop not found")  # Raise 404 if not found
    laptops[asset_id] = laptop  # Update the laptop details
    return laptop  # Return the updated laptop

# Endpoint to delete a laptop by asset ID
@app.delete("/laptops/{asset_id}")
def delete_laptop(asset_id: int):
    if asset_id not in laptops:  # Check if the laptop exists
        raise HTTPException(status_code=404, detail="Laptop not found")  # Raise 404 if not found
    del laptops[asset_id]  # Delete the laptop entry
    return {"detail": "Laptop deleted"}  # Return confirmation message



# Output:

# GET /laptops
# Response:

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
#     "status": "assigned",
#     "purchase_year": 2021,
#     "location": "Chennai"
#   },
#   {
#     "asset_id": 3,
#     "serial_number": "QWERTY12",
#     "model_name": "Lenovo ThinkPad X1",
#     "assigned_to_emp_id": null,
#     "status": "in_stock",
#     "purchase_year": 2023,
#     "location": "Bengaluru"
#   }
# ]


# GET /laptops/1
# Response:

# {
#   "asset_id": 1,
#   "serial_number": "ABC12345",
#   "model_name": "Dell Latitude 5420",
#   "assigned_to_emp_id": 12345,
#   "status": "assigned",
#   "purchase_year": 2022,
#   "location": "Bengaluru"
# }


# POST /laptops
# Example request body:

# {
#   "asset_id": 4,
#   "serial_number": "DEF45678",
#   "model_name": "Acer Swift 3",
#   "assigned_to_emp_id": 67890,
#   "status": "assigned",
#   "purchase_year": 2020,
#   "location": "Mumbai"
# }


# Response:

# {
#   "asset_id": 4,
#   "serial_number": "DEF45678",
#   "model_name": "Acer Swift 3",
#   "assigned_to_emp_id": 67890,
#   "status": "assigned",
#   "purchase_year": 2020,
#   "location": "Mumbai"
# }


# PUT /laptops/2
# Example request body:

# {
#   "asset_id": 2,
#   "serial_number": "XYZ98765",
#   "model_name": "HP EliteBook 840 G9",
#   "assigned_to_emp_id": 54321,
#   "status": "assigned",
#   "purchase_year": 2022,
#   "location": "Pune"
# }


# Response:

# {
#   "asset_id": 2,
#   "serial_number": "XYZ98765",
#   "model_name": "HP EliteBook 840 G9",
#   "assigned_to_emp_id": 54321,
#   "status": "assigned",
#   "purchase_year": 2022,
#   "location": "Pune"
# }


# DELETE /laptops/3
# Response:

# {
#   "detail": "Laptop deleted"
# }