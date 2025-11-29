import pymysql

def get_connection():
    """
    Creates and returns a MySQL database connection using pymysql.
    
    This function is used every time the API interacts with the database.
    It establishes a connection with the MySQL server using the given
    host, username, password, and database name.
    
    Returns:
        conn (pymysql.connections.Connection): Active DB connection object.
    """

    # Establish connection to MySQL database
    conn = pymysql.connect(
        host="localhost",        # Database server location (usually localhost)
        user="root",             # MySQL username
        password="pass@word1",   # MySQL password for authentication
        database="employee_db"   # Database name used by the application
    )

    # Return the database connection object
    return conn
