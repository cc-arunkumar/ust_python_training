def validate_asset_tag(asset_tag: str) -> None:
    # Ensure asset_tag follows required company prefix format
    if not asset_tag.startswith("UST-"):
        raise ValueError("asset_tag must start with 'UST-'")

def validate_asset_type(asset_type: str) -> None:
    # Allowed asset categories for inventory standardization
    allowed = ["Laptop", "Monitor", "Docking Station", "Keyboard", "Mouse"]
    # Validate that the provided asset type is within the allowed list
    if asset_type not in allowed:
        raise ValueError(f"asset_type must be one of {allowed}")

def validate_warranty_years(warranty_years: int) -> None:
    # Warranty must be a positive integer value
    if not isinstance(warranty_years, int) or warranty_years <= 0:
        raise ValueError("warranty_years must be greater than 0")

def validate_status_and_assignment(asset_status: str, assigned_to) -> None:
    # Valid operational statuses for an asset
    allowed = ["Available", "Assigned", "Repair", "Retired"]
    # Validate asset_status against allowed values
    if asset_status not in allowed:
        raise ValueError(f"asset_status must be one of {allowed}")

    # If asset is Assigned, assigned_to must have a valid value (cannot be empty/null)
    if asset_status == "Assigned" and not assigned_to:
        raise ValueError("assigned_to must NOT be null when asset_status is 'Assigned'")
    # If asset is Available or Retired, it should not be assigned to anyone
    if asset_status in ["Available", "Retired"] and assigned_to is not None:
        raise ValueError("assigned_to must be NULL when asset_status is 'Available' or 'Retired'")

def validate_asset_id(asset_id) -> int:
    # Validate that asset_id can be converted to a valid integer
    try:
        asset_id_int = int(asset_id)
    except (TypeError, ValueError):
        raise ValueError("Invalid asset_id")
    # Ensure asset_id is a positive integer
    if asset_id_int <= 0:
        raise ValueError("Invalid asset_id")
    return asset_id_int  # Return validated integer ID for further use
