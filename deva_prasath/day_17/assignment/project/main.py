from fastapi import FastAPI, HTTPException, status, Depends
from typing import List
from datetime import timedelta
from models import TaskModel, LoginRequest, Token, User
from utils import tasks, users, ACCESS_TOKEN_EXPIRE_MINUTES
from auth import create_access_token, verify_token

#defining title
app=FastAPI(title="Task Tracker API")
next_id=1


#login api that returns authentication token

@app.post("/login",response_model=Token)
def login(data:LoginRequest):
    #checking with the username from inside the defined part
    if data.username not in users or users[data.username]["password"]!=data.password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password"
        )
    
    expires=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    #creating token
    token=create_access_token(subject=data.username, expires_delta=expires)
    
    return Token(access_token=token, token_type="bearer")


# post api that creates task_data
@app.post("/tasks",response_model=TaskModel)
#verifies the token
def create_task(task:TaskModel,current_user:User=Depends(verify_token)):
    #autoincrement id
    global next_id
    task_data={
        "id":next_id,
        "title":task.title,
        "description":task.description,
        "completed":task.completed
    }
    tasks.append(task_data)
    next_id+=1
    return task_data 

#get all api that retruns all tasks
@app.get("/tasks",response_model=List[TaskModel])
#verifies the token
def get_all_tasks(current_user:User=Depends(verify_token)):
    return tasks

#getting tasks by id 
@app.get("/tasks/{id}",response_model=TaskModel)
#verifies the token
def get_task_by_id(id:int,current_user:User=Depends(verify_token)):
    task=None
    for t in tasks:
        if t["id"]==id:
            task=t
            break  # Exit loop once the task is found
    if not task:
        raise HTTPException(status_code=404,detail="Task not found")
    return task


#update api with id
@app.put("/tasks/{id}",response_model=TaskModel)
#verifies the token
def update_task(id:int,task:TaskModel,current_user:User=Depends(verify_token)):
    for t in tasks:
        if t["id"]==id:
            t["title"]=task.title
            t["description"]=task.description
            t["completed"]=task.completed
            return t
    raise HTTPException(status_code=404,detail="Task not found")


#api for delete a task by id
@app.delete("/tasks/{id}")
#verifies the token
def delete_task(id:int,current_user:User=Depends(verify_token)):
    global tasks
    task=None
    # Loop through the tasks to find the task with the given id
    for t in tasks:
        if t["id"]==id:
            task=t
            break
    
    # If task is not found, raise HTTPException
    if task is None:
        raise HTTPException(status_code=404,detail="Task not found")
    
    # Remove the task from the list
    tasks=[task for task in tasks if task["id"]!=id]
    
    return {"message":"Task deleted successfully"}
