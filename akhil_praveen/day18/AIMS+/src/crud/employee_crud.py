import pymysql
from typing import Optional
from ..models.employeedirectory import EmployeeDirectory
from ..config.db_connection import get_connection
from datetime import datetime
import csv

#Creating asset obj and inserting to db
def create_employee(data:EmployeeDirectory):
    try:
        conn = get_connection()
        cursor =conn.cursor()
        query = "insert into ust_aims_plus.employee_directory (emp_code,full_name,email,phone,department,location,join_date,status) values (%s,%s,%s,%s,%s,%s,%s,%s)"
        values = tuple(data.values()) 
        cursor.execute(query,values)
        conn.commit()
            
        
    except Exception as e:
        print("Exception : ",e)
    finally:
        if conn.open:
            cursor.close()
            conn.close()
            
# with open("C:/Users/Administrator/Desktop/ust_python_training/akhil_praveen/day18/AIMS+/database/sample_data/final/employee_directory.csv","r") as employee_file:
#     csv_file = csv.DictReader(employee_file)
    
#     for data in csv_file:
#         create_employee(data)