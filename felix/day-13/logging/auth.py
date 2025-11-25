from typing import Optional
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import FastAPI, HTTPException, status, Depends
from pydantic import BaseModel
from jose import JWTError, jwt

SECRET_KEY =  "UST-TaskTracker-Secret"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30 

