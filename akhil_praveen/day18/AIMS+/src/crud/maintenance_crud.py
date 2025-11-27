import pymysql
from typing import Optional
from ..models.maintenancelog import MaintenanceLog,StatusValidate
from ..config.db_connection import get_connection
from datetime import datetime
import csv

def get_keys():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""SELECT COLUMN_NAME
    FROM INFORMATION_SCHEMA.COLUMNS
    WHERE TABLE_SCHEMA = 'ust_aims_plus'
    AND TABLE_NAME = 'maintenance_log'
    ORDER BY ORDINAL_POSITION;""")
        col = cursor.fetchall()
        keys = []
        for i in col:
            keys.append(i[0])
        return keys
    except Exception as e:
        raise
    finally:
        if conn.open:
            cursor.close()
            conn.close()
            print("Connection Closed!")

#Creating maintenance obj and inserting to db
class MaintenanceCrud:
    def create_maintenance(self,data:MaintenanceLog):
        try:
            conn = get_connection()
            cursor =conn.cursor()
            query = """
            insert into ust_aims_plus.maintenance_log (asset_tag,maintenance_type,vendor_name,description,
            cost,maintenance_date,technician_name,status) 
            values (%s,%s,%s,%s,
            %s,%s,%s,%s)
            """
            values = tuple(data.__dict__.values())
            cursor.execute(query,values)
            conn.commit()
            print("Data added successfully!")
            return data
            
                
            
        except Exception as e:
            print(e)
            raise
        finally:
            if conn.open:
                cursor.close()
                conn.close()
                print("Connection Closed!")


                
    def get_all_maintenance(self,status):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            
            keys = get_keys()
            if status=="ALL":
                query = """
                select * 
                from ust_aims_plus.maintenance_log  
                """
                cursor.execute(query)
            else:
                query = """
                select * 
                from ust_aims_plus.maintenance_log 
                where status = %s 
                """
                cursor.execute(query,(status,))
            rows = cursor.fetchall()
            if rows:
                list_rows = []
                for values in rows:
                    list_rows.append(dict(zip(keys,values)))
                return list_rows
            else:
                return None
        except Exception as e:
            raise
        finally:
            if conn.open:
                cursor.close()
                conn.close()
                print("Connection Closed!")
        
                
    def get_maintenance_by_id(self,log_id):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            
            keys = get_keys()
            query = """
            select * 
            from ust_aims_plus.maintenance_log 
            where log_id = %s 
            """
            cursor.execute(query,(log_id,))
            row = cursor.fetchone()
            if row:
                list_rows = []
                list_rows.append(dict(zip(keys,row)))
                return list_rows
            else:
                return False
        except Exception as e:
            raise
        finally:
            if conn.open:
                cursor.close()
                conn.close()
                print("Connection Closed!")
        
            
    def update_maintenance(self,id,data:MaintenanceLog):
        try:
            conn = get_connection()
            cursor =conn.cursor()
            query = """
            update ust_aims_plus.maintenance_log set asset_tag=%s,maintenance_type=%s,vendor_name=%s,description=%s
            ,cost=%s,maintenance_date=%s,technician_name=%s,status=%s where log_id=%s
            """
            values =  tuple(data.__dict__.values()) + (id,)
            cursor.execute(query,values)
            conn.commit()
            print("Data updated successfully!")
            return data
            
        except Exception as e:
            print(str(e))
            raise
        finally:
            if conn.open:
                cursor.close()
                conn.close()
                print("Connection Closed!")

    def update_maintenance_status(self,id,status):
        try:
            
            conn = get_connection()
            cursor =conn.cursor()
            query = """
            update ust_aims_plus.maintenance_log set status=%s where log_id=%s
            """
            values =  (status,id)
            cursor.execute(query,values)
            conn.commit()
            print("status updated!")
            return self.get_maintenance_by_id(id)
            # return True
                
            
        except Exception as e:
            raise
        finally:
            if conn.open:
                cursor.close()
                conn.close()
                print("Connection Closed!")  
                
    def delete_maintenance(self,id):
        try:
            conn = get_connection()
            cursor =conn.cursor()
            condition = self.get_maintenance_by_id(id)
            if condition:
                query = """
                delete from ust_aims_plus.maintenance_log 
                where log_id=%s
                """
                values =  (id,)
                cursor.execute(query,values)
                conn.commit()
                print("maintenance deleted from id = ",id)
                keys = get_keys()
                list_rows = []
                list_rows.append(dict(zip(keys,condition)))
                return list_rows
                
            else:
                return False
                
            
        except Exception as e:
            print(e)
            raise
        finally:
            if conn.open:
                cursor.close()
                conn.close()
                print("Connection Closed!")

    def get_maintenance_by_keyword(self,keyword,value):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            
            keys = get_keys()
            query = f"""
            select  *
            from ust_aims_plus.maintenance_log 
            where {keyword}=%s
            """
            cursor.execute(query,(value,))
            rows = cursor.fetchall()
            if rows:
                list_rows = []
                for values in rows:
                    list_rows.append(dict(zip(keys,values)))
                return list_rows
            else:
                return False
        except Exception as e:
            raise
        finally:
            if conn.open:
                cursor.close()
                conn.close()
                print("Connection Closed!")
                
    def get_all_maintenance_count(self):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            query = """
            select * 
            from ust_aims_plus.maintenance_log
            """
            cursor.execute(query)
            rows = cursor.fetchall()
            if rows:
                return len(rows)
            else:
                return None
        except Exception as e:
            raise
        finally:
            if conn.open:
                cursor.close()
                conn.close()
                print("Connection Closed!")
                
    # def bluk_upload(self):
    #     try:
    #         with open("C:/Users/Administrator/Desktop/ust_python_training/akhil_praveen/day18/AIMS+/database/sample_data/final/maintenance_log.csv","r") as maintenance_file:
    #             csv_file = csv.DictReader(maintenance_file)
                
    #             for data in csv_file:
    #                 self.create_maintenance(data)
    #     except Exception as e:
    #         return e

# with open("C:/Users/Administrator/Desktop/ust_python_training/akhil_praveen/day18/AIMS+/database/sample_data/final/maintenance_log.csv","r") as maintenance_file:
#     csv_file = csv.DictReader(maintenance_file)
    
#     for data in csv_file:
#         create_maintenance_log(data)