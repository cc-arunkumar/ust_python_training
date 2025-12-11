from pymongo import MongoClient
from modify_each_data import fetch_and_modify_employees 

def get_mongo_client():
    try:

        client = MongoClient("mongodb://localhost:27017/")
        db = client["ust_mongo_db"] 
        collection = db["employees"] 
        return collection
    except Exception as e:
        print(f"Error connecting to MongoDB: {str(e)}")
        return None

def store_in_mongodb(modified_employees):

    collection = get_mongo_client()


    if collection is not None:

        collection.delete_many({})


        if modified_employees:
            collection.insert_many(modified_employees)
            print("Modified employee data inserted into MongoDB successfully!")
        else:
            print("No modified employee data to insert.")
    else:
        print("Error: MongoDB connection failed.")

modified_employees = fetch_and_modify_employees()


store_in_mongodb(modified_employees)
