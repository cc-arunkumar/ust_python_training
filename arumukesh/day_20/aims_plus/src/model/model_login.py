from pydantic import BaseModel, Field, field_validator
from datetime import date
from typing import Optional
from enum import Enum


#===model to validate logins======

class LoginRequest(BaseModel):
    """Model for login request body"""
    username: str
    password: str

class Token(BaseModel):
    """Response model for returned JWT token"""
    access_token: str
    token_type: str

class User(BaseModel):
    """Model representing a user"""
    username: str
