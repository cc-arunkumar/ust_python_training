from config.db_connection import get_connection

conn = get_connection()
cursor = conn.cursor()
cursor.execute("""INSERT INTO asset_inventory
(asset_tag, asset_type, serial_number, manufacturer, model, purchase_date, warranty_years, assigned_to, asset_status)
VALUES ('UST-TEST-001','Laptop','SN-TEST-001','Dell','XPS 13','2024-01-01',2,NULL,'Available')""")
conn.commit()
cursor.close()
conn.close()
