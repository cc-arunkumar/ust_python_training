import aims_project

# ---------------------- SAMPLE ASSET DATA ----------------------
# We are using tuples because aims_project expects asset data
# in the format:
# (asset_tag, asset_type, serial_number, manufacturer,
#  model, purchase_date, warranty_years, assigned_to, asset_status)

data = [
    ('UST-LTP-0001', 'Laptop', 'SN-DL-9988123', 'Dell', 'Latitude 5520',
     '2023-01-15', 3, None, 'Available'),

    ('UST-MNT-0002', 'Monitor', 'SN-LG-7719231', 'LG', 'UltraWide 29WL500',
     '2022-10-10', 2, None, 'Available'),

    ('UST-KEY-0003', 'Keyboard', 'SN-HP-6612321', 'HP', 'HP Wired 160',
     '2023-05-01', 1, None, 'Available'),

    ('UST-LTP-0004', 'Laptop', 'SN-LN-1234987', 'Lenovo', 'ThinkPad E15',
     '2022-05-11', 3, 'Rohit Sharma (UST Bangalore)', 'Assigned'),

    ('UST-DCK-0005', 'Docking Station', 'SN-DL-5543123', 'Dell', 'Dell D6000',
     '2021-11-20', 3, 'Anjali Nair (UST Trivandrum)', 'Assigned'),

    ('UST-MNT-0006', 'Monitor', 'SN-SAM-9834567', 'Samsung', 'Samsung S24R350',
     '2023-03-12', 2, 'Vivek Reddy (UST Hyderabad)', 'Assigned'),

    ('UST-LTP-0007', 'Laptop', 'SN-HP-8834129', 'HP', 'HP ProBook 440 G8',
     '2021-09-18', 3, None, 'Repair'),

    ('UST-MNT-0008', 'Monitor', 'SN-LG-9925511', 'LG', 'LG 24MK600',
     '2019-08-12', 3, None, 'Retired')
]


# --------------------------- INSERT ---------------------------
print("\n************* INSERTING SAMPLE ASSETS *************")
for asset in data:
    # This will call create_asset() in aims_project
    # Validation happens internally
    aims_project.create_asset(asset)


# --------------------------- READ ALL -------------------------
print("\n************* READ ALL ASSETS *************")
aims_project.read_all_assets()


# ---------------- READ BY STATUS (FILTER) ---------------------
print("\n************* READ ASSETS WHERE STATUS = Available *************")
# This prints only assets that are Available
aims_project.read_all_assets("Available")


# ---------------------- READ BY ID ----------------------------
print("\n************* READ ASSET WITH ID = 3 *************")
aims_project.read_asset(3)


# ------------------------- UPDATE ------------------------------
print("\n************* UPDATE ASSET ID = 3 *************")

# IMPORTANT:
# Must match exact same tuple format (same index order)
updated_data = (
    'UST-LTP-0999', 'Laptop', 'SN-HP-NEW9911',
    'HP', 'HP EliteBook 845',
    '2023-06-01', 2, None, 'Available'
)

# This will also validate the tuple
aims_project.update_asset(3, updated_data)


# ------------------------- DELETE ------------------------------
print("\n************* DELETE ASSET ID = 5 *************")
aims_project.delete_asset(5)


# ----------------------- FINAL RESULTS -------------------------
print("\n************* FINAL ASSET LIST *************")
aims_project.read_all_assets()


# ****************** Inserting Assets to Database ******************

# DB Connection Established
# Error: (1062, "Duplicate entry 'UST-LTP-0001' for key 'asset_inventory.asset_tag'")
# DB Connection Established
# Asset inserted successfully
# DB Connection Established  
# Asset inserted successfully
# DB Connection Established
# Error: (1062, "Duplicate entry 'UST-LTP-0004' for key 'asset_inventory.asset_tag'")
# DB Connection Established
# Asset inserted successfully
# DB Connection Established
# Asset inserted successfully
# DB Connection Established
# Asset inserted successfully
# DB Connection Established
# Asset inserted successfully

# ******************** Read ALL assets ***************************

# DB Connection Established
# (1, 'UST-LTP-0001', 'Laptop', 'SN-DL-9988123', 'Dell', 'Latitude 5520', datetime.date(2023, 1, 15), 3, None, 'Available', datetime.datetime(2025, 11, 26, 16, 51, 7))
# (2, 'UST-LTP-0004', 'Laptop', 'SN-LN-1234987', 'Lenovo', 'ThinkPad E15', datetime.date(2022, 5, 11), 3, 'Rohit Sharma (UST Bangalore)', 'Assigned', datetime.datetime(2025, 11, 26, 16, 51, 7))
# (3, 'UST-LPT-9001', 'Laptop', 'SN-DL-9090', 'DELL', 'Latitude 5430', datetime.date(2023, 3, 10), 2, None, 'Available', datetime.datetime(2025, 11, 26, 22, 21, 15))
# (5, 'UST-MNT-0002', 'Monitor', 'SN-LG-7719231', 'LG', 'UltraWide 29WL500', datetime.date(2022, 10, 10), 2, None, 'Available', datetime.datetime(2025, 11, 26, 23, 18, 39))
# (6, 'UST-KEY-0003', 'Keyboard', 'SN-HP-6612321', 'HP', 'HP Wired 160', datetime.date(2023, 5, 1), 1, None, 'Available', datetime.datetime(2025, 11, 26, 23, 18, 39))
# (8, 'UST-DCK-0005', 'Docking Station', 'SN-DL-5543123', 'Dell', 'Dell D6000', datetime.date(2021, 11, 20), 3, 'Anjali Nair (UST 
# Trivandrum)', 'Assigned', datetime.datetime(2025, 11, 26, 23, 18, 39))
# (9, 'UST-MNT-0006', 'Monitor', 'SN-SAM-9834567', 'Samsung', 'Samsung S24R350', datetime.date(2023, 3, 12), 2, 'Vivek Reddy (UST 
# Hyderabad)', 'Assigned', datetime.datetime(2025, 11, 26, 23, 18, 39))
# (10, 'UST-LTP-0007', 'Laptop', 'SN-HP-8834129', 'HP', 'HP ProBook 440 G8', datetime.date(2021, 9, 18), 3, None, 'Repair', datetime.datetime(2025, 11, 26, 23, 18, 39))
# (11, 'UST-MNT-0008', 'Monitor', 'SN-LG-9925511', 'LG', 'LG 24MK600', datetime.date(2019, 8, 12), 3, None, 'Retired', datetime.datetime(2025, 11, 26, 23, 18, 39))

# ********************** Read Assets where status = Available ******************

# DB Connection Established
# (1, 'UST-LTP-0001', 'Laptop', 'SN-DL-9988123', 'Dell', 'Latitude 5520', datetime.date(2023, 1, 15), 3, None, 'Available', datetime.datetime(2025, 11, 26, 16, 51, 7))
# (3, 'UST-LPT-9001', 'Laptop', 'SN-DL-9090', 'DELL', 'Latitude 5430', datetime.date(2023, 3, 10), 2, None, 'Available', datetime.datetime(2025, 11, 26, 22, 21, 15))
# (5, 'UST-MNT-0002', 'Monitor', 'SN-LG-7719231', 'LG', 'UltraWide 29WL500', datetime.date(2022, 10, 10), 2, None, 'Available', datetime.datetime(2025, 11, 26, 23, 18, 39))
# (6, 'UST-KEY-0003', 'Keyboard', 'SN-HP-6612321', 'HP', 'HP Wired 160', datetime.date(2023, 5, 1), 1, None, 'Available', datetime.datetime(2025, 11, 26, 23, 18, 39))

# ******************* Read asset by ID **************************

# DB Connection Established
# Asset: (3, 'UST-LPT-9001', 'Laptop', 'SN-DL-9090', 'DELL', 'Latitude 5430', datetime.date(2023, 3, 10), 2, None, 'Available', datetime.datetime(2025, 11, 26, 22, 21, 15))

# ****************** Update Asset 3 ***************************
# DB Connection Established
# Asset: (3, 'UST-LPT-9001', 'Laptop', 'SN-DL-9090', 'DELL', 'Latitude 5430', datetime.date(2023, 3, 10), 2, None, 'Available', datetime.datetime(2025, 11, 26, 22, 21, 15))
# DB Connection Established
# Asset updated successfully

# ********************** Delete Asset ID 5 ***************

# DB Connection Established
# Asset: (5, 'UST-MNT-0002', 'Monitor', 'SN-LG-7719231', 'LG', 'UltraWide 29WL500', datetime.date(2022, 10, 10), 2, None, 'Available', datetime.datetime(2025, 11, 26, 23, 18, 39))
# DB Connection Established
# Asset deleted

# ************************* Final List ******
# DB Connection Established
# (1, 'UST-LTP-0001', 'Laptop', 'SN-DL-9988123', 'Dell', 'Latitude 5520', datetime.date(2023, 1, 15), 3, None, 'Available', datetime.datetime(2025, 11, 26, 16, 51, 7))
# (2, 'UST-LTP-0004', 'Laptop', 'SN-LN-1234987', 'Lenovo', 'ThinkPad E15', datetime.date(2022, 5, 11), 3, 'Rohit Sharma (UST Bangalore)', 'Assigned', datetime.datetime(2025, 11, 26, 16, 51, 7))
# (3, 'UST-LTP-0999', 'Laptop', 'SN-HP-NEW9911', 'HP', 'HP EliteBook 845', datetime.date(2023, 6, 1), 2, None, 'Available', datetime.datetime(2025, 11, 26, 23, 18, 40))
# (6, 'UST-KEY-0003', 'Keyboard', 'SN-HP-6612321', 'HP', 'HP Wired 160', datetime.date(2023, 5, 1), 1, None, 'Available', datetime.datetime(2025, 11, 26, 23, 18, 39))
# (8, 'UST-DCK-0005', 'Docking Station', 'SN-DL-5543123', 'Dell', 'Dell D6000', datetime.date(2021, 11, 20), 3, 'Anjali Nair (UST 
# Trivandrum)', 'Assigned', datetime.datetime(2025, 11, 26, 23, 18, 39))
# (9, 'UST-MNT-0006', 'Monitor', 'SN-SAM-9834567', 'Samsung', 'Samsung S24R350', datetime.date(2023, 3, 12), 2, 'Vivek Reddy (UST 
# Hyderabad)', 'Assigned', datetime.datetime(2025, 11, 26, 23, 18, 39))
# (10, 'UST-LTP-0007', 'Laptop', 'SN-HP-8834129', 'HP', 'HP ProBook 440 G8', datetime.date(2021, 9, 18), 3, None, 'Repair', datetime.datetime(2025, 11, 26, 23, 18, 39))
# (11, 'UST-MNT-0008', 'Monitor', 'SN-LG-9925511', 'LG', 'LG 24MK600', datetime.date(2019, 8, 12), 3, None, 'Retired', datetime.datetime(2025, 11, 26, 23, 18, 39))
