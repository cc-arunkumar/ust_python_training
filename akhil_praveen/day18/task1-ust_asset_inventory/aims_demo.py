import asset_crud as asset

data=[('UST-LTP-0001', 'Laptop', 'SN-DL-9988123', 'Dell', 'Latitude 5520', '2023-01-15', 3, None, 'Available',None),
('UST-MNT-0002', 'Monitor', 'SN-LG-7719231', 'LG', 'UltraWide 29WL500', '2022-10-10', 2, None, 'Available', None),
('UST-KEY-0003', 'Keyboard', 'SN-HP-6612321', 'HP', 'HP Wired 160', '2023-05-01', 1, None, 'Available', None),
('UST-LTP-0004', 'Laptop', 'SN-LN-1234987', 'Lenovo', 'ThinkPad E15', '2022-05-11', 3, 'Rohit Sharma (UST Bangalore)', 'Assigned', None),
('UST-DCK-0005', 'Docking Station', 'SN-DL-5543123', 'Dell', 'Dell D6000', '2021-11-20', 3, 'Anjali Nair (UST Trivandrum)', 'Assigned', None),
('UST-MNT-0006', 'Monitor', 'SN-SAM-9834567', 'Samsung', 'Samsung S24R350', '2023-03-12', 2, 'Vivek Reddy (UST Hyderabad)', 'Assigned', None),
('UST-LTP-0007', 'Laptop', 'SN-HP-8834129', 'HP', 'HP ProBook 440 G8', '2021-09-18', 3, None, 'Repair', None),
('UST-MNT-0008', 'Monitor', 'SN-LG-9925511', 'LG', 'LG 24MK600', '2019-08-12', 3, None, 'Retired', None)
]

print("-----------------------------")
for dat in data:
    asset.create_asset(dat)

print("-----------------------------")

asset.read_all_assets()

print("-----------------------------")

for i in range(1,9):
    asset.read_asset_by_id(i)
    print("-----------------------------")

print("-----------------------------")
print("Before Update")
update=('UST-MNT-0008', 'Monitor', 'SN-LG-9925511', 'LG Goods', 'LG 24MK600', '2019-08-12', 3, None, 'Retired', None)
asset.read_asset_by_id(8)
print("-----------------------------")
asset.update_asset(8,update)
print("-----------------------------")
print("After update")
asset.read_asset_by_id(8)
print("-----------------------------")
print("Before Delete")
asset.read_asset_by_id(7)
print("-----------------------------")
asset.delete_asset(7)
print("-----------------------------")
print("After delete")
asset.read_asset_by_id(7)
print("-----------------------------")

#Output
# -----------------------------
# Connection Established
# Data added successfully
# Connection Closed      
# Connection Established
# Data added successfully
# Connection Closed      
# Connection Established
# Data added successfully
# Connection Closed      
# Connection Established
# Data added successfully
# Connection Closed
# Connection Established
# Data added successfully
# Connection Closed
# Connection Established
# Data added successfully
# Connection Closed
# Connection Established
# Data added successfully
# Connection Closed
# Connection Established
# Data added successfully
# Connection Closed
# -----------------------------
# Connection Established
# Record 1 : (1, 'UST-LTP-0001', 'Laptop', 'SN-DL-9988123', 'Dell', 'Latitude 5520', datetime.date(2023, 1, 15), 3, None, 'Available', datetime.datetime(2025, 11, 26, 16, 45, 31))
# Record 2 : (2, 'UST-MNT-0002', 'Monitor', 'SN-LG-7719231', 'LG', 'UltraWide 29WL500', datetime.date(2022, 10, 10), 2, None, 'Available', datetime.datetime(2025, 11, 26, 16, 45, 31))
# Record 3 : (3, 'UST-KEY-0003', 'Keyboard', 'SN-HP-6612321', 'HP', 'HP Wired 160', datetime.date(2023, 5, 1), 1, None, 'Available', datetime.datetime(2025, 11, 26, 16, 45, 31))
# Record 4 : (4, 'UST-LTP-0004', 'Laptop', 'SN-LN-1234987', 'Lenovo', 'ThinkPad E15', datetime.date(2022, 5, 11), 3, 'Rohit Sharma (UST Bangalore)', 'Assigned', datetime.datetime(2025, 11, 26, 16, 45, 31))
# Record 5 : (5, 'UST-DCK-0005', 'Docking Station', 'SN-DL-5543123', 'Dell', 'Dell D6000', datetime.date(2021, 11, 20), 3, 'Anjali Nair (UST Trivandrum)', 'Assigned', datetime.datetime(2025, 11, 26, 16, 45, 31))
# Record 6 : (6, 'UST-MNT-0006', 'Monitor', 'SN-SAM-9834567', 'Samsung', 'Samsung S24R350', datetime.date(2023, 3, 12), 2, 'Vivek Reddy (UST Hyderabad)', 'Assigned', datetime.datetime(2025, 11, 26, 16, 45, 31))
# Record 7 : (7, 'UST-LTP-0007', 'Laptop', 'SN-HP-8834129', 'HP', 'HP ProBook 440 G8', datetime.date(2021, 9, 18), 3, None, 'Repair', datetime.datetime(2025, 11, 26, 16, 45, 31))
# Record 8 : (8, 'UST-MNT-0008', 'Monitor', 'SN-LG-9925511', 'LG', 'LG 24MK600', datetime.date(2019, 8, 12), 3, None, 'Retired', datetime.datetime(2025, 11, 26, 16, 45, 31))
# Connection Closed
# -----------------------------
# Connection Established
# Asset 1 : (1, 'UST-LTP-0001', 'Laptop', 'SN-DL-9988123', 'Dell', 'Latitude 5520', datetime.date(2023, 1, 15), 3, None, 'Available', datetime.datetime(2025, 11, 26, 16, 45, 31))
# Connection Closed
# -----------------------------
# Connection Established
# Asset 2 : (2, 'UST-MNT-0002', 'Monitor', 'SN-LG-7719231', 'LG', 'UltraWide 29WL500', datetime.date(2022, 10, 10), 2, None, 'Available', datetime.datetime(2025, 11, 26, 16, 45, 31))
# Connection Closed
# -----------------------------
# Connection Established
# Asset 3 : (3, 'UST-KEY-0003', 'Keyboard', 'SN-HP-6612321', 'HP', 'HP Wired 160', datetime.date(2023, 5, 1), 1, None, 'Available', datetime.datetime(2025, 11, 26, 16, 45, 31))
# Connection Closed
# -----------------------------
# Connection Established
# Asset 4 : (4, 'UST-LTP-0004', 'Laptop', 'SN-LN-1234987', 'Lenovo', 'ThinkPad E15', datetime.date(2022, 5, 11), 3, 'Rohit Sharma (UST Bangalore)', 'Assigned', datetime.datetime(2025, 11, 26, 16, 
# 45, 31))
# Connection Closed
# -----------------------------
# Connection Established
# Asset 5 : (5, 'UST-DCK-0005', 'Docking Station', 'SN-DL-5543123', 'Dell', 'Dell D6000', datetime.date(2021, 11, 20), 3, 'Anjali Nair (UST Trivandrum)', 'Assigned', datetime.datetime(2025, 11, 26, 16, 45, 31))
# Connection Closed
# -----------------------------
# Connection Established
# Asset 6 : (6, 'UST-MNT-0006', 'Monitor', 'SN-SAM-9834567', 'Samsung', 'Samsung S24R350', datetime.date(2023, 3, 12), 2, 'Vivek Reddy (UST Hyderabad)', 'Assigned', datetime.datetime(2025, 11, 26, 16, 45, 31))
# Connection Closed
# -----------------------------
# Connection Established
# Asset 7 : (7, 'UST-LTP-0007', 'Laptop', 'SN-HP-8834129', 'HP', 'HP ProBook 440 G8', datetime.date(2021, 9, 18), 3, None, 'Repair', datetime.datetime(2025, 11, 26, 16, 45, 31))
# Connection Closed
# -----------------------------
# Connection Established
# Asset 8 : (8, 'UST-MNT-0008', 'Monitor', 'SN-LG-9925511', 'LG', 'LG 24MK600', datetime.date(2019, 8, 12), 3, None, 'Retired', datetime.datetime(2025, 11, 26, 16, 45, 31))
# Connection Closed
# -----------------------------
# -----------------------------
# Before Update
# Connection Established
# Asset 8 : (8, 'UST-MNT-0008', 'Monitor', 'SN-LG-9925511', 'LG', 'LG 24MK600', datetime.date(2019, 8, 12), 3, None, 'Retired', datetime.datetime(2025, 11, 26, 16, 45, 31))
# Connection Closed
# -----------------------------
# Connection Established
# Data updated added successfully
# Connection Closed
# -----------------------------
# After update
# Connection Established
# Asset 8 : (8, 'UST-MNT-0008', 'Monitor', 'SN-LG-9925511', 'LG Goods', 'LG 24MK600', datetime.date(2019, 8, 12), 3, None, 'Retired', datetime.datetime(2025, 11, 26, 16, 45, 32))
# Connection Closed
# -----------------------------
# Before Delete
# Connection Established
# Asset 7 : (7, 'UST-LTP-0007', 'Laptop', 'SN-HP-8834129', 'HP', 'HP ProBook 440 G8', datetime.date(2021, 9, 18), 3, None, 'Repair', datetime.datetime(2025, 11, 26, 16, 45, 31))
# Connection Closed
# -----------------------------
# Connection Established
# Connection Established
# Asset 7 : (7, 'UST-LTP-0007', 'Laptop', 'SN-HP-8834129', 'HP', 'HP ProBook 440 G8', datetime.date(2021, 9, 18), 3, None, 'Repair', datetime.datetime(2025, 11, 26, 16, 45, 31))
# Connection Closed
# Deleted Successfully
# Connection Closed
# -----------------------------
# After delete
# Connection Established
# Asset Not Found
# Connection Closed
# -----------------------------