import pymysql
from datetime import datetime
def get_connection():
    conn = pymysql.connect(
        host="localhost",
        user="root",
        password="pass@word1",
        database="ust_db"
    )
    return conn

def read_all_employees():
    try:
        conn=get_connection()
        cursor=conn.cursor()
        
        cursor.execute("SELECT * FROM EMP;")
        row=cursor.fetchall()
        for emp in row:
            print(f"ID:{emp[0]},NAME:{emp[1]},SALARY:{emp[2]}")
    except Exception as e:
        print("Error:",e)
    finally:
        if conn:
            cursor.close()
            conn.close()
    
def read_employee_by_id(emp_id):
    try:
        conn=get_connection()
        cursor=conn.cursor()
        
        cursor.execute("SELECT * FROM EMP WHERE EMP_ID=%s",(emp_id))
        row=cursor.fetchone()
        if row:
            print("Read employee data with id:",end="")
            print(f"ID:{row[0]},NAME:{row[1]},SALARY:{row[2]}")
            return row
        else:
            return None
    except Exception as e:
        print("Error:",e)
    finally:
        if conn:
            cursor.close()
            conn.close()
        print("connection closed")
            
def create_employee(name,sal):
    try:
        conn=get_connection()
        cursor=conn.cursor()
        cursor.execute("INSERT INTO EMP (EMP_NAME, EMP_SALARY) VALUES (%s, %s)",(name,sal))
        conn.commit()
        print("Employee added..")
    except Exception as e:
        print("Error:",e)
        
    finally:
        if conn:
            cursor.close()
            conn.close() 
        print("Connection closed")
        
def update_asset(asset_id, asset_type, manufacturer, model, warranty_years, asset_status, assigned_to):
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            UPDATE asset_inventory
            SET asset_type=%s,
                manufacturer=%s,
                model=%s,
                warranty_years=%s,
                asset_status=%s,
                assigned_to=%s,
                last_updated=%s
            WHERE asset_id=%s
        """, (asset_type, manufacturer, model, warranty_years, asset_status, assigned_to, datetime.now(), asset_id))

        conn.commit()
        if cursor.rowcount == 0:
            print("Asset not found.")
        else:
            print("Asset updated successfully.")

    except Exception as e:
        print("Error:", e)

    finally:
        if conn:
            cursor.close()
            conn.close()
        print("Connection closed")
        
def delete_employee(emp_id):
    try:
        conn=get_connection()
        cursor=conn.cursor()

        emp_deleted=read_employee_by_id(emp_id)
        if emp_deleted:
            cursor.execute("delete FROM EMP WHERE EMP_ID=%s" ,(emp_id))
            conn.commit()
            print(f"Employee with ID {emp_id} deleted successfully!")
        else:
            print(f"No employee found with ID {emp_id}.")
        
    except Exception as e:
        print("Error:",e)
        
    finally:
        if conn:
            cursor.close()
            conn.close()
        
        

         

# read_all_employees()
# # read_employee_by_id(1)
# create_employee("ROHIT",74000)
# update_employee(1,"PRITHVI",72000)
delete_employee(6)
read_all_employees()

