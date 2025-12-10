from pymongo import MongoClient
import json

# Establish connection to MongoDB server
client = MongoClient("mongodb://localhost:27017/")

# Select the database 'ust_db'
db = client["ust_db"]
# db.create_collection("employees")  # Uncomment if you want to create a collection
# print("Collection created successfully")

# Reference to 'employees' collection
employees = db.employees

# Function to insert a single employee record from a JSON file
def insert_new_employee_individually():
    with open("input.json", "r") as file:
        # Read the JSON record from file
        record = json.load(file)
        # Insert the record into the 'employees' collection
        employees.insert_one(record)

# Function to insert multiple employee records from a JSON file
def insert_multiple_employees():
    with open("input_multiple_record.json", "r") as file:
        # Read multiple records from the JSON file
        records = json.load(file)
        # Insert the records into the 'employees' collection
        employees.insert_many(records)

# Function to find employees by department
def find_employee_by_department():
    department = input("Enter department: ")
    # Query the collection for employees in the specified department
    data = employees.find({"department": department})
    # Print each matching employee record
    for emp in data:
        print(emp)

# Function to find employees by skillset
def find_employee_by_skill():
    skill = input("Enter skill: ")
    # Query the collection for employees with the specified skill
    data = employees.find({"skills": skill})
    # Print each matching employee record
    for emp in data:
        print(emp)

# Function to find employees by city (based on nested address)
def find_employee_by_city():
    city = input("Enter city: ")
    # Query the collection for all employees
    data = employees.find()
    # Print employees whose address contains the specified city
    for emp in data:
        if "address" in emp and emp["address"]["city"] == city:
            print(emp)

# List of required fields for employee profiles
required_fields = ["emp_id", "name", "age", "department", "skills", "address", "projects"]

# Function to find employees with missing fields
def read_missing_field():
    data = employees.find()
    for emp in data:
        for field in required_fields:
            if field not in emp:
                # Print employee profile if any required field is missing
                print(emp)
                break

# Function to filter employees by minimum experience years
def filter_by_experience():
    limit = int(input("Enter the minimum experience: "))
    # Query the collection for employees with experience greater than the specified limit
    data = employees.find({"experience_years": {"$gt": limit}})
    # Print each matching employee record
    for emp in data:
        print(emp)

# Function to project only specific fields for employees
def projection_for_limited_fields():
    # Query the collection to project only 'emp_id', 'name', and 'department' fields
    data = employees.find({}, {"emp_id": 1, "name": 1, "department": 1})
    # Print each matching employee record
    for emp in data:
        print(emp)

# Function to sort employees by age (ascending order)
def sort_by_age():
    # Query the collection and sort the result by 'age' field
    data = employees.find({}).sort({"age": 1})
    # Print each employee record sorted by age
    for emp in data:
        print(emp)

# Function to modify an employee's department
def modify_emp_department():
    emp_id = int(input("Enter id: "))
    department = input("Enter new department name: ")
    # Update the 'department' field for the employee with the given 'emp_id'
    employees.update_one({"emp_id": emp_id}, {"$set": {"department": department}})

# Function to remove a specific skill from an employee's profile
def remove_skills():
    emp_id = int(input("Enter id: "))
    skill = input("Enter the skill to remove: ")
    # Update the 'skills' field by pulling (removing) the specified skill
    employees.update_one({"emp_id": emp_id}, {"$pull": {"skills": skill}})

# Function to update the status of a project for an employee (nested field)
def update_nested_project_status():
    emp_id = int(input("Enter id: "))
    status = input("Enter status: ")
    # Update the 'status' of the first project (index 0) in the 'projects' array
    employees.update_one({"emp_id": emp_id}, {"$set": {"projects.0.status": status}})

# Function to add a new project entry to an employee's profile
def add_new_project():
    emp_id = int(input("Enter id: "))
    name = input("Enter new project: ")
    status = input("Enter status: ")
    # Create a new project dictionary
    project = {"name": name, "status": status}
    # Push (add) the new project to the 'projects' array
    employees.update_one({"emp_id": emp_id}, {"$push": {"projects": project}})

# Function to increment an employee's experience by 1 year
def increment_experience_counter():
    emp_id = int(input("Enter id: "))
    # Increment the 'experience_years' field by 1 for the specified employee
    employees.update_one({"emp_id": emp_id}, {"$inc": {"experience_years": 1}})

# Function to rename a field for all employee records
def rename_field():
    field = input("Enter the field to rename: ")
    new_field = input("Enter new field name: ")
    # Rename the specified field to the new field name for all records
    employees.update_many({}, {"$rename": {field: new_field}})

# Function to delete a specific field from an employee's profile
def delete_field():
    emp_id = int(input("Enter id: "))
    field = input("Enter the field to delete: ")
    # Remove the specified field for the employee with the given 'emp_id'
    employees.update_one({"emp_id": emp_id}, {"$unset": {field: 1}})

# Function to bulk update all employees based on a condition (e.g., project status)
def bulk_update_based_on_conditions():
    # Update the status of the first project for all employees where 'projects.0.status' exists
    employees.update_many({"projects.0.status": {"$exists": True}}, {"$set": {"projects.0.status": "in-progress"}})

# Function to delete an employee by their 'emp_id'
def delete_emp_by_id():
    emp_id = int(input("Enter id: "))
    # Delete the employee with the given 'emp_id'
    employees.delete_one({"emp_id": emp_id})

# Function to delete employees based on a condition (e.g., experience < 2 years)
def delete_emp_by_condition():
    # Delete all employees with less than 2 years of experience
    employees.delete_many({"experience_years": {"$lt": 2}})

# Main menu loop for interacting with the system
while True:
    # Print the menu options for the user
    print("1.Insert new employee profiles individually")
    print("2.Bulk insertion of multiple employees")
    print("3.Find employees by department")
    print("4.Find employees by skillset")
    print("5.Find employees by city")
    print("6.Read employees missing particular fields")
    print("7.Filter by experience range")
    print("8.Query nested fields")
    print("9.Projection for limited fields")
    print("10.Sorting by age")
    print("11.Modify employee department")
    print("12.Remove skills")
    print("13.Update nested project status")
    print("14.Add new project entries")
    print("15.Increment experience counter")
    print("16.Rename fields")
    print("17.Delete fields")
    print("18.Bulk update based on conditions")
    print("19.Delete individual employee profiles")
    print("20.Delete employees matching conditions")
    # Get user input for menu choice
    choice = int(input("Enter choice: "))
    
    # Match the user input with the corresponding function
    match choice:
        case 1:
            insert_new_employee_individually()
        case 2:
            insert_multiple_employees()
        case 3:
            find_employee_by_department()
        case 4:
            find_employee_by_skill()
        case 5:
            find_employee_by_city()
        case 6:
            read_missing_field()
        case 7:
            filter_by_experience()
        case 9:
            projection_for_limited_fields()
        case 10:
            sort_by_age()
        case 11:
            modify_emp_department()
        case 12:
            remove_skills()
        case 13:
            update_nested_project_status()
        case 14:
            add_new_project()
        case 15:
            increment_experience_counter()
        case 16:
            rename_field()
        case 17:
            delete_field()
        case 18:
            bulk_update_based_on_conditions()
        case 19:
            delete_emp_by_id()
        case 20:
            delete_emp_by_condition()
        case _:
            exit()  # Exit the program if an invalid choice is entered
