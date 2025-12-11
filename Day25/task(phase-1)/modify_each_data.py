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


def fetch_and_modify_employees():
    conn = get_db_connection()
    cursor = conn.cursor(pymysql.cursors.DictCursor) 

    try:
        cursor.execute("SELECT * FROM new_data")
        employees = cursor.fetchall()  
        
        modified_employees = []
        
        for employee in employees:
            if employee['age'] <= 25:
                employee['category'] = 'Fresher'
            else:
                employee['category'] = 'Experienced'
            
            modified_employees.append(employee)
            print(employee)
        return modified_employees
    except Exception as e:

        print(f"Exception occurred: {str(e)}")
        