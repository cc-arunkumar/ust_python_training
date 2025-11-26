import pymysql                           # Library for MySQL database operations
from pymysql import Error                # Error class for MySQL exceptions
import pymysql.cursors                   # Provides cursor types like DictCursor
from src.config.db_connection import get_connection   # Function to establish DB connection
from src.helpers.validators import (     # Importing validation helper functions
    validate_asset_tag,
    validate_asset_type,
    validate_warranty_years,
    validate_status_and_assignment,
    validate_asset_id  
)


def create_asset(asset_tag, asset_type, serial_number, manufacturer, model,
                 purchase_date, warranty_years, assigned_to, asset_status):
    connection, cursor = None, None      # Initialize connection and cursor for cleanup in finally
    try:
        # Input validations before database operations
        validate_asset_tag(asset_tag)
        validate_asset_type(asset_type)
        validate_warranty_years(warranty_years)
        validate_status_and_assignment(asset_status, assigned_to)

        connection = get_connection()    # Establish DB connection
        if connection is None:
            raise RuntimeError("Database connection failed.")
        cursor = connection.cursor()     # Create cursor for executing SQL queries

        # Check if asset_tag already exists (uniqueness constraint)
        cursor.execute("SELECT COUNT(*) AS cnt FROM asset_inventory WHERE asset_tag = %s", (asset_tag,))
        if cursor.fetchone()["cnt"] > 0:
            raise ValueError("asset_tag already exists.")

        # Check if serial_number already exists (uniqueness constraint)
        cursor.execute("SELECT COUNT(*) AS cnt FROM asset_inventory WHERE serial_number = %s", (serial_number,))
        if cursor.fetchone()["cnt"] > 0:
            raise ValueError("serial_number already exists.")

        # SQL insert statement to create a new asset record
        insert_sql = """
            INSERT INTO asset_inventory
            (asset_tag, asset_type, serial_number, manufacturer, model, purchase_date,
             warranty_years, assigned_to, asset_status, last_updated)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, NOW())
        """
        cursor.execute(insert_sql, (
            asset_tag, asset_type, serial_number, manufacturer, model,
            purchase_date, warranty_years, assigned_to, asset_status
        ))
        connection.commit()              # Commit DB transaction

        print(f"Asset created successfully with asset_id: {cursor.lastrowid}")

    except Exception as e:
        print(f"Error: {e}")             # Log any error during processing
    finally:
        if cursor: cursor.close()        # Ensure cursor is closed
        if connection: connection.close()# Ensure DB connection is closed


def read_all_assets(status_filter="ALL"):
    connection, cursor = None, None
    try:
        # Allowed filters to avoid invalid status queries
        valid_filters = ["Available", "Assigned", "Repair", "Retired", "ALL"]
        if status_filter not in valid_filters:
            raise ValueError(f"status_filter must be one of {valid_filters}")

        connection = get_connection()    # Establish DB connection
        if connection is None:
            raise RuntimeError("Database connection failed.")
        cursor = connection.cursor(pymysql.cursors.DictCursor)  # Dict cursor for key-based retrieval

        # Query all assets or filter by status
        if status_filter == "ALL":
            sql = "SELECT * FROM asset_inventory ORDER BY asset_id ASC"
            cursor.execute(sql)
        else:
            sql = "SELECT * FROM asset_inventory WHERE asset_status = %s ORDER BY asset_id ASC"
            cursor.execute(sql, (status_filter,))

        rows = cursor.fetchall()         # Fetch all results
        if not rows:
            print("No assets found.")
            return

        # Print asset records one by one
        for r in rows:
            print(
                f"asset_id: {r['asset_id']}, asset_tag: {r['asset_tag']}, asset_type: {r['asset_type']}, "
                f"serial_number: {r['serial_number']}, manufacturer: {r['manufacturer']}, model: {r['model']}, "
                f"purchase_date: {r['purchase_date']}, warranty_years: {r['warranty_years']}, "
                f"assigned_to: {r['assigned_to']}, asset_status: {r['asset_status']}, last_updated: {r['last_updated']}"
            )

    except Exception as e:
        print(f"Error: {e}")             # Log errors
    finally:
        if cursor: cursor.close()        # Cleanup
        if connection: connection.close()


def read_asset_by_id(asset_id):
    connection, cursor = None, None
    try:
        # Ensure asset_id is a positive integer
        try:
            asset_id_int = int(asset_id)
        except (TypeError, ValueError):
            print("Asset not found.")
            return
        if asset_id_int <= 0:
            print("Asset not found.")
            return

        connection = get_connection()    # Establish DB connection
        if connection is None:
            raise RuntimeError("Database connection failed.")
        cursor = connection.cursor(pymysql.cursors.DictCursor)

        # Fetch asset by ID
        sql = "SELECT * FROM asset_inventory WHERE asset_id = %s"
        cursor.execute(sql, (asset_id_int,))
        row = cursor.fetchone()

        if not row:
            print("Asset not found.")
            return

        # Print asset details
        print(
            f"asset_id: {row['asset_id']}\n"
            f"asset_tag: {row['asset_tag']}\n"
            f"asset_type: {row['asset_type']}\n"
            f"serial_number: {row['serial_number']}\n"
            f"manufacturer: {row['manufacturer']}\n"
            f"model: {row['model']}\n"
            f"purchase_date: {row['purchase_date']}\n"
            f"warranty_years: {row['warranty_years']}\n"
            f"assigned_to: {row['assigned_to']}\n"
            f"asset_status: {row['asset_status']}\n"
            f"last_updated: {row['last_updated']}"
        )

    except Exception as e:
        print(f"Error: {e}")             # Log errors
    finally:
        if cursor: cursor.close()        # Cleanup
        if connection: connection.close()


def update_asset(asset_id, asset_type=None, manufacturer=None, model=None,
                 warranty_years=None, asset_status=None, assigned_to=None):
    connection, cursor = None, None
    try:
        # Validate asset_id format and positivity
        try:
            asset_id_int = int(asset_id)
        except (TypeError, ValueError):
            raise ValueError("Invalid asset_id")
        if asset_id_int <= 0:
            raise ValueError("Invalid asset_id")

        connection = get_connection()    # Establish DB connection
        if connection is None:
            raise RuntimeError("Database connection failed.")
        cursor = connection.cursor(pymysql.cursors.DictCursor)

        # Check if the asset exists before updating
        cursor.execute("SELECT * FROM asset_inventory WHERE asset_id = %s", (asset_id_int,))
        existing = cursor.fetchone()
        if not existing:
            raise ValueError("Asset not found.")

        # Validate only fields that are being updated
        if asset_type is not None:
            validate_asset_type(asset_type)
        if warranty_years is not None:
            validate_warranty_years(warranty_years)
        if asset_status is not None:
            validate_status_and_assignment(asset_status, assigned_to)

        # Prepare dynamic update fields
        fields, values = [], []
        if asset_type is not None:
            fields.append("asset_type = %s"); values.append(asset_type)
        if manufacturer is not None:
            fields.append("manufacturer = %s"); values.append(manufacturer)
        if model is not None:
            fields.append("model = %s"); values.append(model)
        if warranty_years is not None:
            fields.append("warranty_years = %s"); values.append(warranty_years)
        if asset_status is not None:
            fields.append("asset_status = %s"); values.append(asset_status)

        # Assignment rules based on asset status
        if asset_status in ["Available", "Retired"]:
            fields.append("assigned_to = %s"); values.append(None)
        elif asset_status == "Assigned":
            fields.append("assigned_to = %s"); values.append(assigned_to)

        # Always update the timestamp
        fields.append("last_updated = NOW()")
        sql = f"UPDATE asset_inventory SET {', '.join(fields)} WHERE asset_id = %s"
        values.append(asset_id_int)

        cursor.execute(sql, tuple(values))
        connection.commit()

        if cursor.rowcount == 0:
            print("Asset not found.")
        else:
            print(f"Asset {asset_id_int} updated successfully.")

    except Exception as e:
        print(f"Error: {e}")             # Log errors
    finally:
        if cursor: cursor.close()        # Cleanup
        if connection: connection.close()


def delete_asset(asset_id):
    connection, cursor = None, None
    try:
        asset_id_int = validate_asset_id(asset_id)  # Validate and convert asset_id

        connection = get_connection()    # Establish DB connection
        if connection is None:
            raise RuntimeError("Database connection failed.")
        cursor = connection.cursor()

        # Check if the asset exists before attempting deletion
        cursor.execute("SELECT COUNT(*) AS cnt FROM asset_inventory WHERE asset_id = %s", (asset_id_int,))
        if cursor.fetchone()["cnt"] == 0:
            print("Asset not found.")
            return

        # Delete the asset record
        delete_sql = "DELETE FROM asset_inventory WHERE asset_id = %s"
        cursor.execute(delete_sql, (asset_id_int,))
        connection.commit()

        if cursor.rowcount == 0:
            print("Asset not found.")
        else:
            print(f"Asset {asset_id_int} deleted successfully.")

    except Exception as e:
        print(f"Error: {e}")             # Log errors
    finally:
        if cursor: cursor.close()        # Cleanup
        if connection: connection.close()
