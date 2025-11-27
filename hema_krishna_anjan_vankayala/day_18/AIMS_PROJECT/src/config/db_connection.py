# DB connection helper - returns a pymysql connection to the local DB
import pymysql 
from pymysql import Error

# Return an open pymysql connection to the `ust_asset_db` database
def get_connection():
    conn = pymysql.connect(
        host="localhost",
        user = "root",
        password = "pass@word1",
        database = "ust_asset_db"
    )
    return conn


# conn = get_connection()
# cursor = conn.cursor()
# cursor.execute("SELECT * FROM asset_inventory")
# # cursor.execute("INSERT INTO asset_inventory(asset_tag, asset_type, serial_number, manufacturer, model, purchase_date, warranty_years, assigned_to, asset_status, last_updated)VALUES('UST-MNT-0008', 'Monitor', 'SN-LG-9925511', 'LG', 'LG 24MK600', '2019-08-12', 3, NULL, 'Retired', NOW());")

# # conn.commit()
# data = cursor.fetchall()
# print(data)