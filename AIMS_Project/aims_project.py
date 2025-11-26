import pymysql
from datetime import datetime

# ---------------- CONNECTION ----------------
# This function connects to MySQL and returns the connection
def get_connection():
    conn = pymysql.connect(
        host="localhost",
        user="root",
        password="pass@word1",
        database="ust_asset_db"
    )
    print("DB Connection Established")
    return conn


# ---------------- VALIDATIONS ----------------
# This function checks the input asset tuple before inserting/updating
def is_valid_asset(asset):
    try:
        # asset tuple indexes
        # 0 asset_tag
        # 1 asset_type
        # 2 serial_number
        # 3 manufacturer
        # 4 model
        # 5 purchase_date
        # 6 warranty_years
        # 7 assigned_to
        # 8 asset_status

        # asset_tag must start with "UST-"
        if not asset[0].startswith("UST-"):
            print("Asset tag must start with UST-")
            return False

        # asset_type must be from allowed list
        allowed_types = ["Laptop", "Monitor", "Docking Station", "Keyboard", "Mouse"]
        if asset[1] not in allowed_types:
            print("Invalid asset type")
            return False

        # warranty must be > 0
        if asset[6] <= 0:
            print("Warranty must be > 0")
            return False

        # manufacturer and model cannot be blank
        if asset[3] == "" or asset[4] == "":
            print("Manufacturer and model cannot be empty")
            return False

        # status must match allowed types
        allowed_status = ["Available", "Assigned", "Repair", "Retired"]
        if asset[8] not in allowed_status:
            print("Invalid asset status")
            return False

        # If status = Assigned → assigned_to must not be null
        if asset[8] == "Assigned" and asset[7] is None:
            print("Assigned asset must have employee name")
            return False

        # If Available or Retired → assigned_to must be null
        if asset[8] in ["Available", "Retired"] and asset[7] is not None:
            print("Available/Retired asset cannot be assigned")
            return False

    except Exception as e:
        print("Validation Error:", e)
        return False

    return True


# ---------------- CREATE ----------------
def create_asset(asset):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        # validate input first
        if is_valid_asset(asset):
            # SQL insert query
            sql = """
                INSERT INTO asset_inventory
                (asset_tag, asset_type, serial_number, manufacturer, model,
                 purchase_date, warranty_years, assigned_to, asset_status, last_updated)
                 VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            """

            # append timestamp (last_updated)
            values = asset + (datetime.now(),)
            cursor.execute(sql, values)
            conn.commit()
            print("Asset inserted successfully")

        else:
            print("Invalid input asset")

    except Exception as e:
        print("Error:", e)
    finally:
        cursor.close()
        conn.close()


# ---------------- READ ALL ----------------
def read_all_assets(status="ALL"):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        # If no filter → read all rows
        if status == "ALL":
            cursor.execute("SELECT * FROM asset_inventory")
        else:
            cursor.execute("SELECT * FROM asset_inventory WHERE asset_status=%s", (status,))

        rows = cursor.fetchall()

        if rows:
            for r in rows:
                print(r)
        else:
            print("No records found")

    except Exception as e:
        print("Error:", e)
    finally:
        cursor.close()
        conn.close()


# ---------------- READ BY ID ----------------
def read_asset(asset_id):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM asset_inventory WHERE asset_id=%s", (asset_id,))
        row = cursor.fetchone()

        # If row exists → return and print
        if row:
            print("Asset:", row)
            return row
        else:
            print("Asset not found")
            return None

    except Exception as e:
        print("Error:", e)
    finally:
        cursor.close()
        conn.close()


# ---------------- UPDATE ----------------
def update_asset(asset_id, new_data):
    try:
        # First check if asset exists
        old = read_asset(asset_id)
        if old is None:
            return

        # Validate the new tuple
        if not is_valid_asset(new_data):
            print("Invalid updated data")
            return

        conn = get_connection()
        cursor = conn.cursor()

        # Update query
        sql = """
            UPDATE asset_inventory
            SET asset_tag=%s, asset_type=%s, serial_number=%s, manufacturer=%s,
                model=%s, purchase_date=%s, warranty_years=%s, assigned_to=%s,
                asset_status=%s, last_updated=%s
            WHERE asset_id=%s
        """

        values = new_data + (datetime.now(), asset_id)
        cursor.execute(sql, values)
        conn.commit()
        print("Asset updated successfully")

    except Exception as e:
        print("Error:", e)
    finally:
        cursor.close()
        conn.close()


# ---------------- DELETE ----------------
def delete_asset(asset_id):
    try:
        # Check if record exists
        record = read_asset(asset_id)
        if record is None:
            return

        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("DELETE FROM asset_inventory WHERE asset_id=%s", (asset_id,))
        conn.commit()
        print("Asset deleted")

    except Exception as e:
        print("Error:", e)
    finally:
        cursor.close()
        conn.close()


# Example object just for testing when running file
sample = (
    "UST-LPT-9001",     # asset_tag
    "Laptop",           # type
    "SN-DL-9090",       # serial number
    "DELL",             # manufacturer
    "Latitude 5430",    # model
    "2023-03-10",       # purchase date
    2,                  # warranty
    None,               # assigned_to
    "Available"         # status
)
