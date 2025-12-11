from pymongo import MongoClient
from day25.mysql_to_mongodb.sql_crud import update_category

client=MongoClient("mongodb://localhost:27017/")
db=client["ust_mongo_db"]
# db.create_collection("employees")

def insert_into_db():
    content=update_category()
    db.employees.insert_many(content)
    
def insert_one_db():
    nme=input("Enter the name")
    depart=input("Enter the department")
    cty=input("Enter the city")
    db.employees.insert_one({"name":nme,"department": depart,"city":cty})

def read_all_emp():
    content=db.employees.find({})
    for row in content:
        print(row)

def update_emp():
    city=input("Enter the city name")
    department=input("Enter the department")
    content=db.employees.update_one({"city":city},
                                    {"$set":{"department":department}})
    print(content)
    
def delete_one_emp():
    emp_id=int(input("Enter the employee id"))
    content=db.employees.delete_one({"emp_id":emp_id})
    print(content)
    
    

def delete_many_emp():
    department=input("Enter the department to be deleted")
    content=db.employees.delete_many({"department":department})
    print(content)
    
# insert_into_db()
# insert_one_db()
# read_all_emp()
# update_emp()
# delete_one_emp()
delete_many_emp()