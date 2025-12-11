from db_connection import get_mongo_connection  # Import the function to establish MongoDB connection

class MongoService:
    # Initialize the MongoService class, which will handle all MongoDB operations
    def __init__(self):
        self.collection = get_mongo_connection()  # Get the MongoDB collection from the connection function

    # Method to clear all documents in the MongoDB collection
    def clear_collection(self):
        self.collection.delete_many({})  # Deletes all documents in the collection
        print("MongoDB Collection Cleared.")  # Print confirmation message

    # Method to insert multiple documents (employees) into the MongoDB collection
    def insert_many(self, docs):
        self.collection.insert_many(docs)  # Inserts a list of documents into the collection
        print("Inserted Modified Employees Into MongoDB.")  # Print confirmation message

    # Method to insert a single document (employee) into the MongoDB collection
    def insert_one(self, doc):
        self.collection.insert_one(doc)  # Insert a single document
        print("One Employee Inserted.")  # Print confirmation message

    # Method to read all documents (employees) from the MongoDB collection
    def read_all(self):
        employees = list(self.collection.find())  # Fetch all employees from MongoDB as a list
        print("All Employees From MongoDB:")  # Print heading message
        for e in employees:  # Iterate over each employee
            print(e)  # Print each employee's details
        return employees  # Return the list of employees

    # Method to update a specific employee's details based on their emp_id
    def update_one(self, emp_id, updates):
        self.collection.update_one({"emp_id": emp_id}, {"$set": updates})  # Update the employee matching emp_id
        print("Employee Updated.")  # Print confirmation message

    # Method to delete a single employee from MongoDB by their emp_id
    def delete_one(self, emp_id):
        self.collection.delete_one({"emp_id": emp_id})  # Delete the employee matching emp_id
        print("One Employee Deleted.")  # Print confirmation message

    # Method to delete multiple employees based on their department
    def delete_many(self, department):
        self.collection.delete_many({"department": department})  # Delete employees matching the department
        print("Employees From Department Deleted:", department)  # Print confirmation message
