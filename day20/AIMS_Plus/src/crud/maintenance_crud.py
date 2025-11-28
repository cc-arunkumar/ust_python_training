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
# Function: Insert maintenance log records from CSV
# -----------------------------
def insert_maintenance_log():
    """
    Reads maintenance log data from a CSV file and inserts it into the maintenance_log table.
    Each row from the CSV is mapped to the table columns.
    """

    # SQL query template for inserting maintenance records
    query = """
    INSERT INTO ust_asset_db.maintenance_log (
        asset_tag, maintenance_type, vendor_name, description,
        cost, maintenance_date, technician_name, status
    ) VALUES (
        %s, %s, %s, %s, %s,
        %s, %s, %s
    )
    """
    print("Inserting data into the database...")

    # Path to the CSV file containing maintenance data
    input_file = r"C:\Users\Administrator\Documents\Himavarsha\ust_python_training\himavarsha\day20\AIMS_Plus\database\sampledata\final_csv\valid_maintenance.csv"

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
                # Print the row to ensure data is being read correctly
                print(row)

                # Prepare data tuple for insertion
                # Mapping CSV columns to table fields
                data = (
                    row['asset_tag'], row['maintenance_type'], row['vendor_name'], row['description'],
                    row['cost'], row['maintenance_date'], row['technician_name'], row['status']
                )
                
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
insert_maintenance_log()
