from fastapi import FastAPI
from database import Base, engine
from routers import auth_router, task_router

app = FastAPI(title="Task Tracker")

# Create tables
Base.metadata.create_all(bind=engine)

# Include routers
app.include_router(auth_router.router)
app.include_router(task_router.router)
