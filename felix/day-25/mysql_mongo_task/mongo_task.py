from pymongo import MongoClient
from mysql_task import read_from_mysql
import json

client = MongoClient("mongodb://localhost:27017/")

db = client["ust_mongo_db"]
# db.create_collection("employees")
# print("collection created")

employees = db.employees

data = read_from_mysql()
employees.insert_many(data)

def insert_one_employee():
    with open("employee.json","r") as file:
        emp = json.load()
    employees.insert_one(emp)
    
def read_all_employee():
    emp = employees.find()
    print(emp)
    
def update_one_employee():
    print("For updating city:")
    emp_id = int(input("Enter ID: "))
    city = input("Enter new city")
    employees.update_one({"emp_id",emp_id},{"city":city})
    
def delete_one_employee():
    print("For deleting:")
    emp_id = int(input("Enter ID: "))
    employees.delete_one({"emp_id",emp_id})
    
def delete_many():
    employees.delete_many({},{"age":{"$lt":20}})
