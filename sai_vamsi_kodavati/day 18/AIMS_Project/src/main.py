# Main.py

# Importing necessary functions from asset_crud to perform CRUD operations on assets
from crud.asset_crud import read_all_assets, create_asset, read_asset_by_id, update_asset, delete_asset

# Creating assets with details like asset_tag, asset_type, serial_number, manufacturer, model, purchase_date, warranty_years, assigned_to, and asset_status
create_asset('UST-LTP-0001', 'Laptop', 'SN-DL-9988123', 'Dell', 'Latitude 5520', '2023-01-15', 3, None, 'Available')
# Sample Output: Asset created with asset_tag 'UST-LTP-0001' and status 'Available'.

create_asset('UST-MNT-0002', 'Monitor', 'SN-LG-7719231', 'LG', 'UltraWide 29WL500', '2022-10-10', 2, None, 'Available')
# Sample Output: Asset created with asset_tag 'UST-MNT-0002' and status 'Available'.

create_asset('UST-KEY-0003', 'Keyboard', 'SN-HP-6612321', 'HP', 'HP Wired 160', '2023-05-01', 1, None, 'Available')
# Sample Output: Asset created with asset_tag 'UST-KEY-0003' and status 'Available'.

create_asset('UST-LTP-0004', 'Laptop', 'SN-LN-1234987', 'Lenovo', 'ThinkPad E15', '2022-05-11', 3, 'Rohit Sharma (UST Bangalore)', 'Assigned')
# Sample Output: Asset created with asset_tag 'UST-LTP-0004' and status 'Assigned' to 'Rohit Sharma (UST Bangalore)'.

create_asset('UST-DCK-0005', 'Docking Station', 'SN-DL-5543123', 'Dell', 'Dell D6000', '2021-11-20', 3, 'Anjali Nair (UST Trivandrum)', 'Assigned')
# Sample Output: Asset created with asset_tag 'UST-DCK-0005' and status 'Assigned' to 'Anjali Nair (UST Trivandrum)'.

create_asset('UST-MNT-0006', 'Monitor', 'SN-SAM-9834567', 'Samsung', 'Samsung S24R350', '2023-03-12', 2, 'Vivek Reddy (UST Hyderabad)', 'Assigned')
# Sample Output: Asset created with asset_tag 'UST-MNT-0006' and status 'Assigned' to 'Vivek Reddy (UST Hyderabad)'.

create_asset('UST-LTP-0007', 'Laptop', 'SN-HP-8834129', 'HP', 'HP ProBook 440 G8', '2021-09-18', 3, None, 'Repair')
# Sample Output: Asset created with asset_tag 'UST-LTP-0007' and status 'Repair'.

create_asset('UST-MNT-0008', 'Monitor', 'SN-LG-9925511', 'LG', 'LG 24MK600', '2019-08-12', 3, None, 'Retired')
# Sample Output: Asset created with asset_tag 'UST-MNT-0008' and status 'Retired'.

# Reading all asset records from the system
read_all_assets()
# Sample Output: 
# 1. 'UST-LTP-0001' - Laptop - Available
# 2. 'UST-MNT-0002' - Monitor - Available
# 3. 'UST-KEY-0003' - Keyboard - Available
# 4. 'UST-LTP-0004' - Laptop - Assigned to 'Rohit Sharma (UST Bangalore)'
# 5. 'UST-DCK-0005' - Docking Station - Assigned to 'Anjali Nair (UST Trivandrum)'
# 6. 'UST-MNT-0006' - Monitor - Assigned to 'Vivek Reddy (UST Hyderabad)'
# 7. 'UST-LTP-0007' - Laptop - Repair
# 8. 'UST-MNT-0008' - Monitor - Retired

# Reading a specific asset by its ID
read_asset_by_id(1)
# Sample Output: Asset with ID 1 - 'UST-LTP-0001' - Laptop - Available

# Updating an asset (Details for the update would need to be specified based on requirements)
update_asset()
# Sample Output: Asset with ID 1 successfully updated.

# Deleting an asset by its ID
delete_asset(3)
# Sample Output: Asset with ID 3 (UST-KEY-0003) deleted successfully.

# Reading all asset records again after deletion
read_all_assets()
# Sample Output (after deletion of asset with ID 3):
# 1. 'UST-LTP-0001' - Laptop - Available
# 2. 'UST-MNT-0002' - Monitor - Available
# 3. 'UST-LTP-0004' - Laptop - Assigned to 'Rohit Sharma (UST Bangalore)'
# 4. 'UST-DCK-0005' - Docking Station - Assigned to 'Anjali Nair (UST Trivandrum)'
# 5. 'UST-MNT-0006' - Monitor - Assigned to 'Vivek Reddy (UST Hyderabad)'
# 6. 'UST-LTP-0007' - Laptop - Repair
# 7. 'UST-MNT-0008' - Monitor - Retired