from ..model.employee_model import EmployeeModel
from ..config.db_connection import get_connection
from fastapi import HTTPException, status


def get_keys():
    """
    Retrieve column names (keys) from the employees table in the database.

    Returns:
        list[str]: A list of column names ordered by their position in the table.
    """
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT COLUMN_NAME
            FROM INFORMATION_SCHEMA.COLUMNS
            WHERE TABLE_SCHEMA = 'ust_db'
              AND TABLE_NAME = 'employees'
            ORDER BY ORDINAL_POSITION;
        """)
        col = cursor.fetchall()
        keys = [i[0] for i in col]  # Extract column names
        return keys
    except Exception as e:
        # Raise HTTPException for API clients if DB query fails
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail=str(e)
        )
    finally:
        # Ensure connection is closed properly
        if conn.open:
            cursor.close()
            conn.close()
            print("Connection Closed!")


class EmployeeCrud:
    """
    CRUD operations for Employee records in the database.
    Provides methods to create, read, update, and delete employees.
    """

    def create_employee(self, employee: EmployeeModel):
        """
        Insert a new employee record into the database.

        Args:
            employee (EmployeeModel): Employee data to be inserted.

        Returns:
            EmployeeModel: The created employee object.
        """
        try:
            conn = get_connection()
            cursor = conn.cursor()
            query = """
                INSERT INTO ust_db.employees (
                    first_name, last_name, email, position,
                    salary, hire_date
                )
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            # Convert EmployeeModel to tuple of values
            values = tuple(employee.__dict__.values())
            cursor.execute(query, values)
            conn.commit()
            print("Employee record added successfully!")
            return employee
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_502_BAD_GATEWAY,
                detail=str(e)
            )
        finally:
            if conn.open:
                cursor.close()
                conn.close()
                print("Connection Closed!")

    def get_all_employee(self):
        """
        Retrieve all employee records from the database.

        Returns:
            list[dict]: List of employees as dictionaries with column names as keys.
        """
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM ust_db.employees")
            rows = cursor.fetchall()
            data = [dict(zip(get_keys(), row)) for row in rows]
            return data
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_502_BAD_GATEWAY,
                detail=str(e)
            )
        finally:
            if conn.open:
                cursor.close()
                conn.close()
                print("Connection closed")

    def get_employee_by_id(self, emp_id: int):
        """
        Retrieve a single employee record by ID.

        Args:
            emp_id (int): Employee ID.

        Returns:
            dict: Employee record as a dictionary.
        """
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute(
                "SELECT * FROM ust_db.employees WHERE employee_id = %s",
                (emp_id,)
            )
            record = cursor.fetchone()
            keys = get_keys()
            return dict(zip(keys, record))
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_502_BAD_GATEWAY,
                detail=str(e)
            )
        finally:
            if conn.open:
                cursor.close()
                conn.close()
                print("Connection closed")

    def update_employee(self, emp_id: int, employee: EmployeeModel):
        """
        Update an existing employee record.

        Args:
            emp_id (int): Employee ID to update.
            employee (EmployeeModel): Updated employee data.

        Returns:
            EmployeeModel: The updated employee object.
        """
        try:
            conn = get_connection()
            cursor = conn.cursor()
            query = """
                UPDATE ust_db.employees
                SET first_name = %s, last_name = %s, email = %s, position = %s,
                    salary = %s, hire_date = %s
                WHERE employee_id = %s
            """
            cursor.execute(
                query,
                (
                    employee.first_name,
                    employee.last_name,
                    employee.email,
                    employee.position,
                    employee.salary,
                    employee.hire_date,
                    emp_id
                )
            )
            conn.commit()
            return employee
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_502_BAD_GATEWAY,
                detail=str(e)
            )
        finally:
            if conn.open:
                cursor.close()
                conn.close()
                print("Connection closed")

    def delete_employee(self, emp_id: int):
        """
        Delete an employee record by ID.

        Args:
            emp_id (int): Employee ID to delete.

        Returns:
            str: Confirmation message.
        """
        try:
            conn = get_connection()
            cursor = conn.cursor()
            query = "DELETE FROM ust_db.employees WHERE employee_id = %s"
            cursor.execute(query, (emp_id,))
            conn.commit()
            return "Employee record deleted"
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_502_BAD_GATEWAY,
                detail=str(e)
            )
        finally:
            if conn.open:
                cursor.close()
                conn.close()
                print("Connection closed")