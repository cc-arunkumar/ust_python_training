import pymysql
from pymysql.cursors import DictCursor

def get_connection():
   
    try:
        # Create a connection object with given parameters
        conn = pymysql.connect(
            host="localhost",          # Database server hostname
            user="root",               # Database username
            password="pass@word1",     # Database password
            database="ust_aims_db",    # Target database name
            port=3306,                 # MySQL default port
            cursorclass=DictCursor     # Return rows as dictionaries instead of tuples
        )
        return conn   # Return the connection object if successful

    except Exception as e:
        # Print error message if connection fails
        print(f"Database connection failed: {e}")
        
       
