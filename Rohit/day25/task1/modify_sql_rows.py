import pymysql
from db_connection import get_connection

try:

    conn = get_connection()
    cursor = conn.cursor(pymysql.cursors.DictCursor)  

    cursor.execute("SELECT * FROM employees")
    employees = cursor.fetchall()   


    modified_employees = []
    for emp in employees:
        emp["category"] = "Fresher" if emp["age"] <= 25 else "Experienced"
        modified_employees.append(emp)


    for emp in modified_employees:
        print(emp)

finally:
    if cursor: cursor.close()
    if conn: conn.close()
