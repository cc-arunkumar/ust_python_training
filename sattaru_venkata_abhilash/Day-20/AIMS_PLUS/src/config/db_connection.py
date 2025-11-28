import pymysql  # Importing the pymysql module to interact with MySQL databases

def get_connection():
    """
    Establishes and returns a connection to the MySQL database.
    Uses pymysql to connect to the database with specified credentials.
    
    :return: A pymysql connection object.
    """
    # Establish the connection to the MySQL database
    conn = pymysql.connect(
        host="localhost",  # The host where the MySQL server is running (localhost means it's on the same machine)
        user="root",  # The username to log into the MySQL server (root is the default admin user)
        password="pass@word1",  # The password associated with the username (ensure this is secure in real applications)
        database="ust_aims_db",  # The database to connect to (make sure this exists on your MySQL server)
        cursorclass=pymysql.cursors.DictCursor  # Ensures that the cursor returns rows as dictionaries (key-value pairs)
    )
    
    # Return the connection object
    return conn
