from fastapi import FastAPI, HTTPException, status, Depends
from datetime import timedelta
from auth import LoginRequest,create_access_token,ACCESS_TOKEN_EXPIRE_MINUTES,users,Token,User,get_current_user
from models import TaskModelCreate,TaskModelUpdate,TaskModel,get_current_user

app = FastAPI(title="UST Task Manager")




# -----------------------------
# IN-MEMORY STORAGE
# -----------------------------
tasks = []  # Stores all tasks
task_id_counter = 1  # Auto-incrementing task ID


# -----------------------------
# AUTH ROUTES
# -----------------------------
@app.post("/login", response_model=Token)
def login(data: LoginRequest):
    """
    Authenticates user and returns JWT token.
    """
    if data.username != users["felix"]["username"] or data.password != users["felix"]["password"]:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password"
        )

    # Generate access token
    expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    token = create_access_token(subject=data.username, expires_delta=expires)

    return Token(access_token=token, token_type="bearer")


# -----------------------------
# TASK MANAGEMENT ROUTES
# -----------------------------
@app.post("/task")
def create_task(task: TaskModelCreate, current_user: User = Depends(get_current_user)):
    """
    Creates a new task and stores it in memory.
    """
    global task_id_counter

    task_item = TaskModel(
        id=task_id_counter,
        title=task.title,
        description=task.description,
        completed=False
    )

    task_id_counter += 1
    tasks.append(task_item.__dict__)

    return task_item


@app.get("/tasks")
def list_all_tasks(current_user: User = Depends(get_current_user)):
    """
    Returns a list of all tasks.
    """
    return tasks


@app.get("/tasks/{task_id}")
def get_task_by_id(task_id: int, current_user: User = Depends(get_current_user)):
    """
    Fetch a single task by its ID.
    """
    for task in tasks:
        if task["id"] == task_id:
            return task

    raise HTTPException(status_code=404, detail="Task not found")


@app.put("/tasks/{task_id}")
def update_task(task_id: int, task: TaskModelUpdate, current_user: User = Depends(get_current_user)):
    """
    Updates an existing task by its ID.
    """
    for index in range(len(tasks)):
        if tasks[index]["id"] == task_id:
            task_item = TaskModel(
                id=task_id,
                title=task.title,
                description=task.description,
                completed=task.completed
            )
            tasks[index] = task_item.__dict__
            return task_item

    raise HTTPException(status_code=404, detail="Task not found")


@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, current_user: User = Depends(get_current_user)):
    """
    Deletes a task by its ID.
    """
    for index in range(len(tasks)):
        if tasks[index]["id"] == task_id:
            tasks.pop(index)
            return {"message": "Task deleted successfully"}

    raise HTTPException(status_code=404, detail="Task not found")
