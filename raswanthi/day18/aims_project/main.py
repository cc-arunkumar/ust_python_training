"""
-------
Exercises all CRUD functions for the Asset Inventory Management System.

Steps:
1. Read all assets (ALL + filtered).
2. Create new assets (Available + Assigned).
3. Read asset by ID.
4. Update asset (change status, assigned_to, etc.).
5. Delete asset.
6. Read all assets again to confirm changes.
"""

from src.crud.asset_crud import (
    create_asset,
    read_all_assets,
    read_asset_by_id,
    update_asset,
    delete_asset,
)


def crud_operations():

    print("\n---- Read all the assets ----")
    read_all_assets("ALL")
    
    print("\n---- Read all the assets ----")
    read_all_assets("Available")

  
    print("\n---- Create new assets ----")
    create_asset(
        asset_tag="UST-KEY-0100",
        asset_type="Keyboard",
        serial_number="SN-NEW-KEY-0100",
        manufacturer="HP",
        model="HP Wired 160",
        purchase_date="2024-02-10",
        warranty_years=2,
        asset_status="Available",
        assigned_to=None,
    )

    print("\n---- Create new assets ----")
    create_asset(
        asset_tag="UST-LTP-0101",
        asset_type="Laptop",
        serial_number="SN-NEW-LTP-0101",
        manufacturer="Dell",
        model="Latitude 5540",
        purchase_date="2024-06-01",
        warranty_years=3,
        asset_status="Assigned",
        assigned_to="Priya Verma (UST Pune)",
    )

   
    print("\n---- Read asset by ID ----")
    read_asset_by_id(1)


    print("\n---- Update asset ----")
    update_asset(
        asset_id=1,
        asset_status="Assigned",
        assigned_to="Arjun Mehta (UST Bangalore)",
    )

    print("\n---- Update asset ----")
    update_asset(
        asset_id=1,
        asset_status="Repair",
        assigned_to=None,
    )

    print("\n---- Update asset ----")
    update_asset(
        asset_id=1,
        asset_status="Retired",
        assigned_to=None,
    )

    
    print("\n---- Delete asset ----")
    delete_asset(1)


    print("\n--- Read all finally ---")
    read_all_assets("ALL")

print(crud_operations())
