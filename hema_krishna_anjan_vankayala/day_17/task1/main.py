from fastapi import FastAPI, HTTPException, status, Depends
from models import Task, LoginRequest ,Token, User
from typing import List
from auth import get_access_token, DEMO_PASSWORD,DEMO_USER_NAME, get_curr_user

app = FastAPI(title="UST Task Manager")
next_id = 0 
task_list : List[Task] = []

@app.post('/login',response_model=Token)
def login(cred: LoginRequest):
    if cred.username != DEMO_USER_NAME or cred.password != DEMO_PASSWORD:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Invalid Credentials")
    subject = cred.username 
    token = get_access_token(subject)
    return Token(access_token=token, token_type = 'Bearer')
    
    
@app.post('/tasks',response_model=Task)
def create_task(new_task : Task,  curr_user: User = Depends(get_curr_user)):
    
    for idx,stored_task in enumerate(task_list):
        if stored_task.title == new_task.title:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Task Already Exists")
    global next_id 
    next_id += 1 
    new_task.id = next_id
    task_list.append(new_task)
    return new_task


@app.get('/tasks',response_model=List[Task])
def get_all_tasks( curr_user: User = Depends(get_curr_user)):
    return task_list

@app.get('/tasks/{task_id}',response_model=Task)
def get_task_id(task_id : int, curr_user: User = Depends(get_curr_user)):
    for idx,stored_task in enumerate(task_list):
        if stored_task.id == task_id:
            return stored_task
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task Not Found")

@app.put('/tasks/{task_id}',response_model=Task)
def update_task(task_id : int,updated_task : Task,curr_user: User = Depends(get_curr_user)):
    for idx,stored_task in enumerate(task_list): 
        if stored_task.id == task_id:
            stored_task.title = updated_task.title
            stored_task.description = updated_task.description
            stored_task.completed = updated_task.completed 
            return updated_task
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task Not Found")

@app.delete('/tasks/{task_id}')
def delete_task(task_id : int,curr_user: User = Depends(get_curr_user)):
    for idx, stored_task in enumerate(task_list):
            if stored_task.id == task_id:
                task_list.pop(idx)
                return {"message": "Task deleted successfully"}
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task Not Found")

        

            
    
    
    