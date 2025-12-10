import json
from pymongo import MongoClient

# Function to establish a connection to the MongoDB database
def get_db_connection():
    client = MongoClient('mongodb://localhost:27017/')  # Connecting to MongoDB server
    return client['ust_db']  # Returning the 'ust_db' database

# Function to insert a single employee record into the 'employees' collection
def insert_employee(db, employee):
    result = db.employees.insert_one(employee)  # Insert the employee record
    return result.inserted_id  # Return the ID of the inserted record

# Function to insert multiple employee records in bulk into the 'employees' collection
def insert_employees_bulk(db, employees):
    result = db.employees.insert_many(employees)  # Insert multiple employee records
    return result.inserted_ids  # Return the IDs of the inserted records

# Function to find employees by department
def find_employees_by_department(db, department):
    result = db.employees.find({"department": department})  # Find employees in the given department
    return list(result)  # Return the results as a list

# Function to find employees who possess a specific skill
def find_employees_by_skill(db, skill):
    result = db.employees.find({"skills": skill})  # Find employees with the specified skill
    return list(result)  # Return the results as a list

# Function to find employees located in a specific city
def find_employees_by_city(db, city):
    result = db.employees.find({},{"city":city})  # Find employees located in the given city
    return list(result)  # Return the results as a list

# Function to find employees with experience within a given range
def find_employees_by_experience_range(db, min_exp, max_exp):
    result = db.employees.find({"experience_years": {"$gte": min_exp, "$lte": max_exp}})  # Find employees within experience range
    return list(result)  # Return the results as a list

# Function to find employees missing a specific field
def find_employees_missing_field(db, field):
    result = db.employees.find({field: {"$exists": False}})  # Find employees missing the specified field
    return list(result)  # Return the results as a list

# Function to update the department of an employee
def update_employee_department(db, emp_id, new_department):
    result = db.employees.update_one(
        {"emp_id": emp_id},  # Find the employee by emp_id
        {"$set": {"department": new_department}}  # Set the new department value
    )
    return result.modified_count  # Return the number of modified records

# Function to remove the 'state' field from the 'address' field in all employee records
def remove_address_state(db):
    result = db.employees.update_many(
        {},
        {"$unset": {"address.state": ""}}  # Remove the state field from address
    )
    return result.modified_count  # Return the number of modified records

# Function to increment the experience years of all employees by a specified number of years
def increment_experience(db, years):
    result = db.employees.update_many(
        {}, 
        {"$inc": {"experience_years": years}}  # Increment experience years by the specified number
    )
    return result.modified_count  # Return the number of modified records

# Function to add a skill to a specific employee
def add_skill_to_employee(db, emp_id, skill):
    result = db.employees.update_one(
        {"emp_id": emp_id}, 
        {"$push": {"skills": skill}}  # Add the skill to the employee's skill set
    )
    return result.modified_count  # Return the number of modified records

# Function to remove a skill from all employee records
def remove_skill_from_all_employees(db, skill):
    result = db.employees.update_many(
        {}, 
        {"$pull": {"skills": skill}}  # Remove the skill from all employees' skill sets
    )
    return result.modified_count  # Return the number of modified records

# Function to update the status of a project for a specific employee
def update_project_status(db, emp_id, project_name, new_status):
    result = db.employees.update_one(
        {"emp_id": emp_id, "projects.name": project_name},  # Find employee and project
        {"$set": {"projects.$.status": new_status}}  # Set the new status for the project
    )
    return result.modified_count  # Return the number of modified records

# Function to rename a field for a specific employee
def rename_fields(db, emp_id, old_field, new_field):
    result = db.employees.update_one(
        {"emp_id": emp_id},
        {"$rename": {old_field: new_field}}  # Rename the field in the employee record
    )
    return result.modified_count  # Return the number of modified records

# Function to add a new project to a specific employee
def add_project_to_employee(db, emp_id, project_name, new_status):
    result = db.employees.update_one(
        {"emp_id": emp_id},
        {"$push": {"projects": {"name": project_name, "status": new_status}}}  # Add the new project to the employee
    )
    return result.modified_count  # Return the number of modified records

# Function to update the department for all employees in bulk
def update_employees_bulk(db):
    result = db.employees.update_many(
        {},
        {"$set": {"department": "Cloud-Engineer"}}  # Set all employees' department to 'Cloud-Engineer'
    )
    return result.modified_count  # Return the number of modified records

# Function to delete a specific employee by their emp_id
def delete_employee_by_emp_id(db, emp_id):
    result = db.employees.delete_one({"emp_id": emp_id})  # Delete employee by emp_id
    return result.deleted_count  # Return the number of deleted records

# Function to delete all employees in a specific department
def delete_employee_by_department(db, department):
    db.employees.delete_many({"department": department})  # Delete all employees in the department

# Function to remove the department field from all employee records
def delete_departmant_from_all_employees(db):
    result = db.employees.update_many(
        {},
        {"$unset": {"department": ""}}  # Remove the department field from all employees
    )
    return result.modified_count  # Return the number of modified records

# Function to delete employees who meet specific conditions (no skills, less than 1 year of experience, no projects)
def delete_employees_with_conditions(db):
    result = db.employees.delete_many(
        {
            "skills": {"$size": 0},  # No skills
            "experience_years": {"$lt": 1},  # Experience less than 1 year
            "projects": {"$size": 0}  # No projects
        }
    )
    return result.deleted_count  # Return the number of deleted records

if __name__ == "__main__":
    
    db = get_db_connection()
    
    with open('employees.json', 'r') as file:
        data = json.load(file)

    insert_employees_bulk(db, data)
    
    new_employee = {
        "emp_id": 111,
        "name": "Abhi",
        "age": 22,
        "department": "AI",
        "skills": ["python", "machine learning"],
        "address": { "city": "Hyderabad", "state": "Telangana" },
        "projects": ["Employee management"],
        "experience_years": 3
    }
    
    insert_employee(db, new_employee)
    
    
    for emp in db.employees.find():
        print(emp)
    
    
    city=find_employees_by_city(db,"Hyderbad")
    print(city)


    dept_employees = find_employees_by_department(db, "Testing")
    print("Department Employees:", dept_employees)

    python_employees = find_employees_by_skill(db, "python")
    print("Employees with Python Skill:", python_employees)

    mid_experience_employees = find_employees_by_experience_range(db, 2, 5)
    print("Employees with Experience (2-5 years):", mid_experience_employees)

    emp_missing_skills = find_employees_missing_field(db, "skills")
    print("Employees Missing Skills:", emp_missing_skills)

    update_employee_department(db, 101, "Cloud")
    emp=db.employees.find_one({"emp_id":101})
    print(emp)
    
    increment_experience(db, 1)

    add_skill_to_employee(db, 102, "docker")

    update_project_status(db, 101, "VisionAI", "deployed")
    
    emp=db.employees.find_one({"emp_id":111})
    print("before update",emp)
    
    add_project_to_employee(db,111,"Employee_service","in-progres")
    
    emp=db.employees.find_one({"emp_id":111})
    print("after update",emp)
    

    
    remove_skill_from_all_employees(db, "docker")
    
    rename_fields(db,101,"address","location")
    remove_address_state(db)
    
    update_employees_bulk(db)
    
    
    delete_employee_by_emp_id(db, 111)
    
    delete_employee_by_department(db,"Cloud-Engineer")
    
    delete_department=delete_departmant_from_all_employees(db)
    
    print("Deleted employees department count: ",delete_department)
    
    
    emp_delete=delete_employees_with_conditions(db)
    
    print("Employess deleted count:",emp_delete)
    
    for emp in db.employees.find():
        print(emp)
    db.employees.find().sort("name", 1)  
    db.employees.find().sort("name", -1) 

    db.employees.find({}, {"name": 1, "skills": 1})

    
    emp=db.employees.find_one({"emp_id":101})
    print(emp)
    