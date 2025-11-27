import aims_crud

# Sample data to insert into the asset database
data = [
    ('UST-LTP-0001', 'Laptop', 'SN-DL-9988123', 'Dell', 'Latitude 5520', '2023-01-15', 3, None, 'Available'),
    ('UST-MNT-0002', 'Monitor', 'SN-LG-7719231', 'LG', 'UltraWide 29WL500', '2022-10-10', 2, None, 'Available'),
    ('UST-KEY-0003', 'Keyboard', 'SN-HP-6612321', 'HP', 'HP Wired 160', '2023-05-01', 1, None, 'Available'),
    ('UST-LTP-0004', 'Laptop', 'SN-LN-1234987', 'Lenovo', 'ThinkPad E15', '2022-05-11', 3, 'Rohit Sharma (UST Bangalore)', 'Assigned'),
    ('UST-DCK-0005', 'Docking Station', 'SN-DL-5543123', 'Dell', 'Dell D6000', '2021-11-20', 3, 'Anjali Nair (UST Trivandrum)', 'Assigned'),
    ('UST-MNT-0006', 'Monitor', 'SN-SAM-9834567', 'Samsung', 'Samsung S24R350', '2023-03-12', 2, 'Vivek Reddy (UST Hyderabad)', 'Assigned'),
    ('UST-LTP-0007', 'Laptop', 'SN-HP-8834129', 'HP', 'HP ProBook 440 G8', '2021-09-18', 3, None, 'Repair'),
    ('UST-MNT-0008', 'Monitor', 'SN-LG-9925511', 'LG', 'LG 24MK600', '2019-08-12', 3, None, 'Retired')
]

# ----------------- Inserting Assets ----------------
print("\n************* Inserting Assets ***********")
for item in data:
    aims_crud.create_asset(item)  # Calls the `create_asset` function to insert each asset

# ----------------- Read All Assets ----------------
print("\n************* Read ALL assets ***********")
aims_crud.read_all_assets()  # Calls the `read_all_assets` function to get all asset records

# ----------------- Read Available Assets ----------------
print("\n************* Read Available assets ***********")
aims_crud.read_all_assets("Available")  # Filters the assets to display only those with status 'Available'

# ----------------- Read Asset by ID ----------------
print("\n************* Read asset by ID = 3 ***********")
aims_crud.read_asset(3)  # Fetches the asset record with asset_id = 3

# ----------------- Update Asset ----------------
print("\n************* Update Asset ID = 3 ***********")
updated_data = (
    'UST-LTP-0999', 'Laptop', 'SN-HP-NEW9911', 'HP', 'HP EliteBook 845',  # New asset details
    '2023-06-01', 2, None, 'Available'  # Warranty of 2 years, status 'Available'
)
aims_crud.update_asset(3, updated_data)  # Calls the `update_asset` function to update the asset with ID = 3

# ----------------- Delete Asset ----------------
# Check if the asset with ID = 5 exists
print("\n************* Delete Asset ID = 5 ***********")
asset = aims_crud.read_asset(5)  # Check if asset with ID 5 exists
if asset:  # If asset exists, delete it
    aims_crud.delete_asset(5)  # Delete the asset with ID = 5
else:
    print("Asset with ID 5 does not exist.")  # If asset does not exist, print a message

# ----------------- Final List of Assets ----------------
print("\n************* Final List ***********")
aims_crud.read_all_assets()  # Fetches and displays all the remaining assets
