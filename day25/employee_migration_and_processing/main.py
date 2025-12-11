from mysql import MySQLService  # Import the MySQL service module
from mongo import MongoService  # Import the MongoDB service module

# Initialize MySQLService and perform database operations
mysql = MySQLService()
mysql.create_table()  # Create a table in MySQL
mysql.load_json_to_mysql("employees.json")  # Load data from a JSON file into MySQL
employees = mysql.read_employees()  # Read all employee data from MySQL

# Modify employee data by adding a 'category' based on age
modified = []  # Initialize an empty list to store modified employees
for emp in employees:  # Iterate through each employee
    emp['category'] = "Fresher" if emp['age'] < 25 else "Experienced"  # Add 'category' based on age
    modified.append(emp)  # Append modified employee data to the list

print("\nModified Employees:", modified)  # Print modified employee data

# Initialize MongoService and perform MongoDB operations
mongo = MongoService()
mongo.clear_collection()  # Clear the MongoDB collection
mongo.insert_many(modified)  # Insert all modified employees into MongoDB

# Insert a single new employee into MongoDB
mongo.insert_one({
    "emp_id": 999,
    "name": "New Employee",
    "department": "AI",
    "age": 24,
    "city": "Kochi",
    "category": "Fresher"
})

# Read all employees from MongoDB
mongo.read_all()

# Update a specific employee's details in MongoDB based on emp_id (201)
mongo.update_one(201, {"city": "UpdatedCity", "department": "UpdatedDept"})  # Update employee with emp_id 201

# Delete a specific employee from MongoDB by emp_id (203)
mongo.delete_one(203)  # Delete employee with emp_id 203

# Delete multiple employees in MongoDB that have a specific category (e.g., "Testing")
mongo.delete_many("Testing")  # Delete employees with the "Testing" category

# Read all employees from MongoDB again after updates
mongo.read_all()
