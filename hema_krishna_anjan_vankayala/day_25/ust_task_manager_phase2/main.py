from fastapi import FastAPI, HTTPException, status, Depends
from models import TaskSchema,Token, UserSchema, UserID
from mongodb_logger import logger
from typing import List
from auth import get_access_token, get_curr_user
from database import create_user,fetch_user_by_name, create_new_task,read_all_tasks,read_task_by_id,update_task,delete_task
from sqlalchemy.exc import IntegrityError

app = FastAPI(title="UST Task Manager")


#CREATE USERS
@app.post("/users", response_model=UserSchema, status_code=status.HTTP_201_CREATED)
def create_user_api(user: UserSchema):

    try:
        new_user = create_user(user.user_name, user.user_password)
        return new_user
    except Exception as e:
        # Handle duplicate username or DB errors
        if "Duplicate entry" in str(e):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Username already exists"
            )
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Error creating user: {e}"
        )
        
#LOGIN
@app.post('/login',response_model=Token)
def login(cred: UserSchema):
    user_id = fetch_user_by_name(cred.user_name,cred.user_password)
    if user_id is None:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Invalid Credentials")
    subject = str(user_id)
    token = get_access_token(subject)
    return Token(access_token=token, token_type = 'Bearer')
    
#CREATE
@app.post('/tasks')
def create_task(new_task : TaskSchema,  curr_user_id: UserID = Depends(get_curr_user)):
    try:
        task = create_new_task(new_task,curr_user_id.user_id)
        logger.info(f"Task created: {task.title} by user {curr_user_id.user_id}")
        return task
    except IntegrityError:
    # Rollback happens inside create_new_task or here
        logger.error(f"Error creating task: {e}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Task with this title already exists"
        )
    except Exception as e:
        logger.error(f"Error creating task: {e}")
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"{e}")

# READ all
@app.get('/tasks', response_model=List[TaskSchema])
def get_all_tasks(curr_user_id: UserID = Depends(get_curr_user)):
    tasks = read_all_tasks(curr_user_id.user_id)
    return tasks

# READ single
@app.get('/tasks/{task_id}', response_model=TaskSchema)
def get_task(task_id: int, curr_user_id: UserID = Depends(get_curr_user)):
    task = read_task_by_id(task_id, curr_user_id.user_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

# UPDATE
@app.put('/tasks/{task_id}', response_model=TaskSchema)
def update_task_api(task_id: int, updated_task: TaskSchema, curr_user_id: UserID = Depends(get_curr_user)):
    task = update_task(task_id, curr_user_id.user_id, updated_task)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

# DELETE
@app.delete('/tasks/{task_id}', status_code=status.HTTP_200_OK)
def delete_task_api(task_id: int, curr_user_id: UserID = Depends(get_curr_user)):
    result = delete_task(task_id, curr_user_id.user_id)
    if not result:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"detail": "Task deleted successfully"}
        

            
    
    
    