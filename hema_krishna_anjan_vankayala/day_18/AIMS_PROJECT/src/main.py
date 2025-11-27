# Example script demonstrating CRUD calls (short comments only)
from crud import asset_crud 
from datetime import date

# Create two sample assets
asset_crud.create_asset_records(
    asset_tag="UST-LTP-0008",
    asset_type="Laptop",
    serial_number="SN-LN-9988123",
    manufacturer="Lenovo",
    model="ThinkPad T14",
    purchase_date=date(2022, 5, 10),
    warranty_years=3,
    asset_status="Available"
)

asset_crud.create_asset_records(
    asset_tag="UST-MNT-0009",
    asset_type="Monitor",
    serial_number="SN-SAM-7719231",
    manufacturer="Samsung",
    model="Samsung S24R350",
    purchase_date=date(2023, 3, 15),
    warranty_years=2,
    asset_status="Assigned",
    assigned_to="Priya Sharma (UST Pune)"
)

# Read and print all assets
asset_crud.read_all_assets()


# Fetch and print specific assets by id
asset_crud.read_asset_by_id(10)
asset_crud.read_asset_by_id(2)


# Update an asset (example)
asset_crud.update_asset(
    asset_id=10,
    asset_tag="UST-LTP-0007",
    asset_type="Laptop",
    serial_number="SN-HP-8834129",
    manufacturer="HP",
    model="HP ProBook 440 G8",
    purchase_date=date(2021, 9, 18),
    warranty_years=3,
    asset_status="Available",
    assigned_to="Vivek Reddy (UST Hyderabad)"
)

# Delete example assets
asset_crud.delete_asset_by_id(9)
asset_crud.delete_asset_by_id(2)
