import pymysql

def get_mysql_connection():
    """Establish connection to MySQL using PyMySQL"""
    try:
        connection = pymysql.connect(
            host='localhost',
            user='root',
            password='password1',
            database='ust_mysql_db'
        )
        return connection
    except pymysql.MySQLError as e:
        print(f"Error connecting to MySQL: {e}")
        return None


def create_mysql_table():
    """Create employees table in MySQL if it doesn't exist"""
    connection = get_mysql_connection()
    print("Connecting to MySQL...")
    if connection:
        cursor = connection.cursor()
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS employees (
            emp_id INT PRIMARY KEY AUTO_INCREMENT,
            name VARCHAR(50) NOT NULL,
            department VARCHAR(30),
            age INT,
            city VARCHAR(30)
        )
        """)
        connection.commit()  # Commit changes
        connection.close()   # Close the connection
        print("MySQL table created successfully.")
    else:
        print("Failed to establish MySQL connection.")


def insert_employee_data(employee_data):
    connection = get_mysql_connection()
    if connection:
        cursor = connection.cursor()
        print(f"Inserting data: {employee_data}")
        for employee in employee_data:
            cursor.execute("""
            INSERT INTO employees (name, department, age, city)
            VALUES (%s, %s, %s, %s)
            """, (employee['name'], employee['department'], employee['age'], employee['city']))
        connection.commit()
        connection.close()
        print("Employee data inserted into MySQL.")


def fetch_all_employees():
    """Fetch all employee records from MySQL and return them as a list of dictionaries"""
    connection = get_mysql_connection()
    if connection:
        cursor = connection.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM employees")
        employees = cursor.fetchall()  # Fetch all records
        connection.close()  # Close the connection
        return employees  # Return fetched data
    else:
        print("Failed to establish MySQL connection.")
        return []


def update_employee_data(emp_id, updated_data):
    """Update employee data in MySQL by emp_id"""
    connection = get_mysql_connection()
    if connection:
        cursor = connection.cursor()
        cursor.execute("""
        UPDATE employees
        SET name = %s, department = %s, age = %s, city = %s
        WHERE emp_id = %s
        """, (updated_data['name'], updated_data['department'], updated_data['age'], updated_data['city'], emp_id))
        connection.commit()  # Commit the update
        connection.close()   # Close the connection
        print(f"Employee with emp_id {emp_id} updated successfully.")
    else:
        print("Failed to establish MySQL connection.")


def delete_employee(emp_id):
    """Delete an employee from MySQL by emp_id"""
    connection = get_mysql_connection()
    if connection:
        cursor = connection.cursor()
        cursor.execute("DELETE FROM employees WHERE emp_id = %s", (emp_id,))
        connection.commit()  # Commit the deletion
        connection.close()   # Close the connection
        print(f"Employee with emp_id {emp_id} deleted successfully.")
    else:
        print("Failed to establish MySQL connection.")
