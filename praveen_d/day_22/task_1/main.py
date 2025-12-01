from fastapi import FastAPI
# from database_connection import get_connection
from crud import get_all_data,get_by_id,create_request,update_request,delete_request,patch_request
from training_request import Training_Request
app=FastAPI()

@app.get("/")
def get_all_data_api():
    result=get_all_data()
    return result

@app.get("/{id}")
def get_by_id_api(id:int):
    result=get_by_id(id)
    return result

@app.post("/")
def create_request_api(emp_request:Training_Request):
    print("Request started")
    result=create_request(emp_request)
    print("Request recivied")
    return result

@app.put("/{id}")
def update_request_api(id:int,emp_request:Training_Request):
    result=update_request(id,emp_request)
    return result

@app.delete("/{id}")
def delete_request_api(id:int):
    result=delete_request(id)
    return result

@app.patch("/{id}")
def patch_request_api(id:int,emp_patch:Training_Request):
    result=patch_request()
    return result