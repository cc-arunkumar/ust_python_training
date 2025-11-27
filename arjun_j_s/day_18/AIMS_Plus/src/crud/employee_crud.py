import csv
from ..models.employee_model import EmployeeDirectory
from src.config.db_connection import get_connection

path = "D:/ust_python_training-1/arjun_j_s/day_18/AIMS_Plus/database/sample_data/final/employee_directory.csv"

with open(path, "r") as employee_file:
    emp_data = csv.DictReader(employee_file)
    emp_data = list(emp_data)

def create_emp(emp:EmployeeDirectory):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        query="""
Insert into ust_aims_plus.employee_directory (emp_code,full_name,email,phone,department,location,join_date,status)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = tuple(emp.values())
        cursor.execute(query,values)
        conn.commit()
        print("Data added successfully")
    except Exception as e:
        print(str(e))
    finally:
        if conn.open:
            cursor.close()
            conn.close()
        print("Connection Closed")

# for data in emp_data:
#     try:
#         create_emp(data)
#     except Exception as e:
#         print(str(e))
    



