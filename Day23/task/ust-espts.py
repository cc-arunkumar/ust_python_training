from pymongo import MongoClient
import json

client = MongoClient("mongodb://localhost:27017/")
db = client["ust_db"]

print("Database 'ust_db' connected successfully")

with open('sample.json', 'r') as file:
    employees_data = json.load(file) 

def bulk_upload(employees_data):
    for employee in employees_data:
        existing_employee = db.employees.find_one({"emp_id": employee["emp_id"]})
        if not existing_employee:
            result = db.employees.insert_one(employee)
            print(f"Successfully inserted employee with emp_id: {employee['emp_id']}")

bulk_upload(employees_data)

def create_new_employee(new_data):
    for emp in new_data:
        existing_employee = db.employees.find_one({"emp_id": emp["emp_id"]})
        if not existing_employee:
            res = db.employees.insert_one(emp)
            print(f"New employee added successfully : {emp['emp_id']}")

new_data = [
    {"name": "madhan kumar",
     "emp_id": 111,
     "age": 22,
     "department": "AI-ML",
     "skills": ["python", "mongodb", "fastApi", "react"]}
]

create_new_employee(new_data)

# ----- Read Employees by Fields -----

def query_by_department(department):
    employees = db.employees.find({"department": department})
    for employee in employees:
        print(employee)



# ----- Update Employee Department -----

def update_employee_department(emp_id, new_department):
    result = db.employees.update_one(
        {"emp_id": emp_id},  
        {"$set": {"department": new_department}} 
    )

emp_id_to_update = 101
new_department = "Data Science"
update_employee_department(emp_id_to_update, new_department)

def query_by_skill(skill):
    employees = db.employees.find({"skills": skill})
    for employee in employees:
        print(employee)

def query_by_city_state(city, state):
    employees = db.employees.find({"address.city": city, "address.state": state})
    for employee in employees:
        print(employee)

def query_by_age_range(min_age, max_age):
    employees = db.employees.find({"age": {"$gte": min_age, "$lte": max_age}})
    for employee in employees:
        print(employee)

def query_by_experience_level(min_experience, max_experience):
    employees = db.employees.find({"experience_years": {"$gte": min_experience, "$lte": max_experience}})
    for employee in employees:
        print(employee)

def query_missing_skills():
    employees = db.employees.find({"skills": {"$exists": False}})
    for employee in employees:
        print(employee)

def query_by_project_status(status):
    employees = db.employees.find({"projects.status": status})
    for employee in employees:
        print(employee)

def query_one_project():
    employees = db.employees.find({"projects": {"$size": 1}})
    for employee in employees:
        print(employee)

def query_sorted_by_field(field, ascending=True):
    sort_order = 1 if ascending else -1
    employees = db.employees.find().sort(field, sort_order)
    for employee in employees:
        print(employee)

def query_with_projection(fields):
    projection = {field: 1 for field in fields}
    employees = db.employees.find({}, projection)
    for employee in employees:
        print(employee)

def query_by_project_name(project_name):
    employees = db.employees.find({"projects.name": project_name})
    for employee in employees:
        print(employee)

def query_by_array_element(field, element_value):
    employees = db.employees.find({field: element_value})
    for employee in employees:
        print(employee)


# ----- Increment Employee Experience -----

def inc_employee_exp():
    result = db.employees.update_many(
        {},
        {"$inc": {"experience_years": 1}}  # Increment experience by 1 year for all employees
    )
    print(f"Incremented experience for {result.modified_count} employees.")

inc_employee_exp()

# ----- Remove Fields -----

def remove_field():
    result = db.employees.update_many(
        {},
        {"$unset": {"department": ""}}  # Remove the 'department' field
    )
    print(f"Removed department field from {result.modified_count} employees.")

remove_field()

# ----- Update Arrays (Add Skills) -----

def update_arrays_add(emp_id, skills):
    result = db.employees.update_one(
        {"emp_id": emp_id}, 
        {"$push": {"skills": {"$each": skills}}}  # Add skills to the 'skills' array
    )
    print(f"Skills added to employee with emp_id: {emp_id}")

update_arrays_add(111, ["AWS", "Azure"])

# ----- Remove Skills -----

def remove_skill(emp_id, skill_to_remove):
    result = db.employees.update_one(
        {"emp_id": emp_id}, 
        {"$pull": {"skills": skill_to_remove}}  # Remove the specified skill from the 'skills' array
    )
    print(f"Skill '{skill_to_remove}' removed from employee with emp_id: {emp_id}")

remove_skill(111, "react")

# ----- Update Project Statuses Using Positional Operator -----

def update_employee_department(emp_id, new_department):
    result = db.employees.update_one(
        {"emp_id": emp_id},  
        {"$set": {"department": new_department}} 
    )
    print(f"Updated department for emp_id: {emp_id}")

def inc_employee_exp():
    result = db.employees.update_many(
        {},
        {"$inc": {"experience_years": 1}}  # Increment experience by 1 year for all employees
    )
    print(f"Incremented experience for {result.modified_count} employees.")

def remove_field():
    result = db.employees.update_many(
        {},
        {"$unset": {"department": ""}}  # Remove the 'department' field
    )
    print(f"Removed department field from {result.modified_count} employees.")

def update_arrays_add(emp_id, skills):
    result = db.employees.update_one(
        {"emp_id": emp_id}, 
        {"$push": {"skills": {"$each": skills}}}  # Add skills to the 'skills' array
    )
    print(f"Skills added to employee with emp_id: {emp_id}")

def update_arrays_remove(emp_id, skill):
    result = db.employees.update_one(
        {"emp_id": emp_id}, 
        {"$pull": {"skills": skill}}  # Remove the specified skill from the 'skills' array
    )
    print(f"Skill '{skill}' removed from employee with emp_id: {emp_id}")

def update_project_status(emp_id, project_name, new_status):
    result = db.employees.update_one(
        {"emp_id": emp_id, "projects.name": project_name}, 
        {"$set": {"projects.$.status": new_status}}  # Update project status using the positional operator
    )
    print(f"Project status updated for emp_id: {emp_id}")

def bulk_update_department_for_cloud():
    result = db.employees.update_many(
        {"department": "Cloud"},
        {"$set": {"department": "Cloud-Engineer"}}
    )
    print(f"Updated {result.modified_count} employees to 'Cloud-Engineer'")

def upsert_employee(emp_id, name, age, department, skills):
    result = db.employees.update_one(
        {"emp_id": emp_id},  
        {"$set": {
            "name": name,
            "age": age,
            "department": department,
            "skills": skills
        }},
        upsert=True  # If emp_id doesn't exist, insert a new document
    )
    if result.upserted_id:
        print(f"Inserted new employee with emp_id: {emp_id}")
    else:
        print(f"Updated employee with emp_id: {emp_id}")


# ----- Delete Employee by emp_id -----

def delete_emp_by_id(emp_id):
    result = db.employees.delete_one(
        {"emp_id": emp_id}
    )
    print(f"Deleted employee with emp_id: {emp_id}")

def delete_employees_no_skills():
    result = db.employees.delete_many(
        {"skills": {"$exists": False}}  # Delete employees with no skills field
    )
    print(f"Deleted {result.deleted_count} employees with no skills.")

def delete_employees_experience_less_than_one():
    result = db.employees.delete_many(
        {"experience_years": {"$lte": 1}}  # Delete employees with experience ≤ 1 year
    )
    print(f"Deleted {result.deleted_count} employees with experience ≤ 1 year.")

def delete_employees_no_projects():
    result = db.employees.delete_many(
        {"projects": {"$size": 0}}  # Delete employees with no projects (empty projects array)
    )
    print(f"Deleted {result.deleted_count} employees with no projects.")

def delete_field():
    result = db.employees.update_many(
        {},
        {"$unset": {"department": ""}}  # Remove the 'department' field
    )
    print(f"Removed 'department' field from {result.modified_count} employees.")

def remove_skill(emp_id, skill_to_remove):
    result = db.employees.update_one(
        {"emp_id": emp_id}, 
        {"$pull": {"skills": skill_to_remove}}  # Remove the specified skill from the 'skills' array
    )
    print(f"Skill '{skill_to_remove}' removed from employee with emp_id: {emp_id}")

def remove_project(emp_id, project_name_to_remove):
    result = db.employees.update_one(
        {"emp_id": emp_id},  
        {"$pull": {"projects": {"name": project_name_to_remove}}}  # Remove project from the 'projects' array
    )
    print(f"Project '{project_name_to_remove}' removed from employee with emp_id: {emp_id}")

