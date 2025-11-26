import asset_crud
# Sample payload for insertion
data = {
            "asset_tag": "UST-LTP-0001",
            "asset_type": "Laptop",
            "serial_number": "1234",
            "manufacturer": "",
            "model": "",
            "purchase_date": "2025-10-12",
            "warranty_years": 2025,
            "assigned_to": None,
            "asset_status": "Available"
        }

# asset_crud.create_asset(data)
# asset_crud.read_all_assets()
# asset_crud.read_asset_by_id(10)
# asset_crud.update_asset(10)
# asset_crud.delete_asset(10)

# output

# create asset
# Asset inserted successfully:
# Connection closed successfully

# read all assets
# Select filter
# 1.Available
# 3.Repair
# 4.Retired
# 5.ALL
# Enter choice:1
# ear 2025 | Assigned To: None | Asset Status: Available | Last Updated 2025-11-26 17:50:42

# reset asset by id
# ear 2025 | Assigned To: None | Asset Status: Available | Last Updated 2025-11-26 17:50:42
# Connection closed successfully

# update asset
# Asset updated successfully
# Connection closed successfully

# delete asset
# Asset ID: 10 | Asset Tag: UST-LTP-0001 | Asset Type: Laptop | Serial Number: 1234 | Manufacturer:  | Model: F15 | Purchase Date: 2025-10-12 | Warrenty_year 2025 | Assigned To: None | Asset Status: Available | Last Updated 2025-11-26 17:50:42
# Connection closed successfully
# Employee deleted successfully
# Connection closed successfully