import pymysql
from pymongo import MongoClient
import json

MYSQL_HOST = "localhost"
MYSQL_USER = "root"
MYSQL_PASSWORD = "akshaya"
MYSQL_DB = "ust_mysql_db"

MONGO_URI = "mongodb://localhost:27017/"
MONGO_DB = "ust_mongo_db"
COLLECTION_NAME = "employees"

def get_mysql_connection():
    try:
        conn = pymysql.connect(
            host=MYSQL_HOST,
            user=MYSQL_USER,
            password=MYSQL_PASSWORD,
            database=MYSQL_DB,
            cursorclass=pymysql.cursors.DictCursor
        )

        if conn.open:
            print("Connected to MySQL database")
        else:
            print("Failed to connect to MySQL")
        return conn
    except pymysql.Error as err:
        print(f"Error: {err}")
        return None

def get_mongo_connection():
    try:
        client = MongoClient(MONGO_URI)
        print("Connected to MongoDB")
        return client[MONGO_DB]
    except Exception as err:
        print(f"Error: {err}")
        return None

# Inserting data into MongoDB
def insert_data_into_mongo(data):
    db = get_mongo_connection()
    
    # Explicitly check if the db is None (instead of truthy check)
    if db is not None:
        collection = db[COLLECTION_NAME]
        # Insert a list of documents
        collection.insert_many(data)
        print("Data inserted into MongoDB successfully.")
    else:
        print("Failed to insert data: MongoDB connection is not established.")

# Function to load data from JSON file
def load_data_from_json(file_path):
    try:
        with open(file_path, "r") as file:
            data = json.load(file)
        print(f"Data loaded from {file_path} successfully.")
        return data
    except Exception as err:
        print(f"Error reading JSON file: {err}")
        return []

# Example: Load data from 'employees.json' and insert into MongoDB
file_path = "employees.json"
data = load_data_from_json(file_path)

# Insert data into MongoDB
if data:
    insert_data_into_mongo(data)
else:
    print("No data to insert.")