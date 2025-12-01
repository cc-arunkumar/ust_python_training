from config.db_connection import get_connection  # Importing the get_connection function to establish DB connections

# Fetch all employees
def get_all():
    conn = get_connection()  # Establishing a connection to the database
    cursor = conn.cursor()  # Creating a cursor object to execute SQL queries
    try:
        cursor.execute("SELECT * FROM ust_emp_db.employees")  # Query to fetch all employees from the employees table
        return cursor.fetchall()  # Returning all records as a list of dictionaries
    finally:
        cursor.close()  # Closing the cursor to free up resources
        conn.close()  # Closing the database connection


# Fetch employee by ID
def get_by_id(emp_id: int):
    conn = get_connection()  # Establishing a connection to the database
    cursor = conn.cursor()  # Creating a cursor object to execute SQL queries
    try:
        cursor.execute("SELECT * FROM ust_emp_db.employees WHERE employee_id = %s", (emp_id,))  # Query to fetch an employee by their ID
        return cursor.fetchone()  # Returning the first record (single employee) as a dictionary
    finally:
        cursor.close()  # Closing the cursor
        conn.close()  # Closing the database connection


# Insert new employee
def insert_to_db(new_data):
    conn = get_connection()  # Establishing a connection to the database
    cursor = conn.cursor()  # Creating a cursor object to execute SQL queries
    try:
        cursor.execute("""  # SQL query to insert a new employee into the employees table
            INSERT INTO ust_emp_db.employees 
            (first_name, last_name, email, position, salary, hire_date)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (
            new_data.first_name,  # Inserting the first name
            new_data.last_name,  # Inserting the last name
            new_data.email,  # Inserting the email
            new_data.position,  # Inserting the position
            new_data.salary,  # Inserting the salary
            new_data.hire_date  # Inserting the hire date
        ))

        conn.commit()  # Committing the transaction to save the changes

        new_id = cursor.lastrowid  # Fetching the ID of the newly inserted record
        return get_by_id(new_id)  # Returning the newly inserted employee data by ID
    except Exception as e:
        raise ValueError("Unable to insert", e)  # Handling exceptions and raising an error if insertion fails
    finally:
        cursor.close()  # Closing the cursor
        conn.close()  # Closing the database connection


# Update employee
def update_db(emp_id: int, update_data):
    conn = get_connection()  # Establishing a connection to the database
    cursor = conn.cursor()  # Creating a cursor object to execute SQL queries
    try:
        cursor.execute("""  # SQL query to update an existing employee's details
            UPDATE ust_emp_db.employees SET
                first_name=%s,
                last_name=%s,
                email=%s,
                position=%s,
                salary=%s,
                hire_date=%s
            WHERE employee_id=%s
        """, (
            update_data.first_name,  # Updating the first name
            update_data.last_name,  # Updating the last name
            update_data.email,  # Updating the email
            update_data.position,  # Updating the position
            update_data.salary,  # Updating the salary
            update_data.hire_date,  # Updating the hire date
            emp_id  # Using the employee_id to specify which record to update
        ))

        conn.commit()  # Committing the transaction to save the changes
        return True  # Returning True indicating the update was successful
    except Exception as e:
        raise ValueError("Update not completed", e)  # Handling exceptions and raising an error if the update fails
    finally:
        cursor.close()  # Closing the cursor
        conn.close()  # Closing the database connection


# Delete employee
def delete(emp_id: int):
    conn = get_connection()  # Establishing a connection to the database
    cursor = conn.cursor()  # Creating a cursor object to execute SQL queries
    try:
        # Verify if the employee exists before attempting to delete
        cursor.execute("SELECT employee_id FROM ust_emp_db.employees WHERE employee_id=%s", (emp_id,))
        if cursor.fetchone() is None:  # If the employee does not exist, return False
            return False

        cursor.execute("DELETE FROM ust_emp_db.employees WHERE employee_id=%s", (emp_id,))  # Query to delete the employee
        conn.commit()  # Committing the transaction to save the changes
        return True  # Returning True indicating the employee was deleted
    finally:
        cursor.close()  # Closing the cursor
        conn.close()  # Closing the database connection
