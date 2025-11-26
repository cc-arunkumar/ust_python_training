import sys, os

# Add project root → AIMS_PROJECT/ (to allow absolute imports for src/)
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

import pymysql
# Import CRUD functions from asset_crud
from src.crud.asset_crud import create_asset,read_all_assets,update_asset,read_asset_by_id, delete_asset_by_id

def main():
    # Create sample assets (inserting into DB)
    create_asset('UST-MNT-0002', 'Monitor', 'SN-LG-7719231', 'LG', 'UltraWide 29WL500', '2022-10-10', 2, None, 'Available', None)
    create_asset ('UST-KEY-0003', 'Keyboard', 'SN-HP-6612321', 'HP', 'HP Wired 160', '2023-05-01', 1, None, 'Available', None)
    create_asset('UST-LTP-0004', 'Laptop', 'SN-LN-1234987', 'Lenovo', 'ThinkPad E15', '2022-05-11', 3, 'Rohit Sharma (UST Bangalore)', 'Assigned', None)
    create_asset('UST-DCK-0005', 'Docking Station', 'SN-DL-5543123', 'Dell', 'Dell D6000', '2021-11-20', 3, 'Anjali Nair (UST Trivandrum)', 'Assigned', None)
    create_asset('UST-MNT-0006', 'Monitor', 'SN-SAM-9834567', 'Samsung', 'Samsung S24R350', '2023-03-12', 2, 'Vivek Reddy (UST Hyderabad)', 'Assigned', None)
    create_asset('UST-LTP-0007', 'Laptop', 'SN-HP-8834129', 'HP', 'HP ProBook 440 G8', '2021-09-18', 3, None, 'Repair', None)
    create_asset('UST-MNT-0008', 'Monitor', 'SN-LG-9925511', 'LG', 'LG 24MK600', '2019-08-12', 3, None, 'Retired', None)
    
    # Fetch and print all asset records
    read_all_assets()

    # Read a single asset by ID
    read_asset_by_id(13)

    # Update an asset (ID: 8)
    update_asset(8, 'UST-MNT-0008', 'Monitor', 'SN-LG-9925511', 'Lenovo', 'LG 24MK600', '2025-08-12', 3, None, 'Retired')

    # Delete an asset (ID: 1)
    delete_asset_by_id(1)

# Entry point check
if __name__=="__main__":
    main()
