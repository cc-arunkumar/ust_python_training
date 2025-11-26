import pymysql

def get_connection():
    # Create and return a MySQL database connection
    conn=pymysql.connect(
        host="localhost",       # Database host
        user="root",            # MySQL username
        password="pass@word1",  # MySQL password
        database="ust_asset_db" # Target database
    )

    return conn  # Return connection object
