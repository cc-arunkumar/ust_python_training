import pymysql
from contextlib import contextmanager

# MySQL connection parameters
HOST = "localhost"
USER = "root"
PASSWORD = "pass@word1"  # Make sure to replace with the actual password
DATABASE = "ust_aims_db"  # Ensure this is the correct database name

@contextmanager
def get_db_connection():
    # Establish the connection
    connection = pymysql.connect(
        host=HOST,  # The host where the MySQL server is running (localhost means it's on the same machine)
        user=USER,  # The username to log into the MySQL server (root is the default admin user)
        password=PASSWORD,  # The password associated with the username (ensure this is secure in real applications)
        database=DATABASE,  # The database to connect to (make sure this exists on your MySQL server)
        cursorclass=pymysql.cursors.DictCursor  # Ensures that the cursor returns rows as dictionaries (key-value pairs)
    )
    
    try:
        yield connection  # Yield the connection so it can be used by the caller
    finally:
        connection.close()  # Close the connection when done
