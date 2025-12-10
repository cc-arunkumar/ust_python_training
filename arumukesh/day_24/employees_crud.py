from pymongo import MongoClient
from model import Employee
from bson import ObjectId
client= MongoClient('mongodb://localhost:27017/')

db=client['employees']
emp_id=100
def create_one():
    global emp_id
    emp_id+=1
    
    raw_input_data = input("Enter Employee JSON: ")
    employee = Employee.model_validate_json(raw_input_data)
    employee_dict = employee.model_dump(exclude_none=True, exclude_unset=True) 

    # Insert into MongoDB
    result = db.employees.insert_one(employee_dict)
    if result.inserted_id:
        print("ADDITION SUCCESS ")
    return result
    
    
def insert_many():
    # y=True 
    employees=[]
    while True:
        raw_input_data = input("Enter Employee JSON: ")
        employee = Employee.model_validate_json(raw_input_data)
        employee_dict = employee.model_dump(exclude_none=True, exclude_unset=True)
        employees.append(employee_dict)
        # y=bool(input("DO u want to continue"))
        cont = input("Do you want to continue? (yes/no): ").strip().lower()
        if cont not in ["yes", "y"]:
            break
        
    result=db.employees.insert_many(employees)
    if result.inserted_ids:
        print("ADDITION SUCCESS ")
    return result

def read_by_column(column,value):
    if value.isdigit():
        value = int(value)

    # Case-insensitive search for string fields
    if isinstance(value, str):
        query = {column: {"$regex": f"^{value}$", "$options": "i"}}
    else:
        query = {column: value}

    result = db.employees.find_one(query)
    if result:
        print(result)
    else:
        print("mo data found")
        
def read_by_proj_stat(stat):
    query={"projects.status":{"$regex": f"^{stat}$", "$options": "i"} }
    result=db.employees.find_one(query)
    if result:
        print(result)
    else:
        print("no result found")

def read_by_length():
    query = {"$expr": {"$gt": [{"$size": "$projects"}, 1]}}
    result=db.employees.find_one(query)
    if result:
        print(result)
    else:
        print("no result found")
def update_dept(obj_id, dept):
    result = db.employees.find_one_and_update(
        {"_id": ObjectId(obj_id)},   # Convert string to ObjectId
        {"$set": {"department": dept}},  
        return_document=True  # Return updated document (optional)
    )
    
    if result:
        print("Department Updated Successfully!")
        print(result)
    else:
        print("No document found with that ID.")
        
def increment_exp(obj_id):
    result=db.employees.find_one_and_update(
        {"_id":ObjectId(obj_id)},
        {"$inc":{"experiance_years":1}},
        return_document=True)
    if result:
        print("Department Updated Successfully!")
        print(result)
    else:
        print("No document found with that ID.")
    
def remove_address():
    result=db.employees.update_many({},
        {"$unset":{"address":""}})
    if result:
        print("Department Updated Successfully!")
        print(f"{result.modified_count} document(s) updated.")
    else:
        print("No document found with that ID.")