import pymysql
import csv

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
# Function: Insert vendor records from CSV
# -----------------------------
def insert_vendors():
    """
    Reads vendor data from a CSV file and inserts it into the vendor_master table.
    Each row from the CSV is mapped to the table columns.
    """

    # SQL query template for inserting vendor records
    query = """
    INSERT INTO ust_asset_db.vendor_master (
        vendor_name, contact_person, contact_phone, gst_number,
        email, address, city, active_status
    ) VALUES (
        %s, %s, %s, %s,
        %s, %s, %s, %s
    )
    """
    print("Inserting vendor data into the database...")

    # Path to the CSV file containing vendor data
    input_file = r"C:\Users\Administrator\Documents\Himavarsha\ust_python_training\himavarsha\day20\AIMS_Plus\database\sampledata\final_csv\valid_vendor.csv"
    
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
                # Prepare data tuple for insertion
                # Mapping CSV columns to table fields
                data = (
                    row["vendor_name"],
                    row["contact_person"],
                    row["contact_phone"],
                    row["gst_number"],
                    row["email"],
                    row["address"],
                    row["city"],
                    row["active_status"]
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

    print("Vendor data insertion completed successfully!")

# -----------------------------
# Run the function
# -----------------------------
insert_vendors()
