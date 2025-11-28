import pymysql
from dotenv import load_dotenv
import os
load_dotenv()

def get_connection():
    # Establish connection to MySQL database
    conn = pymysql.connect(
        host="localhost",      # Database host
        user="root",           # Database username
        password=os.getenv("DB_PASSWORD"), # Database password
        database=os.getenv("DB") # Database name
    )
    print("Connection Established")  # Confirmation message
    return conn  # Return connection object