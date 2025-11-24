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

#import libraries
from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from typing import Optional, List

app = FastAPI(title='UST Employee Laptop Inventory')

# Data Model: LaptopAsset

class LaptopAsset(BaseModel):
    asset_id: int = Field(
        ...,
        ge=1,
        le=999999,
        description="Unique asset identifier ( between 1 and 999999).",
        example=101
    )
    serial_number: str = Field(
        ...,
        pattern='[A-Za-z0-9]{8,20}$',
        description="Alphanumeric serial number of the laptop (8-20 characters).",
        example="SN1234ABCD"
    )
    model_name: str = Field(
        ...,
        min_length=3,
        max_length=50,
        description="Model name of the laptop (3-50 characters).",
        example="Dell Latitude 5420"
    )
    assigned_to_emp_id: Optional[int] = Field(
        None,
        ge=1000,
        le=999999,
        description="Invalid Employee ID",
        example=2025
    )
    status: str = Field(
        ...,
        pattern='^(in_stock|assigned|retired)$',
        description="Invalid status of the laptop asset.",
        example="assigned"
    )
    purchase_year: int = Field(
        ...,
        ge=2015,
        le=2025,
        description="Invalid Year of purchase (between 2015 and 2025).",
        example=2021
    )
    location: Optional[str] = Field(
        default="Bengaluru",
        description="Invalid Location of the laptop asset (defaults to Bengaluru).",
        example="Hyderabad"
    )
 
# In-Memory Storage

laptops_list : List[LaptopAsset] = []

#  API Endpoints
 
# GET /laptops → Retrieve all laptops
@app.get('/laptops',response_model=List[LaptopAsset])
def all_laptops():
    return laptops_list

# GET /laptops/{asset_id} → Retrieve laptop by ID
@app.get('/laptops/{asset_id}',response_model=LaptopAsset)
def get_laptop(asset_id : int):
    for idx,stored in enumerate(laptops_list):
        stored_id = stored.asset_id 
        if stored_id == asset_id:
            return stored 
    raise HTTPException(status_code=404,detail="Laptop Not Found")

# POST /laptops → Create a new laptop record
@app.post('/laptops',response_model=LaptopAsset)
def create_record(new_record : LaptopAsset):
    for idx,stored in enumerate(laptops_list):
        stored_id = stored.asset_id 
        if stored_id == new_record.asset_id:
            raise HTTPException(status_code=400,detail='Asset ID already Exists')
    laptops_list.append(new_record)
    return new_record

# DELETE /laptops/{asset_id} → Delete a laptop record
@app.delete('/laptops/{asset_id}')
def delete_record(asset_id : int):
    for idx,stored in enumerate(laptops_list):
        stored_id = stored.asset_id 
        if stored_id == asset_id:
            laptops_list.pop(idx)
            return {'detail':"Laptop Deleted"}
    raise HTTPException(status_code=404,detail="Laptop not Found")

# PUT /laptops/{asset_id} → Update an existing laptop record
@app.put('/laptops/{asset_id}',response_model=LaptopAsset)
def update_record(asset_id : int,updated_record : LaptopAsset):
    if asset_id != updated_record.asset_id:
        raise HTTPException(status_code=400,detail="Asset ID in path and body must match")
    
    for idx,stored in enumerate(laptops_list):
        stored_id = stored.asset_id 
        if stored_id == asset_id:
            # Replace fields with updated values
            stored.serial_number = updated_record.serial_number 
            stored.model_name  = updated_record.model_name
            stored.assigned_to_emp_id = updated_record.assigned_to_emp_id
            stored.status = updated_record.status
            stored.purchase_year = updated_record.purchase_year
            stored.location = updated_record.location
            return updated_record
    raise HTTPException(status_code=404,detail="Laptop not Found")
        



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
