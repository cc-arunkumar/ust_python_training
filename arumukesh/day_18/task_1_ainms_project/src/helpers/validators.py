import re
# unique_asset_tag=set()
# unique
def val_asset_tag(asset_tag):
    pattern=r"^UST"
    if re.match(pattern,asset_tag):
        return asset_tag
    raise ValueError("not valid status tag")


def val_asset_type(asset_type):
    allowed_types=("Laptop","Monitor","Docking Station","Keyboard","Mouse")
    
    if asset_type.title() not in allowed_types:
        raise ValueError("Not valid asset_type")
    return asset_type

def val_asset_status(asset_status):
    allowed_status=("Available","Assigned","Repair","Retired")
    if asset_status not in allowed_status:
        raise ValueError("invalid Asset status")   
    return asset_status 


        

    
# print(val_asset_tag("USTkfvwsh"))