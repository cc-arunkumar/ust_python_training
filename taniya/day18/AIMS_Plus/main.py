from fastapi import FastAPI,HTTPException
from src.models.asset_model import Asset
from src.api.asset_api import asset_router
import csv
app=FastAPI(title="UST-AIMS+")
app.include_router(asset_router)