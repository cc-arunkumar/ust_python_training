import pymysql
import csv
from datetime import datetime

def get_Connection():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="pass@word1",
        database="ust_aims_plus"
    )
 
def create_assets():
    try:
        conn = get_Connection()
        cursor = conn.cursor()
        query = """
        INSERT INTO ust_aims_plus.vendor_master(
            vendor_name, contact_person, contact_phone,
            gst_number, email, address,
            city, active_status
        ) VALUES (%s,%s,%s,
        %s,%s,%s,
        %s,%s)
        """

        with open("C:/Users/Administrator/Desktop/ust_python_training-1/felix/day-13/my-first-fastapi-app/day-18/aims_final_project/database/sample_data/final/vendor_master.csv", "r") as file:
            content = csv.DictReader(file)
            for row in content:
                try:
                    data = (
                        row["vendor_name"],
                        row["contact_person"],
                        row["contact_phone"],
                        row["gst_number"],
                        row["email"],
                        row["address"],
                        row["city"],
                        row["active_status"]
                    )
                    cursor.execute(query, data)
                except Exception as e:
                    print(e, row)
 
        conn.commit()
        print("Asset records inserted successfully")
    except Exception as e:
        print("Database error:", e)
    finally:
        if conn.open:
            cursor.close()
            conn.close()
        print("Connection closed")

 
create_assets()