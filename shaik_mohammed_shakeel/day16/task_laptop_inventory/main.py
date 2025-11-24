from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from typing import Optional, List

# Initialize FastAPI app with a title
app = FastAPI(title="UST Laptop Inventory")

# Global in-memory store to hold laptop data
laptops: List["LaptopAsset"] = []

# Pydantic model to define the structure and validation rules for laptop assets
class LaptopAsset(BaseModel):
    # Asset ID should be between 1 and 999999, representing a unique identifier for the laptop
    asset_id: int = Field(..., ge=1, le=999999, description="Unique asset")
    # Serial number should be alphanumeric and between 8 to 20 characters
    serial_number: str = Field(..., min_length=8, max_length=20, pattern=r"^[A-Za-z0-9]{8,20}$", description="Alphanumeric serial number")
    # Laptop model name should be between 3 and 50 characters long
    model_name: str = Field(..., min_length=3, max_length=50, description="Laptop model name")
    # Optional field for employee ID if the laptop is assigned
    assigned_to_emp_id: Optional[int] = Field(None, ge=1000, le=999999, description="Employee ID if assigned")
    # Laptop status: in_stock, assigned, or retired
    status: str = Field(..., pattern=r"^(in_stock|assigned|retired)$", description="Laptop status")
    # Purchase year should be between 2015 and 2025
    purchase_year: int = Field(..., ge=2015, le=2025, description="Purchase year")
    # Location of the laptop (defaults to 'Bengaluru')
    location: str = Field("Bengaluru", description="Laptop location")

# Route to get a list of all laptops in inventory
@app.get("/laptops", response_model=List[LaptopAsset])
def get_all_laptops():
    return laptops

# Route to get details of a specific laptop by its asset_id
@app.get("/laptops/{asset_id}", response_model=LaptopAsset)
def get_laptop_by_id(asset_id: int):
    # Look for a laptop with the given asset_id
    laptop = next((l for l in laptops if l.asset_id == asset_id), None)
    # If no laptop is found, raise a 404 HTTP exception
    if laptop is None:
        raise HTTPException(status_code=404, detail="Laptop not found")
    return laptop

# Route to add a new laptop to the inventory
@app.post("/laptops", response_model=LaptopAsset, status_code=status.HTTP_201_CREATED)
def create_laptop(new_laptop: LaptopAsset):
    # Check if the asset_id already exists to avoid duplication
    if any(l.asset_id == new_laptop.asset_id for l in laptops):
        raise HTTPException(status_code=409, detail="Asset ID already exists")
    # Append the new laptop to the inventory
    laptops.append(new_laptop)
    return new_laptop

# Route to update an existing laptop in the inventory by its asset_id
@app.put("/laptops/{asset_id}", response_model=LaptopAsset)
def update_laptop(asset_id: int, updated_laptop: LaptopAsset):
    # Ensure that the asset_id in the URL matches the one in the body of the request
    if asset_id != updated_laptop.asset_id:
        raise HTTPException(status_code=400, detail="Asset ID in path and body must match")
    # Find the existing laptop to update
    existing_laptop = next((l for l in laptops if l.asset_id == asset_id), None)
    # If no matching laptop is found, raise a 404 error
    if existing_laptop is None:
        raise HTTPException(status_code=404, detail="Laptop not found")
    # Remove the old laptop and append the updated laptop to the list
    laptops.remove(existing_laptop)
    laptops.append(updated_laptop)
    return updated_laptop

# Route to delete a laptop from the inventory by its asset_id
@app.delete("/laptops/{asset_id}", status_code=status.HTTP_200_OK)
def delete_laptop(asset_id: int):
    # Find the laptop to delete
    existing_laptop = next((l for l in laptops if l.asset_id == asset_id), None)
    # If the laptop is not found, raise a 404 error
    if existing_laptop is None:
        raise HTTPException(status_code=404, detail="Laptop not found")
    # Remove the laptop from the inventory
    laptops.remove(existing_laptop)
    return {"detail": "Laptop deleted"}
