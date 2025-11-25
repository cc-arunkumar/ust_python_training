from fastapi import FastAPI,HTTPException,status, Depends
from models import Task,CreateTask,Token,LoginRequest,User,task_list
from datetime import datetime, timedelta, timezone
from typing import List
from auth import DEMO_PASSWORD,DEMO_USERNAME,create_access_token,ACCESS_TOKEN_EXPIRE_MINUTES,get_current_user,COUNT



app = FastAPI(title="UST Task Tracker")



@app.post("/login", response_model=Token)
def login(data: LoginRequest):
    """
    Login endpoint: validates credentials and returns JWT token.
    """
    if data.username != DEMO_USERNAME or data.password != DEMO_PASSWORD:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password")

    expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    token = create_access_token(subject=data.username, expires_delta=expires)

    return Token(access_token=token, token_type="bearer")


# @app.get("/me")
# def read_me(current_user: User = Depends(get_current_user)):
#     """
#     Protected endpoint: requires valid JWT token.
#     """
#     return {
#         "message": "This is a protected endpoint",
#         "user": current_user
#     }


@app.get("/task",response_model=List[Task])
def get_all_task(current_user: User = Depends(get_current_user)):
    return task_list

@app.get("/task/{id}",response_model=Task)
def get_task_by_id(id:int,current_user: User = Depends(get_current_user)):
    for data in task_list:
        if(data.id==id):
            return data
    raise HTTPException(status_code=404,detail="Task Not Found")

@app.post("/task",response_model=Task)
def create_task(task:CreateTask,current_user: User = Depends(get_current_user)):
    global COUNT
    new_task = Task(
        id=COUNT,
        title=task.title,
        description=task.description,
        completed=task.completed
    )
    COUNT+=1
    task_list.append(new_task)
    return new_task

@app.put("/task/{id}",response_model=Task)
def update_task(id:int,task:CreateTask,current_user: User = Depends(get_current_user)):
    for idx,data in enumerate(task_list):
        if(data.id==id):
            updated = Task(
                id=id,
                title=task.title,
                description=task.description,
                completed=task.completed
            )
            task_list[idx]=updated
            return updated
    raise HTTPException(status_code=404,detail="Task Not Found")

@app.delete("/task/{id}")
def delete_task(id:int,current_user: User = Depends(get_current_user)):
    for idx,data in enumerate(task_list):
        if(data.id == id):
            task_list.pop(idx)
            return {"message":"Task Deleted Successfully"}
        
    raise HTTPException(status_code=404,detail="Not Found")

