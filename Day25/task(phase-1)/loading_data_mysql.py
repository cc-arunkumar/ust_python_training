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

with open('sample.json', 'r') as file:
    employees_data = json.load(file)

def insert_employee_data(data):
    conn = get_db_connection()
    cursor = conn.cursor()

    for emp in data:
        try:
            emp_id = emp.get("emp_id")
            name = emp.get("name")
            age = emp.get("age")
            department = emp.get("department")
            city = emp.get("city")  
            
            print(f"Processing emp_id: {emp_id}, city: {city}") 
            print(f"Inserting data for emp_id: {emp_id}, city: {city}") 
            cursor.execute("""
                INSERT INTO new_data (emp_id, name, age, department, city)
                VALUES (%s, %s, %s, %s, %s)
            """, (emp_id, name, age, department, city))
            conn.commit()
            
        except Exception as e:
            print(f"Exception occurred: {str(e)}")

insert_employee_data(employees_data)



def fetch_all_employees():
    conn = get_db_connection()
    cursor = conn.cursor(pymysql.cursors.DictCursor)

    try:
        cursor.execute("SELECT * FROM new_data")
        employees = cursor.fetchall() 
        print("Employee data from the database:")
        for employee in employees:
            print(employee)  
    except Exception as e:
        print(f"Error fetching employee data: {str(e)}")
    finally:
        cursor.close()
        conn.close()
fetch_all_employees()