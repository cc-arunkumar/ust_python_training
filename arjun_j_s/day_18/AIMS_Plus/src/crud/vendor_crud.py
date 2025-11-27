import csv
from ..models.vendor_model import VendorMaster,StatusValidator
from src.config.db_connection import get_connection

path = "D:/ust_python_training-1/arjun_j_s/day_18/AIMS_Plus/database/sample_data/final/vendor_master.csv"

with open(path, "r") as vendor_file:
    vendor_data = csv.DictReader(vendor_file)
    vendor_data = list(vendor_data)


class Vendor:
            
    def create_vendor(self,vendor:VendorMaster):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            query="""
    Insert into ust_aims_plus.vendor_master (vendor_name,contact_person,contact_phone,gst_number,email,address,city,active_status)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """
            values = tuple(vendor.__dict__.values())
            cursor.execute(query,values)
            conn.commit()
            print("Data added successfully")
            return True
        except Exception as e:
            print(str(e))
        finally:
            if conn.open:
                cursor.close()
                conn.close()
            print("Connection Closed")

    def get_all_vendor(self,status="all"):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("""SELECT column_name
FROM information_schema.columns
WHERE table_schema = 'ust_aims_plus'
  AND table_name = 'vendor_master' order by ordinal_position;""")
            head=cursor.fetchall()
            header = [col[0] for col in head]
            cursor.execute("select * from ust_aims_plus.vendor_master")
            rows = cursor.fetchall()
            if status!="all":
                cursor.execute("select * from ust_aims_plus.vendor_master where active_status=%s",(status,))
                rows = cursor.fetchall()
            if rows:
                response = []
                for data in rows:
                    response.append(dict(zip(header, data)))
                return response
            else:
                return None
        except Exception as e:
            raise e
        finally:
            if conn.open:
                cursor.close()
                conn.close()
                print("Connection Closed")

    def get_vendor_by_id(self,vendor_id:int):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("""SELECT column_name
FROM information_schema.columns
WHERE table_schema = 'ust_aims_plus'
  AND table_name = 'vendor_master' order by ordinal_position;""")
            head=cursor.fetchall()
            header = [col[0] for col in head]
            cursor.execute("select * from ust_aims_plus.vendor_master where vendor_id=%s",(vendor_id,))
            row = cursor.fetchone()
            if row:
                return dict(zip(header,row))
            else:
                return None
        except Exception as e:
            raise e
        finally:
            if conn.open:
                cursor.close()
                conn.close()
            print("Connection Closed")

    def get_vendor_count(self):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("select * from ust_aims_plus.vendor_master")
            row = cursor.fetchall()
            if row:
                return len(row)
            else:
                return None
        except Exception as e:
            raise e
        finally:
            if conn.open:
                cursor.close()
                conn.close()
            print("Connection Closed")

    def get_vendor_keyword(self,keyword,value):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("""SELECT column_name
FROM information_schema.columns
WHERE table_schema = 'ust_aims_plus'
  AND table_name = 'vendor_master' order by ordinal_position;""")
            head=cursor.fetchall()
            header = [col[0] for col in head]
            cursor.execute(f"select * from ust_aims_plus.vendor_master where {keyword}=%s",(value,))
            rows = cursor.fetchall()
            if rows:
                response=[]
                for row in rows:
                    response.append(dict(zip(header,row)))
                return response
            else:
                return None
        except Exception as e:
            raise e
        finally:
            if conn.open:
                cursor.close()
                conn.close()
            print("Connection Closed")

    def bulk_upload(self):
        with open(path, "r") as vendor_file:
            vendor_data = csv.DictReader(vendor_file)
            vendor_data = list(vendor_data)
        for data in vendor_data:
            try:
                self.create_vendor(data)
            except Exception as e:
                raise e
        return True


    def update_vendor_status(self,vendor_id,status):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            StatusValidator(active_status=status)
            cursor.execute("update ust_aims_plus.vendor_master set active_status=%s where vendor_id=%s",(status,vendor_id))
            conn.commit()
            print("Status Updated")
            return True
        except Exception as e:
            raise e
        finally:
            if conn.open:
                cursor.close()
                conn.close()
            print("Connection Closed")


    def update_vendor(self,vendor_id:int,vendor:VendorMaster):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            query="""
    Update ust_aims_plus.vendor_master set vendor_name=%s,contact_person=%s,contact_phone=%s,gst_number=%s,email=%s,address=%s,city=%s,active_status=%s
    where vendor_id=%s
            """
            values = tuple(vendor.__dict__.values()) + (vendor_id,)
            cursor.execute(query,values)
            conn.commit()
            print("Data updated successfully")
            return True
        except Exception as e:
            print(str(e))
            raise e
        finally:
            if conn.open:
                cursor.close()
                conn.close()
            print("Connection Closed")

    def delete_vendor(self,vendor_id:int):
        try:
            conn = get_connection()
            cursor = conn.cursor()

            if self.get_vendor_by_id(vendor_id):
                cursor.execute("delete from ust_aims_plus.vendor_master where vendor_id=%s",(vendor_id,))
                print("Deleted Successfully")
                conn.commit()
                return True
            else:
                return None
        except Exception as e:
            raise e
        finally:
            if conn.open:
                cursor.close()
                conn.close()
            print("Connection Closed")
    




    



