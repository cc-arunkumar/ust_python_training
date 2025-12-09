# UST – Employee Skills & Project Tracking
# System (ESPTS)
# Project Requirement Document (MongoDB-based)
# 1. Project Overview
# UST wants to build an internal Employee Skills & Project Tracking System
# (ESPTS) to maintain accurate information about employees, skills, departments,
# project allocations, and experience levels.
# This system will be used by:
# HR team
# Delivery Managers
# Resource Allocation team
# Internal L&D team
# The backend database for this system must be built using MongoDB, utilizing its
# flexible document model.
# 2. Purpose of the System
# The goal is to create a single MongoDB collection that stores employees and
# their related operational data, allowing for:
# Easy insertion of new employee profiles
# Searching / filtering based on skillsets, department, experience
# Updating employee competencies and project status
# Archival and deletion operations for outdated records
# Day 24 1
# This project MUST demonstrate full coverage of CRUD operations (Create, Read,
# Update, Delete) in MongoDB.
# 3. Target Collection
# The system will maintain a single MongoDB collection:
# employees
# Each document represents a UST employee.
# 4. Functional Requirements
# The system MUST support the following MongoDB operations:
# 4.1 Create Operations
# Insert new employee profiles individually
# Bulk insertion of multiple employees
# Create nested fields
# Store project details as an array of objects
# Store skills as an array of strings
# 4.2 Read Operations
# Find employees by department
# Find employees by skillset
# Find employees by city
# Read employees missing particular fields (e.g., skills missing)
# Filter by experience range
# Query nested fields (e.g., project-status)
# Projection for limited fields
# Day 24 2
# Sorting by age, experience, name
# 4.3 Update Operations
# Modify employee department
# Add or remove skills
# Update nested project status
# Add new project entries
# Increment experience counter
# Rename and delete fields
# Bulk update based on conditions
# Upsert employee profile if not found
# 4.4 Delete Operations
# Delete individual employee profiles
# Delete employees matching conditions (e.g., low experience)
# Delete specific fields (not entire document)
# Remove array elements (skills, projects)
# 5. Employee Document Structure
# Every employee record MUST follow below structure (fields may vary across
# employees):
# {
#  "emp_id": <Number>,
#  "name": <String>,
#  "age": <Number>,
#  "department": <String>, // Examples: "AI", "Cloud", "Testing", "Cybersec
# urity"
#  "skills": [<String>], // List of competencies
# Day 24 3
#  "address": { // Nested document
#  "city": <String>,
#  "state": <String>
#  },
#  "projects": [ // Array of objects
#  {
#  "name": <String>,
#  "status": <String> // "planned", "in-progress", "completed", "deploye
# d"
#  }
#  ],
#  "experience_years": <Number> // 0–30
# }
# 6. Detailed Requirements
# 6.1 CREATE Requirements
# 6.1.1 The system must allow insertion of new employees
# Records can be inserted one-by-one and in bulk
# Some employees intentionally have missing fields (e.g., no skills, no projects)
# 6.1.2 Each inserted employee must be unique by emp_id
# 6.1.3 The database must automatically create the collection on
# first insert
# 6.2 READ Requirements
# 6.2.1 The system must support querying by:
# Day 24 4
# Department
# Skill
# City / State
# Age range
# Experience level
# Employees missing “skills” field
# Employees with specific project status
# Employees working on >1 project
# 6.2.2 Results must support:
# Ascending/descending sorting
# Field projection (retrieve only selected fields)
# Filtering nested documents
# Handling arrays (finding by element value)
# 6.3 UPDATE Requirements
# The system must support ALL major MongoDB update operations:
# 6.3.1 Update fields using $set
# (E.g., change department of an employee)
# 6.3.2 Increment values using $inc
# (E.g., increase experience for all employees annually)
# 6.3.3 Remove fields using $unset
# (E.g., remove address.state for all employees)
# 6.3.4 Update arrays:
# Add new skills ( $push , $addToSet )
# Day 24 5
# Remove skills ( $pull )
# Update project statuses using positional operator ( $ )
# 6.3.5 Update nested fields
# (E.g., modify project status inside projects array)
# 6.3.6 Bulk update using update_many
# (E.g., mark all cloud employees as "Cloud-Engineer")
# 6.3.7 Upsert unregistered employees
# If emp_id does not exist, create a new entry automatically
# 6.4 DELETE Requirements
# System must support:
# 6.4.1 Delete employee record
# Precise deletion using emp_id (delete_one)
# Department-based deletion (delete_many)
# 6.4.2 Delete fields within employee doc
# (e.g., remove department field from all employees — simulated cleanup)
# 6.4.3 Remove array entries
# (E.g., remove a project or specific skill)
# 6.4.4 Delete employees with:
# No skills
# Experience < 1 year
# No ongoing projects
# Day 24 6
# 7. Non-Functional Requirements
# 7.1 Data Consistency
# Employees must be uniquely identifiable via emp_id .
# 7.2 Flexibility
# Documents may vary in structure (MongoDB dynamic schema).
# 7.3 Maintainability
# Every update and delete operation must be reversible using backups.
# 7.4 Simplicity
# The project must use basic MongoDB, not advanced drivers or ORMs.
# 8. Expected Deliverables
# 1. Database Setup
# One collection: employees
# 25 sample documents meeting required structure
# 2. CRUD Implementation
# Full PyMongo script executing all mandatory CRUD operations
# 3. Project Report (optional)
# Summary of operations performed
# Screenshots of Compass views
# Python code snippets
# 9. Completion Criteria
# The project is considered complete when the trainee can:
# ✔ Insert flexible employee records
# Day 24 7
# ✔ Retrieve documents in complex ways
# ✔ Update nested structures, arrays, and multiple documents
# ✔ Use all essential MongoDB update operators
# ✔ Delete documents and their fields safely
# ✔ Demonstrate confidence in CRUD operations

from pymongo import MongoClient
import json

# Establishing a connection to MongoDB
client = MongoClient('mongodb://localhost:27017/')
client["ust_db"]
print(client.list_database_names())  # Listing all databases
print("Database created successfully")

# Selecting the database
db = client["ust_db"]
# db.create_collection("employee")  # Uncomment to create collection manually
print("Collection created successfully")

# Function to insert a single employee from JSON file into the collection
def insert_by_one():
    with open("out.json", "r") as file:
        content = json.load(file)
        for item in content:
            db.employee.insert_one(item)  # Insert each item in the file into the collection
            break  # Only insert the first employee for this function

# Function to insert multiple employees from JSON file into the collection
def insert_many():
    with open("insert_manyfile.json", "r") as file:
        content = json.load(file)
        db.employee.insert_many(content)  # Insert multiple employee documents

# Function to find employees by department
def find_by_dept(department):
    result = db.employee.find({"department": department})
    for emp in result:
        print(emp)

# Function to find employees by skill
def find_by_skill(skill):
    result = db.employee.find({"skills": skill})
    for res in result:
        print(res)

# Function to find employees by city in their address
def find_by_city(city):
    result = db.employee.find()
    for res in result:
        if "address" in res and res["address"]["city"] == city:
            print(res)

# Function to find employees missing any required fields
def read_missing_fields():
    headers = ["emp_id", "name", "age", "department", "skills", "address", "projects"]
    content = db.employee.find()
    for emp in content:
        for req in headers:
            if req not in emp:
                print(emp)  # Print the employee with missing fields
                break

# Function to filter employees based on experience greater than a given limit
def filter_by_experience(age_limit):
    result = db.employee.find({"experience_years": {"$gt": age_limit}})
    for res in result:
        print(res)

# Function to limit fields shown in query result (projection)
def project_limitedfields():
    content = db.employee.find({}, {"emp_id": 1, "name": 1, "age": 1, "department": 1})  # Limit the fields displayed
    for res in content:
        print(res)

# Function to sort employees by age in ascending order
def sort_by_age():
    content = db.employee.find({}).sort({"age": 1})  # Sorting by age in ascending order
    for emp in content:
        print(emp)

# Function to modify an employee's department based on their emp_id
def modify_emp_depart(emps_id, department):
    content = db.employee.update_one({"emp_id": emps_id}, {"$set": {"department": department}})
    print(content)

# Function to remove a specific skill from an employee's skills list
def remove_skill(emps_id, skill):
    content = db.employee.update_one({"emp_id": emps_id}, {"$pull": {"skills": skill}})
    print(content)

# Function to update the status of a nested project
def update_nested_project(emps_id, status):
    content = db.employee.update_one({"emp_id": emps_id}, {"$set": {"projects.0.status": status}})
    print(content)

# Function to add a new project to an employee's project list
def add_new_project(emps_id, name, status):
    project = {"name": name, "status": status}
    content = db.employee.update_one({"emp_id": emps_id}, {"$push": {"projects": project}})
    print(content)

# Function to increment an employee's years of experience
def incre_experience(emps_id):
    emp = db.employee.update_one({"emp_id": emps_id}, {"$inc": {"experience_years": 1}})

# Function to rename a field in all documents
def rename_delete(field, new_field):
    db.employee.update_many({}, {"$rename": {field: new_field}})

# Function to delete a specific field from an employee's document
def delete_fields(emps_id, field):
    db.employee.update_one({"emp_id": emps_id}, {"$unset": {field: 1}})

# Function to update all employees with a certain project status condition
def bulk_update_based_on_conditions():
    db.employees.update_many({"projects.0.status": {"$exists": True}}, {"$set": {"projects.0.status": "in-progress"}})

# Function to delete an employee by their emp_id
def delete_emp_by_id():
    emp_id = int(input("Enter id: "))
    db.employees.delete_one({"emp_id": emp_id})

# Function to delete employees matching certain conditions (e.g., experience years less than 2)
def delete_emp_by_condition():
    db.employees.delete_many({"experience_years": {"$lt": 2}})

# Main loop to interact with the user and allow them to select operations
while True:
    print("1: Insert one employee into collection")
    print("2: Insert many employees into collection")
    print("3: Find employees by department")
    print("4: Find employees by skillset")
    print("5: Find employees by city")
    print("6: Read employees missing particular fields")
    print("7: Filter by experience range")
    print("8: Query nested fields")
    print("9: Projection for limited fields")
    print("10: Sorting by age")
    print("11: Modify employee department")
    print("12: Remove skills")
    print("13: Update nested project status")
    print("14: Add new project entries")
    print("15: Increment experience counter")
    print("16: Rename fields")
    print("17: Delete fields")
    print("18: Bulk update based on conditions")
    print("19: Delete individual employee profiles")
    print("20: Delete employees matching conditions")
    
    value = int(input("Choose a choice: "))
    
    # Match based on user's choice and execute the corresponding function
    match value:
        case 1:
            insert_by_one()
            print("Employee inserted successfully")
        case 2:
            insert_many()
            print("Employees inserted successfully")
        case 3:
            dept = input("Enter the department name: ")
            find_by_dept(dept)
            print("Employee found by department")
        case 4:
            skill = input("Enter your skill: ")
            find_by_skill(skill)
        case 5:
            city = input("Enter your city name: ")
            find_by_city(city)
        case 6:
            read_missing_fields()
        case 7:
            range_limit = int(input("Enter the age limit range: "))
            filter_by_experience(range_limit)
        case 9:
            project_limitedfields()
        case 10:
            sort_by_age()
        case 11:
            emps_id = int(input("Enter employee id: "))
            dept = input("Enter the department name: ")
            modify_emp_depart(emps_id, dept)
        case 12:
            emps_id = int(input("Enter employee id: "))
            skill = input("Enter your skill: ")
            remove_skill(emps_id, skill)
        case 13:
            status = input("Enter the status: ")
            emps_id = int(input("Enter the employee id: "))
            update_nested_project(emps_id, status)
        case 14:
            emps_id = int(input("Enter the employee id: "))
            status = input("Enter the field name: ")
            name = input("Enter the entry fields: ")
            add_new_project(emps_id, name, status)
        case 15:
            emps_id = int(input("Enter the employee id: "))
            incre_experience(emps_id)
        case 16:
            field = input("Enter the field name: ")
            new_field = input("Enter the new field name: ")
            rename_delete(field, new_field)
        case 17:
            emps_id = int(input("Enter the employee id: "))
            field = input("Enter the employee field to delete: ")
            delete_fields(emps_id, field)
        case 18:
            bulk_update_based_on_conditions()
        case 19:
            delete_emp_by_id()
        case 20:
            delete_emp_by_condition()
        case _: break  # Exit the loop
