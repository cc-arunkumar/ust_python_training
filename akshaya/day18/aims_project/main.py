from src.crud.asset_crud import (
    create_asset,
    read_all_assets,
    read_asset_by_id,
    update_asset,
    delete_asset
)

def main():

    print("\n--- CREATE ASSET ---")
    # Create a new asset record in the inventory
    create_asset(
        asset_tag="UST-LTP-0100",
        asset_type="Laptop",
        serial_number="SN-NEW-0000100",
        manufacturer="Dell",
        model="Latitude 5520",
        purchase_date="2024-01-10",
        warranty_years=3,
        assigned_to=None,                 # Asset not assigned to anyone initially
        asset_status="Available"          # Asset marked as available
    )

    print("\n--- READ ALL ASSETS (ALL) ---")
    # Fetch and display all asset records regardless of status
    read_all_assets("ALL")

    print("\n--- READ ALL ASSETS (Assigned only) ---")
    # Fetch and display only assets that are currently assigned
    read_all_assets("Assigned")

    print("\n--- READ ASSET BY ID ---")
    # Fetch and display details of asset with ID 1
    read_asset_by_id(1)
    # Attempt to read an invalid ID to demonstrate error handling
    read_asset_by_id("abc")

    print("\n--- UPDATE ASSET ---")
    # Update an existing asset record (ID = 1) with new details
    update_asset(
        asset_id=1,
        asset_type="Monitor",                     # Changing asset type
        manufacturer="LG",
        model="UltraWide 29WL500",
        warranty_years=2,
        asset_status="Assigned",                  # Marking asset as assigned
        assigned_to="John Doe (UST Pune)"         # Assigning asset to a user
    )

    print("\n--- DELETE ASSET ---")
    # Delete asset with valid ID (1)
    delete_asset(1)
    # Attempt to delete a non-existing asset to showcase handling
    delete_asset(9999)


if __name__ == "__main__":
    # Entry point for script execution
    main()
