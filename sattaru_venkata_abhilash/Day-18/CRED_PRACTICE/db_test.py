import pymysql

# Function to establish a connection to the MySQL database
def get_connection():
    conn = pymysql.connect(
        host="localhost",  # Database host (localhost means it is running on the local machine)
        user="root",  # MySQL username
        password="pass@word1",  # MySQL password
        database="ust_db"  # Database name to connect to
    )
    return conn

# Function to read and display all employee records from the EMP table
def read_all_employees():
    conn = get_connection()  # Get a connection to the database
    cursor = conn.cursor()  # Create a cursor to interact with the database
    cursor.execute("SELECT * FROM EMP;")  # Execute the query to fetch all employees
    rows = cursor.fetchall()  # Fetch all rows from the query result
    print("\n--- All Employees ---")
    
    # Check if any employees were found
    if rows:
        # Loop through each row (representing an employee) and print details
        for emp in rows:
            print(f"ID: {emp[0]} | NAME: {emp[1]} | SALARY: {emp[2]}")
    else:
        print("No employees found.")  # If no employees are found in the database
    print("\n--- End of Employee List ---")

# Function to read a specific employee's record by employee ID
def read_employee_by_id(emp_id):
    try:
        conn = get_connection()  # Get a connection to the database
        cursor = conn.cursor()  # Create a cursor
        cursor.execute("SELECT * FROM EMP WHERE EMP_ID = %s", (emp_id,))  # Execute query with the employee ID parameter
        row = cursor.fetchone()  # Fetch a single row that matches the employee ID
        
        # Check if the employee exists
        if row:
            print(f"\n--- Employee Record (ID: {emp_id}) ---")
            print(f"ID: {row[0]} | NAME: {row[1]} | SALARY: {row[2]}")  # Display employee details
            print("--- End of Employee Record ---")
        else:
            print(f"\nEmployee with ID {emp_id} not found.")  # If no employee is found with that ID
    except Exception as e:
        print("Error: ", e)  # If there's an error during the database operation
    finally:
        cursor.close()  # Ensure the cursor is closed after the operation
        conn.close()  # Close the database connection
        print("\nConnection closed successfully.")

# Function to create a new employee record in the EMP table
def create_employee(name, salary):
    try:
        conn = get_connection()  # Get a connection to the database
        cursor = conn.cursor()  # Create a cursor to interact with the database
        cursor.execute("INSERT INTO ust_db.emp(EMP_NAME, EMP_SALARY) VALUES (%s, %s)", (name, salary))  # Insert the new employee
        conn.commit()  # Commit the transaction to make the change permanent
        print(f"\nEmployee '{name}' with salary {salary} has been added successfully.")  # Confirm successful creation
    except Exception as e:
        print("Error: ", e)  # If there's an error during the insertion
    finally:
        cursor.close()  # Close the cursor
        conn.close()  # Close the database connection
        print("\nConnection closed successfully!")

# Function to update an employee's details (name and salary) by employee ID
def update_employee_by_id(emp_id, new_name, new_salary):
    try:
        conn = get_connection()  # Get a connection to the database
        cursor = conn.cursor()  # Create a cursor
        cursor.execute("UPDATE ust_db.emp SET EMP_NAME = %s, EMP_SALARY = %s WHERE EMP_ID = %s", (new_name, new_salary, emp_id))  # Update the employee's details
        conn.commit()  # Commit the transaction to save the changes

        # Check if any rows were affected (i.e., if the employee exists)
        if cursor.rowcount > 0:
            print(f"\nEmployee with ID {emp_id} has been updated successfully to Name: {new_name}, Salary: {new_salary}.")
        else:
            print(f"\nNo employee found with ID {emp_id}.")  # If no employee is found with that ID
    except Exception as e:
        print("Exception: ", e)  # If an error occurs during the update operation
    finally:
        cursor.close()  # Close the cursor
        conn.close()  # Close the database connection
        print("\nConnection closed successfully.")

# Function to delete an employee's record by employee ID
def delete_employee_by_id(emp_id):
    try:
        conn = get_connection()  # Get a connection to the database
        cursor = conn.cursor()  # Create a cursor
        cursor.execute("DELETE FROM ust_db.emp WHERE EMP_ID = %s", (emp_id,))  # Delete the employee by ID
        conn.commit()  # Commit the transaction to save the changes

        # Check if any rows were affected (i.e., if the employee exists and was deleted)
        if cursor.rowcount > 0:
            print(f"\nEmployee with ID {emp_id} has been deleted successfully.")
        else:
            print(f"\nNo employee found with ID {emp_id}.")  # If no employee is found with that ID
    except Exception as e:
        print(f"Exception: {e}")  # If an error occurs during the deletion
    finally:
        cursor.close()  # Close the cursor
        conn.close()  # Close the database connection
        print("\nConnection closed successfully.")

# Example function calls to demonstrate sequence
print("\n=== Initial Employee List ===")
read_all_employees()  # Display all employees

# Example operations:
# create_employee("Yashwanth", 35000)  # Uncomment to add a new employee
update_employee_by_id(3, "Deepu", 320000)  # Update employee with ID 3
delete_employee_by_id(2)  # Delete employee with ID 2
read_employee_by_id(1)  # Read employee with ID 1

print("\n=== Final Employee List ===")
read_all_employees()  # Display all employees again to see changes