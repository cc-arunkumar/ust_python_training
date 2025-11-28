import pymysql
import csv
import datetime

# --------------------------------------------------------
# Function: get_connection()
# Purpose: Establish and return a connection to MySQL DB
# --------------------------------------------------------
def get_connection():
    """
    Creates and returns a MySQL database connection using pymysql.

    Returns:
        connection (pymysql.connections.Connection): A connection object 
        used to interact with the database.
    """
    return pymysql.connect(
        host="localhost",          # Database server host
        user="root",               # Username for DB login
        password="pass@word1",     # Password for DB login
        database="aims"            # Target database name
    )

