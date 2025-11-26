from src.crud.asset_crud import create_asset, read_all_assets, read_asset_by_id, update_asset

def demo():
    create_asset("UST-LTP-0099", "Laptop", "SN-TEST-123", "Dell", "Latitude 5520","2023-11-01", 3, None, "Available")

    read_all_assets("ALL")

    read_asset_by_id(2)

    update_asset(2, asset_type="Monitor", manufacturer="LG", model="UltraWide 29WL500",
                 warranty_years=2, asset_status="Repair", assigned_to=None)

if __name__ == "__main__":
    demo()