import pymysql
import csv
from datetime import datetime

# Function to get the database connection
def get_connection():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="pass@word1",   
        database="ust_asset_db"
    )

# Function to insert assets into the database
def insert_employee_log():
    query = """
    INSERT INTO ust_asset_db.employee_directory (
        emp_code, full_name, email, phone,
        department, location, join_date, status
    ) VALUES (
        %s, %s, %s, %s,
        %s, %s, %s, %s
    )
    """
    print("Inserting data into the database...")

    # Correct file path
    input_file = r'C:\Users\Administrator\Desktop\Training\ust_python_training\vinutha\day13\day19\AIMS_PLUS\database\sample_data\validated_employee_directory.csv'
    # Open the CSV file and read the data
    with open(input_file, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        print("CSV headers:", reader.fieldnames)
        
        # Connect to the database
        conn = get_connection()
        cursor = conn.cursor()

        # Process each row from the CSV and insert into the database
        for row in reader:
            try:
                # Print the row to ensure data is being read correctly
                print(row)

                # Prepare data without log_id and add current timestamp (if needed)
                data = (
                    row['emp_code'], row['full_name'], row['email'], row['phone'],
                    row['department'], row['location'], row['join_date'], row['status']
                )
                
                # Execute the insert query
                cursor.execute(query, data)
            except Exception as e:
                # Handle any errors and print the row that failed
                print(f"Error inserting row: {row} | Error: {str(e)}")
        
        # Commit the transaction after inserting all rows
        conn.commit()

        # Close the cursor and connection
        cursor.close()
        conn.close()

    print("Data insertion completed successfully!")

# Call the function to insert assets
insert_employee_log()
