from datetime import datetime
from typing import Optional

from config.db_connection import get_db_connection
from exceptions.custom_exception import (
    RecordNotFoundException,
    DuplicateRecordException,
    ValidationErrorException,
    DatabaseConnectionException,
)
from models.employee_model import EmployeeCreate, EmployeeUpdate
import csv
from os import path

VALID_DEPARTMENTS = ["HR", "IT", "Admin", "Finance"]
VALID_LOCATIONS = ["TVM", "Bangalore", "Chennai", "Hyderabad"]
VALID_STATUS = ["Active", "Inactive", "Resigned"]


def validate_employee(data: EmployeeCreate | EmployeeUpdate):
    # emp_code validation only for create (we check in create function)
    if hasattr(data, "emp_code"):
        if not data.emp_code.startswith("USTEMP-"):
            raise ValidationErrorException("emp_code must start with 'USTEMP-'")

    if not data.full_name.replace(" ", "").isalpha():
        raise ValidationErrorException("full_name must contain only alphabets and spaces")

    if not data.email.endswith("@ust.com"):
        raise ValidationErrorException("email must end with @ust.com")

    if not (data.phone.isdigit() and len(data.phone) == 10 and data.phone[0] in "6789"):
        raise ValidationErrorException("phone must be a valid 10-digit Indian mobile number")

    if data.department not in VALID_DEPARTMENTS:
        raise ValidationErrorException("Invalid department")

    if data.location not in VALID_LOCATIONS:
        raise ValidationErrorException("Invalid location")

    try:
        join_date = datetime.strptime(data.join_date, "%Y-%m-%d")
        if join_date > datetime.now():
            raise ValidationErrorException("join_date cannot be in the future")
    except Exception:
        raise ValidationErrorException("join_date must be in YYYY-MM-DD format")

    if data.status not in VALID_STATUS:
        raise ValidationErrorException("Invalid status")


def create_employee(payload: EmployeeCreate):
    validate_employee(payload)

    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        # check duplicate emp_code
        cursor.execute("SELECT emp_id FROM employee_directory WHERE emp_code = %s", (payload.emp_code,))
        if cursor.fetchone():
            raise DuplicateRecordException("emp_code already exists")

        insert_query = """
            INSERT INTO employee_directory (
                emp_code, full_name, email, phone,
                department, location, join_date, status
            ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
        """

        cursor.execute(
            insert_query,
            (
                payload.emp_code,
                payload.full_name,
                payload.email,
                payload.phone,
                payload.department,
                payload.location,
                payload.join_date,
                payload.status,
            ),
        )
        conn.commit()

        emp_id = cursor.lastrowid
        cursor.execute("SELECT * FROM employee_directory WHERE emp_id = %s", (emp_id,))
        row = cursor.fetchone()
        return row
    except (DuplicateRecordException, ValidationErrorException):
        raise
    except Exception as e:
        raise DatabaseConnectionException(str(e))
    finally:
        try:
            cursor.close()
            conn.close()
        except:
            pass


def list_employees(status: Optional[str] = None):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        if status:
            cursor.execute("SELECT * FROM employee_directory WHERE status = %s", (status,))
        else:
            cursor.execute("SELECT * FROM employee_directory")

        rows = cursor.fetchall()
        return rows
    except Exception as e:
        raise DatabaseConnectionException(str(e))
    finally:
        try:
            cursor.close()
            conn.close()
        except:
            pass


def get_employee_by_id(emp_id: int):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM employee_directory WHERE emp_id = %s", (emp_id,))
        row = cursor.fetchone()
        if not row:
            raise RecordNotFoundException("Employee not found")
        return row
    except RecordNotFoundException:
        raise
    except Exception as e:
        raise DatabaseConnectionException(str(e))
    finally:
        try:
            cursor.close()
            conn.close()
        except:
            pass


def update_employee(emp_id: int, payload: EmployeeUpdate):
    validate_employee(payload)

    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT emp_id FROM employee_directory WHERE emp_id = %s", (emp_id,))
        if not cursor.fetchone():
            raise RecordNotFoundException("Employee not found")

        update_query = """
            UPDATE employee_directory
            SET full_name=%s,
                email=%s,
                phone=%s,
                department=%s,
                location=%s,
                join_date=%s,
                status=%s
            WHERE emp_id=%s
        """

        cursor.execute(
            update_query,
            (
                payload.full_name,
                payload.email,
                payload.phone,
                payload.department,
                payload.location,
                payload.join_date,
                payload.status,
                emp_id,
            ),
        )
        conn.commit()

        cursor.execute("SELECT * FROM employee_directory WHERE emp_id = %s", (emp_id,))
        row = cursor.fetchone()
        return row
    except (RecordNotFoundException, ValidationErrorException):
        raise
    except Exception as e:
        raise DatabaseConnectionException(str(e))
    finally:
        try:
            cursor.close()
            conn.close()
        except:
            pass


def update_employee_status(emp_id: int, new_status: str):
    if new_status not in VALID_STATUS:
        raise ValidationErrorException("Invalid status")

    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT emp_id FROM employee_directory WHERE emp_id = %s", (emp_id,))
        if not cursor.fetchone():
            raise RecordNotFoundException("Employee not found")

        cursor.execute(
            "UPDATE employee_directory SET status = %s WHERE emp_id = %s",
            (new_status, emp_id),
        )
        conn.commit()

        cursor.execute("SELECT * FROM employee_directory WHERE emp_id = %s", (emp_id,))
        row = cursor.fetchone()
        return row
    except (RecordNotFoundException, ValidationErrorException):
        raise
    except Exception as e:
        raise DatabaseConnectionException(str(e))
    finally:
        try:
            cursor.close()
            conn.close()
        except:
            pass


def delete_employee(emp_id: int):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT emp_id FROM employee_directory WHERE emp_id = %s", (emp_id,))
        if not cursor.fetchone():
            raise RecordNotFoundException("Employee not found")

        cursor.execute("DELETE FROM employee_directory WHERE emp_id = %s", (emp_id,))
        conn.commit()
        return True
    except RecordNotFoundException:
        raise
    except Exception as e:
        raise DatabaseConnectionException(str(e))
    finally:
        try:
            cursor.close()
            conn.close()
        except:
            pass


def search_employee(keyword: str):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        like = f"%{keyword}%"
        cursor.execute(
            """
            SELECT * FROM employee_directory
            WHERE emp_code LIKE %s
               OR full_name LIKE %s
               OR email LIKE %s
            """,
            (like, like, like),
        )
        rows = cursor.fetchall()
        return rows
    except Exception as e:
        raise DatabaseConnectionException(str(e))
    finally:
        try:
            cursor.close()
            conn.close()
        except:
            pass


def count_employees():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) AS cnt FROM employee_directory")
        row = cursor.fetchone()
        return row["cnt"] if isinstance(row, dict) else row[0]
    except Exception as e:
        raise DatabaseConnectionException(str(e))
    finally:
        try:
            cursor.close()
            conn.close()
        except:
            pass


def bulk_upload_employees_from_csv():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        base_dir = path.dirname(path.dirname(__file__))  # src -> aims_plus
        csv_path = path.join(base_dir, "Assignment", "cleaned", "employee_directory_validated.csv")

        with open(csv_path, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            insert_query = """
                INSERT INTO employee_directory (
                    emp_code, full_name, email, phone,
                    department, location, join_date, status
                ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
            """

            for row in reader:
                cursor.execute(
                    insert_query,
                    (
                        row["emp_code"],
                        row["full_name"],
                        row["email"],
                        row["phone"],
                        row["department"],
                        row["location"],
                        row["join_date"],
                        row["status"],
                    ),
                )

        conn.commit()
        return True
    except Exception as e:
        raise DatabaseConnectionException(str(e))
    finally:
        try:
            cursor.close()
            conn.close()
        except:
            pass
