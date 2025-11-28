import pymysql
from typing import Optional
from ..models.employeedirectory import EmployeeDirectory, StatusValidate
from ..config.db_connection import get_connection
from datetime import datetime
import csv

# Function to retrieve column names from the employee_directory table
def get_keys():
    try:
        conn = get_connection()  # Establish the database connection
        cursor = conn.cursor()
        
        # Query to fetch the column names of the employee_directory table
        cursor.execute("""SELECT COLUMN_NAME
                          FROM INFORMATION_SCHEMA.COLUMNS
                          WHERE TABLE_SCHEMA = 'ust_aims_plus'
                          AND TABLE_NAME = 'employee_directory'
                          ORDER BY ORDINAL_POSITION;""")
        col = cursor.fetchall()
        keys = []
        
        # Append each column name to the keys list
        for i in col:
            keys.append(i[0])
        return keys  # Return the list of column names
    except Exception as e:
        raise
    finally:
        # Close the database connection and cursor
        if conn.open:
            cursor.close()
            conn.close()
            print("Connection Closed!")

# Class for performing CRUD operations on employee data in the database
class EmployeeCrud:
    
    # Method to insert a new employee record into the database
    def create_employee(self, data: EmployeeDirectory):
        try:
            conn = get_connection()  # Get the database connection
            cursor = conn.cursor()
            
            # Query to insert new employee data
            query = """
            insert into ust_aims_plus.employee_directory (emp_code, full_name, email, phone,
            department, location, join_date, status) 
            values (%s, %s, %s, %s,
            %s, %s, %s, %s)
            """
            values = tuple(data.__dict__.values())  # Convert the data object to a tuple
            cursor.execute(query, values)  # Execute the insertion query
            conn.commit()  # Commit the transaction to save changes
            print("Data added successfully!")
            return data  # Return the newly created employee data
            
        except Exception as e:
            print(e)
            raise
        finally:
            # Close the database connection and cursor
            if conn.open:
                cursor.close()
                conn.close()
                print("Connection Closed!")

    # Method to retrieve all employees, or filter by status
    def get_all_employee(self, status):
        try:
            conn = get_connection()  # Get the database connection
            cursor = conn.cursor()
            
            # Retrieve column names from the employee directory table
            keys = get_keys()
            
            # Query to retrieve employees based on the provided status
            if status == "ALL":
                query = """select * from ust_aims_plus.employee_directory"""
                cursor.execute(query)
            else:
                query = """select * from ust_aims_plus.employee_directory where status = %s"""
                cursor.execute(query, (status,))
            
            rows = cursor.fetchall()  # Fetch all the rows from the executed query
            if rows:
                list_rows = []
                # Convert each row to a dictionary using the column names as keys
                for values in rows:
                    list_rows.append(dict(zip(keys, values)))
                return list_rows  # Return the list of employees
            else:
                return None  # Return None if no rows are found
        except Exception as e:
            raise
        finally:
            # Close the database connection and cursor
            if conn.open:
                cursor.close()
                conn.close()
                print("Connection Closed!")

    # Method to retrieve an employee by their employee ID
    def get_employee_by_id(self, emp_id):
        try:
            conn = get_connection()  # Get the database connection
            cursor = conn.cursor()
            
            # Retrieve column names from the employee directory table
            keys = get_keys()
            query = """select * from ust_aims_plus.employee_directory where emp_id = %s"""
            cursor.execute(query, (emp_id,))
            row = cursor.fetchone()  # Fetch a single row by employee ID
            if row:
                list_rows = [dict(zip(keys, row))]  # Convert the row into a dictionary
                return list_rows  # Return the found employee data
            else:
                raise  # Raise an exception if employee is not found
        except Exception as e:
            raise
        finally:
            # Close the database connection and cursor
            if conn.open:
                cursor.close()
                conn.close()
                print("Connection Closed!")

    # Method to update an existing employee record by ID
    def update_employee(self, id, data: EmployeeDirectory):
        try:
            conn = get_connection()  # Get the database connection
            cursor = conn.cursor()
            
            # Query to update the employee data by ID
            query = """
            update ust_aims_plus.employee_directory set emp_code = %s, full_name = %s, email = %s, phone = %s,
            department = %s, location = %s, join_date = %s, status = %s where emp_id=%s
            """
            values = tuple(data.__dict__.values()) + (id,)  # Append the employee ID to the values tuple
            cursor.execute(query, values)  # Execute the update query
            conn.commit()  # Commit the transaction to save the changes
            print("Data updated successfully!")
            return data  # Return the updated employee data
            
        except Exception as e:
            print(str(e))
            raise
        finally:
            # Close the database connection and cursor
            if conn.open:
                cursor.close()
                conn.close()
                print("Connection Closed!")

    # Method to update the status of an employee by their employee ID
    def update_employee_status(self, id, status):
        try:
            conn = get_connection()  # Get the database connection
            cursor = conn.cursor()
            
            # Query to update the employee status
            query = """update ust_aims_plus.employee_directory set status=%s where emp_id=%s"""
            values = (status, id)  # Set the status and employee ID
            cursor.execute(query, values)  # Execute the update query
            conn.commit()  # Commit the transaction to save the changes
            print("Status updated!")
            return self.get_employee_by_id(id)  # Return the updated employee data
                
        except Exception as e:
            raise
        finally:
            # Close the database connection and cursor
            if conn.open:
                cursor.close()
                conn.close()
                print("Connection Closed!")

    # Method to delete an employee record by employee ID
    def delete_employee(self, id):
        try:
            conn = get_connection()  # Get the database connection
            cursor = conn.cursor()
            condition = self.get_employee_by_id(id)  # Check if the employee exists
            if condition:
                # Query to delete the employee by their employee ID
                query = """delete from ust_aims_plus.employee_directory where emp_id=%s"""
                values = (id,)  # Set the employee ID to be deleted
                cursor.execute(query, values)  # Execute the delete query
                conn.commit()  # Commit the transaction to delete the employee
                print("Employee deleted from id =", id)
                keys = get_keys()
                list_rows = [dict(zip(keys, condition))]  # Convert the deleted employee data to a dictionary
                return list_rows  # Return the deleted employee data
                
            else:
                raise  # Raise exception if employee is not found
                
        except Exception as e:
            print(e)
            raise
        finally:
            # Close the database connection and cursor
            if conn.open:
                cursor.close()
                conn.close()
                print("Connection Closed!")

    # Method to search for employees by a specific keyword and value
    def get_employee_by_keyword(self, keyword, value):
        try:
            conn = get_connection()  # Get the database connection
            cursor = conn.cursor()
            
            # Retrieve column names from the employee directory table
            keys = get_keys()
            
            # Construct the query to search for employees by the given keyword
            query = f"""select * from ust_aims_plus.employee_directory where {keyword}=%s"""
            cursor.execute(query, (value,))
            rows = cursor.fetchall()  # Fetch all matching rows
            if rows:
                list_rows = []
                # Convert each row into a dictionary
                for values in rows:
                    list_rows.append(dict(zip(keys, values)))
                return list_rows  # Return the matched employees
            else:
                raise  # Raise exception if no employees are found
        except Exception as e:
            raise
        finally:
            # Close the database connection and cursor
            if conn.open:
                cursor.close()
                conn.close()
                print("Connection Closed!")

    # Method to get the total count of employees in the employee directory
    def get_all_employee_count(self):
        try:
            conn = get_connection()  # Get the database connection
            cursor = conn.cursor()
            query = """select * from ust_aims_plus.employee_directory"""
            cursor.execute(query)
            rows = cursor.fetchall()  # Fetch all rows
            if rows:
                return len(rows)  # Return the count of rows (employees)
            else:
                return None  # Return None if no employees are found
        except Exception as e:
            raise
        finally:
            # Close the database connection and cursor
            if conn.open:
                cursor.close()
                conn.close()
                print("Connection Closed!")
    
    # Method to bulk upload assets from a CSV file     
    def bluk_upload(self):
        try:
            with open("C:/Users/Administrator/Desktop/ust_python_training/akhil_praveen/day18/AIMS+/database/sample_data/final/employee_directory.csv","r") as employee_file:
                csv_file = csv.DictReader(employee_file)
                
                for data in csv_file:
                    self.create_employee(data)
        except Exception as e:
            return e


