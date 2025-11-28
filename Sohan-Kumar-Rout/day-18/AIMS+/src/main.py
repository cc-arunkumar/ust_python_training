import datetime
import pymysql
from fastapi import FastAPI, HTTPException
from api.vendor_api import get_vendor,vendor_by_id,vendor_by_status,vendor_searching,count_vendor,delete_vendor,update_vendor,update_vendor_status
from api.asset_api import get_task,asset_by_id,assets_by_status,asset_searching,count_assets,delete_asset,creating_task,update_asset,update_asset_status
from config.db_connection import get_connection
from models.asset_model import Asset_inventory
from models.vendor_model import VendorModel
from models.maintenance import MaintenanceBase
from models.employee_model import Employee
from api.employee_api import create_employee,get_all_employees,get_employee_by_id,update_employee_by_id,update_employee_status,delete_employee,search_employees,count_employees
from api.maintenance_api import create_maintenance,list_maintenance,list_maintenance_by_status,get_maintenance_by_id,update_maintenance,update_maintenance_status,delete_maintenance

app = FastAPI()

@app.get("/assets")
def get_all_assets():
    try:
        assets= get_task()
        return assets
    except Exception as e:
        raise HTTPException(status_code=500,detail="fetching issue")

@app.get("/assets/{id}")
def get_assets_by_id(id: int):
    return asset_by_id(id)

@app.get("/asset/list")
def list_assets(status:str):
    return assets_by_status(status)

@app.get("/assets/search")
def search_assets(keyword: str):
    return {"assets": asset_searching(keyword)}

@app.get("/assets/count")
def count_assets():
    return count_assets()

@app.delete("/assets/{id}")
def delete_asset_api(id: int):
    return delete_asset(id)

#Implementing the post the most hardest one
@app.post("/assets/create")
def create_asset(asset: Asset_inventory):
    return creating_task(
        asset.asset_id,
        asset.asset_tag,
        asset.asset_type,
        asset.serial_number,
        asset.manufacturer,
        asset.model,
        asset.purchase_date,
        asset.warranty_years,
        asset.condition_status,
        asset.assigned_to,
        asset.location,
        asset.asset_status,
    )

def create_task(asset_id, asset_tag, asset_type, serial_number, manufacturer, model,
                purchase_date, warranty_years, condition_status,
                assigned_to, location, asset_status):
    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor()

        sql = """
        INSERT INTO ust_asset_db.asset_inventory (
            asset_id, asset_tag, asset_type, serial_number, manufacturer,
            model, purchase_date, warranty_years, condition_status,
            assigned_to, location, asset_status
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        values = (
            asset_id,
            asset_tag,
            str(asset_type),          
            serial_number,
            str(manufacturer),        
            model,
            purchase_date.strftime("%Y-%m-%d"),  
            warranty_years,
            str(condition_status),   
            assigned_to,
            str(location),           
            str(asset_status), 
        )

        cursor.execute(sql, values)
        conn.commit()
        return {"message": "Asset inserted successfully", "asset_tag": asset_tag}

    except Exception as e:
        if conn: conn.rollback()
        raise HTTPException(status_code=500, detail=f"Error inserting asset: {str(e)}")
    finally:
        if cursor: cursor.close()
        if conn: conn.close()
        
@app.put("/assets/{asset_id}")
def update_asset_details(asset_id: int, asset: Asset_inventory):
    return update_asset(
        asset_id,
        asset.asset_tag,
        asset.asset_type,
        asset.serial_number,
        asset.manufacturer,
        asset.model,
        asset.purchase_date,
        asset.warranty_years,
        asset.condition_status,
        asset.assigned_to,
        asset.location,
        asset.asset_status,
    )

# Update only asset status
@app.patch("/assets/{asset_id}/status")
def change_asset_status(asset_id: int, asset_status: str):
    return update_asset_status(asset_id, asset_status)

@app.get("/vendors")
def get_all_vendors():
    try:
        assets= get_vendor()
        return assets
    except Exception as e:
        raise HTTPException(status_code=500,detail="fetching issue")

@app.get("/assets/{id}")
def get_vendor_by_id(id: int):
    return vendor_by_id(id)

@app.get("/asset/list")
def list_vendors(status:str):
    return vendor_by_status(status)

@app.get("/assets/search")
def search_vendors(keyword: str):
    return {"assets": vendor_searching(keyword)}
    
@app.get("/assets/count")
def count_vendors():
    return count_vendor()

@app.delete("/assets/{id}")
def delete_vendor_api(id: int):
    return delete_vendor(id)

@app.post("/vendors/create")
def create_vendor(vendor: VendorModel):   # VendorModel is your Pydantic model
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
            
@app.put("/vendors/{vendor_id}")
def update_vendor_details(vendor_id: str, vendor: VendorModel):
    return update_vendor(vendor_id, vendor)

@app.patch("/vendors/{vendor_id}/status")
def change_vendor_status(vendor_id: str, status: str):
    return update_vendor_status(vendor_id, status)


### Maintance
def api_create_maintenance(log: MaintenanceBase):
    return create_maintenance(log)

@app.get("/maintenance")
def api_list_maintenance():
    return list_maintenance()

@app.get("/maintenance/status/{status}")
def api_list_maintenance_by_status(status):
    return list_maintenance_by_status(status)

@app.get("/maintenance/{log_id}")
def api_get_maintenance_by_id(log_id):
    return get_maintenance_by_id(log_id)

@app.put("/maintenance/{log_id}")
def api_update_maintenance(log_id: int, row: dict):
    return update_maintenance(log_id, row)

@app.patch("/maintenance/{log_id}/status")
def api_update_maintenance_status(log_id: int, status: str):
    return update_maintenance_status(log_id, status)

# --- DELETE ---
@app.delete("/maintenance/{log_id}")
def api_delete_maintenance(log_id: int):
    return delete_maintenance(log_id)

##Employeee
@app.post("/employees/create")
def add_employee(emp: Employee):
    try:
        return create_employee(emp)
    except Exception as e:
        print(f"Error in create_employee: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@app.get("/employees/list")
def list_employees(status: str | None = None):
    return get_all_employees(status)

@app.get("/employees/count")
def count():
    return count_employees()

@app.get("/employees/search")
def search(column_name: str, keyword: str):
    return search_employees(column_name, keyword)

@app.get("/employees/{id}")
def read_employee(id: int):
    result = get_employee_by_id(id)
    if not result:
        raise HTTPException(status_code=404, detail="Employee not found")
    return result

@app.put("/employees/{id}")
def update_employee(id: int, emp: Employee):
    result = update_employee_by_id(id, emp)
    if not result:
        raise HTTPException(status_code=404, detail="Employee not found")
    return result

@app.patch("/employees/{id}/status")
def update_status(id: int, new_status: str):
    result = update_employee_status(id, new_status)
    if not result:
        raise HTTPException(status_code=404, detail="Employee not found")
    return result

@app.delete("/employees/{id}")
def remove_employee(id: int):
    result = delete_employee(id)
    if not result:
        raise HTTPException(status_code=404, detail="Employee not found")
    return result





    




    