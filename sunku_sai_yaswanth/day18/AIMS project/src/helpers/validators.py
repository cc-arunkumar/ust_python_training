# validators
from typing import Optional
 
 
def validate_asset(conn,asset_tag: str, asset_type: str, serial_number: str, manufacturer: str, model: str, purchase_date: str, warranty_years: int, assigned_to:Optional[str], asset_status: str):
    if not asset_tag.startswith("UST-"):
        raise ValueError("asset_tag must start with 'UST-'")
   
    valid_types=["Laptop", "Monitor", "Docking Station","Keyboard", "Mouse"]
    if asset_type not in valid_types:
        raise ValueError(f"asset_type must be one of {valid_types}")
   
    if warranty_years <= 0:
        raise ValueError(f"Warranty_years should be greater than zero")
   
    if asset_status == "Assigned" and not assigned_to:
        raise ValueError("assigned_to must NOT be null when asset_status is 'Assigned'")
   
    if asset_status in ["Available", "Retired"] and assigned_to is not None:
        raise ValueError("assigned_to must be null when asset_status is 'Available' or 'Retired'")
   
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM asset_inventory WHERE asset_tag = %s OR serial_number = %s", (asset_tag, serial_number))
    existing_asset = cursor.fetchone()
    if existing_asset:
        raise ValueError("asset_tag or serial_number already exists.")