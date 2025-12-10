#Task UST – Employee Migration & Processing

import json
import pymysql

# Connect to MySQL database
conn = pymysql.connect(
    host="localhost",
    user="root",
    password="pass@word1",
    database="ust_mysql_db",
    cursorclass=pymysql.cursors.DictCursor
)
cursor = conn.cursor()

def load_json_to_mysql(json_file):
    # Load employee data from JSON file
    with open(json_file, "r") as f:
        employees = json.load(f)

    # Insert each employee record into MySQL
    for emp in employees:
        try:
            cursor.execute(
                "INSERT INTO employees (emp_id, name, department, age, city) VALUES (%s, %s, %s, %s, %s)",
                (emp["emp_id"], emp["name"], emp["department"], emp["age"], emp["city"])
            )
        except Exception:
            # Skip duplicates based on emp_id
            print(f"Duplicate emp_id {emp['emp_id']} skipped")
    conn.commit()

def read_mysql_to_python():
    # Read all employee records from MySQL
    cursor = conn.cursor()
    cursor.execute("SELECT emp_id, name, department, age, city FROM employees")
    rows = cursor.fetchall()
    return rows

if __name__ == "__main__":
    # Load JSON data into MySQL
    load_json_to_mysql("employees.json")
    # Read back data into Python
    employees = read_mysql_to_python()
    print("Employees from MySQL:", employees)

    # Close cursor and connection
    cursor.close()
    conn.close()


#Sample Execution
# Employees from MySQL: [{'emp_id': 201, 'name': 'Anu Joseph', 'department': 'AI', 'age': 23, 'city': 'Trivandrum'}, {'emp_id': 202, 'name': 'Rahul Menon', 'department': 'Cloud', 'age': 26, 'city': 'Kochi'}, {'emp_id': 203, 'name': 'Sahana R', 'department': 'Testing', 'age': 22, 'city': 'Chennai'}, {'emp_id': 204, 'name': 'Vishnu Prakash', 'department': 'Cybersecurity', 'age': 29, 'city': 'Trivandrum'}, {'emp_id': 205, 'name': 'Maya Kumar', 'department': 'AI', 'age': 25, 'city': 'Bangalore'}]