import mysql.connector


def get_Connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="pass@word1",
        database="ust_db"
    )