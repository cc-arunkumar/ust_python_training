import pymysql

# Create and return a connection to MySQL database
def get_db_connection():
    conn = pymysql.connect(
        host="localhost",
        user="root",
        password="pass1word",
        database="ust_mysql_db"
    )
    return conn

# Fetch all employees from the database and add a 'category' field based on age
def fetch_and_modify_employees():
    conn = get_db_connection()
    cursor = conn.cursor(pymysql.cursors.DictCursor) 

    try:
        # Fetch all employees from table
        cursor.execute("SELECT * FROM employees")
        employees = cursor.fetchall()  
        
        modified_employees = []
        
        # Add category based on age
        for employee in employees:
            if employee['age'] <= 25:
                employee['category'] = 'Fresher'
            else:
                employee['category'] = 'Experienced'
            
            modified_employees.append(employee)
            print(employee)  
        return modified_employees
    except Exception as e:
        print(f"Exception occurred: {str(e)}")

        


