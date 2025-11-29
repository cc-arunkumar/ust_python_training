import pymysql

def get_connection():
    """
    Establishes and returns a connection to the MySQL database.

    Connection details:
    - host: localhost (database server running locally)
    - user: root (default MySQL user)
    - password: pass@word1 (user password for authentication)
    - database: ust_db (target database name)

    Returns:
        conn (pymysql.connections.Connection): Active database connection object
    """
    # Create a connection object using PyMySQL
    conn = pymysql.connect(
        host="localhost",      # Database server address
        user="root",           # Database username
        password="pass@word1", # Database password
        database="ust_db" # Target database name
    )
    return conn  # Return the connection object for use in queries