# Importing the pymysql library to handle MySQL database connections
import pymysql

# Function to establish a connection to the MySQL database
def get_connection():
    try:
        # Log message indicating the attempt to connect to the database
        print("Attempting to connect to the database...") 
        
        # Establishing a connection to the database using pymysql.connect
        conn = pymysql.connect(
            host='localhost',  # Database host (localhost means the database is on the same machine)
            user='root',  # Database username
            password='pass@word1',  # Database password
            database='ust_asset_db'  # Database name (ust_asset_db)
        )
        
        # If connection is successful, print success message
        print("Connection established successfully.")
        
        # Return the connection object to be used for further database operations
        return conn
    except Exception as e:
        # If an error occurs during the connection attempt, print the error message
        print(f"Error: {e}")  
        
        # Return None to indicate the connection attempt failed
        return None

# Calling the function to test the connection
get_connection()
