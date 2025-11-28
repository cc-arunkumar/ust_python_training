import mysql.connector  # MySQL connector for database interaction

# Establish connection to MySQL database
def db_connector():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="pass@word1",
        database="aiims"
    )
    return conn
