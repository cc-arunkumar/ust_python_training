import pymysql
from motor.motor_asyncio import AsyncIOMotorClient
def get_connection():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="pass@word1",
        database="ust_mysql_db"
    )
def mongo_connection():
        return  AsyncIOMotorClient("mongodb://localhost:27017")
