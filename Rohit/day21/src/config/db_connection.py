import pymysql


# Define a function to establish a database connection
def get_connection():
    # Return a connection object using pymysql.connect()
    # Parameters:
    # - host: the database server address (here it's localhost)
    # - user: the MySQL username (here it's 'root')
    # - password: the password for the MySQL user
    # - database: the specific database to connect to ('ust_asset_inventory')
    return pymysql.connect(
        host="localhost",       # Database server is running locally
        user="root",            # MySQL username
        password="pass@word1",  # MySQL password
        database="ust_db_employee"  # Target database name
    )

    

    