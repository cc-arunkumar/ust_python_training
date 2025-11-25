from fastapi import FastAPI,HTTPException,status,Response
from pydantic import BaseModel, Field
from typing import Optional, List


app = FastAPI(title="UST Employee Laptop Inventory")


class Laptop_asset(BaseModel):
    asset_id :int =Field(...,ge=1 , le=999999)
    serial_number:str = Field(...,pattern=r"^(in_stock|assigned|retired)$")
    model_name:str = Field(...,min_length=3 , max_length=50)
    assign_to_emp_id:int=Field(ge=1000,le=999999)
    status:str = Field(..., pattern=r"^(in_stock|assigned|retired)$")
    purchase_year:str= Field(...,ge=2020,le=2025)
    location:str = Field(default="Bengaluru")
    
all_Laptop_assets=List[Laptop_asset] = []


@app.get("/laptops",response_model=List[Laptop_asset])
def get_laptops():
    return all_Laptop_assets


@app.get("/laptops/asset/{id}", response_model=Laptop_asset)
def get_laptop_by_id(id :int):
    for row in Laptop_asset:
        if id == row["asset_id"]:
            return row 
    return HTTPException(status_code=404,detail="Id not found or not exists")

@app.post("/laptops", response_model=Laptop_asset, status_code=status.HTTP_201_CREATED)
def add_laptops(laptop_asset: Laptop_asset):
    if laptop_asset.asset_id in all_Laptop_assets:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Asset id already exists"
        )
    all_Laptop_assets.append(laptop_asset)
    return laptop_asset
    
    




    
