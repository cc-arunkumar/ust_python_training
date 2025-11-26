def validate_asset(asset_tag,asset_type,warranty_years,assigned_to,asset_status):
    if not asset_tag.startswith("UST-"):
        return False
    
    allowed_types=["Laptop", "Monitor", "Docking Station", "Keyboard", "Mouse"]
    
    if asset_type not in allowed_types:
        return False
    if warranty_years<=0:
        return False
    
    if asset_status=="Assigned" and not assigned_to:
        return False
    
    if asset_status in ["Available", "Retired"] and assigned_to:
        return False
    
    allowed_status = ["Available", "Assigned", "Repair", "Retired"]
    if asset_status not in allowed_status:
        return False
    
    return True
    