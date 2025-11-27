import pymysql
from datetime import datetime

# ---------------- CONNECTION ----------------
# This function connects to MySQL and returns the connection object
def get_connection():
    conn = pymysql.connect(
        host="localhost",       # Database host
        user="root",            # Database user
        password="pass@word1",  # Database password
        database="ust_asset_db" # Database name
    )
    print("DB Connection Established")
    return conn


# ---------------- VALIDATIONS ----------------
# This function checks the input asset tuple before inserting/updating to ensure it meets the required constraints
def is_valid_asset(asset):
    try:
        if not asset[0].startswith("UST-"):
            print("Asset tag must start with UST-")
            return False

        # asset_type must be from allowed list
        allowed_types = ["Laptop", "Monitor", "Docking Station", "Keyboard", "Mouse"]
        if asset[1] not in allowed_types:
            print("Invalid asset type")
            return False

        # warranty_years must be > 0
        if asset[6] <= 0:
            print("Warranty must be > 0")
            return False

        # manufacturer and model cannot be blank
        if asset[3] == "" or asset[4] == "":
            print("Manufacturer and model cannot be empty")
            return False

        # asset_status must be from allowed list
        allowed_status = ["Available", "Assigned", "Repair", "Retired"]
        if asset[8] not in allowed_status:
            print("Invalid asset status")
            return False

        # If asset status is "Assigned", "assigned_to" cannot be null
        if asset[8] == "Assigned" and asset[7] is None:
            print("Assigned asset must have employee name")
            return False

        # If status is "Available" or "Retired", "assigned_to" must be null
        if asset[8] in ["Available", "Retired"] and asset[7] is not None:
            print("Available/Retired asset cannot be assigned")
            return False

    except Exception as e:
        print("Validation Error:", e)
        return False

    return True


# ---------------- CREATE ----------------
# This function inserts a new asset into the database after validating the asset tuple
def create_asset(asset):
    try:
        # Establish connection to the database
        conn = get_connection()
        cursor = conn.cursor()

        # Validate the asset before inserting
        if is_valid_asset(asset):
            # SQL query to insert a new asset record into the asset_inventory table
            sql = """
                INSERT INTO asset_inventory
                (asset_tag, asset_type, serial_number, manufacturer, model,
                 purchase_date, warranty_years, assigned_to, asset_status, last_updated)
                 VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            """

            # Append the current timestamp to the asset data (for last_updated field)
            values = asset + (datetime.now(),)
            cursor.execute(sql, values)  # Execute the query with asset data
            conn.commit()  # Commit the transaction to the database
            print("Asset inserted successfully")

        else:
            print("Invalid input asset")  # If the asset data is invalid, print an error

    except Exception as e:
        print("Error:", e)
    finally:
        cursor.close()  
        conn.close()   


# ---------------- READ ALL ----------------
# This function retrieves all assets, or assets filtered by their status
def read_all_assets(status="ALL"):
    try:
        # Establish connection to the database
        conn = get_connection()
        cursor = conn.cursor()

        # If no filter provided, retrieve all assets
        if status == "ALL":
            cursor.execute("SELECT * FROM asset_inventory")
        else:
            cursor.execute("SELECT * FROM asset_inventory WHERE asset_status=%s", (status,))

        rows = cursor.fetchall()  # Fetch all rows that match the query

        if rows:
            for r in rows:
                print(r)  # Print each asset record
        else:
            print("No records found")  # If no assets are found

    except Exception as e:
        print("Error:", e)
    finally:
        cursor.close()  # Close the cursor
        conn.close()    # Close the database connection


# ---------------- READ BY ID ----------------
# This function retrieves an asset by its asset_id
def read_asset(asset_id):
    try:
        # Establish connection to the database
        conn = get_connection()
        cursor = conn.cursor()

        # Execute the query to find the asset by asset_id
        cursor.execute("SELECT * FROM asset_inventory WHERE asset_id=%s", (asset_id,))
        row = cursor.fetchone()  # Fetch the first matching asset

        if row:
            print("Asset:", row)  # If asset found, print the asset details
            return row
        else:
            print("Asset not found")  # If no asset found, print a message
            return None

    except Exception as e:
        print("Error:", e)
    finally:
        cursor.close()  # Close the cursor
        conn.close()    # Close the database connection


# ---------------- UPDATE ----------------
# This function updates an existing asset's details based on asset_id
def update_asset(asset_id, new_data):
    try:
        # Check if the asset exists before trying to update
        old = read_asset(asset_id)
        if old is None:
            return  # If asset does not exist, stop the update

        # Validate the new data
        if not is_valid_asset(new_data):
            print("Invalid updated data")
            return  # Stop if the new data is invalid

        # Establish connection to the database
        conn = get_connection()
        cursor = conn.cursor()

        # SQL query to update the asset details
        sql = """
            UPDATE asset_inventory
            SET asset_tag=%s, asset_type=%s, serial_number=%s, manufacturer=%s,
                model=%s, purchase_date=%s, warranty_years=%s, assigned_to=%s,
                asset_status=%s, last_updated=%s
            WHERE asset_id=%s
        """

        # Append the timestamp and asset_id to the new data
        values = new_data + (datetime.now(), asset_id)
        cursor.execute(sql, values)  # Execute the update query with new data
        conn.commit()  # Commit the transaction
        print("Asset updated successfully")

    except Exception as e:
        print("Error:", e)
    finally:
        cursor.close()  # Close the cursor
        conn.close()    # Close the database connection


# ---------------- DELETE ----------------
# This function deletes an asset from the database by asset_id
def delete_asset(asset_id):
    try:
        # Check if the asset exists before trying to delete it
        record = read_asset(asset_id)
        if record is None:
            return  # If asset does not exist, stop the deletion

        # Establish connection to the database
        conn = get_connection()
        cursor = conn.cursor()

        # Execute the delete query for the given asset_id
        cursor.execute("DELETE FROM asset_inventory WHERE asset_id=%s", (asset_id,))
        conn.commit()  # Commit the transaction
        print("Asset deleted")

    except Exception as e:
        print("Error:", e)
    finally:
        cursor.close()  # Close the cursor
        conn.close()    # Close the database connection


# Example asset object for testing when running the file
sample = (
    "UST-LPT-9001",     # asset_tag (must start with "UST-")
    "Laptop",           # asset_type (must be from allowed types: Laptop, Monitor, etc.)
    "SN-DL-9090",       # serial_number
    "DELL",             # manufacturer (cannot be empty)
    "Latitude 5430",    # model (cannot be empty)
    "2023-03-10",       # purchase_date (should be in a valid format)
    2,                  # warranty_years (must be > 0)
    None,               # assigned_to (should be None if status is not "Assigned")
    "Available"         # asset_status (must be from allowed status: Available, Assigned, etc.)
)



#o/p:
# ************* Inserting Assets ***********
# DB Connection Established
# Asset inserted successfully
# DB Connection Established
# Asset inserted successfully
# DB Connection Established
# Asset inserted successfully
# DB Connection Established
# Asset inserted successfully
# DB Connection Established
# Asset inserted successfully
# DB Connection Established
# Asset inserted successfully
# DB Connection Established
# Asset inserted successfully
# DB Connection Established
# Asset inserted successfully

# ************* Read ALL assets ***********
# DB Connection Established
# (1, 'UST-LTP-0001', 'Laptop', 'SN-DL-9988123', 'Dell', 'Latitude 5520', datetime.date(2023, 1, 15), 3, None, 'Available', datetime.datetime(2025, 11, 27, 0, 18, 21))
# (2, 'UST-MNT-0002', 'Monitor', 'SN-LG-7719231', 'LG', 'UltraWide 29WL500', datetime.date(2022, 10, 10), 2, None, 'Available', datetime.datetime(2025, 11, 27, 0, 18, 21))
# (3, 'UST-KEY-0003', 'Keyboard', 'SN-HP-6612321', 'HP', 'HP Wired 160', datetime.date(2023, 5, 1), 1, None, 'Available', datetime.datetime(2025, 11, 27, 0, 18, 21))
# (4, 'UST-LTP-0004', 'Laptop', 'SN-LN-1234987', 'Lenovo', 'ThinkPad E15', datetime.date(2022, 5, 11), 3, 'Rohit Sharma (UST Bangalore)', 'Assigned', datetime.datetime(2025, 11, 27, 0, 18, 21))
# (5, 'UST-DCK-0005', 'Docking Station', 'SN-DL-5543123', 'Dell', 'Dell D6000', datetime.date(2021, 11, 20), 3, 'Anjali Nair (UST 
# Trivandrum)', 'Assigned', datetime.datetime(2025, 11, 27, 0, 18, 21))
# (6, 'UST-MNT-0006', 'Monitor', 'SN-SAM-9834567', 'Samsung', 'Samsung S24R350', datetime.date(2023, 3, 12), 2, 'Vivek Reddy (UST 
# Hyderabad)', 'Assigned', datetime.datetime(2025, 11, 27, 0, 18, 21))
# (7, 'UST-LTP-0007', 'Laptop', 'SN-HP-8834129', 'HP', 'HP ProBook 440 G8', datetime.date(2021, 9, 18), 3, None, 'Repair', datetime.datetime(2025, 11, 27, 0, 18, 21))
# (8, 'UST-MNT-0008', 'Monitor', 'SN-LG-9925511', 'LG', 'LG 24MK600', datetime.date(2019, 8, 12), 3, None, 'Retired', datetime.datetime(2025, 11, 27, 0, 18, 21))

# ************* Read Available assets ***********
# DB Connection Established
# (1, 'UST-LTP-0001', 'Laptop', 'SN-DL-9988123', 'Dell', 'Latitude 5520', datetime.date(2023, 1, 15), 3, None, 'Available', datetime.datetime(2025, 11, 27, 0, 18, 21))
# (2, 'UST-MNT-0002', 'Monitor', 'SN-LG-7719231', 'LG', 'UltraWide 29WL500', datetime.date(2022, 10, 10), 2, None, 'Available', datetime.datetime(2025, 11, 27, 0, 18, 21))
# (3, 'UST-KEY-0003', 'Keyboard', 'SN-HP-6612321', 'HP', 'HP Wired 160', datetime.date(2023, 5, 1), 1, None, 'Available', datetime.datetime(2025, 11, 27, 0, 18, 21))

# ************* Read asset by ID = 3 ***********
# DB Connection Established
# Asset: (3, 'UST-KEY-0003', 'Keyboard', 'SN-HP-6612321', 'HP', 'HP Wired 160', datetime.date(2023, 5, 1), 1, None, 'Available', datetime.datetime(2025, 11, 27, 0, 18, 21))

# ************* Update Asset ID = 3 ***********
# DB Connection Established
# Asset: (3, 'UST-KEY-0003', 'Keyboard', 'SN-HP-6612321', 'HP', 'HP Wired 160', datetime.date(2023, 5, 1), 1, None, 'Available', datetime.datetime(2025, 11, 27, 0, 18, 21))
# DB Connection Established
# Asset updated successfully

# ************* Delete Asset ID = 5 ***********
# DB Connection Established
# Asset: (5, 'UST-DCK-0005', 'Docking Station', 'SN-DL-5543123', 'Dell', 'Dell D6000', datetime.date(2021, 11, 20), 3, 'Anjali Nair (UST Trivandrum)', 'Assigned', datetime.datetime(2025, 11, 27, 0, 18, 21))
# DB Connection Established
# Asset deleted

# ************* Final List ***********
# DB Connection Established
# (1, 'UST-LTP-0001', 'Laptop', 'SN-DL-9988123', 'Dell', 'Latitude 5520', datetime.date(2023, 1, 15), 3, None, 'Available', datetime.datetime(2025, 11, 27, 0, 18, 21))
# (2, 'UST-MNT-0002', 'Monitor', 'SN-LG-7719231', 'LG', 'UltraWide 29WL500', datetime.date(2022, 10, 10), 2, None, 'Available', datetime.datetime(2025, 11, 27, 0, 18, 21))
# (3, 'UST-LTP-0999', 'Laptop', 'SN-HP-NEW9911', 'HP', 'HP EliteBook 845', datetime.date(2023, 6, 1), 2, None, 'Available', datetime.datetime(2025, 11, 27, 0, 18, 21))
# (4, 'UST-LTP-0004', 'Laptop', 'SN-LN-1234987', 'Lenovo', 'ThinkPad E15', datetime.date(2022, 5, 11), 3, 'Rohit Sharma (UST Bangalore)', 'Assigned', datetime.datetime(2025, 11, 27, 0, 18, 21))
# (6, 'UST-MNT-0006', 'Monitor', 'SN-SAM-9834567', 'Samsung', 'Samsung S24R350', datetime.date(2023, 3, 12), 2, 'Vivek Reddy (UST 
# Hyderabad)', 'Assigned', datetime.datetime(2025, 11, 27, 0, 18, 21))
# (7, 'UST-LTP-0007', 'Laptop', 'SN-HP-8834129', 'HP', 'HP ProBook 440 G8', datetime.date(2021, 9, 18), 3, None, 'Repair', datetime.datetime(2025, 11, 27, 0, 18, 21))
# (8, 'UST-MNT-0008', 'Monitor', 'SN-LG-9925511', 'LG', 'LG 24MK600', datetime.date(2019, 8, 12), 3, None, 'Retired', datetime.datetime(2025, 11, 27, 0, 18, 21))