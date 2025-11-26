import pymysql
from config.db_connection import get_connection

def create_table():
    -- # Establishing the database connection
    conn = get_connection()
    cursor = conn.cursor()

    -- # SQL query to create the asset_inventory table
    create_table_query = """
    CREATE TABLE asset_inventory (
        asset_id INT PRIMARY KEY AUTO_INCREMENT,  -- Unique asset identifier, automatically increments
        asset_tag VARCHAR(50) UNIQUE NOT NULL,  -- Company asset tag (e.g., UST-LTP-000293), must be unique
        asset_type VARCHAR(50) NOT NULL,  -- Type of asset (Laptop, Monitor, Docking Station, Keyboard, Mouse)
        serial_number VARCHAR(100) UNIQUE NOT NULL,  -- Manufacturer serial number, must be unique
        manufacturer VARCHAR(50) NOT NULL,  -- Manufacturer name (e.g., Dell, HP, Lenovo)
        model VARCHAR(100) NOT NULL,  -- Asset model (e.g. "Latitude 5520")
        purchase_date DATE NOT NULL,  -- Date when asset was purchased
        warranty_years INT NOT NULL CHECK (warranty_years > 0),  -- Warranty validity in years, must be > 0
        assigned_to VARCHAR(100) NULL,  -- Name of the employee assigned the asset, can be NULL if unassigned
        asset_status VARCHAR(20) NOT NULL CHECK (asset_status IN ('Available', 'Assigned', 'Repair', 'Retired')),  -- Valid status values: Available, Assigned, Repair, Retired
        last_updated DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP  -- Timestamp of the last update, auto-updates whenever a record is modified
    );
    """

    try:
        -- # Execute the SQL query to create the table
        cursor.execute(create_table_query)
        conn.commit()  # Commit the transaction to make changes permanent
        print("Table 'asset_inventory' created successfully!")  # Confirmation message on successful table creation
    except pymysql.MySQLError as e:
        -- # Print any error that occurs during table creation and rollback the transaction
        print(f"Error creating table: {e}")
        conn.rollback()  # Rollback to ensure the database remains in a consistent state in case of an error

    finally:
        -- # Close the cursor and the connection to the database
        cursor.close()
        conn.close()

-- # Call the function to create the table
create_table()