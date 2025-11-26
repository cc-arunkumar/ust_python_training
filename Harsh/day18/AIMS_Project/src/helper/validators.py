def validate_asset_tag(asset_tag):
    if not asset_tag.startswith("UST-"):
        raise ValueError("asset_tag must start with 'UST-'")
    return True

def validate_asset_type(asset_type):
    valid_types = ["Laptop", "Monitor", "Docking Station", "Keyboard", "Mouse"]
    if asset_type not in valid_types:
        raise ValueError(f"asset_type must be one of {valid_types}")
    return True

def validate_warranty(warranty_years):
    if warranty_years <= 0:
        raise ValueError("warranty_years must be greater than 0")
    return True

def validate_status_and_assignment(asset_status, assigned_to):
    if asset_status in ["Available", "Retired"] and assigned_to is not None:
        raise ValueError(f"assigned_to must be NULL when asset_status is '{asset_status}'")
    if asset_status == "Assigned" and assigned_to is None:
        raise ValueError("assigned_to must NOT be NULL when asset_status is 'Assigned'")
    return True
