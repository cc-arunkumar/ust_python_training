from src.crud.asset_crud import create_asset, read_all_assets, read_asset_by_id, update_asset, delete_asset_by_id

def demo():
    # Create a new asset
    create_asset("UST-LTP-112", "Laptop", "SN-TEST-124", "Dell", "Latitude 5520", "2023-11-01", 3, None, "Available")

    # Read all assets
    read_all_assets("ALL")

    # Read asset by ID
    read_asset_by_id(2)

    # Update asset details
    update_asset(3, asset_type="Monitor", manufacturer="LG", model="UltraWide 29WL500",
                 warranty_years=2, asset_status="Repair", assigned_to=None)

    # Delete asset by ID
    delete_asset_by_id(2)

# Run demo if executed directly
if __name__ == "__main__":
    demo()

#Sample Execution
# Asset created successfully with ID: 1
# ID: 1 | TAG: UST-LTP-0099 | TYPE: Laptop | SERIAL: SN-TEST-123 | MANUFACTURER: Dell | MODEL: Latitude 552Connection closed successfully !
# Asset not found.

# Asset created successfully with ID: 3
# ID: 1 | TAG: UST-LTP-0099 | TYPE: Monitor | SERIAL: SN-TEST-123 | MANUFACTURER: LG | MODEL: UltraWide 29WL500 | 
# PURCHASE_DATE: 2023-11-01 | WARRANTY: 2 | ASSIGNED_TO: None | STATUS: Repair | LAST_UPDATED: 2025-11-26 16:49:53ID: 3 | TAG: UST-LTP-112 | TYPE: Laptop | SERIAL: SN-TEST-124 | MANUFACTURER: Dell | MODEL: Latitude 5520 | PURCHASE_DATE: 2023-11-01 | WARRANTY: 3 | ASSIGNED_TO: None | STATUS: Available | LAST_UPDATED: 2025-11-26 17:32:05 
# Connection closed successfully !
# Asset not found.