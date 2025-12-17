from pymongo import MongoClient

client=MongoClient("mongodb://localhost:27017/")
db=client["ust_emp_manag"]
# db.create_collection("task")
tasks=db.task
# db.create_collection("logs")
print("Connection successfully")
