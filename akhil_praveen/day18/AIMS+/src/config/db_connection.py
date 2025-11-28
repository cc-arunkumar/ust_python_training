import pymysql

# Function to establish and return a connection to the MySQL database
def get_connection():
    conn = pymysql.connect(
        host="localhost",           # The host where the MySQL server is running (localhost for local connection)
        user="root",                # The MySQL username
        password="pass@word1",      # The MySQL password for the username
        database="ust_aims_plus"    # The name of the database to connect to
    )
    return conn  # Return the connection object for use in queries
