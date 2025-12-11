from pymongo import MongoClient

def get_mongo_client():
    try:

        client = MongoClient("mongodb://localhost:27017/")
        db = client["ust_mongo_db"] 
        collection = db["employees"] 
        return collection
    except Exception as e:
        print(f"Error connecting to MongoDB: {str(e)}")
        return None

def perform_mongo_crud_operations():
    collection = get_mongo_client()

    if collection:

        new_employee = {
            "emp_id": 206,
            "name": "New Employee",
            "department": "Sales",
            "age": 28,
            "city": "Mumbai",
            "category": "Experienced"
        }
        collection.insert_one(new_employee)
        print("Inserted a new employee:", new_employee)

        # 2. Read ALL employees
        print("\nAll employees:")
        all_employees = collection.find()
        for emp in all_employees:
            print(emp)

        # 3. Update ONE employee 
        collection.update_one(
            {"emp_id": 202}, 
            {"$set": {"city": "Delhi", "department": "AI"}}
        )
        print("\nUpdated employee with emp_id 202.")

        # 4. Delete ONE employee using emp_id
        collection.delete_one({"emp_id": 203})
        print("\nDeleted employee with emp_id 203.")

        # 5. Delete MANY employees 
        collection.delete_many({"department": "Testing"})
        print("\nDeleted employees in the 'Testing' department.")

    else:
        print("Error: MongoDB connection failed. Cannot perform CRUD operations.")

perform_mongo_crud_operations()
