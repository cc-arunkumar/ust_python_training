from pydantic import Field,model_validator,field_validator,
from typing import Optional



class AssetTag:
    asset_tag:str

class Asset:
    # asset_id:int
    asset_tag:str=Field(...)
    asset_type:Asset_type_enum()
    manufacturer:str
    model:str
    warranty_years:int
    asset_status:Asset_type_enum
    serial_number:str
    manufacturer:str
    
    
           
def update(asset_id,asset_type,
manufacturer,
model,
warranty_years,
asset_status,
assigned_to):
    try:
        conn=get_connection()
        cursor=conn.cursor()
        cursor.execute("update asset_inventory set ASSET_TYPE=%s ,MANUFACTURER=%s,MODEL=%s,ASSET_STATUS=%s,ASSIGNED_TO=%s",(asset_type,manufacturer,model,warranty_years,asset_status,assigned_to))
        
   
 
def read_all_users():
    try:
        conn=get_connection()
        cursor=conn.cursor()
        cursor.execute("select * from asset_inventory;")
        rows=cursor.fetchall()
        print(rows)
        # conn.commit()
        print("executed")
    except Exception as e:
        print("Error ",e)
    finally:
        if conn.open:
            conn.close()
            cursor.close()
            print("closing the database ")
            
def read_user_by_id(id):
    try:
        conn=get_connection()
        cursor=conn.cursor()
        cursor.execute("select * from asset_inventory where asset_id=%s;",(id,))
        rows=cursor.fetchone()
        print(rows)
    except Exception as e:
        print("Error ",e)
    finally:
        if conn.open:
            conn.close()
            cursor.close()
            print("closing the database ")
        
def update(asset_id,asset_type,
manufacturer,
model,
warranty_years,
asset_status,
assigned_to):
    try:
        conn=get_connection()
        cursor=conn.cursor()
        cursor.execute("update asset_inventory set ASSET_TYPE=%s ,MANUFACTURER=%s,MODEL=%s,ASSET_STATUS=%s,ASSIGNED_TO=%s",(asset_type,manufacturer,model,warranty_years,asset_status,assigned_to))
        
        
    


       
# create_asset('UST-LTP-0021', 'Laptop', 'SN-DL-0988123', 'Dell', 'Latitude 5520', '2023-01-15', 3,None, 'Available')
# read_all_users()
# read_user_by_id(1)


# asset_tag,
# asset_type,
# serial_number,
# manufacturer,
# model,
# purchase_date,
# warranty_years,
# assigned_to,
# asset_status