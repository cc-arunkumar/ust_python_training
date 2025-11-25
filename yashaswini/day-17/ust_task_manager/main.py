from fastapi import FastAPI, Depends, HTTPException
from models import LoginRequest, Task, TaskResponse
from auth import users, create_access_token, verify_token
from utils import tasks, get_next_id

app = FastAPI(title="UST Task Manager")

# LOGIN
@app.post("/login")
def login(request: LoginRequest):
    user = users.get(request.username)
    if not user or user["password"] != request.password:
        raise HTTPException(status_code=401, detail="Invalid username or password")
    token = create_access_token({"sub": request.username})
    return {"access_token": token, "token_type": "bearer"}

# CREATE TASK
@app.post("/tasks", response_model=TaskResponse)
def create_task(task: Task, username: str = Depends(verify_token)):
    new_task = TaskResponse(id=get_next_id(), **task.dict())
    tasks.append(new_task)
    return new_task

# GET ALL TASKS
@app.get("/tasks", response_model=list[TaskResponse])
def get_tasks(username: str = Depends(verify_token)):
    return tasks

# GET SINGLE TASK
@app.get("/tasks/{task_id}", response_model=TaskResponse)
def get_task(task_id: int, username: str = Depends(verify_token)):
    for task in tasks:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")

# UPDATE TASK
@app.put("/tasks/{task_id}", response_model=TaskResponse)
def update_task(task_id: int, updated_task: Task, username: str = Depends(verify_token)):
    for i, task in enumerate(tasks):
        if task.id == task_id:
            tasks[i] = TaskResponse(id=task_id, **updated_task.dict())
            return tasks[i]
    raise HTTPException(status_code=404, detail="Task not found")

# DELETE TASK
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, username: str = Depends(verify_token)):
    for i, task in enumerate(tasks):
        if task.id == task_id:
            tasks.pop(i)
            return {"message": "Task deleted successfully"}
    raise HTTPException(status_code=404, detail="Task not found")
