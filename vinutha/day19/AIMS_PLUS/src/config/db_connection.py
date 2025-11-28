import pymysql
from datetime import datetime

# Function to establish and return a connection to the MySQL database
def get_Connection():
    return pymysql.connect(
        host="localhost",      # Database server host
        user="root",           # Database username
        password="pass@word1", # Database password
        database="ust_asset_db" # Database name
    )