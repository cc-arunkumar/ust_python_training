import mysql.connector
from config import get_mysql_connection
import json

def load_data_to_mysql(data):
    conn = get_mysql_connection()
    
    if conn is None:
        print("Failed to connect to MySQL.")
        return

    try:
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS employees (
            emp_id INT PRIMARY KEY,
            name VARCHAR(50),
            department VARCHAR(30),
            age INT,
            city VARCHAR(30)
        )
        """)

        insert_query = """
        INSERT INTO employees (emp_id, name, department, age, city)
        VALUES (%s, %s, %s, %s, %s)
        ON DUPLICATE KEY UPDATE name=VALUES(name), department=VALUES(department), age=VALUES(age), city=VALUES(city)
        """
        
        for emp in data:
            cursor.execute(insert_query,(
                emp["emp_id"],emp["name"],emp["department"],emp["age"],emp["city"]
            ))
        conn.commit()
        print("Data inserted/updated successfully")
    
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    
    finally:
        cursor.close()
        conn.close()

def read_from_mysql():
    conn = get_mysql_connection()
    if conn is None:
        return []

    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM employees")
        result = cursor.fetchall()
        return result
    
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return []
    
    finally:
        conn.close()
