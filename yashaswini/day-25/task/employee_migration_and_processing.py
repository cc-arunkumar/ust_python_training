import pymysql
import json

# MySQL connection function
def get_connection():
    return pymysql.connect(
        host="localhost", 
        user="root", 
        password="password123", 
        database="ust_mysql_db", 
    )

# Read JSON file
with open(r'C:\Users\Administrator\Desktop\training\ust_python_training\yashaswini\day-25\task\data.json', 'r') as file:
    employees_data = json.load(file)

# MySQL Insert Query
query = """
    INSERT INTO employees (emp_id, name, department, age, city, category)
    VALUES (%s, %s, %s, %s, %s, %s)
    ON DUPLICATE KEY UPDATE
    name=VALUES(name), department=VALUES(department), age=VALUES(age), city=VALUES(city), category=VALUES(category);
"""

# Modify data based on age
def modify_data():
    try:
        # Check if 'category' column exists in the 'employees' table
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SHOW COLUMNS FROM employees LIKE 'category';")
        result = cursor.fetchone()

        if not result:
            # Add 'category' column if it doesn't exist
            alter_query = "ALTER TABLE employees ADD COLUMN category VARCHAR(20);"
            cursor.execute(alter_query)
            conn.commit()
            print("Column 'category' added successfully.")
        else:
            print("Column 'category' already exists.")

        # Modify employee data with category based on age
        for employee in employees_data:
            employee["category"] = "Fresher" if employee["age"] < 25 else "Experienced"

        # Insert or update records into MySQL
        for employee in employees_data:
            cursor.execute(query, (employee["emp_id"], employee["name"], employee["department"], employee["age"], employee["city"], employee["category"]))

        conn.commit()

        # Confirm row count after insertion
        cursor.execute("SELECT COUNT(*) FROM employees")
        row_count = cursor.fetchone()[0]  
        print(f"Row count: {row_count}")

        print("Data inserted/updated successfully with category.")

    except Exception as e:
        print("Error:", e)
        if conn:
            conn.rollback()

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

# Task 1 and 2: Insert and read data
def read_data():
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM employees")
        employees = cursor.fetchall()

        for employee in employees:
            print(employee)

    except Exception as e:
        print("Error:", e)

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

# Running the tasks in sequence
modify_data()          # Task 3: Modify data and insert into MySQL
read_data()            # Task 2: Read data from MySQL





# with open(r'C:\Users\Administrator\Desktop\training\ust_python_training\yashaswini\day-25\task\data.json', 'r') as file:
