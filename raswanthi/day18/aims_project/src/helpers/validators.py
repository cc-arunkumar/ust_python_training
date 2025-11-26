# -----------------------------
# Allowed asset types and statuses
# -----------------------------
asset_type_list = ["Laptop", "Monitor", "Docking Station", "Keyboard", "Mouse"]
allowed_status = ["Available", "Assigned", "Repair", "Retired"]

# -----------------------------
# Function: validate_asset_tag
# Purpose: Ensure asset_tag is non-empty and follows naming convention
# -----------------------------
def validate_asset_tag(asset_tag: str):
    # Check for null or empty string
    if asset_tag is None or asset_tag.strip() == "":
        raise ValueError("asset_tag must be non-empty")
    # Must start with prefix "UST-"
    if not asset_tag.startswith("UST-"):
        raise ValueError("asset_tag must start with 'UST-'")

# -----------------------------
# Function: validate_asset_type
# Purpose: Ensure asset_type is one of the predefined valid types
# -----------------------------
def validate_asset_type(asset_type: str):
    if asset_type not in asset_type_list:
        raise ValueError(f"asset_type must be one of {asset_type_list}")

# -----------------------------
# Function: validate_serial_number
# Purpose: Ensure serial_number is non-empty
# -----------------------------
def validate_serial_number(serial_number: str):
    if serial_number is None or serial_number.strip() == "":
        raise ValueError("serial_number must be non-empty")

# -----------------------------
# Function: validate_warranty_years
# Purpose: Ensure warranty_years is a positive integer
# -----------------------------
def validate_warranty_years(warranty_years: int):
    # Must be an integer
    if not isinstance(warranty_years, int):
        raise ValueError("warranty_years must be an integer")
    # Must be greater than 0
    if warranty_years <= 0:
        raise ValueError("warranty_years must be greater than 0")

# -----------------------------
# Function: validate_asset_status
# Purpose: Ensure asset_status is valid and assigned_to rules are respected
# -----------------------------
def validate_asset_status(asset_status: str, assigned_to: str | None):
    # Check if status is in allowed list
    if asset_status not in allowed_status:
        raise ValueError(f"asset_status must be one of {allowed_status}")

    # Rule: If status is "Assigned", assigned_to must be non-empty
    if asset_status == "Assigned":
        if assigned_to is None or str(assigned_to).strip() == "":
            raise ValueError("assigned_to must NOT be null/empty when status is 'Assigned'")

    # Rule: If status is "Available" or "Retired", assigned_to must be null/empty
    elif asset_status in ["Available", "Retired"]:
        if assigned_to is not None and str(assigned_to).strip() != "":
            raise ValueError("assigned_to MUST be null when status is 'Available' or 'Retired'")
