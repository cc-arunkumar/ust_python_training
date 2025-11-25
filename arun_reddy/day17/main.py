from datetime import datetime, timedelta, timezone
from typing import Optional
from fastapi import FastAPI, HTTPException, status, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel
from jose import JWTError, jwt
from auth import create_access_token,ACCESS_TOKEN_EXPIRE_MINUTES,DEMO_PASSWORD,DEMO_USERNAME,get_current_user
from models import LoginRequest,Token,User,Taskmodel,Tasks
from typing import List
app=FastAPI(title="UST TASK MANAGER")
next_task_id=1
@app.post("/login", response_model=Token)
def login(data: LoginRequest):
    if data.username != DEMO_USERNAME or data.password != DEMO_PASSWORD:
        # Invalid credentials
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password")
    expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    token = create_access_token(subject=data.username, expires_delta=expires)
    return Token(access_token=token, token_type="bearer")

tasks: List[Taskmodel]=[]
@app.post("/tasks",response_model=Taskmodel)

def create_task(task:Tasks,current_user: User = Depends(get_current_user)):
    print(task)
    global next_task_id
    task_obj=Taskmodel(id=next_task_id,title=task.title,description=task.description)
    next_task_id+=1
    tasks.append(task_obj)
    return task_obj
@app.get("/tasks")
def get_tasks(current_user: User = Depends(get_current_user)):
    return tasks
@app.get("/tasks/{task_id}")
def get_task(task_id:int,current_user: User = Depends(get_current_user)):
    for K in tasks:
        if K.id==task_id:
            return K
    return {"detail":"Task not found"}

@app.put("/tasks/{task_id}")

def update_task(task_id:int,task:Tasks,current_user: User = Depends(get_current_user)):
    for K in tasks:
        if K.id==task_id:
            K.title=task.title
            K.description=task.description
            K.completed=task.completed
            return K
    return {"detail":"Invalid Id"}


@app.delete("/tasks/{task_id}")

def delete_task(task_id:int,current_user: User = Depends(get_current_user)):
    for K in tasks:
        if K.id==task_id:
            tasks.remove(K)
            return {"detail":"task deleted successfully"}
    return {"detail":"task not found"}
        
    
