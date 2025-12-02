import pymysql  # Import the pymysql library to interact with MySQL

# Function to establish a connection to the MySQL database
def get_db_connection():
    try:
        # Establish a connection to the database using pymysql.connect
        conn = pymysql.connect(
            host="localhost",  # Database host (localhost for local MySQL server)
            user="root",  # Database username
            password="pass@word1",  # Database password
            database="ust_training_db",  # Name of the database to connect to
            cursorclass=pymysql.cursors.DictCursor  # Use DictCursor so query results are returned as dictionaries
        )
        
        print("Connected to the MySQL database successfully!")  # Print a success message if the connection is established
        
        return conn  # Return the connection object
    
    except pymysql.MySQLError as e:
        # Handle any MySQL errors that occur during the connection attempt
        print(f"Failed to connect to the database: {e}")
        return None  # Return None if the connection fails

# Test the connection by calling the function
conn = get_db_connection()

# If the connection is successful, close it
if conn:
    conn.close()  # Always close the connection when done to avoid leaks
