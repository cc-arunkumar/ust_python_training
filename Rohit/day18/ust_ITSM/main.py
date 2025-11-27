import datetime
import pymysql
from fastapi import FastAPI, HTTPException
from pydentic.asset_inventory_pydentic import Asset_inventory
from api.asset_inventory import get_task, get_task_by_id,update_asset,update_asset_status,delete_asset, get_assets_by_status,search_assets,count_assets
from db_connection.db import get_connection
app = FastAPI()
@app.post("/assets/create")
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
    
@app.get("/assets/{id}")
def get_assets_by_id(id: int):
    return get_task_by_id(id)

    
@app.get("/assets/list")
def list_assets(status: str):
    return {"assets": get_assets_by_status(status)}
@app.get("/assets/search")
def search_assets_api(keyword: str):
    return {"assets": search_assets(keyword)}

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

 