from pymongo import MongoClient
import json

# Establish connection to MongoDB server
client = MongoClient("mongodb://localhost:27017/")  # Connect to the local MongoDB instance

# Select the database 'ust_db' or create it if it doesn't exist
db = client["ust_db"]

# Reference to 'employees' collection, which will hold the employee records
employees = db.employees

# Function to insert a single employee record from a JSON file
def insert_new_employee_individually():
    with open("data.json", "r") as file:  # Open the input JSON file containing a single employee record
        # Read the JSON record from the file
        record = json.load(file)
        # Insert the record into the 'employees' collection
        employees.insert_one(record)
        print("Employee added successfully.")  # Print confirmation after insertion

# Function to insert multiple employee records from a JSON file
def insert_multiple_employees():
    with open("data.json", "r") as file:  # Open the input JSON file containing multiple employee records
        # Read multiple records from the file
        records = json.load(file)
        # Insert the records into the 'employees' collection
        employees.insert_many(records)
        print("Multiple employees added successfully.")  # Print confirmation after bulk insertion

# Function to find employees by department
def find_employee_by_department():
    department = input("Enter department: ")  # Ask the user to input the department to search for
    # Query the collection for employees in the specified department
    data = employees.find({"department": department})
    # Print each matching employee record
    for emp in data:
        print(emp)

# Function to find employees by skillset
def find_employee_by_skill():
    skill = input("Enter skill: ")  # Ask the user to input the skill to search for
    # Query the collection for employees with the specified skill
    data = employees.find({"skills": skill})
    # Print each matching employee record
    for emp in data:
        print(emp)

# Function to find employees by city (based on nested address)
def find_employee_by_city():
    city = input("Enter city: ")  # Ask the user to input the city to search for
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
    data = employees.find()  # Retrieve all employee records from the collection
    for emp in data:
        for field in required_fields:  # Loop through the list of required fields
            if field not in emp:  # Check if the field is missing in the employee record
                # Print employee profile if any required field is missing
                print(emp)
                break  # Exit the loop once a missing field is found

# Function to filter employees by minimum experience years
def filter_by_experience():
    limit = int(input("Enter the minimum experience: "))  # Ask for the minimum years of experience
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
    # Query the collection and sort the result by 'age' field in ascending order
    data = employees.find({}).sort({"age": 1})
    # Print each employee record sorted by age
    for emp in data:
        print(emp)

# Function to modify an employee's department
def modify_emp_department():
    emp_id = int(input("Enter id: "))  # Ask the user for the employee's id
    department = input("Enter new department name: ")  # Ask the user for the new department name
    # Update the 'department' field for the employee with the given 'emp_id'
    employees.update_one({"emp_id": emp_id}, {"$set": {"department": department}})
    print("Employee department updated successfully.")  # Print confirmation after update

# Function to remove a specific skill from an employee's profile
def remove_skills():
    emp_id = int(input("Enter id: "))  # Ask the user for the employee's id
    skill = input("Enter the skill to remove: ")  # Ask the user for the skill to be removed
    # Update the 'skills' field by pulling (removing) the specified skill from the employee's record
    employees.update_one({"emp_id": emp_id}, {"$pull": {"skills": skill}})
    print("Skill removed successfully.")  # Print confirmation after removal

# Function to update the status of a project for an employee (nested field)
def update_nested_project_status():
    emp_id = int(input("Enter id: "))  # Ask for the employee's id
    status = input("Enter status: ")  # Ask for the new status
    # Update the 'status' of the first project (index 0) in the 'projects' array for the given employee
    employees.update_one({"emp_id": emp_id}, {"$set": {"projects.0.status": status}})
    print("Project status updated successfully.")  # Print confirmation after update

# Function to add a new project entry to an employee's profile
def add_new_project():
    emp_id = int(input("Enter id: "))  # Ask for the employee's id
    name = input("Enter new project: ")  # Ask for the name of the new project
    status = input("Enter status: ")  # Ask for the status of the new project
    # Create a new project dictionary with 'name' and 'status' fields
    project = {"name": name, "status": status}
    # Push (add) the new project to the 'projects' array for the given employee
    employees.update_one({"emp_id": emp_id}, {"$push": {"projects": project}})
    print("New project added successfully.")  # Print confirmation after addition

# Function to increment an employee's experience by 1 year
def increment_experience_counter():
    emp_id = int(input("Enter id: "))  # Ask for the employee's id
    # Increment the 'experience_years' field by 1 for the specified employee
    employees.update_one({"emp_id": emp_id}, {"$inc": {"experience_years": 1}})
    print("Experience incremented by 1 year.")  # Print confirmation after increment

# Function to rename a field for all employee records
def rename_field():
    field = input("Enter the field to rename: ")  # Ask for the field to rename
    new_field = input("Enter new field name: ")  # Ask for the new field name
    # Rename the specified field to the new field name for all records
    employees.update_many({}, {"$rename": {field: new_field}})
    print("Field renamed successfully.")  # Print confirmation after renaming

# Function to delete a specific field from an employee's profile
def delete_field():
    emp_id = int(input("Enter id: "))  # Ask for the employee's id
    field = input("Enter the field to delete: ")  # Ask for the field to delete
    # Remove the specified field for the employee with the given 'emp_id'
    employees.update_one({"emp_id": emp_id}, {"$unset": {field: 1}})
    print("Field deleted successfully.")  # Print confirmation after deletion

# Function to bulk update all employees based on a condition (e.g., project status)
def bulk_update_based_on_conditions():
    # Update the status of the first project for all employees where 'projects.0.status' exists
    employees.update_many({"projects.0.status": {"$exists": True}}, {"$set": {"projects.0.status": "in-progress"}})
    print("Bulk update completed successfully.")  # Print confirmation after bulk update

# Function to delete an employee by their 'emp_id'
def delete_emp_by_id():
    emp_id = int(input("Enter id: "))  # Ask for the employee's id
    # Delete the employee with the given 'emp_id'
    employees.delete_one({"emp_id": emp_id})
    print("Employee deleted successfully.")  # Print confirmation after deletion

# Function to delete employees based on a condition (e.g., experience < 2 years)
def delete_emp_by_condition():
    # Delete all employees with less than 2 years of experience
    employees.delete_many({"experience_years": {"$lt": 2}})
    print("Employees matching condition deleted.")  # Print confirmation after deletion

# Main menu loop for interacting with the system
while True:
    # Print the menu options for the user
    print(" ............EMPLOYEE SKILLS AND PROJECT TRACKING..........")
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
