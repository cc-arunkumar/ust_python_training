import pymysql

def get_connection():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="pass@word1",
        database="ust_assets"
    )

def create_task( vendor_name, contact_person,
                contact_phone, gst_number, email,
                address, city, active_status="Active"): 
    conn = get_connection()
    cursor = conn.cursor()  

    sql = """
    INSERT INTO vendor_master(
         vendor_name, contact_person,
        contact_phone, gst_number, email,
        address, city, active_status
    )
    VALUES(
        %s, %s, %s, %s,
        %s, %s, %s, %s
    )
    """

    values = (
         vendor_name, contact_person,
        contact_phone, gst_number, email,
        address, city, active_status
    )

    cursor.execute(sql, values)
    conn.commit()
    cursor.close()
    conn.close()

    print("Vendor record created successfully")

# 🔹 Example Input
create_task(
    
    vendor_name="Tech Supplies Pvt Ltd",
    contact_person="Ravi Kumar",
    contact_phone="9876543210",
    gst_number="27ABCDE1234F1Z5",
    email="ravi.kumar@techsupplies.com",
    address="Plot 12, IT Park Road",
    city="Hyderabad"
)