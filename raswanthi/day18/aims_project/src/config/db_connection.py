import pymysql

# -----------------------------
# Function: get_connection
# Purpose: Establish and return a connection to the MySQL database
# -----------------------------
def get_connection():
    # Create a connection object using pymysql
    # Parameters:
    # - host: Database server address (localhost means the same machine)
    # - user: Username to authenticate with MySQL
    # - password: Password for the given user
    # - database: Specific database to connect to
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password='pass@word1',
        database='ust_asset_db'
    )
    
    # Return the connection object so it can be used for queries
    return conn
