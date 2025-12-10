from fastapi import FastAPI, HTTPException, Depends
from datetime import timedelta
from models import Task, LoginRequest, Token, User, Tasks, ID_COUNT
from auth import create_access_web_token, get_current_user, users, ACCESS_TOKEN_EXPIRE_MINUTES
from utils import find_task_by_id
from motor.motor_asyncio import AsyncIOMotorClient
from database import get_connection,mongo_connection

def get_mongo_connection():
    client =  mongo_connection()
    db = client["ust_mongo_db"]
    return db["task"]




app = FastAPI(title="Task Manager")

@app.get("/")
def check():
    return "Hello from the server side"

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
async def post_tasks(task: Task):
    try:
        collection = get_mongo_connection()
        await collection.insert_one(task.dict())   

        return task  
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/tasks", response_model=list[Task])
async def get_tasks(current_user = Depends(get_current_user)):
    collection = get_mongo_connection()

    # find() just builds the query cursor, no await needed
    cursor = collection.find()

#     Think of find() like ordering food at a restaurant:

# find() = you get a menu (cursor) with instructions on how to fetch dishes. No food yet, so no waiting.

# to_list() or iterating = you actually place the order and wait for the kitchen (MongoDB) to serve. That’s when you await.
    # to_list() actually fetches results from MongoDB, so we await it
    tasks = await cursor.to_list(length=None)

    # return [Task(**doc) for doc in tasks]
    return tasks


@app.get("/tasks/{id}", response_model=Task)
async def get_task_by_id(id: int):
    collection = get_mongo_connection()
    task = await collection.find_one({"id": id})   # query by your own field
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@app.put("/tasks/{id}")
async def update_task(id: int, task: Task):
    collection = get_mongo_connection()

    # Update only title and description
    result = await collection.update_one(
        {"id": id}, 
        {"$set": {"title": task.title, "description": task.description, "completed":task.completed}}
    )

    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Task not found")

    updated_task = await collection.find_one({"id": id})
    return Task(**updated_task)

@app.delete("/tasks/{id}")
async def delete_task(id: int):
    collection = get_mongo_connection()
    await collection.delete_one({"id":id})
    print("delete successfully")
