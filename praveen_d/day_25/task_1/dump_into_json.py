import json
from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["ust_db"]

def dump_data_to_json(emp_data):
    db.emp_mig.insert_many(emp_data)
    print("Data inserted sucessfully")
    
    