import csv
from ..models.maintenance_model import MaintenanceLog,StatusValidator
from src.config.db_connection import get_connection

path = "D:/ust_python_training-1/arjun_j_s/day_18/AIMS_Plus/database/sample_data/final/maintenance_log.csv"

with open(path, "r") as maintenance_file:
    maintenance_data = csv.DictReader(maintenance_file)
    maintenance_data = list(maintenance_data)

class Maintain:
            
    def create_maintenance(self,maintenance:MaintenanceLog):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            query="""
    Insert into ust_aims_plus.maintenance_log (asset_tag,maintenance_type,vendor_name,description,cost,maintenance_date,technician_name,status)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """
            values = tuple(maintenance.__dict__.values())
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

    def get_all_log(self,status="all"):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("""SELECT column_name
FROM information_schema.columns
WHERE table_schema = 'ust_aims_plus'
  AND table_name = 'maintenance_log' order by ordinal_position;""")
            head=cursor.fetchall()
            header = [col[0] for col in head]
            cursor.execute("select * from ust_aims_plus.maintenance_log")
            rows = cursor.fetchall()
            if status!="all":
                cursor.execute("select * from ust_aims_plus.maintenance_log where status=%s",(status,))
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

    def get_log_by_id(self,log_id:int):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("""SELECT column_name
FROM information_schema.columns
WHERE table_schema = 'ust_aims_plus'
  AND table_name = 'maintenance_log' order by ordinal_position;""")
            head=cursor.fetchall()
            header = [col[0] for col in head]
            cursor.execute("select * from ust_aims_plus.maintenance_log where log_id=%s",(log_id,))
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

    def get_log_count(self):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("select * from ust_aims_plus.maintenance_log")
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

    def get_log_keyword(self,keyword,value):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("""SELECT column_name
FROM information_schema.columns
WHERE table_schema = 'ust_aims_plus'
  AND table_name = 'maintenance_log' order by ordinal_position;""")
            head=cursor.fetchall()
            header = [col[0] for col in head]
            cursor.execute(f"select * from ust_aims_plus.maintenance_log where {keyword}=%s",(value,))
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
        with open(path, "r") as log_file:
            log_data = csv.DictReader(log_file)
            log_data = list(log_data)
        for data in log_data:
            try:
                self.create_maintenance(data)
            except Exception as e:
                raise e
        return True


    def update_log_status(self,log_id,status):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            StatusValidator(status=status)
            cursor.execute("update ust_aims_plus.maintenance_log set status=%s where log_id=%s",(status,log_id))
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


    def update_log(self,log_id:int,maintain:MaintenanceLog):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            query="""
    Update ust_aims_plus.maintenance_log set asset_tag=%s,maintenance_type=%s,vendor_name=%s,description=%s,cost=%s,maintenance_date=%s,technician_name=%s,status=%s
    where log_id=%s
            """
            values = tuple(maintain.__dict__.values()) + (log_id,)
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

    def delete_log(self,log_id:int):
        try:
            conn = get_connection()
            cursor = conn.cursor()

            if self.get_log_by_id(log_id):
                cursor.execute("delete from ust_aims_plus.maintenance_log where log_id=%s",(log_id,))
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
    



