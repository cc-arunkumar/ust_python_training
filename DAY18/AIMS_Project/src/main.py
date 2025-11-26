from crud.asset_crud import create_asset, read_all_assets, read_asset_by_id, update_asset, delete_asset

def run_demo():
    # Test all CRUD operations
    create_asset('UST-LTP-0010', 'Laptop', 'SN-HP-1234568', 'HP', 'HP EliteBook', '2023-09-01', 2, None, 'Available')
    read_all_assets()  # Print all assets in the DB
    read_asset_by_id(1)  # Read asset by ID
    update_asset(1, 'Laptop', 'HP', 'HP Spectre', 3, 'John Doe', 'Assigned')
    delete_asset(1)  # Delete an asset by ID

if __name__ == "__main__":
    run_demo()
