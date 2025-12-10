from fastapi import FastAPI,HTTPException,APIRouter
from api import router
# from api import 
app=FastAPI(title="Training Request Manager ")

app.include_router(router)
