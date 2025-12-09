from pymongo import MongoClient

# MongoDB Client Setup
client = MongoClient('mongodb://localhost:27017/')
db = client["EMP_data"]
collection = db["employees"]

# Insert one employee
def insert_employee(employee):
    result = collection.insert_one(employee)
    print(f"Employee inserted with _id: {result.inserted_id}")

# Insert many employees
def insert_many_employees(employees):
    result = collection.insert_many(employees)
    print(f"Inserted {len(result.inserted_ids)} employee documents")

# Find employees by department
def find_employee_by_department(department):
    result = db.employees.find({"department": department})
    print(list(result))

# Find employees by skill
def find_employee_by_skill(skill):
    result = db.employees.find({"skills": skill})
    print(list(result))

# Find employees by city/state
def find_employee_by_city_state(city, state):
    result = db.employees.find({"address.city": city, "address.state": state})
    print(list(result))

# Find employees by age range
def find_employee_by_age_range(min_age, max_age):
    result = db.employees.find({"age": {"$gte": min_age, "$lte": max_age}})
    print(list(result))

# Find employees by experience range
def find_employee_by_experience(min_experience, max_experience):
    result = db.employees.find({"experience_years": {"$gte": min_experience, "$lte": max_experience}})
    print(list(result))

# Find employees missing skills field
def find_employee_without_skills():
    result = db.employees.find({"skills": {"$exists": False}})
    print(list(result))

# Find employees with a specific project status
def find_employee_by_project_status(status):
    result = db.employees.find({"projects.status": status})
    print(list(result))

# Find employees working on more than one project
def find_employee_with_multiple_projects():
    result = collection.find({"projects": {"$exists": True, "$ne": []}, "$expr": {"$gt": [{"$size": "$projects"}, 1]}})
    for emp in result:
        print(emp)

# Update employee department
def update_employee_department(emp_id, new_department):
    result = db.employees.update_one(
        {"emp_id": emp_id},
        {"$set": {"department": new_department}}
    )
    if result.matched_count > 0:
        print(f"Employee {emp_id} department updated to {new_department}!")
    else:
        print(f"Employee {emp_id} not found!")

# Add skill to employee
def add_skill_to_employee(emp_id, skill):
    result = db.employees.update_one(
        {"emp_id": emp_id},
        {"$addToSet": {"skills": skill}}
    )
    if result.matched_count > 0:
        print(f"Skill {skill} added to employee {emp_id}!")
    else:
        print(f"Employee {emp_id} not found!")

# Remove skill from employee
def remove_skill_from_employee(emp_id, skill):
    result = db.employees.update_one(
        {"emp_id": emp_id},
        {"$pull": {"skills": skill}}
    )
    if result.matched_count > 0:
        print(f"Skill {skill} removed from employee {emp_id}!")
    else:
        print(f"Employee {emp_id} not found!")

# Delete employee record
def delete_employee(emp_id):
    result = db.employees.delete_one({"emp_id": emp_id})
    if result.deleted_count > 0:
        print(f"Employee {emp_id} deleted successfully!")
    else:
        print(f"Employee {emp_id} not found!")

# Delete a field from employee record
def delete_field_from_employee(emp_id, field):
    result = db.employees.update_one(
        {"emp_id": emp_id},
        {"$unset": {field: ""}}
    )
    if result.matched_count > 0:
        print(f"Field {field} removed from employee {emp_id}!")
    else:
        print(f"Employee {emp_id} not found!")

# Main menu for user interaction
while True:
    print("1: Insert one employee into collection")
    print("2: Insert many employees into collection")
    print("3: Find employees by department")
    print("4: Find employees by skill")
    print("5: Find employees by city/state")
    print("6: Find employees by age range")
    print("7: Find employees by experience range")
    print("8: Find employees missing skills")
    print("9: Find employees by project status")
    print("10: Find employees with multiple projects")
    print("11: Update employee department")
    print("12: Add skill to employee")
    print("13: Remove skill from employee")
    print("14: Delete employee record")
    print("15: Delete a field from employee record")
    print("16: Exit")

    try:
        choice = int(input("Choose an option: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    if choice == 1:
        emp = {
            "emp_id": 111,
            "name": "John Doe",
            "age": 30,
            "department": "HR",
            "skills": ["communication", "recruitment"],
            "address": {"city": "Delhi", "state": "Delhi"},
            "projects": [{"name": "Hiring", "status": "in-progress"}],
            "experience_years": 5
        }
        insert_employee(emp)
    elif choice == 2:
        employees = [
            {"emp_id": 112, "name": "Jane Smith", "age": 28, "department": "Finance", "skills": ["excel", "accounting"], "address": {"city": "Mumbai", "state": "Maharashtra"}, "projects": [{"name": "Budgeting", "status": "completed"}], "experience_years": 3},
            {"emp_id": 113, "name": "James Bond", "age": 35, "department": "IT", "skills": ["python", "networking"], "address": {"city": "Bangalore", "state": "Karnataka"}, "projects": [{"name": "NetworkUpgrade", "status": "in-progress"}], "experience_years": 7}
        ]
        insert_many_employees(employees)
    elif choice == 3:
        dept = input("Enter the department name: ")
        find_employee_by_department(dept)
    elif choice == 4:
        skill = input("Enter the skill: ")
        find_employee_by_skill(skill)
    elif choice == 5:
        city = input("Enter city: ")
        state = input("Enter state: ")
        find_employee_by_city_state(city, state)
    elif choice == 6:
        min_age = int(input("Enter minimum age: "))
        max_age = int(input("Enter maximum age: "))
        find_employee_by_age_range(min_age, max_age)
    elif choice == 7:
        min_exp = int(input("Enter minimum experience: "))
        max_exp = int(input("Enter maximum experience: "))
        find_employee_by_experience(min_exp, max_exp)
    elif choice == 8:
        find_employee_without_skills()
    elif choice == 9:
        status = input("Enter project status: ")
        find_employee_by_project_status(status)
    elif choice == 10:
        find_employee_with_multiple_projects()
    elif choice == 11:
        emp_id = int(input("Enter employee ID: "))
        new_dept = input("Enter new department: ")
        update_employee_department(emp_id, new_dept)
    elif choice == 12:
        emp_id = int(input("Enter employee ID: "))
        skill = input("Enter skill to add: ")
        add_skill_to_employee(emp_id, skill)
    elif choice == 13:
        emp_id = int(input("Enter employee ID: "))
        skill = input("Enter skill to remove: ")
        remove_skill_from_employee(emp_id, skill)
    elif choice == 14:
        emp_id = int(input("Enter employee ID to delete: "))
        delete_employee(emp_id)
    elif choice == 15:
        emp_id = int(input("Enter employee ID: "))
        field = input("Enter field to delete: ")
        delete_field_from_employee(emp_id, field)
    elif choice == 16:
        print("Exiting...")
        break
    else:
        print("Invalid choice! Please try again.")
        

