import json
import pymysql
from config import MYSQL_CONFIG

def load_json_to_mysql():
    # Connect to MySQL
    conn = pymysql.connect(**MYSQL_CONFIG)
    cursor = conn.cursor()

    # Load JSON file
    with open(r"C:\Users\Administrator\Desktop\Training\ust_python_training\harsh\day25\UST – Employee Migration & Processing\employee.json", "r") as f:
        data = json.load(f)
        employees=data["employees"]

    # Insert records into existing table
    insert_sql = """
        INSERT IGNORE INTO employees (emp_id, name, department, age, city)
        VALUES (%s, %s, %s, %s, %s)
    """
    for emp in employees:
        cursor.execute(insert_sql, (
            emp.get("emp_id"),
            emp.get("name"),
            emp.get("department"),
            emp.get("age"),
            emp.get("city")
        ))

    conn.commit()

    # Confirm row count
    cursor.execute("SELECT COUNT(*) AS count FROM employees")
    result = cursor.fetchone()
    print(f" JSON data loaded into MySQL. Current row count: {result[0]}")

    # Cleanup
    cursor.close()
    conn.close()

