import mysql.connector
from pymongo import MongoClient

def get_mysql_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",         
            password="password1", 
            database="ust_mysql_db"   
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None


def get_mongo_client():
    try:
        client = MongoClient("mongodb://localhost:27017/")
        print("MongoDB connection successful")
        return client
    except Exception as e:
        print(f"Error connecting to MongoDB: {e}")
        return None

def get_mongo_db():
    client = get_mongo_client()
    if client:
        return client['ust_mongo_db']
    else:
        return None
