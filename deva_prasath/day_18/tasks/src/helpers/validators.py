import re
from datetime import datetime,date

# Validates that asset_tag starts with UST-
def validate_asset_tag(asset_tag):
    return bool(re.match(r"^UST-",asset_tag))


# Checks if the asset type is one of the allowed predefined categories
def validate_asset_type(asset_type):
    allowed_types=["Laptop","Monitor","Docking Station","Keyboard","Mouse"]
    return asset_type in allowed_types


# Ensures warranty years is greater than zero
def validate_warranty_years(warranty_years):
    return warranty_years>0


# Validates assigned_to value based on asset_status rules
def validate_assigned_to(asset_status, assigned_to):
    if asset_status in ["Available","Retired"]:
        return assigned_to is None          
    elif asset_status=="Assigned":
        return assigned_to is not None       
    return True

# Placeholder validation – always returns True for now
def validate_serial_number(serial_number):
    return True

# Validates purchase_date string format (YYYY-MM-DD)
def validate_date(date_str):
    try:
        datetime.strptime(date_str,"%Y-%m-%d")
        return True
    except ValueError:
        return False