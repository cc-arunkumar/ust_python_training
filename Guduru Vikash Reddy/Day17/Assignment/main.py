from fastapi import FastAPI, Depends, HTTPException
from models import LoginData, TaskNew, TaskEdit, Task
from auth import make_token, get_user
from utils import user_db, task_list, next_id, find_task

app = FastAPI(title="UST Task Manager")

@app.post("/login")
def login(data: LoginData):
    user = user_db.get(data.username)
    if not user or user["password"] != data.password:
        raise HTTPException(status_code=401, detail="Invalid username or password")
    token = make_token(data.username)
    return {"access_token": token, "token_type": "bearer"}

@app.post("/tasks", response_model=Task)
def create_task(task: TaskNew, current_user: str = Depends(get_user)):
    new_task = Task(id=next_id(), title=task.title, description=task.description, completed=False)
    task_list.append(new_task)
    return new_task

@app.get("/tasks", response_model=list[Task])
def get_tasks(current_user: str = Depends(get_user)):
    return task_list

@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int, current_user: str = Depends(get_user)):
    idx = find_task(task_id)
    if idx is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task_list[idx]

@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_id: int, data: TaskEdit, current_user: str = Depends(get_user)):
    idx = find_task(task_id)
    if idx is None:
        raise HTTPException(status_code=404, detail="Task not found")
    updated = Task(id=task_id, title=data.title, description=data.description, completed=data.completed)
    task_list[idx] = updated
    return updated

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, current_user: str = Depends(get_user)):
    idx = find_task(task_id)
    if idx is None:
        raise HTTPException(status_code=404, detail="Task not found")
    task_list.pop(idx)
    return {"message": "Task deleted successfully"}
