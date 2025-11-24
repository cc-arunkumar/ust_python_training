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

from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from typing import Optional, List


app = FastAPI(title=

"UST Employee Laptop Inventory")

class LaptopAsset(BaseModel):
    asset_id:int = Field(...,ge=1,le=999999,description="Asset id must be in between 1 abd 999999")
    serial_number:str = Field(...,pattern=r"^[A-Za-z0-9]{8,20}$",description="serial number patters not matching")
    model_name:str = Field(...,min_length=3 , max_length=50,description="model name length is between 3 and 50")
    assigned_to_emp_id:Optional[int] = Field(None,ge=1000,le=999999)
    status:str = Field(...,pattern=r"^(in_stock|assigned|retired)$",description="status does not match")
    purchase_year:int = Field(...,ge=2015,le=2025,description="invalid puchase year")
    location:Optional[str] = Field("Bangaluru")

laptops = []

@app.get("/laptops")
def get_laptops():
    return laptops

@app.get("/laptops/{asset_id}")
def get_laptop_by_id(asset_id:int):
    for i in laptops:
        if i.asset_id == asset_id:
            return i
    raise HTTPException(status_code=404,detail="No laptop found")

@app.post("/laptops")
def create_new_laptop(laptop:LaptopAsset):
    laptops.append(laptop)
    return {"Laptop added":laptop}

@app.put("/laptops/{asset_id}")
def update_laptop(asset_id:int,laptop:LaptopAsset):
    for i in range(len(laptops)):
        if laptops[i].asset_id == asset_id:
            laptops[i] = laptop
            return {"laptop updated":laptop}
    raise HTTPException(status_code=404,detail="No laptop found")

@app.delete("/laptops.{asset_id}")
def delete_laptop(asset_id:int):
    for i in range(len(laptops)):
        if laptops[i].asset_id == asset_id:
            return {"laptop data deleted":laptops.pop(i)}
        
    raise HTTPException(status_code=404,detail="No laptop found")