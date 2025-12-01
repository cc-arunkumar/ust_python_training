# Import the necessary modules from pymysql for database connection
import pymysql
from pymysql.cursors import DictCursor  # Allows results to be returned as dictionaries

# Function to establish a connection to the MySQL database
def get_connection():
    try:
        # Attempt to connect to the MySQL database using the specified credentials
        conn = pymysql.connect(
            host="localhost",          # Database host (typically 'localhost' for local servers)
            user="root",               # MySQL username (replace with actual user)
            password="pass@word1",     # MySQL password (ensure it's kept secure in production)
            database="ust_db",         # Name of the database to connect to
            port=3306,                 # Port number for MySQL (default is 3306)
            cursorclass=DictCursor     # Returns query results as dictionaries (useful for named access)
        )
        return conn
    except Exception as e:
        print(f"Database connection failed: {e}")
        raise
