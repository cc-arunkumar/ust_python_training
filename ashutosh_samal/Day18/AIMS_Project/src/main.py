from crud.asset_crud import create_asset, read_all_assets, read_asset_by_id, update_asset, delete_asset

def demo():
    # Create a new asset
    create_asset("UST-LTP-113", "Laptop", "SN-TEST-123", "Dell", "Latitude 5520", "2023-11-01", 3, None, "Available")

    # Read all assets
    read_all_assets("ALL")

    # Read asset by ID
    read_asset_by_id(2)

    # Update asset details
    update_asset(2, asset_type="Monitor", manufacturer="LG", model="UltraWide 29WL500",
                 warranty_years=2, asset_status="Repair", assigned_to=None)

    # Delete asset by ID
    delete_asset(2)

# Run demo if executed directly
if __name__ == "__main__":
    demo()

#Sample Execution
# Asset created successfully with ID: 2
# ID: 1 | TAG: UST-LTP-0001 | TYPE: Laptop | SERIAL: SN-DL-9988123 | MANUFACTURER: Dell | MODEL: Latitude 5520 | PURCHASE_DATE: 2023-01-15 | WARRANTY: 3 | ASSIGNED_TO: NULL | STATUS: Available | LAST_UPDATED: 2025-11-26 17:42:58
# ID: 2 | TAG: UST-LTP-113 | TYPE: Laptop | SERIAL: SN-TEST-123 | MANUFACTURER: Dell | MODEL: Latitude 5520 | PURCHASE_DATE: 2023-11-01 | WARRANTY: 3 | ASSIGNED_TO: None | STATUS: Available | LAST_UPDATED: 2025-11-26 22:11:43
# Connection closed successfully !
# ID: 2 | TAG: UST-LTP-113 | TYPE: Laptop | SERIAL: SN-TEST-123 | MANUFACTURER: Dell | MODEL: Latitude 5520 | PURCHASE_DATE: 2023-11-01 | WARRANTY: 3 | ASSIGNED_TO: None | STATUS: Available | LAST_UPDATED: 2025-11-26 22:11:43
# Asset has been deleted successfully
# Connection got closed