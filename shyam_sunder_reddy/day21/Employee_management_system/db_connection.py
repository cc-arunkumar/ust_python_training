# Import the PyMySQL library to enable Python to connect and interact with MySQL databases
import pymysql
# Import DictCursor so query results are returned as dictionaries (column names as keys) instead of tuples
from pymysql.cursors import DictCursor

def get_connection():
    # """
    # Establishes and returns a connection to the MySQL database.

    # Returns:
    #     conn (pymysql.connections.Connection): A live connection object 
    #     that can be used to execute queries.
    # """
    # Create a connection object with database credentials
    conn = pymysql.connect(
        host="localhost",       # Database server hostname (local machine in this case)
        user="root",            # Database username
        password="pass@word1",  # Database password
        database="ust_db",      # Target database name
        cursorclass=DictCursor  # Cursor type: results returned as dictionaries
    )
    # Return the connection object to the caller
    return conn
