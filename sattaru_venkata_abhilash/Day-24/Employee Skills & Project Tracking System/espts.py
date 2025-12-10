from pymongo import MongoClient
import json

client = MongoClient('mongodb://localhost:27017/')
db = client["ust_db"]
collection = db["employee"]

try:
    print("Connected to MongoDB!")
    print("Available databases:", client.list_database_names())
    print("Current database:", db.name)
except Exception as e:
    print("Failed to connect to MongoDB: " + str(e))

def insert_by_one():
    try:
        emp_id = int(input("Enter the employee ID to insert: "))
        with open("out.json", "r") as file:
            content = json.load(file)
            employee = next((item for item in content if item['emp_id'] == emp_id), None)
            if employee:
                collection.insert_one(employee)
                print(f"Employee {emp_id} inserted successfully!")
            else:
                print(f"Employee with ID {emp_id} not found in the file.")
    except Exception as e:
        print("Error inserting employee: " + str(e))

def insert_many():
    try:
        with open("out.json", "r") as file:
            content = json.load(file)
            collection.insert_many(content)
            print("All employees inserted successfully!")
    except Exception as e:
        print("Error inserting employees: " + str(e))

def find_by_dept(department):
    try:
        if not department.isalpha():
            print("Invalid department name! Please use only alphabetic characters (A-Z, a-z).")
            return

        result = collection.find({"department": department})
        if result.count() == 0:
            print("No employees found in the given department.")
        for employee in result:
            print(employee)
    except Exception as e:
        print("Error finding employees by department: " + str(e))

def update_department(emp_id, new_department):
    try:
        if not new_department.isalpha():
            print("Invalid department name! Please use only alphabetic characters (A-Z, a-z).")
            return

        result = collection.update_one(
            {"emp_id": emp_id},
            {"$set": {"department": new_department}}
        )
        if result.matched_count > 0:
            print(f"Employee {emp_id} department updated to {new_department}!")
        else:
            print(f"Employee {emp_id} not found!")
    except Exception as e:
        print("Error updating department: " + str(e))

def add_skill(emp_id, skill):
    try:
        result = collection.update_one(
            {"emp_id": emp_id},
            {"$addToSet": {"skills": skill}}
        )
        if result.matched_count > 0:
            print(f"Skill {skill} added to employee {emp_id}!")
        else:
            print(f"Employee {emp_id} not found!")
    except Exception as e:
        print("Error adding skill: " + str(e))

def remove_skill(emp_id, skill):
    try:
        result = collection.update_one(
            {"emp_id": emp_id},
            {"$pull": {"skills": skill}}
        )
        if result.matched_count > 0:
            print(f"Skill {skill} removed from employee {emp_id}!")
        else:
            print(f"Employee {emp_id} not found!")
    except Exception as e:
        print("Error removing skill: " + str(e))

def delete_employee(emp_id):
    try:
        result = collection.delete_one({"emp_id": emp_id})
        if result.deleted_count > 0:
            print(f"Employee {emp_id} deleted successfully!")
        else:
            print(f"Employee {emp_id} not found!")
    except Exception as e:
        print("Error deleting employee: " + str(e))

def delete_field(emp_id, field):
    try:
        result = collection.update_one(
            {"emp_id": emp_id},
            {"$unset": {field: ""}}
        )
        if result.matched_count > 0:
            print(f"Field {field} removed from employee {emp_id}!")
        else:
            print(f"Employee {emp_id} not found!")
    except Exception as e:
        print("Error deleting field: " + str(e))

def find_missing_skills():
    try:
        result = collection.find({"skills": {"$exists": False}})
        for employee in result:
            print(employee)
    except Exception as e:
        print("Error finding employees with missing skills: " + str(e))

while True:
    print("1: Insert one employee into collection")
    print("2: Insert many employees into collection")
    print("3: Find employees by department")
    print("4: Update employee department")
    print("5: Add skill to employee")
    print("6: Remove skill from employee")
    print("7: Delete employee record")
    print("8: Delete a field from employee record")
    print("9: Find employees missing skills")
    print("10: Exit")
    
    try:
        choice = int(input("Choose an option: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue
    
    if choice == 1:
        insert_by_one()
    elif choice == 2:
        insert_many()
    elif choice == 3:
        dept = input("Enter the department name: ")
        find_by_dept(dept)
    elif choice == 4:
        emp_id = int(input("Enter employee ID: "))
        new_dept = input("Enter the new department: ")
        update_department(emp_id, new_dept)
    elif choice == 5:
        emp_id = int(input("Enter employee ID: "))
        skill = input("Enter skill to add: ")
        add_skill(emp_id, skill)
    elif choice == 6:
        emp_id = int(input("Enter employee ID: "))
        skill = input("Enter skill to remove: ")
        remove_skill(emp_id, skill)
    elif choice == 7:
        emp_id = int(input("Enter employee ID to delete: "))
        delete_employee(emp_id)
    elif choice == 8:
        emp_id = int(input("Enter employee ID: "))
        field = input("Enter field to delete: ")
        delete_field(emp_id, field)
    elif choice == 9:
        find_missing_skills()
    elif choice == 10:
        print("Exiting...")
        break
    else:
        print("Invalid choice! Please try again.")