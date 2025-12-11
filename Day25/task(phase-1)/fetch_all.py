import pymysql
import json

def get_db_connection():
    try:
        conn = pymysql.connect(
        host = "localhost",
        user = "root",
        password = "pass@word1",
        database = "aims_plus",
        )
        return conn
    except Exception as e:
        raise(f"Database connection failed {str(e)}") 

def fetch_all_employees():
    conn = get_db_connection()
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    try:
        cursor.execute("SELECT * FROM new_data")
        employees = cursor.fetchall() 
        print("Employee data from the database:")
        for employee in employees:
            print(employee)  
        return employees
    except Exception as e:
        print(f"Error fetching employee data: {str(e)}")
    finally:
        cursor.close()
        conn.close()
fetch_all_employees()
