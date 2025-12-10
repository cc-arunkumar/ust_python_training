from pymongo import MongoClient
from config import MONGO_URI, MONGO_DB, MONGO_COLLECTION

def transform_employee(emp):
    emp["category"] = "Fresher" if emp["age"] <= 25 else "Experienced"
    return emp

def insert_into_mongodb(employees):
    client = MongoClient(MONGO_URI)
    db = client[MONGO_DB]
    col = db[MONGO_COLLECTION]

    col.drop()  
    transformed = [transform_employee(emp) for emp in employees]
    col.insert_many(transformed)

    print(f" Inserted {len(transformed)} employees into MongoDB.")
    client.close()

