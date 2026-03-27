import pymysql
from config import MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DATABASE
from modify_data import modify_data  # Import the modify_data function

def read_from_mysql():
    # MySQL connection setup
    conn = pymysql.connect(
        host=MYSQL_HOST,
        user=MYSQL_USER,
        password=MYSQL_PASSWORD,
        database=MYSQL_DATABASE
    )

    cursor = conn.cursor()

    # Read all employee rows
    cursor.execute("SELECT * FROM employees")
    employees = cursor.fetchall()

    # Convert to Python dictionaries
    employees_data = []
    for emp in employees:
        employees_data.append({
            "emp_id": emp[0],
            "name": emp[1],
            "department": emp[2],
            "age": emp[3],
            "city": emp[4]
        })

    # Modify the data (add category field)
    modified_employees = modify_data(employees_data)

    # Print the modified employee data
    print(modified_employees)

    cursor.close()
    conn.close()

# Call the function to read data from MySQL and modify it
read_from_mysql()

# [{'emp_id': 201, 'name': 'Anu Joseph', 'department': 'AI', 'age': 23, 'city': 'Trivandrum', 'category': 'Fresher'}, {'emp_id': 202, 'name': 'Rahul Menon', 'department': 'Cloud', 'age': 26, 'city': 'Kochi', 'category': 'Experienced'}, {'emp_id': 203, 'name': 'Sahana R', 'department': 'Testing', 'age': 22, 'city': 'Chennai', 'category': 'Fresher'}, {'emp_id': 204, 'name': 'Vishnu Prakash', 'department': 'Cybersecurity', 'age': 29, 'city': 'Trivandrum', 'category': 'Experienced'}, {'emp_id': 205, 'name': 'Maya Kumar', 'department': 'AI', 'age': 25, 'city': 'Bangalore', 'category': 'Experienced'}]
