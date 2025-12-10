from pymongo import MongoClient

# Create MongoDB client and connect to database & collection
client = MongoClient("mongodb://localhost:27017/")
db = client["employee_db"]
collection = db["employee_table"]


# ----------------------------
# INSERT ONE DOCUMENT
# ----------------------------
def insert():
    """Insert a new employee document into MongoDB."""
    result = collection.insert_one({
        "emp_id": 207,
        "name": "Arumueksh",
        "department": "IT",
        "age": 45
    })

    if result.inserted_id:
        print("Insertion success")


# ----------------------------
# READ ALL DOCUMENTS
# ----------------------------
# Fetch all records from MongoDB as a list of dictionaries
result = list(collection.find())
print(result)


# ----------------------------
# UPDATE DOCUMENT BY emp_id
# ----------------------------
def update(emp_id, column, value):
    """
    Update a specific column of an employee based on emp_id.
    
    Args:
        emp_id (int): Employee ID to locate the record.
        column (str): Field name to update.
        value (any): New value to set.
    """
    result = collection.update_one(
        {"emp_id": emp_id},          # Filter document
        {"$set": {column: value}}    # Update operation
    )
    
    if result.modified_count:
        print("Update successful")


# ----------
