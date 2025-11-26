USE ust_asset_db;

INSERT INTO asset_inventory
(asset_tag, asset_type, serial_number, manufacturer, model, purchase_date, warranty_years, assigned_to, asset_status)
VALUES
('UST-LTP-0001','Laptop','SN-LAP-0001','Dell','Latitude 5520','2023-06-15',3,NULL,'Available'),
('UST-KBD-0001','Keyboard','SN-KBD-0001','Logitech','MX Keys','2023-02-20',2,'Anita Sharma','Assigned');
