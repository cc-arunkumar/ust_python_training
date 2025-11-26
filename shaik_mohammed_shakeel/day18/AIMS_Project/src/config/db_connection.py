import pymysql  # Import the pymysql library to interact with MySQL

# Function to establish and return a database connection
def get_connection():
    # Establishing a connection to the MySQL database
    conn = pymysql.connect(
        host="localhost",       # The host where the database is running (localhost in this case)
        user="root",            # The username used to authenticate with MySQL
        password="pass@word1",  # The password associated with the 'root' user
        database="ust_asset_db" # The name of the database to connect to
    )
    return conn  # Return the connection object to be used for executing queries
