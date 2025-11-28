import pymysql
import csv
from datetime import datetime

# -----------------------------
# Function: Get database connection
# -----------------------------
def get_connection():
    """
    Establish and return a connection to the MySQL database.
    - host: MySQL server (localhost if running locally)
    - user: MySQL username
    - password: MySQL password
    - database: target database name
    """
    return pymysql.connect(
        host="localhost",
        user="root",
        password="pass@word1",   
        database="ust_asset_db"
    )

# -----------------------------
# Function: Insert assets from CSV into database
# -----------------------------
def insert_assets():
    """
    Reads asset data from a CSV file and inserts it into the assets_inventory table.
    Each row from the CSV is mapped to the table columns.
    Adds a timestamp for 'last_updated' automatically.
    """

    # SQL query template for inserting asset records
    query = """
    INSERT INTO ust_asset_db.assets_inventory (
        asset_tag, asset_type, serial_number, manufacturer, model,
        purchase_date, warranty_years, condition_status, assigned_to,
        location, asset_status, last_updated
    ) VALUES (
        %s, %s, %s, %s, %s,
        %s, %s, %s, %s,
        %s, %s, %s
    )
    """
    print("Inserting data into the database...")

    # Path to the CSV file containing asset data
    input_file = r"C:\Users\Administrator\Documents\Himavarsha\ust_python_training\himavarsha\day20\AIMS_Plus\database\sampledata\final_csv\valid_asset.csv"

    # -----------------------------
    # Step 1: Open CSV file
    # -----------------------------
    with open(input_file, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)  # Reads CSV rows as dictionaries (column_name → value)
        print("CSV headers:", reader.fieldnames)  # Print headers for debugging
        
        # -----------------------------
        # Step 2: Connect to database
        # -----------------------------
        conn = get_connection()
        cursor = conn.cursor()

        # -----------------------------
        # Step 3: Process each row in CSV
        # -----------------------------
        for row in reader:
            try:
                # Convert row values to tuple and append current timestamp
                # row.values() → all column values from CSV
                # datetime.now() → current timestamp for last_updated
                data = tuple(row.values()) + (datetime.now(),)
                
                # Execute SQL insert query with prepared data
                cursor.execute(query, data)
            except Exception as e:
                # If insertion fails, print the row and error message
                print(f"Error inserting row: {row} | Error: {str(e)}")
        
        # -----------------------------
        # Step 4: Commit transaction
        # -----------------------------
        conn.commit()  # Save all changes to database

        # -----------------------------
        # Step 5: Close resources
        # -----------------------------
        cursor.close()
        conn.close()

    print("Data insertion completed successfully!")

# -----------------------------
# Run the function
# -----------------------------
insert_assets()
