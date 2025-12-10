import pymysql 
from pymongo import MongoClient
def get_connection():
    conn = pymysql.connect(
        user="root",
        password="password123",
        host="localhost",
        database="ust_mysql_db",
        cursorclass=pymysql.cursors.DictCursor
    )
    
    return conn

def get_connection_mongo():
    client = MongoClient('mongodb://localhost:27017/')
    db = client['ust_mongo_db']
    collection = db['employees']
    collection.create_index("emp_id",unique=True)
    return collection