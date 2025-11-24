# CRUD API Development
# UST Employee Laptop Inventory
# 1. Context
# UST maintains an internal inventory of company laptops assigned to employees.
# The IT department needs a small internal API to:
# Register laptops
# View laptop details
# Update laptop records
# Remove laptops that are retired or disposed
# All data will be stored in memory for this exercise.

# 4. Endpoints Specification
# Exactly 5 APIs must be implemented:
# 1. GET /laptops – Get all laptops
# 2. GET /laptops/{asset_id} – Get laptop by asset_id
# 3. POST /laptops – Create a new laptop record
# 4. PUT /laptops/{asset_id} – Update an existing laptop record
# 5. DELETE /laptops/{asset_id} – Delete an existing laptop record


# 6. Deliverables
# Participants should submit:
# 1. Pydantic model definition: LaptopAsset with all constraints.
# 2. FastAPI code defining the 5 endpoints:
# GET /laptops
# GET /laptops/{asset_id}
# POST /laptops
# PUT /laptops/{asset_id}
# DELETE /laptops/{asset_id}
# 3. Screenshots or logs of:
# Successful creation of laptops (full and minimal)
# Retrieval by asset_id
# Successful update and delete operations
# Validation error responses for the listed invalid scenarios

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Optional, List

# Create FastAPI app instance
app = FastAPI()

# Define LaptopAsset model with validation rules
class LaptopAsset(BaseModel):
    asset_id: int = Field(..., ge=1, le=999999)  # unique ID, must be between 1 and 999999
    serial_number: str = Field(..., pattern=r"^[A-Za-z0-9]{8,20}$")  # alphanumeric, length 8–20
    model_name: str = Field(..., min_length=3, max_length=50)  # model name length 3–50
    assigned_to_emp_id: Optional[int] = Field(ge=1000, le=999999)  # optional employee ID
    status: str = Field(..., pattern=r"^(in_stock|assigned|retired)$")  # only 3 valid statuses
    purchase_year: int = Field(..., ge=2015, le=2025)  # purchase year range
    location: Optional[str] = "Bengaluru"  # default location

# In-memory list to store laptops
Laptops: List[LaptopAsset] = []

# GET all laptops
@app.get("/laptops")
def get_laptops():
    return Laptops

# GET laptop by asset_id
@app.get("/laptops/{asset_id}")
def get_laptop_byid(asset_id: int):
    for K in Laptops:
        if K.asset_id == asset_id:
            return K
    # If not found, raise 404 error
    raise HTTPException(status_code=404, detail="Laptop not found")

# POST create new laptop
@app.post("/laptops")
def create_laptop(laptop: LaptopAsset):
    # Check if asset_id already exists
    for K in Laptops:
        if K.asset_id == laptop.asset_id:
            raise HTTPException(status_code=409, detail="asset_id already exists")
    # Add new laptop to list
    Laptops.append(laptop)
    return laptop

# PUT update laptop details by asset_id
@app.put("/laptops/{asset_id}", response_model=LaptopAsset)
def update_laptop(asset_id: int, laptop: LaptopAsset):
    for K in Laptops:
        if K.asset_id == asset_id:
            # Update fields
            K.serial_number = laptop.serial_number
            K.model_name = laptop.model_name
            K.status = laptop.status
            K.purchase_year = laptop.purchase_year
            K.location = laptop.location
            return K
    # If not found, raise 404 error
    raise HTTPException(status_code=404, detail="id does not exits")

# DELETE laptop by asset_id
@app.delete("/laptops/{asset_id}")
def delete_laptop(asset_id: int):
    for K in Laptops:
        if K.asset_id == asset_id:
            Laptops.remove(K)  # remove from list
            return {"detail": "Laptop deleted"}
    # If not found, raise 404 error
    raise HTTPException(status_code=404, detail="Laptop not found")


# #sample output
# 1. POST /laptops – Create a New Laptop Record
# Request:
# POST /laptops
# {
#     "asset_id": 1,
#     "serial_number": "ABC12345",
#     "model_name": "Dell Latitude 5420",
#     "assigned_to_emp_id": 12345,
#     "status": "assigned",
#     "purchase_year": 2022,
#     "location": "Bengaluru"
# }
# Response:
# {
#     "asset_id": 1,
#     "serial_number": "ABC12345",
#     "model_name": "Dell Latitude 5420",
#     "assigned_to_emp_id": 12345,
#     "status": "assigned",
#     "purchase_year": 2022,
#     "location": "Bengaluru"
# }


# 2. GET /laptops – Get All Laptops
# Request:
# GET /laptops
# Response:
# [
#     {
#         "asset_id": 1,
#         "serial_number": "ABC12345",
#         "model_name": "Dell Latitude 5420",
#         "assigned_to_emp_id": 12345,
#         "status": "assigned",
#         "purchase_year": 2022,
#         "location": "Bengaluru"
#     }
# ]

# 3. GET /laptops/{asset_id} – Get Laptop by Asset ID
# Request:
# GET /laptops/1
# Response:
# {
#     "asset_id": 1,
#     "serial_number": "ABC12345",
#     "model_name": "Dell Latitude 5420",
#     "assigned_to_emp_id": 12345,
#     "status": "assigned",
#     "purchase_year": 2022,
#     "location": "Bengaluru"
# }

# 4. PUT /laptops/{asset_id} – Update an Existing Laptop Record
# Request:
# PUT /laptops/1
# {
#     "asset_id": 1,
#     "serial_number": "DEF67890",
#     "model_name": "Dell Latitude 7420",
#     "assigned_to_emp_id": 12345,
#     "status": "assigned",
#     "purchase_year": 2023,
#     "location": "Chennai"
# }
# Response:
# {
#     "asset_id": 1,
#     "serial_number": "DEF67890",
#     "model_name": "Dell Latitude 7420",
#     "assigned_to_emp_id": 12345,
#     "status": "assigned",
#     "purchase_year": 2023,
#     "location": "Chennai"
# }

# 5. DELETE /laptops/{asset_id} – Delete a Laptop
# Request:
# DELETE /laptops/1
# Response:
# {
#     "detail": "Laptop deleted"
# }

# 6. Validation Error Responses
# Invalid asset_id (POST)
# Request:
# POST /laptops
# {
#     "asset_id": 1000000,
#     "serial_number": "XYZ12345",
#     "model_name": "HP EliteBook",
#     "status": "assigned",
#     "purchase_year": 2021
# }
# Response:
# {
#     "detail": "Validation error",
#     "errors": [
#         {
#             "loc": ["body", "asset_id"],
#             "msg": "ensure this value is less than or equal to 999999",
#             "type": "value_error.number.not_le"
#         }
#     ]
# }

# Invalid serial_number (POST)
# Request:
# POST /laptops
# {
#     "asset_id": 2,
#     "serial_number": "XYZ-1234!",
#     "model_name": "HP EliteBook",
#     "status": "assigned",
#     "purchase_year": 2021
# }
# Response:
# {
#     "detail": "Validation error",
#     "errors": [
#         {
#             "loc": ["body", "serial_number"],
#             "msg": "string does not match regex \"^[A-Za-z0-9]{8,20}$\"",
#             "type": "value_error.str.regex"
#         }
#     ]
# }

# Invalid status (POST)
# Request:
# POST /laptops
# {
#     "asset_id": 2,
#     "serial_number": "XYZ12345",
#     "model_name": "HP EliteBook",
#     "status": "lost",
#     "purchase_year": 2021
# }
# Response:
# {
#     "detail": "Validation error",
#     "errors": [
#         {
#             "loc": ["body", "status"],
#             "msg": "string does not match regex \"^(in_stock|assigned|retired)$\"",
#             "type": "value_error.str.regex"
#         }
#     ]
# }


# Invalid purchase_year (POST)
# Request:
# POST /laptops
# {
#     "asset_id": 2,
#     "serial_number": "XYZ12345",
#     "model_name": "HP EliteBook",
#     "status": "assigned",
#     "purchase_year": 2026
# }
# Response:
# {
#     "detail": "Validation error",
#     "errors": [
#         {
#             "loc": ["body", "purchase_year"],
#             "msg": "ensure this value is less than or equal to 2025",
#             "type": "value_error.number.not_le"
#         }
#     ]
# }
