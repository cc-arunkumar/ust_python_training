from config import get_mongo_db  # Assuming get_mongo_db returns the MongoDB client connection

def insert_employees_to_mongo(employee_data):
    """Insert employee data into MongoDB"""
    db = get_mongo_db()  # Get the MongoDB connection
    if db is not None:  # Ensure db is not None
        for employee in employee_data:
            db.employees.insert_one(employee)
        print("Employee data inserted into MongoDB.")
    else:
        print("Failed to establish MongoDB connection.")

def fetch_all_employees_from_mongo():
    """Fetch all employee records from MongoDB"""
    db = get_mongo_db()  # Get the MongoDB connection
    if db is not None:  # Ensure db is not None
        collection = db['employees']  # Access the 'employees' collection
        return list(collection.find())  # Return a list of all employees
    else:
        print("Failed to establish MongoDB connection.")
        return []

def update_employee_in_mongo(emp_id, updated_data):
    """Update an employee's data in MongoDB by emp_id"""
    db = get_mongo_db()  # Get the MongoDB connection
    if db is not None:  # Ensure db is not None
        collection = db['employees']  # Access the 'employees' collection
        result = collection.update_one({"emp_id": emp_id}, {"$set": updated_data})
        if result.modified_count > 0:
            print(f"Employee with emp_id {emp_id} updated successfully.")
        else:
            print(f"No employee found with emp_id {emp_id} or no changes made.")
    else:
        print("Failed to establish MongoDB connection.")

def delete_employee_from_mongo(emp_id):
    """Delete an employee from MongoDB by emp_id"""
    db = get_mongo_db()  # Get the MongoDB connection
    if db is not None:  # Ensure db is not None
        collection = db['employees']  # Access the 'employees' collection
        result = collection.delete_one({"emp_id": emp_id})
        if result.deleted_count > 0:
            print(f"Employee with emp_id {emp_id} deleted successfully.")
        else:
            print(f"No employee found with emp_id {emp_id}.")
    else:
        print("Failed to establish MongoDB connection.")

def delete_employees_by_department(department):
    """Delete employees by their department from MongoDB"""
    db = get_mongo_db()  # Get the MongoDB connection
    if db is not None:  # Ensure db is not None
        collection = db['employees']  # Access the 'employees' collection
        result = collection.delete_many({"department": department})
        print(f"Deleted {result.deleted_count} employees from the {department} department.")
    else:
        print("Failed to establish MongoDB connection.")
