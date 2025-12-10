from motor.motor_asyncio import AsyncIOMotorClient
import pymysql

def get_connection():
    return pymysql.connect(
        host="localhost",
        user="root",
        password="pass@word1",
        database="task_table_users_phase2"
    )
def mongo_connection():
        return AsyncIOMotorClient("mongodb://localhost:27017")
