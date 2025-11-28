from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field, field_validator
from datetime import datetime
from typing import Set
from src.crud.asset_crud import (
    create_asset,
    read_all_asset,
    update_asset,
    delete_asset,
    get_asset_by_id
)

app = FastAPI(title="UST AIMS+")

class AssetInventory(BaseModel):
    asset_id: int
    asset_tag: str
    asset_type: str
    serial_number: str = Field(..., pattern=r"^[A-Za-z0-9]+$")
    manufacturer: str
    model: str
    purchase_date: datetime
    warranty_years: int
    condition_status: str
    location: str
    asset_status: str
    assigned_to: str

    serial_numbers_seen: Set[str] = set()

    @field_validator("asset_tag")
    def asset_tag_validation(cls, v):
        if not v.startswith("UST-"):
            raise ValueError("Must start with UST-")
        return v

    @field_validator("model")
    def validate_model(cls, v):
        if not v or v not in ["Laptop", "Monitor", "Keyboard", "Mouse"]:
            raise ValueError("Invalid asset type")
        return v

    @field_validator("serial_number")
    def validate_serial_number(cls, v):
        if not v:
            raise ValueError("Serial number cannot be empty")
        if v in cls.serial_numbers_seen:
            raise ValueError(f"Duplicate serial number: {v}")
        cls.serial_numbers_seen.add(v)
        return v

    @field_validator("manufacturer")
    def validate_manufacturer(cls, v):
        if not v or v not in ["Dell", "HP", "Lenovo", "Samsung"]:
            raise ValueError(f"Invalid manufacturer: {v}")
        return v

    @field_validator("purchase_date")
    def validate_purchase_date(cls, v: datetime):
        if v > datetime.today():
            raise ValueError("Purchase date cannot be in the future")
        return v

    @field_validator("warranty_years")
    def validate_warranty_years(cls, v: int):
        if not (1 <= v <= 5):
            raise ValueError("Warranty years must be between 1 and 5")
        return v

    @field_validator("condition_status")
    def validate_condition_status(cls, v):
        if v not in ["New", "Good", "Used", "Damaged"]:
            raise ValueError(f"Invalid condition_status: {v}")
        return v

    @field_validator("location")
    def validate_location(cls, v):
        if v not in ["TVM", "Bangalore", "Chennai", "Hyderabad"]:
            raise ValueError(f"Invalid location: {v}")
        return v

    @field_validator("asset_status")
    def validate_asset_status(cls, v):
        if v not in ["Available", "Assigned", "Repair", "Retired"]:
            raise ValueError(f"Invalid asset_status: {v}")
        return v


# ---------------- Endpoints ----------------

@app.post("/assets")
def api_create_asset(asset: AssetInventory):
    try:
        return create_asset(asset)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/assets")
def api_read_all_assets():
    try:
        return read_all_asset()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/assets/{asset_id}")
def api_get_asset(asset_id: int):
    try:
        result = get_asset_by_id(asset_id)
        if result == "Not found":
            raise HTTPException(status_code=404, detail="Asset not found")
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.put("/assets/{asset_id}")
def api_update_asset(asset_id: int, asset: AssetInventory):
    try:
        asset.asset_id = asset_id
        return update_asset(asset)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.delete("/assets/{asset_id}")
def api_delete_asset(asset_id: int):
    try:
        return delete_asset(asset_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
