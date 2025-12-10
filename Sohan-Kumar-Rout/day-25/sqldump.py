import pymysql
import json
from db_connection import get_connection
from pymongo import MongoClient


data=r"C:\Users\Administrator\Desktop\PTraining\ust_python_training\sohan-kumar-rout\day-25\employeess.json"
 
with open(data) as file:
    employeess=json.load(file)
    
conn=get_connection()
cursor=conn.cursor()

for emp in employeess:
    try:
        cursor.execute(
    """
    INSERT INTO employeess (emp_id,name,department,age,city) VALUES(%s,%s,%s,%s,%s)
    """, (emp["emp_id"], emp["name"], emp["department"], emp["age"],emp["city"])
        )
    except pymysql.err.IntegrityError:
        print("Duplicate emp_id skipped")
        
conn.commit()
print("Dumpped Successfully")
#--reading the files from the dictionary 
# for row in employeess:
#     print(row)

cursor.execute("SELECT * FROM employeess")
rows=cursor.fetchall()
columns = [desc[0] for desc in cursor.description]
# print(rows)
employee_dicts = [dict(zip(columns, row)) for row in rows]
print(" Employees from MySQL:", employee_dicts)

#--add category field----
for emp in employee_dicts:
    if emp["age"] < 25:
        emp["category"] ="Fresher"
    
    else:
        emp["category"] ="Experienced"

print("Transformed the data with a category field",employee_dicts)

client = MongoClient("mongodb+srv://msovan928_db_user:sovan@clusterfastapi.yrq0el1.mongodb.net/")
# mongo_db = MongoClient["employeess"]
db = client["test_db"]
mongo_collection = db["employeess"] 

mongo_collection.delete_many({})
mongo_collection.insert_many(employee_dicts)

print("Data inserted to mongodb")

    