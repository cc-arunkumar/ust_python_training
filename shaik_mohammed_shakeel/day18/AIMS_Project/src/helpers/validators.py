# Validators.py

from typing import Optional

# Function to validate asset details
def validate_asset(conn, asset_tag: str, asset_type: str, serial_number: str, manufacturer: str, model: str, purchase_date: str, warranty_years: int, assigned_to: Optional[str], asset_status: str):
    # Check if asset_tag starts with 'UST-', raising an error if not
    if not asset_tag.startswith("UST-"):
        raise ValueError("asset_tag must start with 'UST-'")
    
    # List of valid asset types
    valid_types = ["Laptop", "Monitor", "Docking Station", "Keyboard", "Mouse"]
    
    # Validate that the provided asset_type is one of the valid options
    if asset_type not in valid_types:
        raise ValueError(f"asset_type must be one of {valid_types}")
    
    # Validate warranty_years to ensure it is greater than zero
    if warranty_years <= 0:
        raise ValueError(f"Warranty_years should be greater than zero")
    
    # If asset_status is "Assigned", assigned_to must not be null
    if asset_status == "Assigned" and not assigned_to:
        raise ValueError("assigned_to must NOT be null when asset_status is 'Assigned'")
    
    # If asset_status is "Available" or "Retired", assigned_to must be null
    if asset_status in ["Available", "Retired"] and assigned_to is not None:
        raise ValueError("assigned_to must be null when asset_status is 'Available' or 'Retired'")
    
    # Query the database to check if the asset_tag or serial_number already exists in the system
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM asset_inventory WHERE asset_tag = %s OR serial_number = %s", (asset_tag, serial_number))
    existing_asset = cursor.fetchone()
    
    # If an existing asset is found with the same asset_tag or serial_number, raise an error
    if existing_asset:
        raise ValueError("asset_tag or serial_number already exists.")
