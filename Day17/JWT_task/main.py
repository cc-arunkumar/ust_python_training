from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel
from jose import jwt, JWTError
from datetime import datetime, timedelta


app = FastAPI(title="UST Task Manager API - Phase 1")


SECRET_KEY = "change-this-secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

security = HTTPBearer()


DEMO_USERNAME = "madhan"
DEMO_PASSWORD = "12345"

tasks = []     
task_id_counter = 1

class LoginRequest(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TaskCreate(BaseModel):
    title: str
    description: str
    status: str


class TaskUpdate(BaseModel):
    title: str
    description: str
    status: str

def create_access_token(data: dict):
    to_encode = data.copy()
    expire_time = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire_time})

    token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return token


def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    try:
        token = credentials.credentials
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")

        if username is None:
            raise HTTPException(status_code=401, detail="Invalid token")

        return username

    except JWTError:
        raise HTTPException(status_code=401, detail="Token expired or invalid")

@app.post("/login", response_model=Token)
def login(data: LoginRequest):
    if data.username != DEMO_USERNAME or data.password != DEMO_PASSWORD:
        raise HTTPException(status_code=401, detail="Invalid username or password")

    token = create_access_token({"sub": data.username})
    return {"access_token": token, "token_type": "bearer"}

@app.post("/tasks", status_code=201)
def create_task(task: TaskCreate, username: str = Depends(get_current_user)):
    global task_id_counter

    new_task = {
        "id": task_id_counter,
        "title": task.title,
        "description": task.description,
        "status": task.status,
        "created_by": username
    }

    tasks.append(new_task)
    task_id_counter += 1

    return new_task


@app.get("/tasks")
def get_all_tasks(username: str = Depends(get_current_user)):
    return tasks


@app.get("/tasks/{task_id}")
def get_task(task_id: int, username: str = Depends(get_current_user)):
    for t in tasks:
        if t["id"] == task_id:
            return t

    raise HTTPException(status_code=404, detail="Task not found")


@app.put("/tasks/{task_id}")
def update_task(task_id: int, data: TaskUpdate, username: str = Depends(get_current_user)):
    for t in tasks:
        if t["id"] == task_id:
            t["title"] = data.title
            t["description"] = data.description
            t["status"] = data.status
            return t

    raise HTTPException(status_code=404, detail="Task not found")


@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int, username: str = Depends(get_current_user)):
    for t in tasks:
        if t["id"] == task_id:
            tasks.remove(t)
            return

    raise HTTPException(status_code=404, detail="Task not found")

