import pymysql
import csv
from datetime import datetime

def get_connection():
    """
    Establish a connection to the MySQL database.

    Returns:
        conn (pymysql.connections.Connection): Active database connection object.
    """
    conn = pymysql.Connect(
        host="localhost",
        user="root",
        password="pass@word1",
        database="ust_inventory_db",
        cursorclass=pymysql.cursors.DictCursor
    )
    return conn

