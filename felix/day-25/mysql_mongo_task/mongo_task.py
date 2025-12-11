from pymongo import MongoClient   # Import MongoClient to connect with MongoDB
from mysql_task import read_from_mysql   # Import function to read data from MySQL
import json   # Import JSON module for reading/writing JSON files

client = MongoClient("mongodb://localhost:27017/")   # Create MongoDB client connected to local server

db = client["ust_mongo_db"]   # Access (or create) database named 'ust_mongo_db'
# db.create_collection("employees")   # Uncomment to explicitly create 'employees' collection
# print("collection created")         # Uncomment to confirm collection creation

employees = db.employees   # Reference to 'employees' collection

data = read_from_mysql()   # Read employee data from MySQL
employees.insert_many(data)   # Insert multiple employee records into MongoDB


def insert_one_employee():   # Function to insert a single employee from JSON file
    with open("employee.json","r") as file:   # Open JSON file
        emp = json.load()   # Load employee data from file
    employees.insert_one(emp)   # Insert one employee record into MongoDB
        

def read_all_employee():   # Function to read all employees
    emp = employees.find()   # Fetch all employee records
    print(emp)   # Print cursor object (can be iterated for actual data)
        

def update_one_employee():   # Function to update one employee's city
    print("For updating city:")
    emp_id = int(input("Enter ID: "))   # Take employee ID input
    city = input("Enter new city")      # Take new city input
    employees.update_one({"emp_id",emp_id},{"city":city})   # Update city for given employee ID
        

def delete_one_employee():   # Function to delete one employee
    print("For deleting:")
    emp_id = int(input("Enter ID: "))   # Take employee ID input
    employees.delete_one({"emp_id",emp_id})   # Delete employee record by ID
        

def delete_many():   # Function to delete multiple employees based on condition
    employees.delete_many({},{"age":{"$lt":20}})   # Delete employees younger than 20