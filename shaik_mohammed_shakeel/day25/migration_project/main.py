import json
import pymysql
 
 
with open('employees.json', 'r') as file:
    employees = json.load(file)
 
 
try:
    connection = pymysql.connect(
        host='localhost',          
        user='root',              
        password='1234',        
        database='ust_mysql_db'    
    )
 
    cursor = connection.cursor()
 
   
    insert_query = """
    INSERT INTO employees (emp_id, name, department, age, city)
    VALUES (%s, %s, %s, %s, %s)
    ON DUPLICATE KEY UPDATE
    name = VALUES(name), department = VALUES(department), age = VALUES(age), city = VALUES(city);
    """
 
    for employee in employees:
        emp_data = (
            employee['emp_id'],
            employee['name'],
            employee['department'],
            employee['age'],
            employee['city']
        )
       
        cursor.execute(insert_query, emp_data)
 
   
    connection.commit()
 
   
    cursor.execute("SELECT * FROM employees")
    rows = cursor.fetchall()
 
    employees_from_db = []
    for row in rows:
        employee_dict = {
            "emp_id": row[0],
            "name": row[1],
            "department": row[2],
            "age": row[3],
            "city": row[4]
        }
        employees_from_db.append(employee_dict)
 
 
    print("Employee records from MySQL:")
    for emp in employees_from_db:
        print(emp)
 
   
    for emp in employees_from_db:
        if emp["age"] < 25:
            emp["category"] = "Fresher"
        else:
            emp["category"] = "Experienced"
 
   
    print("\nModified employee records with category:")
    for emp in employees_from_db:
        print(emp)
 
except pymysql.MySQLError as err:
    print(f"Error: {err}")
finally:
 
    cursor.close()
    connection.close()