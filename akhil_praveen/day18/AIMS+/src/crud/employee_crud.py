import pymysql
from typing import Optional
from ..models.employeedirectory import EmployeeDirectory,StatusValidate
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
    AND TABLE_NAME = 'employee_directory'
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

#Creating employee obj and inserting to db
class EmployeeCrud:
    def create_employee(self,data:EmployeeDirectory):
        try:
            conn = get_connection()
            cursor =conn.cursor()
            query = """
            insert into ust_aims_plus.employee_directory (emp_code,full_name,email,phone,
            department,location,join_date,status) 
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


                
    def get_all_employee(self,status):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            
            keys = get_keys()
            if status=="ALL":
                query = """
                select * 
                from ust_aims_plus.employee_directory  
                """
                cursor.execute(query)
            else:
                query = """
                select * 
                from ust_aims_plus.employee_directory 
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
        
                
    def get_employee_by_id(self,emp_id):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            
            keys = get_keys()
            query = """
            select * 
            from ust_aims_plus.employee_directory 
            where emp_id = %s 
            """
            cursor.execute(query,(emp_id,))
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
        
            
    def update_employee(self,id,data:EmployeeDirectory):
        try:
            conn = get_connection()
            cursor =conn.cursor()
            query = """
            update ust_aims_plus.employee_directory set emp_code = %s,full_name = %s,email = %s,phone = %s,
            department = %s,location = %s,join_date = %s,status = %s where emp_id=%s
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

    def update_employee_status(self,id,status):
        try:
            
            conn = get_connection()
            cursor =conn.cursor()
            query = """
            update ust_aims_plus.employee_directory set status=%s where emp_id=%s
            """
            values =  (status,id)
            cursor.execute(query,values)
            conn.commit()
            print("status updated!")
            return self.get_employee_by_id(id)
            # return True
                
            
        except Exception as e:
            raise
        finally:
            if conn.open:
                cursor.close()
                conn.close()
                print("Connection Closed!")  
                
    def delete_employee(self,id):
        try:
            conn = get_connection()
            cursor =conn.cursor()
            condition = self.get_employee_by_id(id)
            if condition:
                query = """
                delete from ust_aims_plus.employee_directory 
                where emp_id=%s
                """
                values =  (id,)
                cursor.execute(query,values)
                conn.commit()
                print("employee deleted from id = ",id)
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

    def get_employee_by_keyword(self,keyword,value):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            
            keys = get_keys()
            query = f"""
            select  *
            from ust_aims_plus.employee_directory 
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
                
    def get_all_employee_count(self):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            query = """
            select * 
            from ust_aims_plus.employee_directory
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
    #         with open("C:/Users/Administrator/Desktop/ust_python_training/akhil_praveen/day18/AIMS+/database/sample_data/final/employee_directory.csv","r") as employee_file:
    #             csv_file = csv.DictReader(employee_file)
                
    #             for data in csv_file:
    #                 self.create_employee(data)
    #     except Exception as e:
    #         return e

# with open("C:/Users/Administrator/Desktop/ust_python_training/akhil_praveen/day18/AIMS+/database/sample_data/final/employee_directory.csv","r") as employee_file:
#     csv_file = csv.DictReader(employee_file)
    
#     for data in csv_file:
#         create_employee(data)


