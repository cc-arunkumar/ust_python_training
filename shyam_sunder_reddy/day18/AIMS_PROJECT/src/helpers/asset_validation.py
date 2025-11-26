from models import asset_model

def validate(asset: asset_model.Asset):

    # Allowed values for asset status and type
    allowed_asset_status = ['available', 'assigned', 'repair', 'retired']
    asset_type_allowed = ['laptop', 'monitor', 'docking station', 'keyboard', 'mouse']

    # 1. Validate asset status
    if asset.asset_status.lower() not in allowed_asset_status:
        print(f"Invalid Asset Status {asset.asset_status}")
        return False

    # 2. Validate asset tag format (must start with 'UST-')
    if asset.asset_tag[0:4] != 'UST-':
        print(f"Invalid Asset Tag {asset.asset_tag}")
        return False

    # 3. Warranty must be greater than 0
    if int(asset.warranty_years) <= 0:
        print("Warranty must be greater than 0")
        return False

    # 4. If status is 'available' or 'retired', assigned_to must be empty
    if asset.asset_status.lower() in ['available', 'retired'] and asset.assigned_to != "":
        print("Assigned_to must be Null")
        return False

    # 5. If status is 'assigned', assigned_to must not be empty
    if asset.asset_status.lower() == "assigned" and asset.assigned_to == "":
        print("Assigned_to must not be Null")
        return False

    # 6. Validate asset type
    if asset.asset_type.lower() not in asset_type_allowed:
        print("Invalid Asset Type")
        return False

    # If all checks pass
    return True


# -------------------------------
# Sample Usage
# -------------------------------
# from datetime import date, datetime

# Valid asset example
# valid_asset = asset_model.Asset(
#     asset_tag="UST-1001",
#     asset_type="Laptop",
#     serial_number="SN123456789",
#     manufacturer="Dell",
#     model="Latitude 5420",
#     purchase_date=date(2023, 5, 20),
#     warranty_years=3,
#     assigned_to="Shyam Sunder",
#     asset_status="Assigned",
#     last_updated=datetime.now()
# )

# Invalid asset example (wrong tag and status)
# invalid_asset = asset_model.Asset(
#     asset_tag="AST-9999",   # Wrong prefix
#     asset_type="Tablet",    # Not in allowed list
#     serial_number="SN987654321",
#     manufacturer="Apple",
#     model="iPad Pro",
#     purchase_date=date(2023, 6, 1),
#     warranty_years=0,       # Invalid warranty
#     assigned_to="",         # Invalid for 'Assigned'
#     asset_status="Assigned",
#     last_updated=datetime.now()
# )

# print("Valid Asset Check:", validate(valid_asset))
# print("Invalid Asset Check:", validate(invalid_asset))

# -------------------------------
# Expected Output
# -------------------------------
# Valid Asset Check: True
# Invalid Asset Tag AST-9999
# Warranty must be greater than 0
# Assigned_to must not be Null
# Invalid Asset Type
# Invalid Asset Check: False
