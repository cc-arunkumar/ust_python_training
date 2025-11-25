from pydantic import BaseModel


class AddTask(BaseModel):
    title: str
    description: str
    completed: bool = False


class GetTask(AddTask):
    id: int


class LoginRequest(BaseModel):
    username: str
    password: str


class TokenResponse(BaseModel):
    access_token: str
    token_type: str
