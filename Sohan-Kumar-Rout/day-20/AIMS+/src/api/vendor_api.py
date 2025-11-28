from fastapi import APIRouter, Depends, HTTPException
from auth.jwt_auth import User, get_curr_user
from crud.vendor_crud import (
    get_vendor, vendor_by_id, vendor_by_status, vendor_searching,
    count_vendor, delete_vendor, update_vendor, update_vendor_status
)
from models.vendor_model import VendorModel
from config.db_connection import get_connection

router = APIRouter(prefix="/vendors", tags=["Vendors"])

@router.get("/count")
def count_vendors(current_user: User = Depends(get_curr_user)):
    return count_vendor()

@router.get("/{id}")
def get_vendor_by_id(id: int, current_user: User = Depends(get_curr_user)):
    return vendor_by_id(id)

@router.get("/list")
def list_vendors(status: str, current_user: User = Depends(get_curr_user)):
    return vendor_by_status(status)

@router.get("/search")
def search_vendors(keyword: str, current_user: User = Depends(get_curr_user)):
    return {"vendors": vendor_searching(keyword)}



@router.delete("/{id}")
def delete_vendor_api(id: int, current_user: User = Depends(get_curr_user)):
    return delete_vendor(id)

@router.post("/create")
def create_vendor(vendor: VendorModel, current_user: User = Depends(get_curr_user)):
    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor()

        sql = """
        INSERT INTO ust_asset_db.vendor_valid (
            vendor_id, vendor_name, contact_person, contact_phone,
            gst_number, email, address, city, active_status
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        values = (
            vendor.vendor_id,
            vendor.vendor_name,
            vendor.contact_person,
            vendor.contact_phone,
            vendor.gst_number,
            vendor.email,
            vendor.address,
            vendor.city,
            vendor.active_status,
        )

        cursor.execute(sql, values)
        conn.commit()

        return {"message": "Vendor inserted successfully", "vendor_id": vendor.vendor_id}

    except Exception as e:
        if conn:
            conn.rollback()
        raise HTTPException(status_code=500, detail=f"Error inserting vendor: {str(e)}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

@router.get("/")
def get_all_vendors(current_user: User = Depends(get_curr_user)):
    try:
        return get_vendor()
    except Exception:
        raise HTTPException(status_code=500, detail="fetching issue")

@router.put("/{vendor_id}")
def update_vendor_details(vendor_id: str, vendor: VendorModel, current_user: User = Depends(get_curr_user)):
    return update_vendor(vendor_id, vendor)

@router.patch("/{vendor_id}/status")
def change_vendor_status(vendor_id: str, status: str, current_user: User = Depends(get_curr_user)):
    return update_vendor_status(vendor_id, status)
