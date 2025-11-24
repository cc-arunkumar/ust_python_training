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
# 2. Data Model Requirements
# Define a single Pydantic model LaptopAsset that represents a laptop record.
# 2.1 LaptopAsset
# Fields
# Field Type Required Rules / Constraints
# asset_id int Yes
# Unique asset identifier; ge=1 ,
# le=999999
# serial_number str Yes
# Must be alphanumeric, 8–20
# characters; pattern: ^[A-Za-z0-9]
# {8,20}$
# model_name str Yes
# Laptop model name;
# min_length=3 , max_length=50
# assigned_to_emp_id int No
# Employee ID if assigned;
# ge=1000 , le=999999 when
# provided
# CRUD API Development 1
# Field Type Required Rules / Constraints
# status str Yes
# One of "in_stock" , "assigned" ,
# "retired" (validated via pattern)
# purchase_year int Yes
# Purchase year; ge=2015 ,
# le=2025
# location str No Default "Bengaluru"
# Recommended status constraint (string pattern):
# Field(..., pattern=r"^(in_stock|assigned|retired)$")
# Participants may also add description and example in Field(...) for better docs.
# 3. FastAPI Service Requirements
# Implement a FastAPI application with:
# In-memory list to store LaptopAsset objects.
# asset_id must be unique and is used as the key for CRUD operations.
# Imports
# from fastapi import FastAPI, HTTPException, status
# from pydantic import BaseModel, Field
# from typing import Optional, List
# 4. Endpoints Specification
# Exactly 5 APIs must be implemented:
# 1. GET /laptops – Get all laptops
# 2. GET /laptops/{asset_id} – Get laptop by asset_id
# 3. POST /laptops – Create a new laptop record
# 4. PUT /laptops/{asset_id} – Update an existing laptop record
# 5. DELETE /laptops/{asset_id} – Delete an existing laptop record
# CRUD API Development 2
# 4.1 GET /laptops – Get all laptops
# Response: list of LaptopAsset objects.
# Status: 200 OK
# Example response (JSON):
# [
#  {
#  "asset_id": 1,
#  "serial_number": "ABC12345",
#  "model_name": "Dell Latitude 5420",
#  "assigned_to_emp_id": 12345,
#  "status": "assigned",
#  "purchase_year": 2022,
#  "location": "Bengaluru"
#  }
# ]
# 4.2 GET /laptops/{asset_id} – Get by ID
# Behavior
# If a laptop with the given asset_id exists → return its details.
# If not found → return HTTP 404.
# Responses
# 200 OK – body: LaptopAsset
# 404 Not Found – body: {"detail": "Laptop not found"}
# Example:
# GET /laptops/1
# Response:
# {
#  "asset_id": 1,
# CRUD API Development 3
#  "serial_number": "ABC12345",
#  "model_name": "Dell Latitude 5420",
#  "assigned_to_emp_id": 12345,
#  "status": "assigned",
#  "purchase_year": 2022,
#  "location": "Bengaluru"
# }
# 4.3 POST /laptops – Create a new laptop
# Request body: LaptopAsset
# Example valid request:
# {
#  "asset_id": 2,
#  "serial_number": "XYZ98765",
#  "model_name": "HP EliteBook 840",
#  "assigned_to_emp_id": 54321,
#  "status": "assigned",
#  "purchase_year": 2021,
#  "location": "Chennai"
# }
# Behavior
# Validate input using Pydantic.
# If asset_id already exists in the in-memory list → return HTTP 409 (Conflict).
# If valid and not duplicate → add to list and return created record.
# Responses
# 201 Created – created LaptopAsset
# 409 Conflict – {"detail": "Asset ID already exists"}
# 422 Unprocessable Entity – Pydantic validation errors (e.g., wrong
# pattern/status/year)
# CRUD API Development 4
# Example minimal valid request (using defaults):
# {
#  "asset_id": 3,
#  "serial_number": "QWERTY12",
#  "model_name": "Lenovo ThinkPad X1",
#  "status": "in_stock",
#  "purchase_year": 2023
# }
# Expected behavior:
# location defaults to "Bengaluru"
# assigned_to_emp_id is null (or omitted depending on response serialization)
# 4.4 PUT /laptops/{asset_id} – Update a laptop
# Request body: LaptopAsset
# Behavior
# If no laptop with {asset_id} exists → return 404.
# If asset_id in the body does not match the path parameter → return 400 (to
# keep IDs consistent).
# If valid → replace the existing record in the list.
# Responses
# 200 OK – updated LaptopAsset
# 400 Bad Request – {"detail": "Asset ID in path and body must match"}
# 404 Not Found – {"detail": "Laptop not found"}
# Example:
# PUT /laptops/2
# Body:
# CRUD API Development 5
# {
#  "asset_id": 2,
#  "serial_number": "XYZ98765",
#  "model_name": "HP EliteBook 840 G9",
#  "assigned_to_emp_id": 54321,
#  "status": "assigned",
#  "purchase_year": 2022,
#  "location": "Pune"
# }
# 4.5 DELETE /laptops/{asset_id} – Delete a laptop
# Behavior
# If laptop exists → remove it from the list and return confirmation message.
# If not found → return 404.
# Responses
# 200 OK – {"detail": "Laptop deleted"}
# 404 Not Found – {"detail": "Laptop not found"}
# Example:
# DELETE /laptops/3
# 5. Validation Scenarios to Test
# Participants should test and observe FastAPI/Pydantic 422 errors for:
# 1. Invalid asset_id :
# < 1 or > 999999
# 2. Invalid serial_number :
# Length < 8 or > 20
# Contains non-alphanumeric characters (e.g., "ABC-12345" )
# 3. Invalid status :
# CRUD API Development 6
# Value not in "in_stock" | "assigned" | "retired" (e.g., "lost" )
# 4. Invalid assigned_to_emp_id when provided:
# < 1000 or > 999999
# 5. Invalid purchase_year :
# < 2015 or > 2025
# 6. Missing required fields:
# Omitting asset_id , serial_number , model_name , status , or purchase_year
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
# CRUD API Development 7
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
