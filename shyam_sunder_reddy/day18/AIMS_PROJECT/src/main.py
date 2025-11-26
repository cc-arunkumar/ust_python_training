# Import required modules
from crud import asset_crud          # CRUD operations for assets
from models import asset_model       # Asset model definition (Pydantic or dataclass)
from datetime import date, datetime  # For handling dates and timestamps
from helpers import asset_validation # Validation helper for asset data

# -------------------------------
# Create a sample Asset object
# -------------------------------
sample_asset = asset_model.Asset(
    asset_tag="UST-1001",            # Unique tag for the asset
    asset_type="Laptop",             # Type of asset
    serial_number="SN123456789",     # Serial number
    manufacturer="Dell",             # Manufacturer name
    model="Latitude 5420",           # Model name
    purchase_date=date(2023, 5, 20), # Date of purchase
    warranty_years=3,                # Warranty period in years
    assigned_to="Shyam Sunder",      # Person the asset is assigned to
    asset_status="Assigned",         # Current status of the asset
    last_updated=datetime.now()      # Timestamp of last update
)

# -------------------------------
# Validate the asset object
# -------------------------------
if not asset_validation.validate(sample_asset):
    print("The format is not correct")
else:
    # If validation passes, fetch all assets from DB
    asset_crud.get_all_assets()

# -------------------------------
# CREATE operation
# -------------------------------
# asset_crud.create_asset(sample_asset)
# Expected Output:
# Asset added successfully!

# asset_crud.get_all_assets()
# Expected Output (table view):
# asset_tag | asset_type | serial_number | manufacturer | model | purchase_date | warranty_years | assigned_to | asset_status | last_updated
# 1  | UST-LTP-0001 | Laptop   | SN-DL-9988123 | Dell    | Latitude 5520 | 2023-01-15 | 3 | None | Available | 2025-11-26 15:08:54
# 2  | UST-MNT-0002 | Monitor  | SN-LG-7719231 | LG      | UltraWide 29WL500 | 2022-10-10 | 2 | None | Available | 2025-11-26 15:08:54
# ...
# 11 | AST-1001     | Laptop   | SN123456789   | Dell    | Latitude 5420 | 2023-05-20 | 3 | Shyam Sunder | In Use | 2025-11-26 16:23:21

# -------------------------------
# READ operation (by ID)
# -------------------------------
# asset_crud.get_asset_by_id(11)
# Expected Output:
# asset_tag | asset_type | serial_number | manufacturer | model | purchase_date | warranty_years | assigned_to | asset_status | last_updated
# 11 | AST-1001 | Laptop | SN123456789 | Dell | Latitude 5420 | 2023-05-20 | 3 | Shyam Sunder | In Use | 2025-11-26 16:23:21

# -------------------------------
# UPDATE operation
# -------------------------------
# sample_asset2 = asset_model.Asset(
#     asset_tag="AST-1001",
#     asset_type="Laptop",
#     serial_number="SN123456789",
#     manufacturer="Dell",
#     model="Latitude 5420",
#     purchase_date=date(2023, 5, 20),
#     warranty_years=3,
#     assigned_to="ram",              # Updated assigned_to field
#     asset_status="In Use",
#     last_updated=datetime.now()
# )
# asset_crud.update_asset_by_id(11, sample_asset2)
# asset_crud.get_asset_by_id(11)
# Expected Output (before update):
# 11 | AST-1001 | Laptop | SN123456789 | Dell | Latitude 5420 | 2023-05-20 | 3 | Shyam Sunder | In Use | 2025-11-26 16:23:21
# Expected Output (after update):
# 11 | AST-1001 | Laptop | SN123456789 | Dell | Latitude 5420 | 2023-05-20 | 3 | ram | In Use | 2025-11-26 16:27:07

# -------------------------------
# DELETE operation
# -------------------------------
# asset_crud.get_asset_by_id(11)
# asset_crud.delete_asset_by_id(11)
# asset_crud.get_asset_by_id(11)
# Expected Output (before delete):
# 11 | AST-1001 | Laptop | SN123456789 | Dell | Latitude 5420 | 2023-05-20 | 3 | ram | In Use | 2025-11-26 16:27:07
# Expected Output (delete confirmation):
# Asset Record Deleted successfully
# Expected Output (after delete):
# ID NOT FOUND
