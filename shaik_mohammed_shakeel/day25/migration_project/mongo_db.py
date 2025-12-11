import pymongo
from pymongo import MongoClient
import json
import pymysql
 
client = MongoClient('mongodb://localhost:27017/')
db = client['ust_mongo_db']
collection = db['employees']  
 
 
connection = pymysql.connect(
    host='localhost',          
    user='root',              
    password='1234',        
    database='ust_mysql_db'    
)
cursor = connection.cursor()
 
cursor.execute("SELECT * FROM employees")
rows = cursor.fetchall()
 
employees_from_db = []
for row in rows:
    employee_dict = {
        "emp_id": row[0],
        "name": row[1],
        "department": row[2],
        "age": row[3],
        "city": row[4]
    }
 
    if employee_dict["age"] < 25:
        employee_dict["category"] = "Fresher"
    else:
        employee_dict["category"] = "Experienced"
   
    employees_from_db.append(employee_dict)
 
collection.delete_many({})
 
 
collection.insert_many(employees_from_db)
 
print("Inserted modified data into MongoDB.")
 
new_employee = {
    "emp_id": 206,
    "name": "Anvesh",
    "department": "Cloud",
    "age": 24,
    "city": "Pune",
    "category": "Fresher"
}
collection.insert_one(new_employee)
print("Inserted one new employee.")
 
 
employees = collection.find()
print("\nAll employees in MongoDB:")
for emp in employees:
    print(emp)
 
update_result = collection.update_one(
    {"emp_id": 202},  
    {"$set": {"city": "Mumbai", "department": "Cloud Engineering"}}
)
print(f"Updated {update_result.modified_count} employee.")
 
delete_result = collection.delete_one({"emp_id": 203})  
print(f"Deleted {delete_result.deleted_count} employee.")
 
 
delete_many_result = collection.delete_many({"department": "Testing"})
print(f"Deleted {delete_many_result.deleted_count} employees from the 'Testing' department.")
 
 
cursor.close()
connection.close()
 