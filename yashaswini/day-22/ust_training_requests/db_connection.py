import pymysql
from contextlib import contextmanager

# MySQL connection parameters (hardcoded)
HOST = "localhost"  # The host where your MySQL server is running
USER = "root"       # Your MySQL username
PASSWORD = "pass@word1"  # Your MySQL password (replace with your actual password)
DATABASE = "ust_db"  # The name of the database

@contextmanager
def get_db_connection():
    # Establish the connection to MySQL database
    connection = pymysql.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        database=DATABASE,
        cursorclass=pymysql.cursors.DictCursor  # Use DictCursor to return rows as dictionaries
    )
    
    try:
        yield connection  # Yield the connection to be used by the caller
    finally:
        connection.close()  # Close the connection when done
