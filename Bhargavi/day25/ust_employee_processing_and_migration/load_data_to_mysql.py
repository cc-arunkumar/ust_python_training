import json
import pymysql
from config import MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DATABASE

def load_data_to_mysql():
    # Read employees data from JSON file
    with open('employees.json') as f:
        employees_data = json.load(f)
    
    # Database connection using PyMySQL
    conn = pymysql.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DATABASE
    )

    if conn.open:
        print("Successfully connected to the database.")
    else:
        print("Failed to connect to the database.")
        return

    cursor = conn.cursor()

    # Insert employee data
    for employee in employees_data:
        print(f"Checking if employee {employee['emp_id']} exists...")
        cursor.execute("SELECT COUNT(*) FROM employees WHERE emp_id=%s", (employee['emp_id'],))
        result = cursor.fetchone()

        if result[0] == 0:
            try:
                cursor.execute("""
                INSERT INTO employees(emp_id, name, department, age, city)
                VALUES (%s, %s, %s, %s, %s)
                """, (employee['emp_id'], employee['name'], employee['department'], employee['age'], employee['city']))
                print(f"Inserted employee {employee['emp_id']}:{employee['name']}")
            except pymysql.MySQLError as err:
                print(f"Error while inserting employee {employee['emp_id']}: {err}")
        else:
            print(f"Employee {employee['emp_id']} already exists, skipping insertion.")
    
    conn.commit()  # Commit the transaction
    print("Data loading completed")
    
    cursor.close()
    conn.close()

# Call the function to load data into MySQL
load_data_to_mysql()
