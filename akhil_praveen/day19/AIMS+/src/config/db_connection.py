import pymysql
import os
from dotenv import load_dotenv

load_dotenv()

# Function to establish and return a connection to the MySQL database
def get_connection():
    conn = pymysql.connect(
        host="localhost",           # The host where the MySQL server is running (localhost for local connection)
        user=os.getenv("db_username"),                # The MySQL username
        password=os.getenv("db_password"),      # The MySQL password for the username
        database="ust_aims_plus"    # The name of the database to connect to
    )
    return conn  # Return the connection object for use in queries
