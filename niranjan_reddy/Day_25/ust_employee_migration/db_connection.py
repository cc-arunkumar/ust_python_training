# Importing the necessary libraries for MySQL and MongoDB connections
import pymysql
from pymongo import MongoClient

# Function to establish a connection to MongoDB
def db_mongo_connection():
    # Create a MongoDB client that connects to the local MongoDB instance
    client = MongoClient('mongodb://localhost:27017/')
    
    # Return the specific database ('ust_mongo_db') to be used for MongoDB operations
    return client['ust_mongo_db']

# Function to establish a connection to MySQL
def get_mysql_connection():
    try:
        # Establish a connection to MySQL with the provided credentials
        conn = pymysql.connect(
            host='localhost',  # Host where MySQL server is running
            user='root',  # MySQL username
            password='1234',  # MySQL password
            database='ust_mysql_db',  # Name of the MySQL database
            cursorclass=pymysql.cursors.DictCursor  # Use dictionary cursor for better results (keys instead of indexes)
        )
        
        # Return the connection object to be used for MySQL operations
        return conn
    
    except Exception as e:
        # Catch and print any connection errors
        print("Error: ", e)
