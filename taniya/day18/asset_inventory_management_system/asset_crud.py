from fastapi import FastAPI
from pydantic import BaseModel,Field,validators
from datetime import datetime,date
from typing import Optional,Literal
import pymysql

app = FastAPI(title="Asset Inventory Management system")
def get_connection():
    conn=pymysql.connect(
        host="localhost",
        user="root",
        password="pass@word1",
        database="ust_asset_db"
    )
    return conn
class Create_asset(BaseModel):
    asset_id:int=0
    asset_tag:str=Field(...,min_length=5,max_length=50,regex=r'^UST-.*$')
    asset_type:Literal["Laptop","Monitor","Docking Station","Keyboard","Mouse"]
    serial_number:str=Field(...,min_length=1,max_length=100)
    manufacturer:str=Field(...,min_length=1,max_length=50)
    model:str=Field(...,min_length=1,max_length=100)
    purchase_date:date=Field(...)
    warranty_years:int=Field(...,gt=0)
    assigned_to:Optional[str]=Field(min_length=1,max_length=100)
    asset_status:Literal["Available","Assigned","Repair","Retired"]
    last_updated:datetime=Field(...)

def create_asset(asset):
    try:
        conn = get_connection()
        cursor=conn.cursor()
        cursor.execute(
    "INSERT INTO asset_inventory(asset_tag,asset_type,serial_number,manufacturer,model,purchase_date,warranty_years,assigned_to, asset_status, last_updated) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
        (
            asset.asset_tag,
            asset.asset_type,
            asset.serial_number,
            asset.manufacturer,
            asset.model,
            asset.purchase_date,
            asset.warranty_years,
            asset.assigned_to,
            asset.asset_status,
            datetime.now()   
        )
        )
        cursor.commit()
        return cursor.lastrowid
    finally:
        if conn:
            cursor.close()
            conn.close()
            
