from motor.motor_asyncio import AsyncIOMotorClient
import asyncio

from modify_sql_rows  import modified_employees
from db_connection import mongo_connection

async def insert_into_mongo(docs):
    client = mongo_connection()
    db = client["ust_mongo_db"]
    collection = db["employees"]


    await collection.delete_many({})

    await collection.insert_many(docs)

    print("Inserted into MongoDB")

asyncio.run(insert_into_mongo(modified_employees))




async def mongo_crud():
    client = mongo_connection()
    db = client["ust_mongo_db"]
    collection = db["employees"]

    await collection.insert_one({"emp_id": 300, "name": "New Guy", "department": "AI", "age": 24, "city": "Delhi", "category": "Fresher"})

    async for emp in collection.find():
        print(emp)

    await collection.update_one({"emp_id": 201}, {"$set": {"city": "Mumbai", "department": "Cloud"}})

    await collection.delete_one({"emp_id": 202})

    await collection.delete_many({"department": "Testing"})

asyncio.run(mongo_crud())
