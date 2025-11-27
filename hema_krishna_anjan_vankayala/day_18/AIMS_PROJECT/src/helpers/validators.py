
# Validation helpers for asset fields (short comments only)
def table_validations(tag,type,warranty,asset_status,assign_to=""):
    # allowed statuses and types
    allowed_asset_status = ['available','assigned','repair','retired']
    asset_type_allowed = ['laptop', 'monitor','docking station', 'keyboard', 'mouse']
    # check status
    if asset_status.lower() not in allowed_asset_status:
        return f"Invalid Asset Status {asset_status}"
    # check tag prefix
    if tag[0:4] != 'UST-':
        return f"Invalid Asset Tag {tag}"
    # check warranty > 0
    if int(warranty) <= 0 :
        return "Warranty must be greater than 0"
    # if available or retired, assign_to must be empty
    if asset_status.lower() in ['available','retired'] and assign_to != "":
        return "Assigned_to must be Null"
    # if assigned, assign_to must be provided
    if asset_status.lower() == "assigned" and assign_to == "":
        return "Assigned_to must not be Null"
    # check asset type
    if type.lower() not in asset_type_allowed:
        return "Invalid Asset Type"
    
    # all good
    return "Data is Valid"