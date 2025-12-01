import pymysql
from typing import List, Optional
from models import EmployeeTraining


# Function to create and return DB connection
def get_db_connection():
    conn = pymysql.connect(
        host="localhost",
        user="root",
        password="pass1word",
        database="ust_training_db"
    )
    return conn


# Function to fetch all training records from DB
def fetch_all_employee():
    conn = get_db_connection()      # Create DB connection
    cursor = conn.cursor()          # Create cursor to execute SQL queries
    try:
        cursor.execute("SELECT * FROM training_requests")  # Run query
        return cursor.fetchall()    # Return all fetched rows
    except Exception as e:
        raise e
    finally:
        cursor.close()              # Always close cursor
        conn.close()                # Always close connection


# Function to fetch a specific record by ID
def fetch_employee_by_id(id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "SELECT * FROM training_requests WHERE id = %s", (id,)
        )  # Execute parameterized query
        return cursor.fetchone()  # Return first matched row
    except Exception as e:
        raise e
    finally:
        cursor.close()
        conn.close()


# Function to insert a new employee training record
def create_new_emp_training(emp: EmployeeTraining):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            '''
            INSERT INTO training_requests
            (employee_id, employee_name, training_title, training_description, requested_date, status, manager_id, last_updated)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            ''',
            (
                emp.employee_id,
                emp.employee_name,
                emp.training_title,
                emp.training_description,
                emp.requested_date,
                emp.status,
                emp.manager_id,
                emp.last_updated
            )
        )
        conn.commit()  # Commit insert transaction
    except Exception as e:
        raise e
    finally:
        cursor.close()
        conn.close()


# Function to update a full training record using ID
def update_emp_training(id: int, emp: EmployeeTraining):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            '''
            UPDATE training_requests
            SET employee_id = %s, employee_name = %s, training_title = %s,
                training_description = %s, requested_date = %s, status = %s,
                manager_id = %s, last_updated = %s
            WHERE id = %s
            ''',
            (
                emp.employee_id,
                emp.employee_name,
                emp.training_title,
                emp.training_description,
                emp.requested_date,
                emp.status,
                emp.manager_id,
                emp.last_updated,
                id
            )
        )
        conn.commit()  # Apply update
    except Exception as e:
        raise e
    finally:
        cursor.close()
        conn.close()


# Function to update only the status of a training request
def update_emp_status(id: int, status: str):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "UPDATE training_requests SET status = %s WHERE id = %s",
            (status, id)
        )
        conn.commit()  # Save status update
    except Exception as e:
        raise e
    finally:
        cursor.close()
        conn.close()


# Function to delete a specific record by ID
def remove_emp_training(id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "DELETE FROM training_requests WHERE id = %s", (id,)
        )  # Delete the record
        conn.commit()  # Commit delete action
    except Exception as e:
        raise e
    finally:
        cursor.close()
        conn.close()
