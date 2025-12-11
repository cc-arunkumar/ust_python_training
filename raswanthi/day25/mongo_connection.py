from pymongo import MongoClient

def get_collection():
    client = MongoClient("mongodb://localhost:27017/")
    db = client["ust_db"]       
    emp_collection = db["employees_data"]      
    emp_collection.delete_many({})        
    return emp_collection

def insert_many(emp_collection, employees_data):
    result = emp_collection.insert_many(employees_data)
    print(f"Inserted {len(result.inserted_ids)} employees into MongoDB.")

def mongo_crud(emp_collection):
    # insert one
    emp_collection.insert_one({
        "emp_id": 300,
        "name": "New Employee",
        "department": "AI",
        "age": 24,
        "city": "Delhi",
        "category": "Fresher"
    })
    print("Inserted a new employee")

    # Read all
    print("All employees in MongoDB:")
    for emp in emp_collection.find():
        print(emp)

    # Update one
    result = emp_collection.update_one({"emp_id": 202}, {"$set": {"city": "Mumbai", "department": "DevOps"}})
    print(f"Updated {result.modified_count} employee(s) with emp_id=202")

    # Delete one
    result = emp_collection.delete_one({"emp_id": 203})
    print(f"Deleted {result.deleted_count} employee(s) with emp_id=203")

    # Delete many
    result = emp_collection.delete_many({"department": "Testing"})
    print(f"Deleted {result.deleted_count} employee(s) in department=Testing")
