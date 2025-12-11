from pymongo import MongoClient
from datetime import datetime
from pydantic import BaseModel

client=MongoClient("mongodb://localhost:27017/")
db=client["ust_task_manager_db"]
# db.create_collection("logger")
print("Databse connected successfully")

class Logger(BaseModel):
    username:str
    action:str
    task_id:int 
    timestamp:datetime=datetime.now()

log=db.logger
    

    

