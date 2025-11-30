import mysql.connector

def get_connection():
    conn = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "pass@word1",
        database = "ust_asset_db"
    )
    return conn

def read_all():
    
    conn = get_connection()
    cursor = conn.cursor()
    
    cursor.execute("SELECT * FROM asset_inventory;")
    rows = cursor.fetchall()
    print("----------")
    for prod in rows:
        print(f"asset_id : {prod[0]} | asset_tag : {prod[1]} | asset_type : {prod[2]} | serial_number : {prod[3]} | manufacturer : {prod[4]} | model : {prod[5]} | purchase_date : {prod[6]} | warranty_years : {prod[7]} | assigned_to : {prod[8]} | asset_status : {prod[9]} | last_update : {prod[10]}")
        
def create_asset(asset_tag, asset_type, serial_number, manufacturer,
                 model, purchase_date, warranty_years, assigned_to, asset_status):
    conn = None
    cursor = None
    try:
        if not asset_tag.startswith("UST-"):
            print("Error: asset_tag must start with 'UST-'.")
            return

        valid_asset_types = ["Laptop", "Monitor", "Docking Station", "Keyboard", "Mouse"]
        if asset_type not in valid_asset_types:
            print("Error: asset_type must be one of:", valid_asset_types)
            return

        valid_status = ["Available", "Assigned", "Repair", "Retired"]
        if asset_status not in valid_status:
            print("Error: asset_status must be one of:", valid_status)
            return

        if warranty_years is None or int(warranty_years) <= 0:
            print("Error: warranty_years must be a positive number.")
            return

        if assigned_to is not None and assigned_to.strip() == "":
            assigned_to = None

        if asset_status == "Assigned":

            if assigned_to is None:
                print("Error: assigned_to cannot be NULL when status is 'Assigned'.")
                return
        elif asset_status == "Available" or asset_status == "Retired":

            if assigned_to is not None:
                print("Error: assigned_to must be NULL when status is 'Available' or 'Retired'.")
                return
        conn = get_connection()
        cursor = conn.cursor()
        
        cursor.execute("SELECT asset_id FROM asset_inventory WHERE asset_tag = %s",(asset_tag, ))
        
        row = cursor.fetchone()
        
        if row is not None:
            print("Error: asset tag already exist")
        cursor.execute("SELECT asset_id FROM asset_inventory WHERE serial_number = %s",(serial_number, ))
        
        row = cursor.fetchone()
        
        if row is not None:
            print("Error: serial_number already exist")
            
            cursor.execute("INSERT INTO asset_inventory (asset_tag, asset_type, serial_number, manufacturer, model, purchase_date, warranty_years, assigned_to, asset_status, last_update) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,NOW())",(asset_tag, asset_type, serial_number, manufacturer, model, purchase_date, warranty_years, assigned_to, asset_status))


        
        conn.commit()
        print("Employee Record Inserted Successfully")
        
    except Exception as e:
        print("Error",e)
    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None and conn.is_connected():
            conn.close()
        print("Connection closed successfully")
        
create_asset('UST-LTP-0001', 'Laptop', 'SN-DL-9988123', 'Dell', 'Latitude 5520', '2023-01-15', 3, None, 'Available')

read_all()

        
        
        
        