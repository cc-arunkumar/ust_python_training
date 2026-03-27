import mysql.connector
from mysql.connector import Error  # Added to handle specific MySQL errors

# ----------------- Database Connection ----------------
# This function establishes the connection to the MySQL database
def get_connection():
    conn = mysql.connector.connect(
        host="localhost",       # MySQL server host
        user="root",            # MySQL user
        password='pass@word1',  # MySQL password
        database='ust_db'       # Database name
    )
    return conn

# ----------------- Read All Employees ----------------
# This function retrieves and prints all employees from the EMP table
def read_all_employees():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        cursor.execute("SELECT * from EMP;")  # Fetching all employee records
        rows = cursor.fetchall()  # Fetch all rows from the query result
        for emp in rows:
            print(f"ID : {emp[0]} |NAME : {emp[1]}|SALARY : {emp[2]}")
    except Error as e:
        print("Error:", e)
    finally:
        if conn.is_connected():
            cursor.close()  # Close cursor to release resources
            conn.close()    # Close connection to the database
        print("Connection closed successfully")

# ----------------- Read Employee by ID ----------------
# This function retrieves an employee record by the given ID
def read_by_id(emp_id):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        cursor.execute("SELECT * from EMP WHERE EMP_ID = %s", (emp_id, ))  # Fetch employee by ID
        rows = cursor.fetchone()  # Fetch a single result
        
        if rows:
            print("The connection was built successfully:", end="")
            print(f"ID : {rows[0]} |NAME : {rows[1]}|SALARY : {rows[2]}")
        else:
            print(f"Employee record not found: {emp_id}")
    except Error as e:
        print("Error:", e)
    finally:
        if conn.is_connected():
            cursor.close()  # Close cursor to release resources
            conn.close()    # Close connection to the database
        print("Connection closed successfully")

# ----------------- Create Employee ----------------
# This function inserts a new employee into the EMP table
def create_employee(name, salary):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        cursor.execute("INSERT INTO ust_db.emp (EMP_NAME, EMP_SALARY) VALUES (%s, %s)", (name, salary))  # Inserting employee data
        conn.commit()  # Commit the transaction to save data
        print("Employee record inserted successfully!")
    except Error as e:
        print("Error:", e)
    finally:
        if conn.is_connected():
            cursor.close()  # Close cursor to release resources
            conn.close()    # Close connection to the database
        print("Connection closed!")

# ----------------- Update Employee ----------------
# This function updates an employee's details by their ID
def update_employee_by_id(emp_id, new_name, new_salary):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        cursor.execute("UPDATE ust_db.emp SET EMP_NAME=%s, EMP_SALARY=%s WHERE EMP_ID=%s", (new_name, new_salary, emp_id))  # Update employee data
        conn.commit()  # Commit the transaction
        print("Employee updated successfully")
    except Error as e:
        print("Error:", e)
    finally:
        if conn.is_connected():
            cursor.close()  # Close cursor to release resources
            conn.close()    # Close connection to the database
        print("Connection closed!")

# ----------------- Delete Employee ----------------
# This function deletes an employee from the EMP table by their ID
def delete_by_id(emp_id):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        
        cursor.execute("SELECT * FROM ust_db.emp WHERE EMP_ID = %s", (emp_id,))  # Check if employee exists
        rows = cursor.fetchone()  # Fetch a single result
        
        if rows:
            print(f"Employee record found: ID: {rows[0]} | NAME: {rows[1]} | SALARY: {rows[2]}")
            
            cursor.execute("DELETE FROM ust_db.emp WHERE EMP_ID = %s", (emp_id,))  # Deleting employee by ID
            conn.commit()  # Commit the transaction
            print(f"Employee with ID {emp_id} has been deleted successfully.")
        else:
            print(f"Employee record not found with ID {emp_id}")
    except Error as e:
        print("Error:", e)
    finally:
        if conn.is_connected():
            cursor.close()  # Close cursor to release resources
            conn.close()    # Close connection to the database
        print("Connection closed successfully")


# read_all_employees()  
# # delete_by_id(4)       

# # update_employee_by_id(3, "Bhanu", 34555) 
# # read_by_id(3)                         
# # create_employee("Veera", 2400000)     
