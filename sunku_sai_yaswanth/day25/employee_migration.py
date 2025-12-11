import pymysql
import json
from pymysql.cursors import DictCursor
from pymongo import MongoClient

# Function to establish MySQL connection
def get_connection():
    try:
        conn = pymysql.connect(
            host='localhost',
            user='root',
            password='1234',
            database='ust_mysql_db',
            cursorclass=DictCursor
        )
        return conn
    except Exception as e:
        print("Error: ", e)
        return None

# Function to load data from JSON and insert into MySQL
def load_json_to_mysql():
    with open('employees.json', 'r') as file:
        employees = json.load(file)

    conn = get_connection()
    if conn:
        cursor = conn.cursor()
        try:
            for employee in employees:
                # Query with ON DUPLICATE KEY UPDATE to handle duplicates
                query = """
                    INSERT INTO EMPLOYEES (EMP_ID, NAME, DEPARTMENT, AGE, CITY)
                    VALUES (%s, %s, %s, %s, %s)
                    ON DUPLICATE KEY UPDATE 
                        NAME = VALUES(NAME),
                        DEPARTMENT = VALUES(DEPARTMENT),
                        AGE = VALUES(AGE),
                        CITY = VALUES(CITY)
                """
                # Execute the query with employee data
                cursor.execute(query, (
                    employee['emp_id'], 
                    employee['name'], 
                    employee['department'], 
                    employee['age'], 
                    employee['city']
                ))
                
            conn.commit()  # Commit the transaction after all inserts
            print(f"{len(employees)} employee records inserted or updated successfully!")

        except Exception as e:
            print("Error:", e)
        finally:
            cursor.close()  # Close the cursor
            conn.close()  # Close the connection

# Function to read all employees from MySQL and return them as dictionaries
def read_all_employees():
    conn = get_connection()
    employees = []  # List to store modified employees
    if conn:
        try:
            cursor = conn.cursor()
            
            # Step 1: Select all employee rows
            cursor.execute("SELECT * FROM EMPLOYEES")
            
            # Step 2: Get all rows (as dictionaries)
            rows = cursor.fetchall()  # Since we're using DictCursor, rows will already be dictionaries
            
            # Step 3: Modify each employee record by adding "category"
            for emp in rows:
                if emp["age"] < 25:
                    emp["category"] = "Fresher"
                else:
                    emp["category"] = "Experienced"
                employees.append(emp)  # Add modified employee to the list

        except Exception as e:
            print("Error:", e)
        finally:
            cursor.close()  # Close the cursor
            conn.close()  # Close the connection

    return employees  # Return the list of modified employees

# Function to connect to MongoDB and insert the modified employee data
def insert_into_mongo(employees):
    try:
        # Connect to MongoDB
        client = MongoClient("mongodb://localhost:27017/")  # Assuming MongoDB is running on localhost:27017
        db = client["ust_mongo_db"]
        collection = db["employees"]

        # Clear the collection before inserting new data
        collection.delete_many({})  # Deletes all documents in the collection

        # Insert modified employee documents into MongoDB
        collection.insert_many(employees)
        print(f"{len(employees)} employee records inserted into MongoDB!")

    except Exception as e:
        print("Error:", e)
    finally:
        client.close()  # Close MongoDB connection

# Function to perform CRUD operations in MongoDB
def mongo_crud():
    try:
        # Connect to MongoDB
        client = MongoClient("mongodb://localhost:27017/")  # Assuming MongoDB is running on localhost:27017
        db = client["ust_mongo_db"]
        collection = db["employees"]

        # Insert ONE
        collection.insert_one({"emp_id": 300, "name": "New Employee", "department": "HR", "city": "Pune"})
        print("Inserted one new employee.")

        # Read ALL
        print("All Employees in MongoDB:")
        for doc in collection.find():
            print(doc)

        # Update ONE
        collection.update_one({"emp_id": 202}, {"$set": {"city": "Mumbai", "department": "DevOps"}})


        # Delete ONE
        collection.delete_one({"emp_id": 203})

        # Delete MANY
        collection.delete_many({"department": "Testing"})

    except Exception as e:
        print("Error:", e)
    finally:
        client.close()  # Close MongoDB connection

# Main function to handle the flow
def main():
    # Step 1: Load employees from MySQL, modify the data, and return as list of dicts
    # employees = read_all_employees()

    # Step 2: Insert the modified data into MongoDB
    # insert_into_mongo(employees)

    # Step 3: Perform MongoDB CRUD operations
    mongo_crud()

# Call the main function
if __name__ == "__main__":
    main()
