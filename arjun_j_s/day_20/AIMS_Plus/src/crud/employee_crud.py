import csv
from ..models.employee_model import EmployeeDirectory, StatusValidator
from src.config.db_connection import get_connection
from datetime import datetime

path = "D:/ust_python_training-1/arjun_j_s/day_18/AIMS_Plus/database/sample_data/final/employee_directory.csv"

class Employee:

    def get_headers(self):  # Get column names of employee_directory table
        conn = None
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("""
                SELECT column_name
                FROM information_schema.columns
                WHERE table_schema = 'ust_aims_plus'
                  AND table_name = 'employee_directory'
                ORDER BY ordinal_position;
            """)
            head = cursor.fetchall()
            return [col[0] for col in head]
        except Exception as e:
            raise e
        finally:
            if conn and conn.open:
                cursor.close()
                conn.close()
            print("Connection Closed")

    def create_emp(self, emp: EmployeeDirectory):  # Insert new employee record
        try:
            conn = get_connection()
            cursor = conn.cursor()
            query = """
                INSERT INTO ust_aims_plus.employee_directory 
                (emp_code, full_name, email, phone, department, location, join_date, status)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """
            values = tuple(emp.__dict__.values())
            cursor.execute(query, values)
            conn.commit()
            print("Data added successfully")
            return True
        except Exception as e:
            print(str(e))
        finally:
            if conn.open:
                cursor.close()
                conn.close()
            print("Connection Closed")

    def get_all_emp(self, status="all"):  # Get all employees (optionally filter by status)
        try:
            conn = get_connection()
            cursor = conn.cursor()
            header = self.get_headers()
            if status != "all":
                cursor.execute("SELECT * FROM ust_aims_plus.employee_directory WHERE status=%s", (status,))
            else:
                cursor.execute("SELECT * FROM ust_aims_plus.employee_directory")
            rows = cursor.fetchall()
            if rows:
                return [dict(zip(header, data)) for data in rows]
            return None
        except Exception as e:
            raise e
        finally:
            if conn.open:
                cursor.close()
                conn.close()
                print("Connection Closed")

    def get_emp_by_id(self, emp_id: int):  # Get employee by ID
        try:
            conn = get_connection()
            cursor = conn.cursor()
            header = self.get_headers()
            cursor.execute("SELECT * FROM ust_aims_plus.employee_directory WHERE emp_id=%s", (emp_id,))
            row = cursor.fetchone()
            if row:
                return dict(zip(header, row))
            return None
        except Exception as e:
            raise e
        finally:
            if conn.open:
                cursor.close()
                conn.close()
            print("Connection Closed")

    def get_emp_count(self):  # Get total employee count
        try:
            conn = get_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM ust_aims_plus.employee_directory")
            row = cursor.fetchall()
            return len(row) if row else None
        except Exception as e:
            raise e
        finally:
            if conn.open:
                cursor.close()
                conn.close()
            print("Connection Closed")

    def get_employee_keyword(self, keyword, value):  # Search employees by keyword/value
        try:
            conn = get_connection()
            cursor = conn.cursor()
            header = self.get_headers()
            cursor.execute(f"SELECT * FROM ust_aims_plus.employee_directory WHERE {keyword}=%s", (value,))
            rows = cursor.fetchall()
            if rows:
                return [dict(zip(header, row)) for row in rows]
            return None
        except Exception as e:
            raise e
        finally:
            if conn.open:
                cursor.close()
                conn.close()
            print("Connection Closed")

    def bulk_upload(self):  # Bulk upload employees from CSV file
        with open(path, "r") as emp_file:
            emp_data = csv.DictReader(emp_file)
            emp_data = list(emp_data)
        for data in emp_data:
            try:
                self.create_emp(data)
            except Exception as e:
                raise e
        return True

    def update_emp_status(self, emp_id, status):  # Update employee status by ID
        try:
            conn = get_connection()
            cursor = conn.cursor()
            StatusValidator(status=status)
            cursor.execute("UPDATE ust_aims_plus.employee_directory SET status=%s WHERE emp_id=%s", (status, emp_id))
            conn.commit()
            print("Status Updated")
            return True
        except Exception as e:
            raise e
        finally:
            if conn.open:
                cursor.close()
                conn.close()
            print("Connection Closed")

    def update_emp(self, emp_id: int, emp: EmployeeDirectory):  # Update full employee record
        try:
            conn = get_connection()
            cursor = conn.cursor()
            query = """
                UPDATE ust_aims_plus.employee_directory 
                SET emp_code=%s, full_name=%s, email=%s, phone=%s, department=%s, location=%s, join_date=%s, status=%s
                WHERE emp_id=%s
            """
            values = tuple(emp.__dict__.values()) + (emp_id,)
            cursor.execute(query, values)
            conn.commit()
            print("Data updated successfully")
            return True
        except Exception as e:
            print(str(e))
            raise e
        finally:
            if conn.open:
                cursor.close()
                conn.close()
            print("Connection Closed")

    def delete_emp(self, emp_id: int):  # Delete employee by ID
        try:
            conn = get_connection()
            cursor = conn.cursor()
            if self.get_emp_by_id(emp_id):
                cursor.execute("DELETE FROM ust_aims_plus.employee_directory WHERE emp_id=%s", (emp_id,))
                conn.commit()
                print("Deleted Successfully")
                return True
            return None
        except Exception as e:
            raise e
        finally:
            if conn.open:
                cursor.close()
                conn.close()
            print("Connection Closed")