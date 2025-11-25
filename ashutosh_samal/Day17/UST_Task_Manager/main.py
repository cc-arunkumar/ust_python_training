from datetime import datetime, timedelta, timezone
from typing import Optional,List
from fastapi import FastAPI, HTTPException, status, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import JWTError, jwt
from auth import verify_token,create_access_token
import utils
from model import tasks,task_id,Task,Token,LoginRequest,User

app = FastAPI(title="UST Task Manager")

@app.post("/login", response_model=Token)
def login(data: LoginRequest):
    if data.username != utils.USERNAME or data.password != utils.PASSWORD:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )

    expires = timedelta(minutes=utils.ACCESS_TOKEN_EXPIRE_MINUTES)
    token = create_access_token(subject=data.username, expires_delta=expires)

    return Token(access_token=token, token_type="bearer")

@app.post("/tasks")
def addtask(tsk:Task,current_user: User = Depends(verify_token)):
    global task_id
    tsk.id = task_id  
    task_id += 1 
    tasks.append(tsk.model_dump())
    return tsk

@app.get("/task",response_model=List[Task])
def gettask(current_user: User = Depends(verify_token)):
    return tasks

@app.get("/task/{id}")
def gettask(id:int,current_user: User = Depends(verify_token)):
    for tsk in tasks:
        if tsk['id'] == id:
            return tsk
    raise HTTPException(status_code=404,detail="Task not found")

@app.put("/tasks/{id}",response_model=Task)
#verifies the token
def update_task(id:int,task:Task,current_user:User=Depends(verify_token)):
    for t in tasks:
        if t["id"] == id:
            t["title"] = task.title
            t["description"] = task.description
            t["completed"] = task.completed
            return t
    raise HTTPException(status_code=404, detail="Task not found")

@app.delete("/task/{id}")
def delete(id: int,current_user: User = Depends(verify_token)):
    for t in tasks:
        if t['id'] == id:
            tasks.remove(t) 
            return {"detail": "Task deleted successfully"}  
    
    raise HTTPException(status_code=404, detail="Task not found")
