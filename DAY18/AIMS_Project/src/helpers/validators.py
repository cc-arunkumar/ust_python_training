def validate_asset_tag(asset_tag):
    """Validate asset tag starts with 'UST-'"""
    return asset_tag.startswith("UST-")

def validate_asset_type(asset_type):
    """Validate that the asset type is one of the predefined values."""
    types = ["Laptop", "Monitor", "Keyboard", "Mouse", "Docking Station"]
    return asset_type in types

def validate_warranty_years(warranty_years):
    """Ensure warranty years is greater than 0."""
    return warranty_years > 0

def validate_status(asset_status):
    """Validate that the asset status is valid."""
    statuses = ["Available", "Assigned", "Repair", "Retired"]
    return asset_status in statuses

def validate_assignment(asset_status, assigned_to):
    """Ensure assignment logic is valid based on the asset status."""
    if asset_status == "Assigned" and not assigned_to:
        return False
    if asset_status in ["Available", "Retired"] and assigned_to is not None:
        return False
    return True
