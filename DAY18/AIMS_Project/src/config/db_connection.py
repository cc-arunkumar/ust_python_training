import mysql.connector

def get_connection():
    conn = mysql.connector.connect(
        host="localhost",  # Update with your MySQL server address
        user="root",       # Your MySQL username
        password="pass@word1",  # Your MySQL password
        database="ust_asset_db"
    )
    return conn
