from typing import Optional
from config.db_connection import get_db_connection
from exceptions.custom_exception import (
    RecordNotFoundException,
    DuplicateRecordException,
    ValidationErrorException,
    DatabaseConnectionException,
)
from models.vendor_model import VendorCreate, VendorUpdate
import csv
from os import path

VALID_LOCATIONS = ["TVM", "Bangalore", "Chennai", "Hyderabad"]
VALID_STATUS = ["Active", "Inactive"]


def validate_vendor(data: VendorCreate | VendorUpdate):
    if not data.vendor_name or not data.vendor_name.replace(" ", "").isalpha():
        raise ValidationErrorException("Invalid vendor_name")

    if not data.contact_person or not data.contact_person.replace(" ", "").isalpha():
        raise ValidationErrorException("Invalid contact_person")

    if not (data.contact_phone.isdigit() and len(data.contact_phone) == 10 and data.contact_phone[0] in "6789"):
        raise ValidationErrorException("Invalid contact_phone")

    if not data.gst_number or len(data.gst_number) != 15:
        raise ValidationErrorException("gst_number must be 15 characters")

    if ("@" not in data.email) or ("." not in data.email):
        raise ValidationErrorException("Invalid email")

    if not data.address or len(data.address) > 200:
        raise ValidationErrorException("Invalid address")

    # here you can use VALID_LOCATIONS or allow any city; we keep simple:
    if not data.city:
        raise ValidationErrorException("city is required")

    if data.active_status not in VALID_STATUS:
        raise ValidationErrorException("Invalid active_status")


def create_vendor(payload: VendorCreate):
    validate_vendor(payload)
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        insert_query = """
            INSERT INTO vendor_master (
                vendor_name, contact_person, contact_phone, gst_number,
                email, address, city, active_status
            ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
        """
        cursor.execute(
            insert_query,
            (
                payload.vendor_name,
                payload.contact_person,
                payload.contact_phone,
                payload.gst_number,
                payload.email,
                payload.address,
                payload.city,
                payload.active_status,
            ),
        )
        conn.commit()

        vendor_id = cursor.lastrowid
        cursor.execute("SELECT * FROM vendor_master WHERE vendor_id = %s", (vendor_id,))
        row = cursor.fetchone()
        return row
    except ValidationErrorException:
        raise
    except Exception as e:
        raise DatabaseConnectionException(str(e))
    finally:
        try:
            cursor.close()
            conn.close()
        except:
            pass


def list_vendors(status: Optional[str] = None):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        if status:
            cursor.execute("SELECT * FROM vendor_master WHERE active_status = %s", (status,))
        else:
            cursor.execute("SELECT * FROM vendor_master")

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


def get_vendor_by_id(vendor_id: int):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM vendor_master WHERE vendor_id = %s", (vendor_id,))
        row = cursor.fetchone()
        if not row:
            raise RecordNotFoundException("Vendor not found")
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


def update_vendor(vendor_id: int, payload: VendorUpdate):
    validate_vendor(payload)
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT vendor_id FROM vendor_master WHERE vendor_id = %s", (vendor_id,))
        if not cursor.fetchone():
            raise RecordNotFoundException("Vendor not found")

        update_query = """
            UPDATE vendor_master
            SET vendor_name=%s,
                contact_person=%s,
                contact_phone=%s,
                gst_number=%s,
                email=%s,
                address=%s,
                city=%s,
                active_status=%s
            WHERE vendor_id=%s
        """
        cursor.execute(
            update_query,
            (
                payload.vendor_name,
                payload.contact_person,
                payload.contact_phone,
                payload.gst_number,
                payload.email,
                payload.address,
                payload.city,
                payload.active_status,
                vendor_id,
            ),
        )
        conn.commit()

        cursor.execute("SELECT * FROM vendor_master WHERE vendor_id = %s", (vendor_id,))
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


def update_vendor_status(vendor_id: int, new_status: str):
    if new_status not in VALID_STATUS:
        raise ValidationErrorException("Invalid active_status")

    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT vendor_id FROM vendor_master WHERE vendor_id = %s", (vendor_id,))
        if not cursor.fetchone():
            raise RecordNotFoundException("Vendor not found")

        cursor.execute(
            "UPDATE vendor_master SET active_status = %s WHERE vendor_id = %s",
            (new_status, vendor_id),
        )
        conn.commit()

        cursor.execute("SELECT * FROM vendor_master WHERE vendor_id = %s", (vendor_id,))
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


def delete_vendor(vendor_id: int):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT vendor_id FROM vendor_master WHERE vendor_id = %s", (vendor_id,))
        if not cursor.fetchone():
            raise RecordNotFoundException("Vendor not found")

        cursor.execute("DELETE FROM vendor_master WHERE vendor_id = %s", (vendor_id,))
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


def search_vendor(keyword: str):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        like = f"%{keyword}%"
        cursor.execute(
            """
            SELECT * FROM vendor_master
            WHERE vendor_name LIKE %s
               OR contact_person LIKE %s
               OR city LIKE %s
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


def count_vendors():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) AS cnt FROM vendor_master")
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


def bulk_upload_vendors_from_csv():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        base_dir = path.dirname(path.dirname(__file__))
        csv_path = path.join(base_dir, "Assignment", "cleaned", "vendor_master_validated.csv")

        with open(csv_path, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            insert_query = """
                INSERT INTO vendor_master (
                    vendor_name, contact_person, contact_phone, gst_number,
                    email, address, city, active_status
                ) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
            """

            for row in reader:
                cursor.execute(
                    insert_query,
                    (
                        row["vendor_name"],
                        row["contact_person"],
                        row["contact_phone"],
                        row["gst_number"],
                        row["email"],
                        row["address"],
                        row["city"],
                        row["active_status"],
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
