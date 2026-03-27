import pymongo

def perform_mongo_crud_operations():
    # Step 1: Connect to MongoDB
    client = pymongo.MongoClient("mongodb://localhost:27017/")  # Connect to MongoDB
    db = client['ust_mongo_db']  # Use the 'ust_mongo_db' database
    collection = db['employees']  # Use the 'employees' collection

    # Step 2: Create - Insert a new employee
    new_employee = {
        "emp_id": 206,
        "name": "Arjun Sharma",
        "department": "AI",
        "age": 28,
        "city": "Mumbai",
        "category": "Experienced"
    }
    collection.insert_one(new_employee)
    print(f"Employee {new_employee['emp_id']} inserted.")

    # Step 3: Read - Find all employees
    all_employees = collection.find()
    print("All employees:")
    for emp in all_employees:
        print(emp)

    # Step 4: Update - Update one employee's city and department
    collection.update_one(
        {"emp_id": 206},
        {"$set": {"city": "Pune", "department": "Cloud Computing"}}
    )
    print("Employee 206 updated.")

    # Step 5: Delete - Delete one employee by emp_id
    collection.delete_one({"emp_id": 206})
    print("Employee 206 deleted.")

    # Step 6: Delete many - Delete all employees from the 'AI' department
    collection.delete_many({"department": "AI"})
    print("All AI department employees deleted.")

    # Close the connection to MongoDB
    client.close()

# Call the function to perform CRUD operations
perform_mongo_crud_operations()


# Employee 206 inserted.
# All employees:
# {'_id': ObjectId('69391f619e836a104a15e34b'), 'emp_id': 201, 'name': 'Anu Joseph', 'department': 'AI', 'age': 23, 'city': 'Trivandrum', 'category': 'Fresher'}
# {'_id': ObjectId('69391f619e836a104a15e34c'), 'emp_id': 202, 'name': 'Rahul Menon', 'department': 'Cloud', 'age': 26, 'city': 'Kochi', 'category': 'Experienced'}
# {'_id': ObjectId('69391f619e836a104a15e34d'), 'emp_id': 203, 'name': 'Sahana R', 'department': 'Testing', 'age': 22, 'city': 'Chennai', 'category': 'Fresher'}
# {'_id': ObjectId('69391f619e836a104a15e34e'), 'emp_id': 204, 'name': 'Vishnu Prakash', 'department': 'Cybersecurity', 'age': 29, 'city': 'Trivandrum', 'category': 'Experienced'}
# {'_id': ObjectId('69391f619e836a104a15e34f'), 'emp_id': 205, 'name': 'Maya Kumar', 'department': 'AI', 'age': 25, 'city': 'Bangalore', 'category': 'Experienced'}
# {'_id': ObjectId('693920301bdaacf2a3381c81'), 'emp_id': 206, 'name': 'Arjun Sharma', 'department': 'AI', 'age': 28, 'city': 'Mumbai', 'category': 'Experienced'}
# Employee 206 updated.
# Employee 206 deleted.
# All AI department employees deleted.
