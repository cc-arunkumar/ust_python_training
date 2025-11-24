from fastapi import FastAPI, HTTPException, status
from pydantic import Field, BaseModel
from typing import List, Optional

# Initialize FastAPI app with a title
app = FastAPI(title="Employee Laptop Inventory")

# Define the LaptopAssets model using Pydantic for validation
class LaptopAssets(BaseModel):
    asset_id: int = Field(..., ge=1, le=99999)  # Unique ID, must be between 1 and 99999
    serial_number: str  # Serial number of the laptop
    model_name: str = Field(..., min_length=3, max_length=50)  # Model name with length constraints
    assigned_to_emp_id: Optional[int] = Field(None, ge=1000, le=99999)  # Employee ID if assigned
    status: str  # Status of the laptop (e.g., "Available", "Assigned", "In Repair")
    purchase_year: int = Field(..., ge=2015, le=2025)  # Purchase year must be between 2015–2025
    location: Optional[str] = "Bengaluru"  # Default location if not provided

# In-memory storage for laptops (acts like a temporary database)
laptops: List[LaptopAssets] = []

# Helper function to find a laptop by asset_id
def find_lap(asset_id: int):
    for laptop in laptops:
        if laptop.asset_id == asset_id:
            return laptop
    return None


# ------------------- API Endpoints -------------------

# GET all laptops
@app.get("/laptops", response_model=List[LaptopAssets])
def get_all():
    # Returns the entire list of laptops
    return laptops


# GET a single laptop by asset_id
@app.get("/laptops/{asset_id}", response_model=LaptopAssets)
def get_laptop(asset_id: int):
    laptop = find_lap(asset_id)
    
    if not laptop:
        # Raise 404 error if laptop not found
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Laptop Not Found"
        )
    return laptop


# POST a new laptop (create)
@app.post("/laptops", response_model=LaptopAssets, status_code=status.HTTP_201_CREATED)
def create_laptops(laptop: LaptopAssets):
    # Check if asset_id already exists
    for item in laptops:
        if item.asset_id == laptop.asset_id:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Asset Already Exist"
            )
    # Add new laptop to list
    laptops.append(laptop)
    return laptop


# PUT update an existing laptop
@app.put("/laptops/{asset_id}", response_model=LaptopAssets)
def update_laptop(asset_id: int, updated_laptop: LaptopAssets):
    # Ensure asset_id in path matches the one in request body
    if asset_id != updated_laptop.asset_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Asset Id in path and body must match"
        )
    
    # Find and update laptop
    for index, laptop in enumerate(laptops):
        if laptop.asset_id == asset_id:
            laptops[index] = updated_laptop
            return updated_laptop
    
    # Raise 404 if laptop not found
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Laptop Not found"
    )
    

# DELETE a laptop by asset_id
@app.delete("/laptops/{asset_id}")
def delete_laptop(asset_id: int):
    for index, laptop in enumerate(laptops):
        if laptop.asset_id == asset_id:
            laptops.pop(index)  # Remove laptop from list
            return {"details": "Laptop Deleted"}
    
    # Raise 404 if laptop not found
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Laptop Not found"
    )
   
    
""" SAMPLE OUTPUT
1. GET ALL
	
Response body
Download
[
  {
    "asset_id": 101,
    "serial_number": "SN001",
    "model_name": "Dell Latitude 5420",
    "assigned_to_emp_id": 2001,
    "status": "Assigned",
    "purchase_year": 2021,
    "location": "Bengaluru"
  },
  {
    "asset_id": 102,
    "serial_number": "SN002",
    "model_name": "HP Latitude 5420",
    "assigned_to_emp_id": 2002,
    "status": "Assigned",
    "purchase_year": 2022,
    "location": "Chennai"
  }
]

2. ADD ASSET
{
  "asset_id": 102,
  "serial_number": "SN002",
  "model_name": "HP Latitude 5420",
  "assigned_to_emp_id": 2002,
  "status": "Assigned",
  "purchase_year": 2022,
  "location": "Chennai"
}

3. GET ASSET BY ID

{
    "asset_id": 101,
    "serial_number": "SN001",
    "model_name": "Dell Latitude 5420",
    "assigned_to_emp_id": 2001,
    "status": "Assigned",
    "purchase_year": 2021,
    "location": "Bengaluru"
  }

4. Update
{
    "asset_id": 101,
    "serial_number": "SN001",
    "model_name": "Lenovo",
    "assigned_to_emp_id": 2001,
    "status": "Assigned",
    "purchase_year": 2021,
    "location": "Chennai"
  }


5. delete 
{
  "detail": "Laptop Deleted"
}
"""