# mongo connection
import json
from pymongo import MongoClient

# Function to connect to MongoDB and return the 'employees' collection
def get_mongo_connection():
    client = MongoClient("mongodb://localhost:27017/")  
    db = client["ust_mongo_db"]                        
    return db.employees                                

# Load employee data from JSON file
with open(r'C:\Users\Administrator\Desktop\training\ust_python_training\yashaswini\day-25\task\data.json', 'r') as file:
    employees_data = json.load(file)

# Function to insert modified employee data into MongoDB
def store_modified_data_to_mongo():
    try:
        mongo_collection = get_mongo_connection()

        mongo_collection.delete_many({})  # Clear existing data in the collection

        # Add 'category' field based on age
        for employee in employees_data:
            employee["category"] = "Fresher" if employee["age"] < 25 else "Experienced"

        # Insert all employees into MongoDB
        mongo_collection.insert_many(employees_data)
        print("Data inserted successfully into MongoDB.")

    except Exception as e:
        print("Error:", e)

# Function to perform CRUD operations on MongoDB
def perform_crud_operations():
    try:
        mongo_collection = get_mongo_connection()

        # Create (Insert One)
        new_employee = {
            "emp_id": 206,
            "name": "John Doe",
            "department": "AI",
            "age": 24,
            "city": "Delhi",
            "category": "Fresher"
        }
        mongo_collection.insert_one(new_employee)
        print("New employee inserted.")

        # Read (Find All)
        employees = mongo_collection.find()
        print("All Employees:")
        for employee in employees:
            print(employee)

        # Update (Update One)
        mongo_collection.update_one(
            {"emp_id": 206},  
            {"$set": {"city": "Mumbai", "department": "Cloud"}}  
        )
        print("Employee updated.")

        # Delete (Delete One)
        mongo_collection.delete_one({"emp_id": 206})
        print("Employee deleted.")

        # Delete Many (Delete all employees from 'Testing' department)
        mongo_collection.delete_many({"department": "Testing"})
        print("Employees from 'Testing' department deleted.")

    except Exception as e:
        print("Error:", e)

# Call functions to execute the pipeline
store_modified_data_to_mongo()   
perform_crud_operations()        
