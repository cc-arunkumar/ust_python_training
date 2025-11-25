from fastapi import FastAPI, HTTPException,status, Depends
from typing import Optional
from pydantic import BaseModel, Field
from jose import JWTError, jwt
from datetime import datetime, timedelta, timezone
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials


app = FastAPI(title="UST Task Manager")

SECRET_KEY =  "UST-TaskTracker-Secret"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30 

class LoginRequest(BaseModel):
    username: str = Field(...,description="username is missing")
    password: str = Field(...,description="password is missing")

class Token(BaseModel):
    access_token: str
    token_type: str

class User(BaseModel):
    username: str

class  TaskModel(BaseModel):
    id:int 
    title:str 
    description:str
    completed:bool

class TaskModelCreate(BaseModel):
    title:str = Field(...,description="Field is required")
    description:str = Field(...,description="Field is required")
    
class  TaskModelUpdate(BaseModel):
    title:str = Field(...,description="Field is required")
    description:str = Field(...,description="Field is required")
    completed:bool = Field(...,description="Field is required")
    
tasks = []

task_id_counter = 1
users = {
 "felix": {
 "username": "felix",
 "password": "password123" 
 }
}


def create_access_token(subject: str, expires_delta: Optional[timedelta] = None) -> str:
   
    to_encode = {"sub": subject}
    
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
        
    to_encode.update({"exp": expire})

    encoded = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded

security = HTTPBearer()

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)) -> User:
    token = credentials.credentials
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token"
        )
    
    username = payload.get("sub")
    if username != users["felix"]["username"]:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found"
        )
    
    return User(username=username)

@app.post("/login", response_model=Token)
def login(data: LoginRequest):
    if data.username != users["felix"]["username"] or data.password != users["felix"]["password"]:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
        )
    
    # Create JWT token with expiration
    expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    token = create_access_token(subject=data.username, expires_delta=expires)
    
    return Token(access_token=token, token_type="bearer")

@app.post("/task")
def tasks_list(task:TaskModelCreate,current_user: User = Depends(get_current_user)):
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

@app.get("/tasks",)
def list_all_tasks(current_user: User = Depends(get_current_user)):
    return tasks

@app.get("/tasks/{task_id}")
def get_task_by_id(task_id:int,current_user: User = Depends(get_current_user)):
    for i in tasks:
        if i["id"] == task_id:
            return i
    raise HTTPException(status_code=404,detail="Task not found")

@app.put("/tasks/{task_id}")
def update_task(task_id:int,task:TaskModelUpdate,current_user: User = Depends(get_current_user)):
    for i in range(len(tasks)):
        if tasks[i]["id"] == task_id:
            task_item = TaskModel(
                id=task_id,
                title=task.title,
                description=task.description,
                completed=task.completed
            )
            tasks[i] = task_item.__dict__
            return task_item
    raise HTTPException(status_code=404,detail="Task not found")

@app.delete("/tasks/{task_id}")
def update_task(task_id:int,current_user: User = Depends(get_current_user)):
    for i in range(len(tasks)):
        if tasks[i]["id"] == task_id:
            tasks.pop(i)        
            return {"message": "Task deleted successfully"}
    raise HTTPException(status_code=404,detail="Task not found")

