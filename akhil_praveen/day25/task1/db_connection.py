from pymongo import MongoClient
import pymysql
 
# Connect to MongoDB
def get_mongo_connection():
    client = MongoClient('mongodb://localhost:27017/')
    db = client['ust_mongo_db']
    employees = db['employees']
    print("Connection Established with Mongo")
    return employees
 
 
def get_mysql_connection():
    conn = pymysql.connect(
        host="localhost",      # Database host
        user="root",           # Database username
        password="password123", # Database password
        database="ust_mysql_db", # Database name
        cursorclass=pymysql.cursors.DictCursor
    )
    print("Connection Established with Mysql")  # Confirmation message
    return conn  # Return connection object
 