# from fastapi import FastAPI
from pydantic import BaseModel, Field, model_validator
from datetime import date, datetime
from enum import Enum
from typing import Optional,Literal
import pymysql
# app = FastAPI()
def get_connection():
     return pymysql.connect(
        host="localhost",
        user="root",
        password="pass@word1",
        database="ust_asset_db"
    )
    

class Status(str, Enum):
    available = "Available"
    assigned = "Assigned"
    repair = "Repair"
    retired = "Retired"

class AssetType(str, Enum):
    laptop = "Laptop"
    monitor = "Monitor"
    docking_station = "Docking Station"
    keyboard = "Keyboard"
    mouse = "Mouse"

class AssetInventory(BaseModel):
    asset_id: int = 0
    asset_tag: str = Field(..., min_length=1, max_length=50, pattern=r'^UST.*$')
    asset_type: AssetType
    serial_number: str = Field(..., min_length=1, max_length=100)
    manufacturer: str
    model: str = Field(..., min_length=1, max_length=100)
    purchase_date: date
    waranty_years: int = Field(gt=0)
    assigned_to: Optional[str]
    asset_status: Status
    last_updated: datetime = Field(default_factory=datetime.now)

    @model_validator(mode="after")
    def validate_business_rules( self):
        if self.asset_status in [Status.available, Status.retired] and self.assigned_to is not None:
            raise ValueError("assigned_to must be NULL if asset_status = Available or Retired")
        if self.asset_status == Status.assigned and self.assigned_to is None:
            raise ValueError("assigned_to must NOT be NULL if asset_status = Assigned")
        return self
 

def create_task(asset_tag, asset_type, serial_number, manufacturer, model,
                purchase_date, waranty_years, assigned_to, asset_status):
    try:

        conn = get_connection()
        cursor = conn.cursor()
        last_updated = datetime.now()
        cursor.execute("""
            INSERT INTO asset_inventory 
            (asset_tag, asset_type, serial_number, manufacturer, model, purchase_date, 
             waranty_years, assigned_to, asset_status, last_updated)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (asset_tag, asset_type, serial_number, manufacturer, model,
              purchase_date, waranty_years, assigned_to, asset_status, last_updated))

        conn.commit()
        print("Asset record created successfully")

    except Exception as e:
        print("Error:", e)
    finally:
        if conn:
            cursor.close()
            conn.close()
def read_asset_by_id(asset_id):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("select * from asset_inventory where asset_id=%s",(asset_id))
        row = cursor.fetchone()
        print(row)
    except Exception as e:
        print("error is", e)
    finally:
        if conn:
            cursor.close()
            conn.close()
        

def read_all_assets(status_filter="ALL"):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        if status_filter == "ALL":
            query = "SELECT * FROM asset_inventory ORDER BY asset_id ASC"
            cursor.execute(query)
        else:
            query = "SELECT * FROM asset_inventory WHERE asset_status = %s ORDER BY asset_id ASC"
            cursor.execute(query, (status_filter,))

        rows = cursor.fetchall()

        if not rows:
            print("No assets found.")
        else:
            for row in rows:
            
                print(
                    f"ID: {row[0]}, Tag: {row[1]}, Type: {row[2]}, Serial: {row[3]}, "
                    f"Manufacturer: {row[4]}, Model: {row[5]}, Purchase Date: {row[6]}, "
                    f"Warranty: {row[7]}, Assigned To: {row[8]}, Status: {row[9]}, Last Updated: {row[10]}"
                )

    except Exception as e:
        print("Error:", e)
    finally:
        if conn:
            cursor.close()
            conn.close()
        
# create_task(
#     asset_tag="UST-LTP-000293",
#     asset_type="Laptop",
#     serial_number="SN123456789",
#     manufacturer="Dell",
#     model="Latitude 5520",
#     purchase_date="2025-11-26",
#     waranty_years=3,
#     assigned_to=None,
#     asset_status="Available"
# )
# read_asset_by_id(1)

read_all_assets("Available")