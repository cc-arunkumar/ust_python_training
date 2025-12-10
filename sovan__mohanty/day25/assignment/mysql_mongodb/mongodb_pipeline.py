from pymongo import MongoClient
import pymysql

# Connect to MySQL database
mysql_conn = pymysql.connect(
    host="localhost",
    user="root",
    password="pass@word1",
    database="ust_mysql_db",
    cursorclass=pymysql.cursors.DictCursor
)
mysql_cursor = mysql_conn.cursor()

# Connect to MongoDB
mongo_client = MongoClient("mongodb://localhost:27017/")
mongo_db = mongo_client["ust_mongo_db"]
mongo_collection = mongo_db["employees"]

def transform_data(rows):
    # Add category based on age
    for row in rows:
        row["category"] = "Fresher" if row["age"] < 25 else "Experienced"
    return rows

def store_to_mongodb(employees):
    # Clear collection and insert new data
    mongo_collection.delete_many({})
    mongo_collection.insert_many(employees)

def mongodb_crud():
    # Insert one new employee
    mongo_collection.insert_one({"emp_id": 300, "name": "New Employee", "department": "AI"})

    # Display all employees
    print("All employees in MongoDB:")
    for emp in mongo_collection.find():
        print(emp)

    # Update one employee
    mongo_collection.update_one({"emp_id": 201}, {"$set": {"city": "Mumbai", "department": "Data"}})

    # Delete one employee
    mongo_collection.delete_one({"emp_id": 202})

    # Delete many employees by department
    mongo_collection.delete_many({"department": "Testing"})

    # Display final employees
    print("Final employees in MongoDB:")
    for emp in mongo_collection.find():
        print(emp)

if __name__ == "__main__":
    # Fetch data from MySQL
    mysql_cursor.execute("SELECT emp_id, name, department, age, city FROM employees")
    rows = mysql_cursor.fetchall()

    # Transform and store in MongoDB
    transformed = transform_data(rows)
    store_to_mongodb(transformed)

    # Perform CRUD operations in MongoDB
    mongodb_crud()

    # Close connections
    mysql_cursor.close()
    mysql_conn.close()
    mongo_client.close()

#Sample Execution
# All employees in MongoDB:
# {'_id': ObjectId('6939baab020cf16a51bf204f'), 'emp_id': 201, 'name': 'Anu Joseph', 'department': 'AI', 'age': 23, 'city': 'Trivandrum', 'category': 'Fresher'}
# {'_id': ObjectId('6939baab020cf16a51bf2050'), 'emp_id': 202, 'name': 'Rahul Menon', 'department': 'Cloud', 'age': 26, 'city': 'Kochi', 'category': 'Experienced'}
# {'_id': ObjectId('6939baab020cf16a51bf2051'), 'emp_id': 203, 'name': 'Sahana R', 'department': 'Testing', 'age': 22, 'city': 'Chennai', 'category': 'Fresher'}
# {'_id': ObjectId('6939baab020cf16a51bf2052'), 'emp_id': 204, 'name': 'Vishnu Prakash', 'department': 'Cybersecurity', 'age': 29, 'city': 'Trivandrum', 'category': 'Experienced'}
# {'_id': ObjectId('6939baab020cf16a51bf2053'), 'emp_id': 205, 'name': 'Maya Kumar', 'department': 'AI', 'age': 25, 'city': 'Bangalore', 'category': 'Experienced'}
# {'_id': ObjectId('6939baab020cf16a51bf2054'), 'emp_id': 300, 'name': 'New Employee', 'department': 'AI'}
# Final employees in MongoDB:
# {'_id': ObjectId('6939baab020cf16a51bf204f'), 'emp_id': 201, 'name': 'Anu Joseph', 'department': 'Data', 'age': 23, 'city': 
# 'Mumbai', 'category': 'Fresher'}
# {'_id': ObjectId('6939baab020cf16a51bf2052'), 'emp_id': 204, 'name': 'Vishnu Prakash', 'department': 'Cybersecurity', 'age': 29, 'city': 'Trivandrum', 'category': 'Experienced'}
# {'_id': ObjectId('6939baab020cf16a51bf2053'), 'emp_id': 205, 'name': 'Maya Kumar', 'department': 'AI', 'age': 25, 'city': 'Bangalore', 'category': 'Experienced'}
# {'_id': ObjectId('6939baab020cf16a51bf2054'), 'emp_id': 300, 'name': 'New Employee', 'department': 'AI'}