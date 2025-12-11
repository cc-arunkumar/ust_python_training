from pymongo import MongoClient  # Import MongoDB client library
import pymysql  # Import MySQL client library


# Function to establish a connection with MongoDB and return the 'employees' collection
def get_mongo_connection():
    client = MongoClient('mongodb://localhost:27017/')  # Connect to MongoDB server at the specified URI
    db = client['ust_mongo_db']  # Access the 'ust_mongo_db' database
    employees = db['employees']  # Access the 'employees' collection within the database
    print("Connection Established with Mongo")  # Log a message indicating successful connection
    return employees  # Return the 'employees' collection for use in other operations


# Function to establish a connection with MySQL and return the connection object
def get_mysql_connection():
    conn = pymysql.connect(  # Establish connection with MySQL database
        host="localhost",  # Host where the MySQL server is running (localhost for local machine)
        user="root",  # MySQL username
        password="password1",  # MySQL password
        database="ust_mysql_db",  # Name of the database to connect to
        cursorclass=pymysql.cursors.DictCursor  # Return rows as dictionaries, making column names accessible by key
    )
    print("Connection Established with Mysql")  # Log a message indicating successful connection
    return conn  # Return the MySQL connection object for use in other operations
