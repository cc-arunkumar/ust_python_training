from fastapi import FastAPI
from database import Base, engine
from routers import auth_router, task_router
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI(title="Task Tracker")

origins = [
    "http://localhost:5173",  # Vite default dev server URL
    "http://localhost:3000",  # If you're using React on a different port
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)
# Create tables
Base.metadata.create_all(bind=engine)

# Include routers
app.include_router(auth_router.router)
app.include_router(task_router.router)
