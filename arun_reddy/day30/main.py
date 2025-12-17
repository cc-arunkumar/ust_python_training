from fastapi import FastAPI
from api.emp_api import emp_router
from api.user_api import user_router
from api.task_api import task_router
from api.login_api import auth_router
from utils.assign_task import assigntask_router
from fastapi.middleware.cors import CORSMiddleware



app=FastAPI()



app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
 
 
app.include_router(auth_router)
app.include_router(emp_router)
app.include_router(user_router)
app.include_router(task_router)
app.include_router(assigntask_router)
