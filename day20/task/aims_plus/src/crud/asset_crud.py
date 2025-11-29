import csv
from datetime import datetime
from typing import Optional

from config.db_connection import get_db_connection
from exceptions.custom_exception import (
    RecordNotFoundException,
    DuplicateRecordException,
    ValidationErrorException,
    DatabaseConnectionException,
)
from models.asset_models import AssetCreate, AssetUpdate

VALID_TYPES = ["Laptop", "Monitor", "Keyboard", "Mouse"]
VALID_MANUFACTURERS = ["Dell", "HP", "Lenovo", "Samsung"]
VALID_CONDITION = ["New", "Good", "Used", "Damaged"]
VALID_LOCATIONS = ["TVM", "Bangalore", "Chennai", "Hyderabad"]
VALID_STATUS = ["Available", "Assigned", "Repair", "Retired"]


def validate_asset_data(data: AssetCreate):
    if not data.asset_tag.startswith("UST-"):
        raise ValidationErrorException("asset_tag must start with 'UST-'")

    if data.asset_type not in VALID_TYPES:
        raise ValidationErrorException("Invalid asset_type")

    if data.manufacturer not in VALID_MANUFACTURERS:
        raise ValidationErrorException("Invalid manufacturer")

    if not data.model.strip():
        raise ValidationErrorException("model cannot be empty")

    try:
        purchase_date = datetime.strptime(data.purchase_date, "%Y-%m-%d")
        if purchase_date > datetime.now():
            raise ValidationErrorException("purchase_date cannot be future")
    except:
        raise ValidationErrorException("purchase_date must be in YYYY-MM-DD format")

    if data.warranty_years < 1 or data.warranty_years > 5:
        raise ValidationErrorException("warranty_years must be between 1 and 5")

    if data.condition_status not in VALID_CONDITION:
        raise ValidationErrorException("Invalid condition_status")

    if data.location not in VALID_LOCATIONS:
        raise ValidationErrorException("Invalid location")

    if data.asset_status not in VALID_STATUS:
        raise ValidationErrorException("Invalid asset_status")

    if data.assigned_to and not data.assigned_to.replace(" ", "").isalpha():
        raise ValidationErrorException("assigned_to must be a valid name")


def create_asset(payload: AssetCreate):
    validate_asset_data(payload)

    try:
        conn = get_db_connection()
        cursor = conn.cursor()  

        # check duplicate serial
        cursor.execute(
            "SELECT asset_id FROM asset_inventory WHERE serial_number = %s",
            (payload.serial_number,),
        )
        if cursor.fetchone():
            raise DuplicateRecordException("serial_number already exists")

        insert_query = """
            INSERT INTO asset_inventory (
                asset_tag, asset_type, serial_number, manufacturer, model,
                purchase_date, warranty_years, condition_status, assigned_to,
                location, asset_status
            )
            VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
        """
        cursor.execute(
            insert_query,
            (
                payload.asset_tag,
                payload.asset_type,
                payload.serial_number,
                payload.manufacturer,
                payload.model,
                payload.purchase_date,
                payload.warranty_years,
                payload.condition_status,
                payload.assigned_to,
                payload.location,
                payload.asset_status,
            ),
        )
        conn.commit()

        asset_id = cursor.lastrowid
        cursor.execute("SELECT * FROM asset_inventory WHERE asset_id = %s", (asset_id,))
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


def list_assets(status: Optional[str] = None):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        if status:
            cursor.execute(
                "SELECT * FROM asset_inventory WHERE asset_status = %s",
                (status,),
            )
        else:
            cursor.execute("SELECT * FROM asset_inventory")

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


def get_asset_by_id(asset_id: int):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM asset_inventory WHERE asset_id = %s", (asset_id,))
        row = cursor.fetchone()
        if not row:
            raise RecordNotFoundException("Asset not found")
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


def update_asset(asset_id: int, payload: AssetUpdate):
    fake = AssetCreate(
        asset_tag="UST-DUMMY-0000",
        asset_type=payload.asset_type,
        serial_number="DUMMY-SERIAL-0000",
        manufacturer=payload.manufacturer,
        model=payload.model,
        purchase_date=payload.purchase_date,
        warranty_years=payload.warranty_years,
        condition_status=payload.condition_status,
        assigned_to=payload.assigned_to,
        location=payload.location,
        asset_status=payload.asset_status,
    )
    validate_asset_data(fake)

    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM asset_inventory WHERE asset_id = %s", (asset_id,))
        if not cursor.fetchone():
            raise RecordNotFoundException("Asset not found")

        update_query = """
            UPDATE asset_inventory
            SET asset_type=%s,
                manufacturer=%s,
                model=%s,
                purchase_date=%s,
                warranty_years=%s,
                condition_status=%s,
                assigned_to=%s,
                location=%s,
                asset_status=%s
            WHERE asset_id=%s
        """
        cursor.execute(
            update_query,
            (
                payload.asset_type,
                payload.manufacturer,
                payload.model,
                payload.purchase_date,
                payload.warranty_years,
                payload.condition_status,
                payload.assigned_to,
                payload.location,
                payload.asset_status,
                asset_id,
            ),
        )
        conn.commit()

        cursor.execute("SELECT * FROM asset_inventory WHERE asset_id = %s", (asset_id,))
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


def update_asset_status(asset_id: int, new_status: str):
    if new_status not in VALID_STATUS:
        raise ValidationErrorException("Invalid asset_status")

    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM asset_inventory WHERE asset_id = %s", (asset_id,))
        if not cursor.fetchone():
            raise RecordNotFoundException("Asset not found")

        cursor.execute(
            "UPDATE asset_inventory SET asset_status = %s WHERE asset_id = %s",
            (new_status, asset_id),
        )
        conn.commit()

        cursor.execute("SELECT * FROM asset_inventory WHERE asset_id = %s", (asset_id,))
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


def delete_asset(asset_id: int):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM asset_inventory WHERE asset_id = %s", (asset_id,))
        if not cursor.fetchone():
            raise RecordNotFoundException("Asset not found")

        cursor.execute("DELETE FROM asset_inventory WHERE asset_id = %s", (asset_id,))
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


def search_asset(keyword: str):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        like_pattern = f"%{keyword}%"
        cursor.execute(
            """
            SELECT * FROM asset_inventory
            WHERE asset_tag LIKE %s
               OR model LIKE %s
               OR manufacturer LIKE %s
            """,
            (like_pattern, like_pattern, like_pattern),
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


def count_assets():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT COUNT(*) AS cnt FROM asset_inventory")
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


def bulk_upload_assets_from_csv():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        from os import path
        base_dir = path.dirname(path.dirname(__file__))  # src/ → parent = aims_plus
        csv_path = path.join(base_dir, "Assignment", "cleaned", "asset_inventory_validated.csv")

        with open(csv_path, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)

            insert_query = """
                INSERT INTO asset_inventory (
                    asset_tag, asset_type, serial_number, manufacturer, model,
                    purchase_date, warranty_years, condition_status, assigned_to,
                    location, asset_status
                )
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            """

            for row in reader:
                cursor.execute(
                    insert_query,
                    (
                        row["asset_tag"],
                        row["asset_type"],
                        row["serial_number"],
                        row["manufacturer"],
                        row["model"],
                        row["purchase_date"],
                        int(row["warranty_years"]),
                        row["condition_status"],
                        row["assigned_to"],
                        row["location"],
                        row["asset_status"],
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
