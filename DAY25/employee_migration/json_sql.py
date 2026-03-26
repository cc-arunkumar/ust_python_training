import json
from db_connection import get_db_connection

def load_mysql():
    try:
        with open("employees.json","r") as f:
            employees=json.load(f)
            
        conn=get_db_connection()
        cursor=conn.cursor()
        
        for i in employees:
            emp_id=i["emp_id"]
            name=i["name"]
            department=i["department"]
            age=i["age"]
            city=i["city"]
            
            cursor.execute("""
            INSERT INTO employees (emp_id, name, department, age, city)
            VALUES (%s, %s, %s, %s, %s)
            """, (emp_id, name, department, age, city))
            
        conn.commit()
        cursor.execute("SELECT COUNT(*) FROM employees")
        row_count=cursor.fetchone()[0]
        # print(f"Count: {row_count}")
        if cursor:
            print("Data Loaded Sucessfully")

    except Exception as e:
        print(f"Error loading - MySQL: {e}")
    
    finally:
        if conn:
            cursor.close()
            conn.close()



