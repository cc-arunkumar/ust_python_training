import re

# Lists to track uniqueness of serial numbers and asset tags
serial_number_list=[]
asset_tag_list=[]

def validate_asset_tag(asset_tag):
    # Asset tag must start with "UST-"
    if not asset_tag.startswith("UST-"):
        raise ValueError("Asset name should starts with UST-")
    # Asset tag must be unique
    if asset_tag in asset_tag_list:
        raise ValueError("Asset tag name should be unique")
    
    asset_tag_list.append(asset_tag)    
    return asset_tag

    
def validate_asset_type(asset_type):
    # Allowed types for assets
    asset_type_list=["Laptop", "Monitor", "Docking Station", "Keyboard", "Mouse"]
    # Validate type is within allowed list
    if asset_type not in asset_type_list:
        raise ValueError("Asset type should be comes under a specfic type")
    return asset_type
    
def validate_serial_number(serial_number):
    # Serial number must be unique
    if serial_number in serial_number_list:
        raise ValueError("serial number sgould be uniquie")
    serial_number_list.append(serial_number)
    return serial_number

def validate_warrenty_years(warrenty_year):
    # Warranty should be a positive integer
    if warrenty_year<=0:
        raise ValueError("The warrenty year should be greater than zero")
    return warrenty_year


def validate_asset_status(asset_status,assigned_to):
    # Assigned → assigned_to cannot be null
    if asset_status=="Assigned" and assigned_to==None:
        raise ValueError("asset_status = Assigned → assigned_to must NOT be null")
    # Available/Retired → assigned_to must be null
    if  (asset_status=="Available" or asset_status=="Retired") and assigned_to!=None:
        raise ValueError("asset_status = Available/Retired → assigned_to MUST be null")
    return asset_status,assigned_to
