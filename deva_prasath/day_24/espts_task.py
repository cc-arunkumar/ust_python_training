# . Project Overview
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


from pymongo import MongoClient
import json

client = MongoClient("mongodb://localhost:27017/")

# Connecting to the 'ust_db' database
db = client['ust_db']

# Reading data from a JSON file
with open(r"D:\training\ust_python_training\deva_prasath\day_24\data.json", 'r') as f1:
    data = json.load(f1)

# Function to insert a single employee document
def insert_one_emp(emp):
    res = db.employees.insert_one(emp)
    print("Inserted ID", res.inserted_id)

# Function to insert multiple employee documents
def insert_many_emp(data):
    res = db.employees.insert_many(data)
    print("Inserted IDs:", res.inserted_ids)
    print(f"{len(res.inserted_ids)} Employee records inserted successfully")

# Function to find employees by department
def find_by_dept(dept):
    return db.employees.find({"department": dept})

# Function to find employees by skill
def find_by_skill(skill):
    return db.employees.find({"skills": skill})

# Function to find employees by city
def find_by_city(city):
    return db.employees.find({"address.city": city})

# Function to find employees with missing field
def find_missing(field):
    return db.employees.find({field: {"$exists": False}})

# Function to find employees with a minimum years of experience
def find_by_experience(min_exp):
    return db.employees.find({"experience": {"$gte": min_exp}})

# Function to find employees by project status
def find_by_status(status):
    return db.employees.find({"projects.status": status})

# Function to sort employees by age or any other field
def sort_by_age(sort_by='age', order=1):
    return db.employees.find().sort(sort_by, order)

# Function to modify an employee's department
def modify_employee_department(emp_id, new_department):
    result = db.employees.update_one(
        {"emp_id": emp_id},
        {"$set": {"department": new_department}}
    )
    print(f"Modified department for emp_id {emp_id}: {result.modified_count} document updated")

# Function to modify employee's skill (add or remove)
def modify_employee(emp_id, action, skill):
    if action == "add":
        result = db.employees.update_one(
            {"emp_id": emp_id},
            {"$addToSet": {"skills": skill}}
        )
        print(f"{emp_id} added")
    elif action == "remove":
        result = db.employees.update_one(
            {"emp_id": emp_id},
            {"$pull": {"skills": skill}}
        )
        print(f"{emp_id} removed")

# Function to update the status of an employee's project
def updated_employee_status(emp_id, project, new_status):
    result = db.employees.update_one(
        {"emp_id": emp_id, "projects.project_name": project},
        {"$set": {"projects.$.status": new_status}}
    )
    print(f"{emp_id} status updated to {new_status}")

# Function to add a new project to an employee's profile
def add_new_project(emp_id, project):
    result = db.employees.update_one(
        {"emp_id": emp_id},
        {"$push": {"projects": project}}
    )
    print(f"Added new project to emp_id {emp_id}")

# Function to increment employee's experience
def increment_experience(emp_id, years):
    result = db.employees.update_one(
        {"emp_id": emp_id},
        {"$inc": {"experience": years}}
    )
    print(f"Incremented experience for emp_id {emp_id} by {years} years")

# Function to rename a field in an employee's profile
def rename_employee_field(emp_id, old_field, new_field):
    result = db.employees.update_one(
        {"emp_id": emp_id},
        {"$rename": {old_field: new_field}}
    )
    print(f"Renamed field {old_field} to {new_field} for emp_id {emp_id}")

# Function to perform bulk updates on employees
def bulk_update_employees(conditions, update_fields):
    op = []
    for c in conditions:
        op.append(
            db.employees.update_one(
                c,
                {"$set": update_fields}
            )
        )
    result = db.employees.bulk_write(op)
    print("Bulk update completed.")

# Function to upsert an employee profile (insert or update)
def upsert_emp_profile(emp_id, employee_data):
    res = db.employees.update_one(
        {"emp_id": emp_id},
        {"$set": employee_data},
        update=True
    )
    action = "upserted" if res.upserted_id else "updated"
    print(f"Employee profile {action} for emp_id {emp_id}")

# Function to delete an employee by ID
def delete_employee(emp_id):
    result = db.employees.delete_one({"emp_id": emp_id})
    print("Deleted employee count:", result.deleted_count)

# Function to delete employees based on a condition
def delete_emp_cond(condition):
    res = db.employees.delete_many(condition)
    print("Deleted employees matching condition:", res.deleted_count)

# Function to remove an element from an array field in an employee's profile
def remove_array_element(emp_id, array_field, element_value):
    res = db.employees.update_one(
        {"emp_id": emp_id},
        {"$pull": {array_field: element_value}}
    )
    print(f"Removed element '{element_value}' from {array_field}")

# Sample employee data
emp_data = {
    "emp_id": 101,
    "name": "Dustin",
    "age": 17,
    "department": "AI",
    "skills": ["python", "mongodb"],
    "address": {"city": "Trivandrum", "state": "Kerala"},
    "projects": [{"project_name": "VisionAI", "status": "completed"}],
    "experience": 1
}

# Insert a single employee
insert_one_emp(emp_data)

# Insert multiple employees
insert_many_emp(data)

# Fetch employees by department, skill, city, etc.
dept = "AI"
employees_in_dept = find_by_dept(dept)
for emp in employees_in_dept:
    print(emp)

skill = "python"
employees_with_skill = find_by_skill(skill)
for emp in employees_with_skill:
    print(emp)

city = "Kochi"
employees_in_city = find_by_city(city)
for emp in employees_in_city:
    print(emp)

field = "skills"
employees_missing_field = find_missing(field)
for emp in employees_missing_field:
    print(emp)

min_exp = 1
employees_with_experience = find_by_experience(min_exp)
for emp in employees_with_experience:
    print(emp)

status = "completed"
employees_by_status = find_by_status(status)
for emp in employees_by_status:
    print(emp)

sorted_employees_by_age = sort_by_age(sort_by='age', order=1)
for emp in sorted_employees_by_age:
    print(emp)

# Modify employee department
emp_id = 101
new_department = "Cloud"
modify_employee_department(emp_id, new_department)

# Add or remove skills from employee
emp_id = 102
action = "add"
skill = "docker"
modify_employee(emp_id, action, skill)

# Update project status for an employee
emp_id = 103
project = "VisionAI"
new_status = "completed"
updated_employee_status(emp_id, project, new_status)

# Increment experience for an employee
emp_id = 105
years = 1
increment_experience(emp_id, years)

# Perform bulk update on employees
conditions = [{"experience": {"$lte": 1}}, {"department": "AI"}]
update_fields = {"department": "Junior AI Developer"}
bulk_update_employees(conditions, update_fields)

# Upsert employee profile
emp_id = 110
employee_data = {
    "emp_id": 110,
    "name": "Rakesh Pillai",
    "department": "Cybersecurity",
    "skills": ["networking", "firewall", "linux"],
    "projects": [{"project_name": "SecuritySuite", "status": "deployed"}],
    "experience": 7
}
upsert_emp_profile(emp_id, employee_data)

# Rename employee field
emp_id = 106
old_field = "address"
new_field = "location"
rename_employee_field(emp_id, old_field, new_field)

# Delete an employee
emp_id = 101
delete_employee(emp_id)

# Delete employees based on condition
condition = {"experience": {"$lte": 1}}
delete_emp_cond(condition)

# Remove element from an array field
emp_id = 102
array_field = "skills"
element_value = "docker"
remove_array_element(emp_id, array_field, element_value)

emp_id = 103
array_field = "projects"
element_value = {"project_name": "VisionAI"}
remove_array_element(emp_id, array_field, element_value)






#Output


# Inserted ID 6937e92a7d7fa2c63878e156
#------------------------------------------------------------------------------------------



# {'_id': ObjectId('6937c83bc9f4db2d9d88e785'), 'emp_id': 101, 'name': 'Anu Joseph', 'age': 23, 'department': 'AI', 'skills': ['python', 'mongodb'], 'address': {'city': 'Trivandrum', 'state': 'Kerala'}, 'projects': [{'name': 'VisionAI', 'status': 'completed'}, {'name': 'DocScan', 'status': 'in-progress'}], 'experience_years': 1}
# {'_id': ObjectId('6937c83bc9f4db2d9d88e789'), 'emp_id': 105, 'name': 'Maya Kumar', 'age': 25, 'department': 'AI', 'skills': ['python', 'deep-learning'], 'address': {'city': 'Bangalore', 'state': 'KA'}, 'projects': [{'name': 'VisionAI', 'status': 'completed'}], 'experience_years': 2}
# {'_id': ObjectId('6937e9079c278a4a9bef47e7'), 'emp_id': 101, 'name': 'Dustin', 'age': 17, 'department': 'AI', 'skills': ['python', 'mongodb'], 'address': {'city': 'Trivandrum', 'state': 'Kerala'}, 'projects': [{'project_name': 'VisionAI', 'status': 'completed'}], 'experience': 1}
# {'_id': ObjectId('6937e92a7d7fa2c63878e156'), 'emp_id': 101, 'name': 'Dustin', 'age': 17, 'department': 'AI', 'skills': ['python', 'mongodb'], 'address': {'city': 'Trivandrum', 'state': 'Kerala'}, 'projects': [{'project_name': 'VisionAI', 'status': 'completed'}], 'experience': 1}

#------------------------------------------------------------------------------------------


# {'_id': ObjectId('6937c83bc9f4db2d9d88e785'), 'emp_id': 101, 'name': 'Anu Joseph', 'age': 23, 'department': 'AI', 'skills': ['python', 'mongodb'], 'address': {'city': 'Trivandrum', 'state': 'Kerala'}, 'projects': [{'name': 'VisionAI', 'status': 'completed'}, {'name': 'DocScan', 'status': 'in-progress'}], 'experience_years': 1}
# {'_id': ObjectId('6937c83bc9f4db2d9d88e789'), 'emp_id': 105, 'name': 'Maya Kumar', 'age': 25, 'department': 'AI', 'skills': ['python', 'deep-learning'], 'address': {'city': 'Bangalore', 'state': 'KA'}, 'projects': [{'name': 'VisionAI', 'status': 'completed'}], 'experience_years': 2}
# {'_id': ObjectId('6937e9079c278a4a9bef47e7'), 'emp_id': 101, 'name': 'Dustin', 'age': 17, 'department': 'AI', 'skills': ['python', 'mongodb'], 'address': {'city': 'Trivandrum', 'state': 'Kerala'}, 'projects': [{'project_name': 'VisionAI', 'status': 'completed'}], 'experience': 1}
# {'_id': ObjectId('6937e92a7d7fa2c63878e156'), 'emp_id': 101, 'name': 'Dustin', 'age': 17, 'department': 'AI', 'skills': ['python', 'mongodb'], 'address': {'city': 'Trivandrum', 'state': 'Kerala'}, 'projects': [{'project_name': 'VisionAI', 'status': 'completed'}], 'experience': 1}

#------------------------------------------------------------------------------------------


# {'_id': ObjectId('6937c83bc9f4db2d9d88e786'), 'emp_id': 102, 'name': 'Rahul Menon', 'age': 
# 26, 'department': 'Cloud', 'skills': ['aws', 'docker'], 'address': {'city': 'Kochi', 'state': 'Kerala'}, 'projects': [{'name': 'USTCloudPortal', 'status': 'planned'}], 'experience_years': 3}
# {'_id': ObjectId('6937c83bc9f4db2d9d88e78a'), 'emp_id': 106, 'name': 'Arjun S', 'age': 28, 
# 'department': 'Cloud', 'skills': ['azure'], 'address': {'city': 'Kochi', 'state': 'Kerala'}, 'projects': [{'name': 'DevOpsBoost', 'status': 'in-progress'}], 'experience_years': 4}   
# {'_id': ObjectId('6937c83bc9f4db2d9d88e78c'), 'emp_id': 108, 'name': 'Suresh B', 'age': 27, 'department': 'Data', 'address': {'city': 'Kochi', 'state': 'Kerala'}, 'projects': [], 'experience_years': 3}

#------------------------------------------------------------------------------------------


# {'_id': ObjectId('6937c83bc9f4db2d9d88e78c'), 'emp_id': 108, 'name': 'Suresh B', 'age': 27, 'department': 'Data', 'address': {'city': 'Kochi', 'state': 'Kerala'}, 'projects': [], 'experience_years': 3}

#------------------------------------------------------------------------------------------


# {'_id': ObjectId('6937e9079c278a4a9bef47e7'), 'emp_id': 101, 'name': 'Dustin', 'age': 17, 'department': 'AI', 'skills': ['python', 'mongodb'], 'address': {'city': 'Trivandrum', 'state': 'Kerala'}, 'projects': [{'project_name': 'VisionAI', 'status': 'completed'}], 'experience': 1}
# {'_id': ObjectId('6937e92a7d7fa2c63878e156'), 'emp_id': 101, 'name': 'Dustin', 'age': 17, 'department': 'AI', 'skills': ['python', 'mongodb'], 'address': {'city': 'Trivandrum', 'state': 'Kerala'}, 'projects': [{'project_name': 'VisionAI', 'status': 'completed'}], 'experience': 1}

#------------------------------------------------------------------------------------------


# {'_id': ObjectId('6937c83bc9f4db2d9d88e785'), 'emp_id': 101, 'name': 'Anu Joseph', 'age': 23, 'department': 'AI', 'skills': ['python', 'mongodb'], 'address': {'city': 'Trivandrum', 'state': 'Kerala'}, 'projects': [{'name': 'VisionAI', 'status': 'completed'}, {'name': 'DocScan', 'status': 'in-progress'}], 'experience_years': 1}
# {'_id': ObjectId('6937c83bc9f4db2d9d88e789'), 'emp_id': 105, 'name': 'Maya Kumar', 'age': 25, 'department': 'AI', 'skills': ['python', 'deep-learning'], 'address': {'city': 'Bangalore', 'state': 'KA'}, 'projects': [{'name': 'VisionAI', 'status': 'completed'}], 'experience_years': 2}
# {'_id': ObjectId('6937e9079c278a4a9bef47e7'), 'emp_id': 101, 'name': 'Dustin', 'age': 17, 'department': 'AI', 'skills': ['python', 'mongodb'], 'address': {'city': 'Trivandrum', 'state': 'Kerala'}, 'projects': [{'project_name': 'VisionAI', 'status': 'completed'}], 'experience': 1}
# {'_id': ObjectId('6937e92a7d7fa2c63878e156'), 'emp_id': 101, 'name': 'Dustin', 'age': 17, 'department': 'AI', 'skills': ['python', 'mongodb'], 'address': {'city': 'Trivandrum', 'state': 'Kerala'}, 'projects': [{'project_name': 'VisionAI', 'status': 'completed'}], 'experience': 1}


#------------------------------------------------------------------------------------------


# {'_id': ObjectId('6937e9079c278a4a9bef47e7'), 'emp_id': 101, 'name': 'Dustin', 'age': 17, 'department': 'AI', 'skills': ['python', 'mongodb'], 'address': {'city': 'Trivandrum', 'state': 'Kerala'}, 'projects': [{'project_name': 'VisionAI', 'status': 'completed'}], 'experience': 1}
# {'_id': ObjectId('6937e92a7d7fa2c63878e156'), 'emp_id': 101, 'name': 'Dustin', 'age': 17, 'department': 'AI', 'skills': ['python', 'mongodb'], 'address': {'city': 'Trivandrum', 'state': 'Kerala'}, 'projects': [{'project_name': 'VisionAI', 'status': 'completed'}], 'experience': 1}
# {'_id': ObjectId('6937c83bc9f4db2d9d88e78d'), 'emp_id': 109, 'name': 'Lavanya N', 'age': 21, 'department': 'Testing', 'skills': [], 'address': {'city': 'Trivandrum', 'state': 'Kerala'}, 'projects': [{'name': 'QualityX', 'status': 'in-progress'}], 'experience_years': 0}    
# {'_id': ObjectId('6937c83bc9f4db2d9d88e787'), 'emp_id': 103, 'name': 'Sahana R', 'age': 22, 'department': 'Testing', 'skills': ['selenium'], 'address': {'city': 'Chennai', 'state': 'TN'}, 'projects': [], 'experience_years': 1}
# {'_id': ObjectId('6937c83bc9f4db2d9d88e785'), 'emp_id': 101, 'name': 'Anu Joseph', 'age': 23, 'department': 'AI', 'skills': ['python', 'mongodb'], 'address': {'city': 'Trivandrum', 'state': 'Kerala'}, 'projects': [{'name': 'VisionAI', 'status': 'completed'}, {'name': 'DocScan', 'status': 'in-progress'}], 'experience_years': 1}
# {'_id': ObjectId('6937c83bc9f4db2d9d88e78b'), 'emp_id': 107, 'name': 'Neha Mohan', 'age': 24, 'department': 'Data', 'skills': ['sql', 'tableau'], 'address': {'city': 'Chennai', 'state': 'TN'}, 'projects': [{'name': 'USTAnalyticsHub', 'status': 'planned'}], 'experience_years': 2}
# {'_id': ObjectId('6937c83bc9f4db2d9d88e789'), 'emp_id': 105, 'name': 'Maya Kumar', 'age': 25, 'department': 'AI', 'skills': ['python', 'deep-learning'], 'address': {'city': 'Bangalore', 'state': 'KA'}, 'projects': [{'name': 'VisionAI', 'status': 'completed'}], 'experience_years': 2}
# {'_id': ObjectId('6937c83bc9f4db2d9d88e786'), 'emp_id': 102, 'name': 'Rahul Menon', 'age': 
# 26, 'department': 'Cloud', 'skills': ['aws', 'docker'], 'address': {'city': 'Kochi', 'state': 'Kerala'}, 'projects': [{'name': 'USTCloudPortal', 'status': 'planned'}], 'experience_years': 3}
# {'_id': ObjectId('6937c83bc9f4db2d9d88e78c'), 'emp_id': 108, 'name': 'Suresh B', 'age': 27, 'department': 'Data', 'address': {'city': 'Kochi', 'state': 'Kerala'}, 'projects': [], 'experience_years': 3}
# {'_id': ObjectId('6937c83bc9f4db2d9d88e78a'), 'emp_id': 106, 'name': 'Arjun S', 'age': 28, 
# 'department': 'Cloud', 'skills': ['azure'], 'address': {'city': 'Kochi', 'state': 'Kerala'}, 'projects': [{'name': 'DevOpsBoost', 'status': 'in-progress'}], 'experience_years': 4}   
# {'_id': ObjectId('6937c83bc9f4db2d9d88e788'), 'emp_id': 104, 'name': 'Vishnu Prakash', 'age': 29, 'department': 'Cybersecurity', 'skills': ['networking', 'siem'], 'address': {'city': 'Trivandrum', 'state': 'Kerala'}, 'projects': [{'name': 'SecureBank', 'status': 'in-progress'}], 'experience_years': 5}
# {'_id': ObjectId('6937c83bc9f4db2d9d88e78e'), 'emp_id': 110, 'name': 'Rakesh Pillai', 'age': 30, 'department': 'Cybersecurity', 'skills': ['networking', 'firewall', 'linux'], 'projects': [{'name': 'SecuritySuite', 'status': 'deployed'}], 'experience_years': 7}

#------------------------------------------------------------------------------------------


# Modified department for emp_id101:1 document updated


#------------------------------------------------------------------------------------------

# 102 added


#------------------------------------------------------------------------------------------

# 103 status updated to completed


#------------------------------------------------------------------------------------------

# Incremented experience for emp_id 105 by 1 years

#------------------------------------------------------------------------------------------


# Renamed field address to location for emp_id 106

#------------------------------------------------------------------------------------------


# Deleted employee count: 1


#------------------------------------------------------------------------------------------

# Deleted employees matching condition: 3

#------------------------------------------------------------------------------------------


# Removed element'docker' from skills

#------------------------------------------------------------------------------------------

# Removed element'{'project_name': 'VisionAI'}' from projects
#------------------------------------------------------------------------------------------
