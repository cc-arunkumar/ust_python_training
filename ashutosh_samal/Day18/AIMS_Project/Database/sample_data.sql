-- Switch to the database
Use ust_asset_db;
-- Insert initial available assets
INSERT INTO asset_inventory
(asset_tag, asset_type, serial_number, manufacturer, model, purchase_date, w
arranty_years, assigned_to, asset_status, last_updated)
VALUES
('UST-LTP-0001', 'Laptop', 'SN-DL-9988123', 'Dell', 'Latitude 5520', '2023-01-15', 3, NULL, 'Available', NOW()),
('UST-MNT-0002', 'Monitor', 'SN-LG-7719231', 'LG', 'UltraWide 29WL500', '20
22-10-10', 2, NULL, 'Available', NOW()),
('UST-KEY-0003', 'Keyboard', 'SN-HP-6612321', 'HP', 'HP Wired 160', '2023-0
5-01', 1, NULL, 'Available', NOW());

-- Insert assigned assets
INSERT INTO asset_inventory
(asset_tag, asset_type, serial_number, manufacturer, model, purchase_date, w
arranty_years, assigned_to, asset_status, last_updated)
VALUES
('UST-LTP-0004', 'Laptop', 'SN-LN-1234987', 'Lenovo', 'ThinkPad E15', '2022-05-11', 3, 'Rohit Sharma (UST Bangalore)', 'Assigned', NOW()),
('UST-DCK-0005', 'Docking Station', 'SN-DL-5543123', 'Dell', 'Dell D6000', '20
21-11-20', 3, 'Anjali Nair (UST Trivandrum)', 'Assigned', NOW()),
('UST-MNT-0006', 'Monitor', 'SN-SAM-9834567', 'Samsung', 'Samsung S24R
350', '2023-03-12', 2, 'Vivek Reddy (UST Hyderabad)', 'Assigned', NOW());

-- Insert asset under repair

INSERT INTO asset_inventory
(asset_tag, asset_type, serial_number, manufacturer, model, purchase_date, w
arranty_years, assigned_to, asset_status, last_updated)
VALUES
('UST-LTP-0007', 'Laptop', 'SN-HP-8834129', 'HP', 'HP ProBook 440 G8', '202
1-09-18', 3, NULL, 'Repair', NOW());

-- Insert retired asset
INSERT INTO asset_inventory
(asset_tag, asset_type, serial_number, manufacturer, model, purchase_date, w
arranty_years, assigned_to, asset_status, last_updated)
VALUES
('UST-MNT-0008', 'Monitor', 'SN-LG-9925511', 'LG', 'LG 24MK600', '2019-08-12', 3, NULL, 'Retired', NOW());
