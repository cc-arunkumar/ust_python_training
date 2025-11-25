# Main.py
from auth import create_access_token,get_curr_user,DEMO_USERNAME,DEMO_PASSWORD
from fastapi import FastAPI,HTTPException,Depends,status
from models import Task,LoginRequest,Token,User,TaskModel
from datetime import timedelta
from typing import List

app=FastAPI(title="Task Tracker API")


ACCESS_TOKEN_EXPIRE_MINUTES = 30 

@app.post("/login", response_model=Token)
def login(data: LoginRequest):
    if data.username != DEMO_USERNAME or data.password != DEMO_PASSWORD:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password"
        )
    if data.username=="":
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="field required",
            type="value error missing"
        )
    expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    token = create_access_token(subject=data.username, expires_delta=expires)
    
    return Token(access_token=token, token_type="bearer")

@app.get("/me")
def read_me(current_user: User = Depends(get_curr_user)):
    return {
        "message": "This is a protected JWT token route.",
        "username": current_user.username,
    }

next_id = 1
task_details : List[Task] = []
 
 
@app.post('/tasks',response_model=Task)
def create_task(new_task : TaskModel,current_user: User = Depends(get_curr_user)):
   
    for idx,task_val in enumerate(task_details):
        if task_val.title == new_task.title:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Task Already Exists")
    global next_id
    next_id += 1
    task = Task(id=next_id, title=new_task.title, description=new_task.description, completed=False)
    task_details.append(task)
    return task
 
 
@app.get('/tasks',response_model=List[Task])
def get_all_tasks(current_user: User = Depends(get_curr_user)):
    return task_details
 
@app.get('/tasks/{task_id}',response_model=Task)
def get_task_id(task_id : int,current_user: User = Depends(get_curr_user)):
    for idx,task_val in enumerate(task_details):
        if task_val.id == task_id:
            return task_val
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task Not Found")
 
@app.put('/tasks/{task_id}',response_model=Task)
def update_task(task_id : int,updated_task : Task,current_user: User = Depends(get_curr_user)):
    for idx,task_val in enumerate(task_details):
        if task_val.id == task_id:
            task_val.title = updated_task.title
            task_val.description = updated_task.description
            task_val.completed = updated_task.completed
            return updated_task
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task Not Found")
 
@app.delete('/tasks/{task_id}')
def delete_task(task_id : int,current_user: User = Depends(get_curr_user)):
    for idx, task_val in enumerate(task_details):
            if task_val.id == task_id:
                task_details.pop(idx)
                return {"message": "Task deleted successfully"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task Not Found")
 
 
       
 
           
   
   
   
 