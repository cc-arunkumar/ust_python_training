from pymongo import MongoClient
from config import get_mongo_connection

def insert_into_mongo(data):
    db = get_mongo_connection()
    if db is None:
        return

    try:
        collection = db["employees"]

        collection.delete_many({})

        collection.insert_many(data)
        print("Data inserted into MongoDB successfully.")
    
    except Exception as err:
        print(f"Error: {err}")

def perform_crud_operations():
    db = get_mongo_connection()
    if db is None:
        return []

    try:
        collection = db["employees"]

        new_employee = {
            "emp_id": 206,
            "name": "Nina Thomas",
            "department": "Cloud",
            "age": 24,
            "city": "Delhi",
            "category": "Fresher"
        }
        collection.insert_one(new_employee)

        all_employees = list(collection.find())

        collection.update_one(
            {"emp_id": 206},
            {"$set": {"city": "Mumbai", "department": "AI"}}
        )

        collection.delete_one({"emp_id": 206})

        collection.delete_many({"department": "AI"})

        return all_employees
    
    except Exception as err:
        print(f"Error: {err}")
        return []
