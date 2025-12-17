from fastapi import FastAPI
from app.core.database import Base, engine
from app.api import auth, employee, task,user
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)
app = FastAPI(title="Task Management System")

# 🔥 CORS FIX (VERY IMPORTANT)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # React dev server
    allow_credentials=True,
    allow_methods=["*"],   # allows OPTIONS, POST, GET, etc.
    allow_headers=["*"],
)


app.include_router(auth.router, tags=["Auth"])
app.include_router(employee.router, tags=["Employees"])
app.include_router(task.router, tags=["Tasks"])
app.include_router(user.router, tags=["Users"])