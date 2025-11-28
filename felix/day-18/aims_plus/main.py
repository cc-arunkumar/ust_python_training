from fastapi import FastAPI,HTTPException
from src.api.asset_api import asset_router
 
 

app = FastAPI(title="UST AIMS+")

app.include_router(asset_router)
