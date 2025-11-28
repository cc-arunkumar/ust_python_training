import pymysql
from dotenv import load_dotenv
import os
load_dotenv()

def get_connection():
    # Establish connection to MySQL database
    conn = pymysql.connect(
        host="localhost",      # Database host
        user="root",           # Database username
        password="pass@word1", # Database password
        database="aims_db" # Database name
    )
    print("Connection Established")  # Confirmation message
    return conn  # Return connection object