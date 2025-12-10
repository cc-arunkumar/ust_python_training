import json
import pymysql

# Function to establish connection with MySQL database
def get_connection():
    conn = pymysql.connect(
        host="localhost",        
        user="root",            
        password="pass1word",    
        database="ust_mysql_db"  
    )
    return conn   


JSON_PATH = r"C:\Users\Administrator\Desktop\training\ust_python_training\ashutosh_samal\Day25\employee_migration_and_processing\employees.json"

# Open and load the existing employee data from the JSON file
with open(JSON_PATH, "r") as employee_json_file:
    emp = json.load(employee_json_file)   
 

# Function to insert employee data into MySQL database
def insert_data(data):
    try:
        conn = get_connection()
        cursor = conn.cursor()   
        for row in data:
            emp_id = row['emp_id']          
            name = row['name']              
            department = row['department']  
            age = row['age']                
            city = row['city']              

            # Execute SQL INSERT query to add employee record into 'employees' table
            cursor.execute('''INSERT INTO employees(emp_id, name, department, age, city)
                               VALUES (%s, %s, %s, %s, %s)''',
                           (emp_id, name, department, age, city))
            conn.commit()

        print("Data inserted successfully")
    except Exception as e:
        print("Error:", e)

    finally:
        if cursor: cursor.close()
        if conn: conn.close()
        print("Connection closed")

# Call the function to insert employee data from JSON into MySQL
insert_data(emp)
