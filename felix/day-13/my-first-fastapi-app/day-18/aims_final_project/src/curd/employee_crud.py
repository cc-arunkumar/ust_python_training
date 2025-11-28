import pymysql
from typing import Optional
from ..models.employeedirectory import EmployeeDirectory, StatusValidate
from ..config.db_connection import get_connection
from datetime import datetime
import csv


def get_keys():
    """
    Retrieve column names (keys) from the employee_directory table in the database.

    Returns:
        list[str]: A list of column names ordered by their position in the table.
    """
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT COLUMN_NAME
            FROM INFORMATION_SCHEMA.COLUMNS
            WHERE TABLE_SCHEMA = 'ust_aims_plus'
            AND TABLE_NAME = 'employee_directory'
            ORDER BY ORDINAL_POSITION;
        """)
        col = cursor.fetchall()
        keys = [i[0] for i in col]  # Extract column names
        return keys
    except Exception as e:
        raise
    finally:
        if conn.open:
            cursor.close()
            conn.close()
            print("Connection Closed!")


# CRUD operations for Employee Directory
class EmployeeCrud:
    def create_employee(self, data: EmployeeDirectory):
        """
        Insert a new employee record into the employee_directory table.

        Args:
            data (EmployeeDirectory): Employee details provided as a Pydantic model.

        Returns:
            EmployeeDirectory: The inserted employee data.
        """
        try:
            conn = get_connection()
            cursor = conn.cursor()
            query = """
                INSERT INTO ust_aims_plus.employee_directory (
                    emp_code, full_name, email, phone,
                    department, location, join_date, status
                )
                VALUES (%s, %s, %s, %s,
                        %s, %s, %s, %s)
            """
            values = tuple(data.__dict__.values())
            cursor.execute(query, values)
            conn.commit()
            print("Data added successfully!")
            return data
        except Exception as e:
            print(e)
            raise
        finally:
            if conn.open:
                cursor.close()
                conn.close()
                print("Connection Closed!")

    def get_all_employee(self, status):
        """
        Retrieve all employees or filter by status.

        Args:
            status (str): 'ALL' to fetch all employees, or a specific status value.

        Returns:
            list[dict] | None: List of employees as dictionaries, or None if no records found.
        """
        try:
            conn = get_connection()
            cursor = conn.cursor()
            keys = get_keys()

            if status == "ALL":
                query = "SELECT * FROM ust_aims_plus.employee_directory"
                cursor.execute(query)
            else:
                query = "SELECT * FROM ust_aims_plus.employee_directory WHERE status = %s"
                cursor.execute(query, (status,))

            rows = cursor.fetchall()
            if rows:
                return [dict(zip(keys, values)) for values in rows]
            return None
        except Exception as e:
            raise
        finally:
            if conn.open:
                cursor.close()
                conn.close()
                print("Connection Closed!")

    def get_employee_by_id(self, emp_id):
        """
        Retrieve a single employee by their ID.

        Args:
            emp_id (int): Unique identifier of the employee.

        Returns:
            list[dict] | bool: Employee details as a dictionary inside a list, or False if not found.
        """
        try:
            conn = get_connection()
            cursor = conn.cursor()
            keys = get_keys()

            query = "SELECT * FROM ust_aims_plus.employee_directory WHERE emp_id = %s"
            cursor.execute(query, (emp_id,))
            row = cursor.fetchone()

            if row:
                return [dict(zip(keys, row))]
            return False
        except Exception as e:
            raise
        finally:
            if conn.open:
                cursor.close()
                conn.close()
                print("Connection Closed!")

    def update_employee(self, id, data: EmployeeDirectory):
        """
        Update an existing employee record by ID.

        Args:
            id (int): Employee ID to update.
            data (EmployeeDirectory): Updated employee details.

        Returns:
            EmployeeDirectory: Updated employee data.
        """
        try:
            conn = get_connection()
            cursor = conn.cursor()
            query = """
                UPDATE ust_aims_plus.employee_directory
                SET emp_code=%s, full_name=%s, email=%s, phone=%s,
                    department=%s, location=%s, join_date=%s, status=%s
                WHERE emp_id=%s
            """
            values = tuple(data.__dict__.values()) + (id,)
            cursor.execute(query, values)
            conn.commit()
            print("Data updated successfully!")
            return data
        except Exception as e:
            print(str(e))
            raise
        finally:
            if conn.open:
                cursor.close()
                conn.close()
                print("Connection Closed!")

    def update_employee_status(self, id, status):
        """
        Update only the status of an employee.

        Args:
            id (int): Employee ID.
            status (str): New status value.

        Returns:
            list[dict]: Updated employee details.
        """
        try:
            conn = get_connection()
            cursor = conn.cursor()
            query = "UPDATE ust_aims_plus.employee_directory SET status=%s WHERE emp_id=%s"
            cursor.execute(query, (status, id))
            conn.commit()
            print("Status updated!")
            return self.get_employee_by_id(id)
        except Exception as e:
            raise
        finally:
            if conn.open:
                cursor.close()
                conn.close()
                print("Connection Closed!")

    def delete_employee(self, id):
        """
        Delete an employee by ID.

        Args:
            id (int): Employee ID.

        Returns:
            list[dict] | bool: Deleted employee details, or False if not found.
        """
        try:
            conn = get_connection()
            cursor = conn.cursor()
            condition = self.get_employee_by_id(id)

            if condition:
                query = "DELETE FROM ust_aims_plus.employee_directory WHERE emp_id=%s"
                cursor.execute(query, (id,))
                conn.commit()
                print("Employee deleted from id =", id)

                keys = get_keys()
                return [dict(zip(keys, condition))]
            return False
        except Exception as e:
            print(e)
            raise
        finally:
            if conn.open:
                cursor.close()
                conn.close()
                print("Connection Closed!")

    def get_employee_by_keyword(self, keyword, value):
        """
        Search employees dynamically by a given column (keyword) and value.

        Args:
            keyword (str): Column name to filter by.
            value (str): Value to match.

        Returns:
            list[dict] | bool: Matching employees, or False if none found.
        """
        try:
            conn = get_connection()
            cursor = conn.cursor()
            keys = get_keys()

            query = f"SELECT * FROM ust_aims_plus.employee_directory WHERE {keyword}=%s"
            cursor.execute(query, (value,))
            rows = cursor.fetchall()

            if rows:
                return [dict(zip(keys, values)) for values in rows]
            return False
        except Exception as e:
            raise
        finally:
            if conn.open:
                cursor.close()
                conn.close()
                print("Connection Closed!")

    def get_all_employee_count(self):
        """
        Count total number of employees in the directory.

        Returns:
            int | None: Number of employees, or None if no records exist.
        """
        try:
            conn = get_connection()
            cursor = conn.cursor()
            query = "SELECT * FROM ust_aims_plus.employee_directory"
            cursor.execute(query)
            rows = cursor.fetchall()
            return len(rows) if rows else None
        except Exception as e:
            raise
        finally:
            if conn.open:
                cursor.close()
                conn.close()
                print("Connection Closed!")
