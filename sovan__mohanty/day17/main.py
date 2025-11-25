from fastapi import FastAPI, HTTPException, Depends
from models import Task, TaskCreate, TaskUpdate, LoginRequest, Token
from auth import users, create_access_token, get_user
from utils import tasks, task_counter, find_task

app = FastAPI(title="UST Task Manager")

@app.post("/login", response_model=Token)
def login(data: LoginRequest):
    user = users.get(data.username)
    if not user or user["password"] != data.password:
        raise HTTPException(status_code=401, detail="Invalid username or password")
    token = create_access_token(subject=data.username)
    return Token(access_token=token, token_type="bearer")

@app.post("/tasks", response_model=Task)
def create_task(task_data: TaskCreate, current_user: str = Depends(get_user)):
    global task_counter
    task_counter += 1
    task = Task(id=task_counter, title=task_data.title,
                description=task_data.description, completed=False)
    tasks.append(task)
    return task

@app.get("/tasks", response_model=list[Task])
def get_tasks(current_user: str = Depends(get_user)):
    return tasks

@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int, current_user: str = Depends(get_user)):
    task = find_task(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, task_data: TaskUpdate, current_user: str = Depends(get_user)):
    task = find_task(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    task.title = task_data.title
    task.description = task_data.description
    task.completed = task_data.completed
    return task

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, current_user: str = Depends(get_user)):
    task = find_task(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    tasks.remove(task)
    return {"message": "Task deleted successfully"}
