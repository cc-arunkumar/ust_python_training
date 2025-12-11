import pymysql   # Import PyMySQL to connect and interact with MySQL database
import json      # Import JSON module to read employee data from JSON file

def get_connection():   # Function to establish MySQL connection
    conn = pymysql.connect(
        host="localhost",       # MySQL server host
        user="root",            # MySQL username
        password="felix_123",   # MySQL password
        database="ust_mysql_db",# Database name
        cursorclass=pymysql.cursors.DictCursor   # Return rows as dictionaries
    )
    return conn   # Return connection object

def read_json():   # Function to read employee data from JSON file
    with open("employees.json","r") as file:   # Open JSON file in read mode
        data = json.load(file)   # Load JSON data into Python object
        return data              # Return employee data
            

def inset_into_mysql():   # Function to insert employee data into MySQL
    try:
        conn = get_connection()   # Establish connection
        cursor = conn.cursor()    # Create cursor object
        query = """
            insert into ust_mysql_db.employees values(
                %s,%s,%s,%s,%s
            )
        """   # SQL query with placeholders for values        
        data = read_json()   # Read employee data from JSON file
        for emp in data:     # Iterate through employee records
            cursor.execute(query,tuple(emp.values()))   # Insert each record
        conn.commit()   # Commit transaction
    except Exception as e:
        print(e)   # Print exception if occurs
    finally:
        if conn.open:   # Ensure connection is open before closing
            cursor.close()   # Close cursor
            conn.close()     # Close connection
        print("Data inserted to mysql")   # Confirmation message
        

def read_from_mysql():   # Function to read employee data from MySQL
    try:
        conn = get_connection()   # Establish connection
        cursor = conn.cursor()    # Create cursor object
        query = """
            select * from ust_mysql_db.employees 
        """   # SQL query to fetch all employees        
        cursor.execute(query)   # Execute query
        data = cursor.fetchall()   # Fetch all records
        for emp in data:   # Iterate through employee records
            print(emp)     # Print each record
            if emp["age"]<25:   # Categorize based on age
                emp["category"] = "Fresher"
            else:
                emp["category"] = "Experienced"
        return data   # Return modified employee data
    except Exception as e:
        print(e)   # Print exception if occurs
    finally:
        if conn.open:   # Ensure connection is open before closing
            cursor.close()   # Close cursor
            conn.close()     # Close connection
        print("Data inserted to mysql")   # Confirmation message


# inset_into_mysql()   # Uncomment to insert data from JSON into MySQL
# read_from_mysql()      # Call function to read data from MySQL