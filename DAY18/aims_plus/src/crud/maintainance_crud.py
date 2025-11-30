from datetime import datetime
from typing import Optional
from config.db_connection import get_db_connection
from exceptions.custom_exception import (
    RecordNotFoundException,
    ValidationErrorException,
    DatabaseConnectionException,
)
from models.maintainance_model import MaintenanceCreate, MaintenanceUpdate
import csv
from os import path

VALID_TYPES = ["Repair", "Service", "Upgrade"]
VALID_STATUS = ["Completed", "Pending"]


def validate_maintenance(data: MaintenanceCreate | MaintenanceUpdate):
    if not data.asset_tag.startswith("UST-"):
        raise ValidationErrorException("asset_tag must start with 'UST-'")

    if data.maintenance_type not in VALID_TYPES:
        raise ValidationErrorException("Invalid maintenance_type")

    if not data.vendor_name.replace(" ", "").isalpha():
        raise ValidationErrorException("Invalid vendor_name")

    if not data.description or len(data.description.strip()) < 10:
        raise ValidationErrorException("description must be at least 10 characters")

    if data.cost <= 0:
        raise ValidationErrorException("cost must be > 0")

    try:
        maint_date = datetime.strptime(data.maintenance_date, "%Y-%m-%d")
        if maint_date > datetime.now():
            raise ValidationErrorException("maintenance_date cannot be in future")
    except Exception:
        raise ValidationErrorException("maintenance_date must be in YYYY-MM-DD format")

    if not data.technician_name.replace(" ", "").isalpha():
        raise ValidationErrorException("Invalid technician_name")

    if data.status not in VALID_STATUS:
        raise ValidationErrorException("Invalid status")


def create_maintenance(payload: MaintenanceCreate):
    validate_maintenance(payload)
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        insert_query = """
            INSERT INTO maintenance_log (
                asset_tag, maintenance_type, vendor_name, description,
                cost, maintenance_date, technician_name, status
            ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
        """
        cursor.execute(
            insert_query,
            (
                payload.asset_tag,
                payload.maintenance_type,
                payload.vendor_name,
                payload.description,
                payload.cost,
                payload.maintenance_date,
                payload.technician_name,
                payload.status,
            ),
        )
        conn.commit()

        log_id = cursor.lastrowid
        cursor.execute("SELECT * FROM maintenance_log WHERE log_id = %s", (log_id,))
        return cursor.fetchone()
    except ValidationErrorException:
        raise
    except Exception as e:
        raise DatabaseConnectionException(str(e))
    finally:
        try:
            cursor.close(); conn.close()
        except:
            pass


def list_maintenance(status: Optional[str] = None):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        if status:
            cursor.execute("SELECT * FROM maintenance_log WHERE status = %s", (status,))
        else:
            cursor.execute("SELECT * FROM maintenance_log")

        rows = cursor.fetchall()
        return rows
    except Exception as e:
        raise DatabaseConnectionException(str(e))
    finally:
        try:
            cursor.close(); conn.close()
        except:
            pass


def get_maintenance_by_id(log_id: int):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM maintenance_log WHERE log_id = %s", (log_id,))
        row = cursor.fetchone()
        if not row:
            raise RecordNotFoundException("Maintenance record not found")
        return row
    except RecordNotFoundException:
        raise
    except Exception as e:
        raise DatabaseConnectionException(str(e))
    finally:
        try:
            cursor.close(); conn.close()
        except:
            pass


def update_maintenance(log_id: int, payload: MaintenanceUpdate):
    validate_maintenance(payload)
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT log_id FROM maintenance_log WHERE log_id = %s", (log_id,))
        if not cursor.fetchone():
            raise RecordNotFoundException("Maintenance record not found")

        update_query = """
            UPDATE maintenance_log
            SET asset_tag=%s,
                maintenance_type=%s,
                vendor_name=%s,
                description=%s,
                cost=%s,
                maintenance_date=%s,
                technician_name=%s,
                status=%s
            WHERE log_id=%s
        """
        cursor.execute(
            update_query,
            (
                payload.asset_tag,
                payload.maintenance_type,
                payload.vendor_name,
                payload.description,
                payload.cost,
                payload.maintenance_date,
                payload.technician_name,
                payload.status,
                log_id,
            ),
        )
        conn.commit()

        cursor.execute("SELECT * FROM maintenance_log WHERE log_id = %s", (log_id,))
        return cursor.fetchone()
    except (RecordNotFoundException, ValidationErrorException):
        raise
    except Exception as e:
        raise DatabaseConnectionException(str(e))
    finally:
        try:
            cursor.close(); conn.close()
        except:
            pass


def update_maintenance_status(log_id: int, new_status: str):
    if new_status not in VALID_STATUS:
        raise ValidationErrorException("Invalid status")
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT log_id FROM maintenance_log WHERE log_id = %s", (log_id,))
        if not cursor.fetchone():
            raise RecordNotFoundException("Maintenance record not found")

        cursor.execute(
            "UPDATE maintenance_log SET status = %s WHERE log_id = %s",
            (new_status, log_id),
        )
        conn.commit()

        cursor.execute("SELECT * FROM maintenance_log WHERE log_id = %s", (log_id,))
        return cursor.fetchone()
    except (RecordNotFoundException, ValidationErrorException):
        raise
    except Exception as e:
        raise DatabaseConnectionException(str(e))
    finally:
        try:
            cursor.close(); conn.close()
        except:
            pass


def delete_maintenance(log_id: int):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT log_id FROM maintenance_log WHERE log_id = %s", (log_id,))
        if not cursor.fetchone():
            raise RecordNotFoundException("Maintenance record not found")

        cursor.execute("DELETE FROM maintenance_log WHERE log_id = %s", (log_id,))
        conn.commit()
        return True
    except RecordNotFoundException:
        raise
    except Exception as e:
        raise DatabaseConnectionException(str(e))
    finally:
        try:
            cursor.close(); conn.close()
        except:
            pass


def search_maintenance(keyword: str):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        like = f"%{keyword}%"
        cursor.execute(
            """
            SELECT * FROM maintenance_log
            WHERE asset_tag LIKE %s
               OR vendor_name LIKE %s
               OR technician_name LIKE %s
            """,
            (like, like, like),
        )
        rows = cursor.fetchall()
        return rows
    except Exception as e:
        raise DatabaseConnectionException(str(e))
    finally:
        try:
            cursor.close(); conn.close()
        except:
            pass


def count_maintenance():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) AS cnt FROM maintenance_log")
        row = cursor.fetchone()
        return row["cnt"] if isinstance(row, dict) else row[0]
    except Exception as e:
        raise DatabaseConnectionException(str(e))
    finally:
        try:
            cursor.close(); conn.close()
        except:
            pass


def bulk_upload_maintenance_from_csv():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        base_dir = path.dirname(path.dirname(__file__))
        csv_path = path.join(base_dir, "Assignment", "cleaned", "maintenance_log_validated.csv")

        with open(csv_path, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            insert_query = """
                INSERT INTO maintenance_log (
                    asset_tag, maintenance_type, vendor_name, description,
                    cost, maintenance_date, technician_name, status
                ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
            """

            for row in reader:
                cursor.execute(
                    insert_query,
                    (
                        row["asset_tag"],
                        row["maintenance_type"],
                        row["vendor_name"],
                        row["description"],
                        float(row["cost"]),
                        row["maintenance_date"],
                        row["technician_name"],
                        row["status"],
                    ),
                )

        conn.commit()
        return True
    except Exception as e:
        raise DatabaseConnectionException(str(e))
    finally:
        try:
            cursor.close(); conn.close()
        except:
            pass
