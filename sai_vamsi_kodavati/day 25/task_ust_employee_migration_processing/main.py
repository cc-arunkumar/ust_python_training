import json
import pymysql
import mysql_connection
import mongo_connection

# 1. Load JSON data into MySQL
def load_json_to_mysql():
    # Open and load the JSON file
    with open("employees.json", "r") as f:
        employees = json.load(f)

    # Establish MySQL connection
    conn = mysql_connection.get_mysql_connection()
    cursor = conn.cursor()

    # Insert employee data into the MySQL database
    for emp in employees:
        try:
            cursor.execute(
                "INSERT INTO employees (emp_id, name, department, age, city) VALUES (%s, %s, %s, %s, %s)",
                (emp["emp_id"], emp["name"], emp["department"], emp["age"], emp["city"])
            )
        except pymysql.err.IntegrityError:
            # Skip duplicate emp_id and print a message
            print(f"Duplicate emp_id {emp['emp_id']} skipped.")

    # Commit the changes and check the row count
    conn.commit()
    cursor.execute("SELECT COUNT(*) AS count FROM employees")
    print("Row count in MySQL:", cursor.fetchone()["count"])
    conn.close()

# 2. Read all employees data from MySQL
def read_mysql_data():
    # Establish MySQL connection
    conn = mysql_connection.get_mysql_connection()
    cursor = conn.cursor()

    # Execute a query to fetch all employee records
    cursor.execute("SELECT * FROM employees")
    rows = cursor.fetchall()
    conn.close()

    # Print and return the fetched rows
    print("Employees from MySQL:", rows)
    return rows

# 3. Transform the employee data based on age
def transform_data(rows):
    for emp in rows:
        # Add a 'category' field based on the employee's age
        emp["category"] = "Fresher" if emp["age"] < 25 else "Experienced"
    
    # Print the transformed data
    print("Transformed Data:", rows)
    return rows

# 4. Store transformed data in MongoDB
def store_in_mongo(data):
    # Establish MongoDB connection
    db = mongo_connection.get_mongo_connection()
    collection = db["employees"]

    # Clear existing documents in the collection
    collection.delete_many({})

    # Insert the new transformed data
    collection.insert_many(data)
    print("Inserted into MongoDB.")

# 5. Perform CRUD operations in MongoDB
def mongo_crud():
    # Establish MongoDB connection
    db = mongo_connection.get_mongo_connection()
    collection = db["employees"]

    # Insert a new employee document
    collection.insert_one({"emp_id": 300, "name": "New Employee", "department": "HR"})
    print("Inserted one new employee.")

    # Retrieve and print all documents from the collection
    for doc in collection.find():
        print(doc)

    # Update the department and city for employee with emp_id 202
    collection.update_one({"emp_id": 202}, {"$set": {"city": "Mumbai", "department": "DevOps"}})
    print("Updated employee 202.")

    # Delete employee with emp_id 203
    collection.delete_one({"emp_id": 203})
    print("Deleted employee 203.")

    # Delete all employees in the 'Testing' department
    collection.delete_many({"department": "Testing"})
    print("Deleted all Testing employees.")

# Main entry point of the program
if __name__ == "__main__":
    # Load data from JSON to MySQL
    load_json_to_mysql()

    # Read the data back from MySQL
    rows = read_mysql_data()

    # Transform the data by adding a category
    transformed = transform_data(rows)

    # Store the transformed data in MongoDB
    store_in_mongo(transformed)

    # Perform CRUD operations on MongoDB
    mongo_crud()
