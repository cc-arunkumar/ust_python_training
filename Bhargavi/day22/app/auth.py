# UST Employee Training Request
# Management – CRUD API
# 1.PROJECT DESCRIPTION
# UST employees frequently submit training requests to enhance skills.
# This API enables Managing Training Requests through full CRUD operations.
# You must build a REST API using FastAPI + MySQL with JWT security.

# 2.ENTITY: TrainingRequest
# This is the single database table for CRUD operations.
# 3.FIELDS (NO ASSUMPTIONS)
# TrainingRequest Table Fields
# Field Name Type Required Example Description
# id INT PK AUTO_INCREMENT Yes 1 Unique request ID
# employee_id VARCHAR(20) Yes "UST12345" Must follow UST
# employee format
# employee_name VARCHAR(100) Yes "John Mathew" Employee full
# name
# training_title VARCHAR(200) Yes
# "Advanced
# Python"
# Requested training
# name
# training_description TEXT Yes
# "Need deep
# Python
# knowledge"
# Reason & details
# requested_date DATE Yes "2025-02-01" Request
# submission date
# status ENUM("PENDING","APPROVED","REJECTED") Yes "PENDING" Current request
# status
# manager_id VARCHAR(20) Yes "UST56789" Approver/manager
# ID
# last_updated DATETIME Auto-managed NULL Auto-updated
# timestamp

# 4.VALIDATION RULES
# 1. employee_id format: Must start with "UST" followed by digits ( ^UST\d+$ ).
# 2. employee_name:
# Cannot be empty
# UST Employee Training Request Management – CRUD API 1
# Cannot contain numbers
# 3. training_title: Minimum 5 characters.
# 4. training_description: Minimum 10 characters.
# 5. requested_date: Cannot be a future date.
# 6. status allowed values only:
# PENDING
# APPROVED
# REJECTED

# 7. manager_id must follow same format as employee_id.
# 5.DATABASE REQUIREMENTS (MySQL)
# Database Name: ust_training_db
# Table Name: training_requests
# SQL Schema (Must be implemented exactly)
# 6.API ENDPOINTS
# Base URL: /api/v1/training-requests
# Method Endpoint Purpose
# POST / Create new request
# GET / Get all requests (NO PAGINATION)
# GET /{id} Get request by ID
# PUT /{id} Update full record
# UST Employee Training Request Management – CRUD API 2
# Method Endpoint Purpose
# PATCH /{id} Partial update
# DELETE /{id} Delete record
# 7.SECURITY REQUIREMENTS – JWT AUTH (MANDATORY)

# JWT Authentication Rules
# 1. Every endpoint (except login) must require a valid JWT token.
# 2. JWT token must be sent using:
# Authorization: Bearer <token_here>
# 3. A separate login endpoint must be created:
# URL: /auth/login
# Accepts: username and password
# Returns: JWT token (access token)
# 4. Password check use these credentials: "admin" / "password123"
# 5. JWT must include:
# sub (username)
# exp (expiration timestamp)
# 6. JWT secret key must be stored in an environment variable:
# JWT_SECRET_KEY
# 7. Algorithm: HS256
# 8. Token expiration: 1 hour
# 8.IMPLEMENTATION RULES

# All Database Operations Must Use:
# mysql-connector-python OR
# PyMySQL
# API should include:
# Input validation using Pydantic
# JSON responses only
# Proper HTTP Status Codes:
# 201 Created
# 200 OK
# 400 Bad Request
# UST Employee Training Request Management – CRUD API 3
# 401 Unauthorized
# 404 Not Found
# 500 Server Error (only when unexpected)
# 9.DELIVERABLES REQUIRED
# You must produce:
# 1. Full and clear requirements (this document)
# 2. FastAPI code
# 3. JWT authentication code
# 4. Database connection code
# 5. CRUD routes implementation
# 6. Sample URL/Postman requests
# 7. SQL file

from fastapi import APIRouter, HTTPException  # Import FastAPI router and exception handling
from pydantic import BaseModel  # Import BaseModel for Pydantic model
from typing import Optional  # For optional typing
from datetime import datetime, timedelta  # For handling date and time
import jwt  # For creating and verifying JSON Web Tokens (JWT)


# Define constants for JWT authentication
SECRET_KEY = "mysecretkey"  # Secret key to encode the JWT
ALGORITHM = "HS256"  # The algorithm to be used for encoding/decoding the JWT
ACCESS_TOKEN_EXPIRE_MINUTES = 60  # The expiration time for the access token (in minutes)

from fastapi.security import OAuth2PasswordBearer  # Import OAuth2PasswordBearer for token-based authentication
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")  # OAuth2PasswordBearer used to retrieve token from request

# Pydantic model for the token response
class Token(BaseModel):
    access_token: str  # The access token
    token_type: str  # The type of token (usually 'bearer')

# Create an APIRouter instance to handle authentication-related routes
router = APIRouter()

# POST route for login
@router.post("/login", response_model=Token)
def login(username: str, password: str):
    # Check if the credentials are valid
    if username == "root" and password == "pass@word1":
        # If valid, create the access token
        token = create_access_token(data={"sub": username})
        # Return the token with the token type 'bearer'
        return {"access_token": token, "token_type": "bearer"}
    # If the credentials are invalid, raise an HTTP 401 Unauthorized error
    raise HTTPException(status_code=401, detail="Invalid credentials")

# Function to create the access token
def create_access_token(data: dict):
    # Set the expiration time of the token
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    
    # Copy the input data and add the expiration time
    to_encode = data.copy()
    to_encode.update({"exp": expire})
    
    # Encode the JWT using the secret key and algorithm specified
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    
    return encoded_jwt  # Return the encoded JWT
