from pymongo import MongoClient, errors
import json

# --- Database Setup ---
client = MongoClient("mongodb://localhost:27017/")
db = client["ust_db"]
conn = db["employees"]

# Ensure emp_id is unique
conn.create_index("emp_id", unique=True)


# --- CREATE Operations ---
# """Insert a single employee"""
def create_one(employee: dict):
   
    try:
        conn.insert_one(employee)
        print("Inserted one employee")
    except errors.DuplicateKeyError:
        print(f"Employee with emp_id {employee.get('emp_id')} already exists!")

#"""Bulk insert employees"""
def create_many(employees: list):
    
    try:
        conn.insert_many(employees, ordered=False)  # skip duplicates
        print("Inserted many employees")
    except errors.BulkWriteError as e:
        print("Some employees were duplicates and skipped:", e.details)


# --- READ Operations ---
# Find employees by department or city/state
def read_by_departmentcity(key, value):
    result = conn.find({key: value})
    for emp in result:
        print(emp)

# Find employees with ANY skill in the list
def read_byskillset(skills: list):
    for emp in conn.find({"skills": {"$in": skills}}):
        print(emp)

# Find employees with ALL skills in the list
def read_by_all_skills(skills: list):
    for emp in conn.find({"skills": {"$all": skills}}):
        print(emp)

# Find employees in age range
def age_in_range(low, high):
    for emp in conn.find({"age": {"$gte": low, "$lte": high}}):
        print(emp)

# Find employees by experience range
def read_by_experience(min_years, max_years=None):
    query = {"experience_years": {"$gte": min_years}}
    if max_years is not None:
        query["experience_years"]["$lte"] = max_years
    for emp in conn.find(query):
        print(emp)

# Find employees missing skills field
def missing_skills():
    for emp in conn.find({"skills": {"$exists": False}}):
        print(emp)

# Find employees with specific project status
def read_by_nested(k,value,status):
    for emp in conn.find({f"{k}.{value}": status}):
        print(emp)

# Find employees with >1 project
def greater_than_oneproject():
    for emp in conn.find({"$expr": {"$gt": [{"$size": "$projects"}, 1]}}):
        print(emp)

# Read all employees sorted by name
def read_all():
    for emp in conn.find().sort("name", 1):
        print(emp)

     
        
#Updates
# Update fields using $set
def update_field(emp_id, key, val):
    res = conn.update_one({"emp_id": emp_id}, {"$set": {key: val}})
    print(f"Matched: {res.matched_count}, Modified: {res.modified_count}")

# Increment values using $inc
def increment(emp_id, key, amount=1):
    res = conn.update_one({"emp_id": emp_id}, {"$inc": {key: amount}})
    print(f"Matched: {res.matched_count}, Modified: {res.modified_count}")

# Remove fields using $unset
def remove_field(emp_id, key):
    res = conn.update_one({"emp_id": emp_id}, {"$unset": {key: ""}})
    print(f"Matched: {res.matched_count}, Modified: {res.modified_count}")

# Update arrays
def add_skill(emp_id, skill):
    res = conn.update_one({"emp_id": emp_id}, {"$addToSet": {"skills": skill}})
    print(f"Added skill '{skill}' to emp_id={emp_id}")

# Remove a skill from the skills array.
def remove_skill(emp_id, skill):
    res = conn.update_one({"emp_id": emp_id}, {"$pull": {"skills": skill}})
    print(f"Removed skill '{skill}' from emp_id={emp_id}")

# Update the status of a project inside the projects array.
def update_project_status(emp_id, project_name, new_status):
    res = conn.update_one(
        {"emp_id": emp_id, "projects.name": project_name},
        {"$set": {"projects.$.status": new_status}}
    )
    print(f"Updated project '{project_name}' to '{new_status}' for emp_id={emp_id}")

# Add a new project entry to the projects array.
def add_project(emp_id, project_name, status):
    res = conn.update_one(
        {"emp_id": emp_id},
        {"$push": {"projects": {"name": project_name, "status": status}}}
    )
    print(f"Added project '{project_name}' with status '{status}' to emp_id={emp_id}")

# Bulk update using update_many
def bulk_update_cloud(key,val,new_val):
    res = conn.update_many({key: val}, {"$set": {key: new_val}})
    print(f"Bulk updated {res.modified_count} Cloud employees.")

# Upsert employee profile if not found
def upsert_employee(emp_id, employee_data):
    res = conn.update_one({"emp_id": emp_id}, {"$set": employee_data}, upsert=True)
    if res.upserted_id:
        print(f"Inserted new employee with emp_id={emp_id}")
    else:
        print(f"Updated existing employee with emp_id={emp_id}")


##Delete
# Delete a single employee by emp_id
def delete_employee(emp_id):
    res = conn.delete_one({"emp_id": emp_id})
    print(f"Deleted count: {res.deleted_count}")

#Delate based on the departmet
def delete_by_department(department):
    res=conn.delete_many({"department":department})
    print(f"Deleted count: {res.deleted_count}")

#Delete field
def delete_field_all(field):
    res = conn.update_many({}, {"$unset": {field: ""}})
    print(f"Removed field '{field}' from all employees, Modified: {res.modified_count}")

#delete employee with no skills
def delete_no_skills():
    res = conn.delete_many({"$or": [{"skills": {"$exists": False}}, {"skills": {"$size": 0}}]})
    print(f"Deleted {res.deleted_count} employees with no skills")

#delete employee with no ongoing projects
def delete_no_ongoing_projects():
    res = conn.delete_many({
        "$or": [
            {"projects": {"$exists": False}},
            {"projects": {"$size": 0}},
            {"projects.status": {"$ne": "in-progress"}}
        ]
    })
    print(f"Deleted {res.deleted_count} employees with no ongoing projects")

# Delete employees with experience less than threshold
def delete_low_experience(threshold):
    res = conn.delete_many({"experience_years": {"$lt": threshold}})
    print(f"Deleted {res.deleted_count} employees with experience < {threshold}")

# Delete a specific field from an employee document
def delete_field(emp_id, field):
    res = conn.update_one({"emp_id": emp_id}, {"$unset": {field: ""}})
    print(f"Removed field '{field}' from emp_id={emp_id}, Modified: {res.modified_count}")

# Remove a skill from an employee’s skills array
def remove_skill(emp_id, skill):
    res = conn.update_one({"emp_id": emp_id}, {"$pull": {"skills": skill}})
    print(f"Removed skill '{skill}' from emp_id={emp_id}, Modified: {res.modified_count}")

# Remove a project by name from an employee’s projects array
def remove_project(emp_id, project_name):
    res = conn.update_one({"emp_id": emp_id}, {"$pull": {"projects": {"name": project_name}}})
    print(f"Removed project '{project_name}' from emp_id={emp_id}, Modified: {res.modified_count}")



# --- MAIN DEMO ---
if __name__ == "__main__":
    # # Load sample data from JSON file
    # with open("data.json", "r") as file:
    #     data = json.load(file)

    # # Insert sample data
    # create_many(data)

    # # Demo reads
    # print("\n--- Employees in AI Department ---")
    # read_by_departmentcity("department", "AI")

    # print("\n--- Employees with skill 'python' ---")
    # read_byskillset(["python"])

    # print("\n--- Employees aged 24–28 ---")
    # age_in_range(24, 28)

    # print("\n--- Employees missing skills ---")
    # missing_skills()

    # print("\n--- Employees with >1 project ---")
    # greater_than_oneproject()

    # print("\n--- Employees with nested searching field , key, value ---")
    # read_by_nested("projects","name","QualityX")
    
    # print("\n--- All employees sorted by name ---")
    # read_all()
    

    # Update fields using $set
    # update_field(101, "department", "AI-Research")

    # Increment values using $inc
    # increment(101, "experience_years", 1)   # increment by 1
    # increment(102, "experience_years", 2)   # increment by 2

    # Remove fields using $unset
    # remove_field(101, "address.state")

    # # 6.3.4 Update arrays
    # add_skill(105, "mlops")                 # add skill
    # add_skill(105, "python")                # addToSet prevents duplicates
    # remove_skill(105, "docker")             # remove skill

    # # Update project statuses using positional operator
    # update_project_status(106, "DevOpsBoost", "completed")

    # # Add new project entries
    # add_project(102, "CloudGuard", "planned")

    # # 6.3.6 Bulk update using update_many
    # bulk_update_cloud("department","Cloud","Cloud-Engineer")                     # mark all Cloud employees as Cloud-Engineer

    # # 6.3.7 Upsert employee profile if not found
    # upsert_employee(999, {
    #     "name": "New Employee",
    #     "age": 26,
    #     "department": "AI",
    #     "skills": ["python"],
    #     "experience_years": 1
    # })

    
    # delete_employee(103)                  # delete employee by emp_id
    # delete_by_department("Testing")       # delete all Testing dept employees

    # delete_field(101, "department")       # remove department field from one employee
    # delete_field_all("department")        # remove department field from all employees

    # remove_skill(105, "docker")           # remove skill from one employee
    # remove_project(102, "CloudGuard")     # remove project from one employee

    # delete_low_experience(1)              # delete employees with <1 year experience
    # delete_no_skills()                    # delete employees with no skills
    # delete_no_ongoing_projects()          # delete employees with no ongoing projects

    
    print("\n--- All employees sorted by name ---")
    read_all()
    
    
    
# Sample output
# Inserted many employees

# --- Employees in AI Department ---
# {'_id': ObjectId('6937d444dd697037b1a5aca9'), 'emp_id': 101, 'name': 'Anu Joseph', 'age': 23, 'department': 'AI', 'skills': ['python', 'mongodb'], 'address': {'city': 'Trivandrum', 'state': 'Kerala'}, 'projects': [{'name': 'VisionAI', 'status': 'completed'}, {'name': 'DocScan', 'status': 'in-progress'}], 'experience_years': 1}
# {'_id': ObjectId('6937d444dd697037b1a5acad'), 'emp_id': 105, 'name': 'Maya Kumar', 'age': 25, 'department': 'AI', 'skills': ['python', 'deep-learning'], 'address': {'city': 'Bangalore', 'state': 'KA'}, 'projects': [{'name': 'VisionAI', 'status': 'completed'}], 'experience_years': 2}

# --- Employees with skill 'python' ---
# {'_id': ObjectId('6937d444dd697037b1a5aca9'), 'emp_id': 101, 'name': 'Anu Joseph', 'age': 23, 'department': 'AI', 'skills': ['python', 'mongodb'], 'address': {'city': 'Trivandrum', 'state': 'Kerala'}, 'projects': [{'name': 'VisionAI', 'status': 'completed'}, {'name': 'DocScan', 'status': 'in-progress'}], 'experience_years': 1}
# {'_id': ObjectId('6937d444dd697037b1a5acad'), 'emp_id': 105, 'name': 'Maya Kumar', 'age': 25, 'department': 'AI', 'skills': ['python', 'deep-learning'], 'address': {'city': 'Bangalore', 'state': 'KA'}, 'projects': [{'name': 'VisionAI', 'status': 'completed'}], 'experience_years': 2}

# --- Employees aged 24–28 ---
# {'_id': ObjectId('6937d444dd697037b1a5acaa'), 'emp_id': 102, 'name': 'Rahul Menon', 'age': 26, 'department': 'Cloud', 'skills': ['aws', 'docker'], 'address': {'city': 'Kochi', 'state': 'Kerala'}, 'projects': [{'name': 'USTCloudPortal', 'status': 'planned'}], 'experience_years': 3}
# {'_id': ObjectId('6937d444dd697037b1a5acad'), 'emp_id': 105, 'name': 'Maya Kumar', 'age': 25, 'department': 'AI', 'skills': ['python', 'deep-learning'], 'address': {'city': 'Bangalore', 'state': 'KA'}, 'projects': [{'name': 'VisionAI', 'status': 'completed'}], 'experience_years': 2}
# {'_id': ObjectId('6937d444dd697037b1a5acae'), 'emp_id': 106, 'name': 'Arjun S', 'age': 28, 'department': 'Cloud', 'skills': ['azure'], 'address': {'city': 'Kochi', 'state': 'Kerala'}, 'projects': [{'name': 'DevOpsBoost', 'status': 'in-progress'}], 'experience_years': 4}
# {'_id': ObjectId('6937d444dd697037b1a5acaf'), 'emp_id': 107, 'name': 'Neha Mohan', 'age': 24, 'department': 'Data', 'skills': ['sql', 'tableau'], 'address': {'city': 'Chennai', 'state': 'TN'}, 'projects': [{'name': 'USTAnalyticsHub', 'status': 'planned'}], 'experience_years': 2}
# {'_id': ObjectId('6937d444dd697037b1a5acb0'), 'emp_id': 108, 'name': 'Suresh B', 'age': 27, 'department': 'Data', 'address': {'city': 'Kochi', 'state': 'Kerala'}, 'projects': [], 'experience_years': 3}

# --- Employees missing skills ---
# {'_id': ObjectId('6937d444dd697037b1a5acb0'), 'emp_id': 108, 'name': 'Suresh B', 'age': 27, 'department': 'Data', 'address': {'city': 'Kochi', 'state': 'Kerala'}, 'projects': [], 'experience_years': 3}

# --- Employees with >1 project ---
# {'_id': ObjectId('6937d444dd697037b1a5aca9'), 'emp_id': 101, 'name': 'Anu Joseph', 'age': 23, 'department': 'AI', 'skills': ['python', 'mongodb'], 'address': {'city': 'Trivandrum', 'state': 'Kerala'}, 'projects': [{'name': 'VisionAI', 'status': 'completed'}, {'name': 'DocScan', 'status': 'in-progress'}], 'experience_years': 1}

# --- Employees with nested searching field , key, value ---
# {'_id': ObjectId('6937d444dd697037b1a5acb1'), 'emp_id': 109, 'name': 'Lavanya N', 'age': 21, 'department': 'Testing', 'skills': [], 'address': {'city': 'Trivandrum', 'state': 'Kerala'}, 'projects': [{'name': 'QualityX', 'status': 'in-progress'}], 'experience_years': 0}
# # --- All employees sorted by name ---
# {'_id': ObjectId('6937d444dd697037b1a5aca9'), 'emp_id': 101, 'name': 'Anu Joseph', 'age': 23, 'department': 'AI', 'skills': ['python', 'mongodb'], 'address': {'city': 'Trivandrum', 'state': 'Kerala'}, 'projects': [{'name': 'VisionAI', 'status': 'completed'}, {'name': 'DocScan', 'status': 'in-progress'}], 'experience_years': 1}
# {'_id': ObjectId('6937d444dd697037b1a5acae'), 'emp_id': 106, 'name': 'Arjun S', 'age': 28, 'department': 'Cloud', 'skills': ['azure'], 'address': {'city': 'Kochi', 'state': 'Kerala'}, 'projects': [{'name': 'DevOpsBoost', 'status': 'in-progress'}], 'experience_years': 4}
# {'_id': ObjectId('6937d444dd697037b1a5acb1'), 'emp_id': 109, 'name': 'Lavanya N', 'age': 21, 'department': 'Testing', 'skills': [], 'address': {'city': 'Trivandrum', 'state': 'Kerala'}, 'projects': [{'name': 'QualityX', 'status': 'in-progress'}], 'experience_years': 0}
# {'_id': ObjectId('6937d444dd697037b1a5acad'), 'emp_id': 105, 'name': 'Maya Kumar', 'age': 25, 'department': 'AI', 'skills': ['python', 'deep-learning'], 'address': {'city': 'Bangalore', 'state': 'KA'}, 'projects': [{'name': 'VisionAI', 'status': 'completed'}], 'experience_years': 2}
# {'_id': ObjectId('6937d444dd697037b1a5acaf'), 'emp_id': 107, 'name': 'Neha Mohan', 'age': 24, 'department': 'Data', 'skills': ['sql', 'tableau'], 'address': {'city': 'Chennai', 'state': 'TN'}, 'projects': [{'name': 'USTAnalyticsHub', 'status': 'planned'}], 'experience_years': 2}
# {'_id': ObjectId('6937d444dd697037b1a5acaa'), 'emp_id': 102, 'name': 'Rahul Menon', 'age': 26, 'department': 'Cloud', 'skills': ['aws', 'docker'], 'address': {'city': 'Kochi', 'state': 'Kerala'}, 'projects': [{'name': 'USTCloudPortal', 'status': 'planned'}], 'experience_years': 3}
# {'_id': ObjectId('6937d444dd697037b1a5acb2'), 'emp_id': 110, 'name': 'Rakesh Pillai', 'age': 30, 'department': 'Cybersecurity', 'skills': ['networking', 'firewall', 'linux'], 'projects': [{'name': 'SecuritySuite', 'status': 'deployed'}], 'experience_years': 7}
# {'_id': ObjectId('6937d444dd697037b1a5acab'), 'emp_id': 103, 'name': 'Sahana R', 'age': 22, 'department': 'Testing', 'skills': ['selenium'], 'address': {'city': 'Chennai', 'state': 'TN'}, 'projects': [], 'experience_years': 1}
# {'_id': ObjectId('6937d444dd697037b1a5acb0'), 'emp_id': 108, 'name': 'Suresh B', 'age': 27, 'department': 'Data', 'address': {'city': 'Kochi', 'state': 'Kerala'}, 'projects': [], 'experience_years': 3}
# {'_id': ObjectId('6937d444dd697037b1a5acac'), 'emp_id': 104, 'name': 'Vishnu Prakash', 'age': 29, 'department': 'Cybersecurity', 'skills': ['networking', 'siem'], 'address': {'city': 'Trivandrum', 'state': 'Kerala'}, 'projects': [{'name': 'SecureBank', 'status': 'in-progress'}], 'experience_years': 5}


   
   
   
