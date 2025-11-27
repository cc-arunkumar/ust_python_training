import csv
from ..models.employee_model import EmployeeDirectory,StatusValidator
from src.config.db_connection import get_connection
from datetime import datetime

path = "D:/ust_python_training-1/arjun_j_s/day_18/AIMS_Plus/database/sample_data/final/employee_directory.csv"

with open(path, "r") as employee_file:
    emp_data = csv.DictReader(employee_file)
    emp_data = list(emp_data)


class Employee:
            
    def create_emp(self,emp:EmployeeDirectory):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            query="""
    Insert into ust_aims_plus.employee_directory (emp_code,full_name,email,phone,department,location,join_date,status)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """
            values = tuple(emp.__dict__.values())
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

    def get_all_emp(self,status="all"):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("""SELECT column_name
FROM information_schema.columns
WHERE table_schema = 'ust_aims_plus'
  AND table_name = 'employee_directory' order by ordinal_position;""")
            head=cursor.fetchall()
            header = [col[0] for col in head]
            cursor.execute("select * from ust_aims_plus.employee_directory")
            rows = cursor.fetchall()
            if status!="all":
                cursor.execute("select * from ust_aims_plus.employee_directory where status=%s",(status,))
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

    def get_emp_by_id(self,emp_id:int):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("""SELECT column_name
FROM information_schema.columns
WHERE table_schema = 'ust_aims_plus'
  AND table_name = 'employee_directory' order by ordinal_position;""")
            head=cursor.fetchall()
            header = [col[0] for col in head]
            cursor.execute("select * from ust_aims_plus.employee_directory where emp_id=%s",(emp_id,))
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

    def get_emp_count(self):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("select * from ust_aims_plus.employee_directory")
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

    def get_employee_keyword(self,keyword,value):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("""SELECT column_name
FROM information_schema.columns
WHERE table_schema = 'ust_aims_plus'
  AND table_name = 'employee_directory' order by ordinal_position;""")
            head=cursor.fetchall()
            header = [col[0] for col in head]
            cursor.execute(f"select * from ust_aims_plus.employee_directory where {keyword}=%s",(value,))
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
        with open(path, "r") as emp_file:
            emp_data = csv.DictReader(emp_file)
            emp_data = list(emp_data)
        for data in emp_data:
            try:
                self.create_emp(data)
            except Exception as e:
                raise e
        return True


    def update_emp_status(self,emp_id,status):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            StatusValidator(status=status)
            cursor.execute("update ust_aims_plus.employee_directory set status=%s where emp_id=%s",(status,emp_id))
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


    def update_emp(self,emp_id:int,emp:EmployeeDirectory):
        try:
            conn = get_connection()
            cursor = conn.cursor()
            query="""
    Update ust_aims_plus.employee_directory set emp_code=%s,full_name=%s,email=%s,phone=%s,department=%s,location=%s,join_date=%s,status=%s
    where emp_id=%s
            """
            values = tuple(emp.__dict__.values()) + (emp_id,)
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

    def delete_emp(self,emp_id:int):
        try:
            conn = get_connection()
            cursor = conn.cursor()

            if self.get_emp_by_id(emp_id):
                cursor.execute("delete from ust_aims_plus.employee_directory where emp_id=%s",(emp_id,))
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
    



