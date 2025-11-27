import csv
import pymysql

def get_connection():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="pass@word1",
        database="ust_asset_inventory"
    )

conn = get_connection()
cursor = conn.cursor()

input_file = r"C:\Users\Administrator\Desktop\ust_python_training\Rohit\day18\ust_ITSM\data\new_vendor_master(in).csv"

with open(input_file, mode="r", encoding="utf-8") as file1:
    reader = csv.DictReader(file1)

    for row in reader:
        try:
            sql = """
            INSERT INTO vendor_master (
                vendor_id, vendor_name, contact_person, contact_phone,
                gst_number, email, address, city, active_status
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """

            values = (
                row["vendor_id"],
                row["vendor_name"],
                row["contact_person"],
                row["contact_phone"],
                row["gst_number"],
                row["email"],
                row["address"],
                row["city"],
                row["active_status"],  
            )

            cursor.execute(sql, values)

        except Exception as e:
            print(f"Error inserting vendor_id {row['vendor_id']}: {e}")

    conn.commit()

cursor.close()
conn.close()

print("CSV data successfully dumped into vendor_master table.")
