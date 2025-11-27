import datetime
import pymysql
from fastapi import FastAPI, HTTPException
from pydentic.asset_inventory_pydentic import Asset_inventory
from pydentic.employee_pydentic import EmployeeDirectory
from pydentic.vendors_pydentic import VendorMaster
from pydentic.maintainance_pydentic import MaintenanceLog
from api.asset_inventory import get_task, get_task_by_id,update_asset,update_asset_status,delete_asset, get_assets_by_status,search_assets_by_column,count_assets
from db_connection.db import get_connection
from api.employee_inventory import count_employees,create_employee,delete_employee,update_employee_by_id,update_employee_status,search_employees,get_all_employees,get_employee_by_id
from api.maintenance_invenotry import get_maintenance_by_id,list_maintenance,list_maintenance_by_status,update_maintenance,update_maintenance_status,delete_maintenance,create_maintenance
from api.vendor_inventory import get_all_data,get_data_by_status,get_data_by_id,create_vendor,update_vendor,count_vendors,get_rows_by_column,delete_vendor,update_vendor_status
app = FastAPI() 
@app.post("/assets/create")
def create_asset(asset: Asset_inventory):
    return create_task(
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
        INSERT INTO ust_asset_inventory.asset_inventory (
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

@app.get("/assets")
def get_all_assets():
    try:
        assets = get_task()
        return {"assets": assets}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error fetching assets: {str(e)}")
    
@app.get("/assets/get{id}")
def get_assets_by_id(id: int):
    return get_task_by_id(id)

    
@app.get("/assets/list")
def list_assets(status: str):
    return {"assets": get_assets_by_status(status)}
@app.get("/assets/search")
def search_assets_api(column: str, value: str):
    return search_assets_by_column(column, value)


@app.get("/assets/count")
def count_assets_api():
    return {"total_assets": count_assets()}


@app.put("/assets/{id}")
def update_asset_api(id: int, asset: Asset_inventory):
    return update_asset(
        id,
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

@app.patch("/assets/{id}/status")
def update_asset_status_api(id: int, asset_status: str):
    return update_asset_status(id, asset_status)

@app.delete("/assets/{id}")
def delete_asset_api(id: int):
    return delete_asset(id)




# vendor master
@app.get("/vendors/list")
def get_data():
    return get_all_data() 


@app.get("/vendors/list/status")
def get_all_status(active_status: str):
    return get_data_by_status(active_status)


@app.get("/vendors/list/{id}")
def get_data_id(id:int):
    return get_data_by_id(id)


@app.post("/vendors/create")
def create_vendor_api(vendor: VendorMaster):
    return create_vendor(vendor)


@app.put("/vendors/{id}")
def update_vendor_api(id: str, vendor: VendorMaster):
    return update_vendor(id, vendor)

@app.patch("/vendors/{id}/status")
def update_vendor_status_api(id: str, status: str):
    return update_vendor_status(id, status)

@app.delete("/vendors/{id}")
def delete_vendor_api(id: str):
    return delete_vendor(id)

@app.get("/vendors/filter")
def filter_vendors(column: str, keyword: str):
    return get_rows_by_column(column, keyword)
@app.get("/vendors/count")
def count_vendors_api():
    return {"total_vendors": count_vendors()}




@app.post("/maintenance/create")
def create_maintenance_api(log: MaintenanceLog):
    return create_maintenance(log)

@app.get("/maintenance/list")
def list_maintenance_api():
    return list_maintenance()

@app.get("/maintenance/list/status")
def list_maintenance_status_api(status: str):
    return list_maintenance_by_status(status)

@app.get("/maintenance/{id}")
def get_maintenance_api(id: int):
    return get_maintenance_by_id(id)

@app.put("/maintenance/{id}")
def update_maintenance_api(id: int, row: dict):
    return update_maintenance(id, row)

@app.patch("/maintenance/{id}/status")
def update_maintenance_status_api(id: int, status: str):
    return update_maintenance_status(id, status)

@app.delete("/maintenance/{id}")
def delete_maintenance_api(id: int):
    return delete_maintenance(id)


# employeee

@app.post("/employees/create")
def add_employee(emp: EmployeeDirectory):
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
def update_employee(id: int, emp: EmployeeDirectory):
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
