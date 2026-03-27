import pymysql
import csv
from datetime import datetime

# Function to get the database connection
def get_connection():
    return pymysql.connect(
        host="localhost",         # Database host
        user="root",              # Database user
        password="pass@word1",    # Database password
        database="ust_asset_db"   # Database name
    )

print("db connected")

# Function to insert employee data into the database
def insert_employee():
    # SQL query to insert data into employee_directory table
    query = """
    INSERT INTO ust_asset_db.employee_directory (
        emp_code, full_name, email, phone, department, location, join_date, status
    ) VALUES (
        %s, %s, %s, %s, %s, %s, %s, %s
    )
    """
    print("Inserting employee records...")

    # Open the CSV file containing employee data
    with open(r'C:\Users\Administrator\Desktop\Training\ust_python_training\Bhargavi\day 19\AIMS_Plus\database\sample_data\validated_employee_directory.csv', "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)  # Reading the CSV data into a dictionary
        print("CSV headers:", reader.fieldnames)  # Printing the CSV headers
        conn = get_connection()  # Establishing database connection
        cursor = conn.cursor()   # Creating a cursor to execute SQL queries
        
        # Loop through each row in the CSV file and insert it into the database
        for row in reader:
            try:
                # Convert 'join_date' string to a datetime object (ignoring time part)
                row['join_date'] = datetime.strptime(row['join_date'].split()[0], "%Y-%m-%d").date()
                
                # Prepare the data tuple for the INSERT query
                data = (
                    row['emp_code'],      # emp_code
                    row['full_name'],     # full_name
                    row['email'],         # email
                    row['phone'],         # phone
                    row['department'],    # department
                    row['location'],      # location
                    row['join_date'],     # join_date (converted to date object)
                    row['status']         # status
                )
                
                # Debugging output: Show the data being passed to the query
                print(f"Inserting row: {data}")
                
                # Execute the query with the data tuple
                cursor.execute(query, data)
                
            except Exception as e:
                # Print any errors that occur while inserting a row
                print(f"Error inserting row: {e}")
        
        # Commit the transaction to the database
        conn.commit()
        print("Employee records inserted successfully.")  # Confirmation message

# Run the function to insert employee data
insert_employee()
