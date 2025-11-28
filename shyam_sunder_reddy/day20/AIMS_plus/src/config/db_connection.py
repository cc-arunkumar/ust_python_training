import pymysql
import csv
from datetime import datetime


# Establish a connection to the MySQL database.

# Returns:
#     conn (pymysql.connections.Connection): Active database connection object.
def get_connection():
    
    conn = pymysql.Connect(
        host="localhost",
        user="root",
        password="pass@word1",
        database="ust_inventory_db",
        cursorclass=pymysql.cursors.DictCursor
    )
    return conn

