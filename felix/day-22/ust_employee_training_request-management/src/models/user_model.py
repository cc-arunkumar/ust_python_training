from pydantic import BaseModel

class User(BaseModel):
    """
    Pydantic model representing a user entity.
    - Contains only the username field.
    - Typically used for authenticated user context.
    """
    username: str


class UserModel(BaseModel):
    """
    Pydantic model for user login credentials.
    - Includes both username and password fields.
    - Used for authentication requests (e.g., login endpoint).
    """
    username: str
    password: str


class Token(BaseModel):
    """
    Pydantic model representing an authentication token response.
    - 'token': The JWT or access token string.
    - 'token_type': The type of token (commonly 'bearer').
    - Used as the response model for login/authentication endpoints.
    """
    token: str
    token_type: str