import pymysql

def get_connection():
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='raswanthi_1',
        database='employees_db'
    )
    return conn


# def create_table_query():
#     conn = get_connection()
#     cursor = conn.cursor()
#     cursor.execute("""
#         CREATE TABLE IF NOT EXISTS employees(
#             emp_id INT PRIMARY KEY,
#             name VARCHAR(50) NOT NULL,
#             department VARCHAR(30),
#             age INT,
#             city VARCHAR(30)
#         )
#     """)
#     conn.commit()
#     cursor.close()
#     conn.close()
# create_table_query()

# CRUD Operations

def load_jsondata_to_mysql(employees):
    conn = get_connection()
    cursor = conn.cursor()

    for emp in employees:
        try:
            cursor.execute("""
                INSERT INTO employees (emp_id, name, department, age, city)
                VALUES (%s, %s, %s, %s, %s)
            """, (emp["emp_id"], emp["name"], emp["department"], emp["age"], emp["city"]))
        except Exception as e:
            print(f"{emp['emp_id']} skipped: {str(e)}")

    conn.commit()

    cursor.execute("SELECT COUNT(*) FROM employees")
    print("Row count in MySQL:", cursor.fetchone()[0])

    cursor.close()
    conn.close()

def read_mysql():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employees")
    rows = cursor.fetchall()
    employees = []
    for row in rows:
        employees.append({
            "emp_id": row[0],
            "name": row[1],
            "department": row[2],
            "age": row[3],
            "city": row[4]
        })
    cursor.close()
    conn.close()
    return employees

def insert_employee(emp_id, name, department, age, city):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO employees (emp_id, name, department, age, city)
        VALUES (%s, %s, %s, %s, %s)
    """, (emp_id, name, department, age, city))
    conn.commit()
    cursor.close()
    conn.close()

