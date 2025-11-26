def validate_asset(asset_tag, asset_type, warranty_years, assigned_to, asset_status):
    # Asset tag must start with "UST-"
    if not asset_tag.startswith("UST-"):
        return False
    
    # Allowed asset types
    allowed_types = ["Laptop", "Monitor", "Docking Station", "Keyboard", "Mouse"]
    if asset_type not in allowed_types:
        return False
    
    # Warranty must be positive
    if warranty_years <= 0:
        return False
    
    # Assigned assets must have a user
    if asset_status == "Assigned" and not assigned_to:
        return False
    
    # Available/Retired assets must not be assigned
    if asset_status in ["Available", "Retired"] and assigned_to:
        return False
    
    # Allowed status values
    allowed_status = ["Available", "Assigned", "Repair", "Retired"]
    if asset_status not in allowed_status:
        return False
    
    return True  # Valid asset