from pymongo import MongoClient
from config import MONGO_URI, MONGO_DB, MONGO_COLLECTION

def mongo_crud_operations():
    client = MongoClient(MONGO_URI)
    col = client[MONGO_DB][MONGO_COLLECTION]

    new_emp = {"emp_id": 300, "name": "New Joiner", "age": 24, "category": "Fresher"}
    col.insert_one(new_emp)
    print(" Inserted one new employee.")

    print(" All employees in MongoDB:")
    for doc in col.find({}):
        print(doc)

    col.update_one(
        {"emp_id": 202}, 
        {"$set": {"city": "Mumbai", "department": "Cloud Platform"}}
    )
    print(" Updated employee with emp_id=202.")

    col.delete_one({"emp_id": 203})
    print(" Deleted employee with emp_id=203.")

    result = col.delete_many({"department": "Testing"})
    print(f" Deleted {result.deleted_count} employees in Testing department.")

    client.close()
