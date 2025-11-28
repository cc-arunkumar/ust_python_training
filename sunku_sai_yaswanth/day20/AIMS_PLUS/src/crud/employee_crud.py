import csv
from typing import Optional

from models.employee_model import EmployeeDirectory
from config.db_connection import get_connection

# query = """
# INSERT INTO ust_aims_db.employee_directory (
#     emp_code,full_name,email,phone,department,location,join_date,status
# ) VALUES (
#     %s, %s, %s, %s, %s,
#     %s, %s, %s
# )
# """
# try:
#     conn=get_connection()
#     cursor=conn.cursor()
#     with open("valid_rows_emp.csv", "r", encoding="utf-8") as file:
#         reader = csv.DictReader(file)

#         for row in reader:
#             data = (
#                 row["emp_code"],
#                 row["full_name"],
#                 row["email"],
#                 row["phone"],
#                 row["department"],
#                 row["location"],
#                 row["join_date"],
#                 row["status"]
#             )
#             cursor.execute(query, data)
    
#     conn.commit()

# except Exception as e:
#     print(f"Error",e)

# finally:
    
#     if conn:
#         cursor.close()
#         conn.close()



def get_all(status_filter:Optional[str]=""):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        if status_filter=="":
            cursor.execute("SELECT * FROM ust_aims_db.employee_directory")
        else:
            cursor.execute("SELECT * FROM ust_aims_db.employee_directory WHERE status=%s",(status_filter, ))
        
        row = cursor.fetchall()
        
        return row if row else None
    except Exception as e:
        raise ValueError
    
    finally:
        if conn:
            cursor.close()
            conn.close()




def get_by_id(emp_id):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM ust_aims_db.employee_directory WHERE emp_id= %s", (emp_id,))
        row = cursor.fetchone()
        
        return row if row else None
    except Exception as e:
        raise ValueError
    finally:
        if conn:
            cursor.close()
            conn.close()

       
def insert_emp(new_emp: EmployeeDirectory):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        # Proceed with insertion if no duplicate
        cursor.execute(
            """
            INSERT INTO ust_aims_db.employee_directory (
#     emp_code,full_name,email,phone,department,location,join_date,status
# ) VALUES (
#     %s, %s, %s, %s, %s,
#     %s, %s, %s
# )
            """, (
                new_emp.emp_code,
                new_emp.full_name,
                new_emp.email,
                new_emp.phone,
                new_emp.department,
                new_emp.location,
                new_emp.join_date,
                new_emp.status
            )
        )
        conn.commit()
        
    except Exception as e:
        print(f"Error: {e}")
        
    finally:
        if conn:
            cursor.close()
            conn.close()


from fastapi import HTTPException

def update_emp_by_id(emp_id: int, update_emp: EmployeeDirectory):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        # Check if the employee exists
        existing_emp = get_by_id(emp_id)
        if not existing_emp:
            raise HTTPException(status_code=404, detail=f"Employee with ID {emp_id} not found.")
        
        # Proceed with the update
        cursor.execute("""
        UPDATE ust_aims_db.employee_directory 
        SET 
            full_name = %s,
            email = %s,
            phone = %s,
            department = %s,
            location = %s,
            join_date = %s,
            status = %s
        WHERE emp_id = %s
        """, (
            update_emp.full_name,
            update_emp.email,
            update_emp.phone,
            update_emp.department,
            update_emp.location,
            update_emp.join_date,
            update_emp.status,
            emp_id 
        ))
        
        conn.commit()
        return update_emp  
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error updating employee: {str(e)}")
    finally:
        if conn:
            cursor.close()
            conn.close()

          
def delete_emp(emp_id):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        
        if get_by_id(emp_id):
            cursor.execute("DELETE FROM ust_aims_db.employee_directory WHERE emp_id = %s", (emp_id,))
            conn.commit()
            return True
        else:
            raise ValueError
        
    except Exception as e:
        raise ValueError
    finally:
        if conn:
            cursor.close()
            conn.close()


def search_emp(field_type:str,keyword : str):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM ust_aims_db.employee_directory WHERE {field_type} LIKE %s",(f'%{keyword}%',))
        data = cursor.fetchall()
        return data
   
    except Exception as e:
        raise Exception(f"Error: {e}")
   
    finally:
        if conn.open:
            cursor.close()
            conn.close()

# valid_rows_emp = []
# invalid_rows_emp = []

# required_fields_emp = [
#     "emp_code",
#     "full_name",
#     "email",
#     "phone",
#     "department",
#     "location",
#     "join_date",
#     "status"
# ]


# with open("employee_directory.csv", "r") as file:
#     csv_reader = csv.DictReader(file)
#     header = csv_reader.fieldnames

#     for row in csv_reader:
#         try:
#             valid = EmployeeDirectory(**row)
#             valid_rows_emp.append(valid.model_dump())  
            
#         except Exception as e:
#             row['error'] = str(e)  
#             invalid_rows_emp.append(row)

# fieldnames_emp = required_fields_emp + ['error']  

# with open("valid_rows_emp.csv", "w", newline='') as file:
#     writer = csv.DictWriter(file, fieldnames=required_fields_emp)
#     writer.writeheader()
#     for row in valid_rows_emp:
#         row.pop('emp_id',None)
#         writer.writerow(row) 

# with open("invalid_rows_emp.csv", "w", newline='') as file:
#     writer = csv.DictWriter(file, fieldnames=fieldnames_emp)
#     writer.writeheader()
#     for row in invalid_rows_emp:
#         row.pop('emp_id',None)
#         writer.writerow(row)
