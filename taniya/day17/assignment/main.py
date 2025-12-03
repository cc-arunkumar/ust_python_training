from fastapi import FastAPI, HTTPException, Depends
from datetime import timedelta
from models import Task, LoginRequest, Token, User, Tasks, ID_COUNT
from auth import create_access_web_token, get_current_user, users, ACCESS_TOKEN_EXPIRE_MINUTES
from utils import find_task_by_id

app = FastAPI(title="Task Manager")

@app.get("/")
def check():
    return "Hello from the server side"
ID_COUNT=0
@app.post("/login", response_model=Token)
def login(data: LoginRequest):
    if data.username != users["rahul"]["username"] or data.password != users["rahul"]["password"]:
        raise HTTPException(
            status_code=401,
            detail="Incorrect username or password"
        )
    expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    token = create_access_web_token(subject=data.username, expires_delta=expires)
    return Token(access_token=token, token_type="bearer")

@app.post("/tasks", response_model=Task)
def post_tasks(task: Task, current_user: User = Depends(get_current_user)):
    task.id = ID_COUNT
    ID_COUNT += 1
    Tasks.append(task)
    return task

@app.get("/tasks")
def get_tasks(current_user: User = Depends(get_current_user)):
    return Tasks

@app.get("/tasks/{id}")
def get_task_by_id(id: int, current_user: User = Depends(get_current_user)):
    return find_task_by_id(Tasks, id)
@app.put("/tasks/{id}")
def update_task(id: int, task: Task, current_user: User = Depends(get_current_user)):
    for index, row in enumerate(Tasks):
        if row.id == id:
            row.title=task.title
            row.description = task.description
            row.completed = task.completed
            
            
            # Tasks[index] = updated_task
            return {"message": "Task updated successfully", "task": task}
    raise HTTPException(status_code=404, detail="Task not found")



@app.delete("/tasks/{id}")
def delete_task(id: int, current_user: User = Depends(get_current_user)):
    for index, row in enumerate(Tasks):
        if row.id == id:
            deleted_task = Tasks.pop(index)
            return {"message": "Task deleted successfully", "task": deleted_task}
    raise HTTPException(status_code=404, detail="Task not found")