import csv       # Import csv module to read data from CSV files
import pymysql   # Import pymysql to connect and interact with MySQL databases

# Function to establish a connection to the MySQL database
def get_connection():
    return pymysql.connect(
        host="localhost",       # Database server address (localhost = local machine)
        user="root",            # MySQL username
        password="pass@word1",  # MySQL password
        database="ust_asset_inventory"  # Target database name
    )

# Create a connection object
conn = get_connection()
# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Path to the input CSV file containing vendor data
input_file = r"C:\Users\Administrator\Desktop\ust_python_training\Rohit\day18\ust_ITSM\data\new_vendor_master(in).csv"

# Open the input CSV file in read mode
with open(input_file, mode="r", encoding="utf-8") as file1:
    reader = csv.DictReader(file1)  # Read CSV rows as dictionaries (keys = column names)

    # Iterate through each row in the CSV file
    for row in reader:
        try:
            # SQL query template for inserting rows into vendor_master table
            # Uses placeholders (%s) for parameterized queries to prevent SQL injection
            sql = """
            INSERT INTO vendor_master (
                vendor_id, vendor_name, contact_person, contact_phone,
                gst_number, email, address, city, active_status
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            """

            # Extract values from the row into a tuple matching the SQL query placeholders
            values = (
                row["vendor_id"],      # Vendor ID
                row["vendor_name"],    # Vendor name
                row["contact_person"], # Contact person name
                row["contact_phone"],  # Contact phone number
                row["gst_number"],     # GST number
                row["email"],          # Email address
                row["address"],        # Vendor address
                row["city"],           # City
                row["active_status"],  # Active status (Active/Inactive)
            )

            # Execute the SQL insert query with the extracted values
            cursor.execute(sql, values)

        except Exception as e:  # Catch any errors during insertion
            print(f"Error inserting vendor_id {row['vendor_id']}: {e}")

    # Commit all changes to the database (make sure inserts are saved)
    conn.commit()

# Close the cursor object
cursor.close()
# Close the database connection
conn.close()

# Print confirmation message after successful insertion
print("CSV data successfully dumped into vendor_master table.")
