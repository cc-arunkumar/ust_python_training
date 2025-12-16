from fastapi import FastAPI
from routes import user_routes, task_routes, utils_routes
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI(title="Jira-Inspired Task Manager", version="1.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# Include routers
app.include_router(user_routes.router, prefix="/api/users", tags=["Users"])
app.include_router(task_routes.router, prefix="/api/tasks", tags=["Tasks"])
app.include_router(utils_routes.router, prefix="/api/utils", tags=["Utils"])

