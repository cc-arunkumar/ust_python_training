from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from jose import jwt, JWTError
from datetime import datetime, timedelta

app = FastAPI()

# Dummy database
users_db = {
    "admin": {
        "username": "admin",
        "password": "admin123",
    }
}

# OAuth / JWT Settings``
SECRET_KEY = "MY_SUPER_SECRET_KEY"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/token")


def authenticate_user(username: str, password: str):
    user = users_db.get(username)
    if not user or user["password"] != password:
        return None
    return user


def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    expire = datetime.now() + expires_delta
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    # Validate client_id & client_secret
    if form_data.client_id != "myclient" or form_data.client_secret != "mysecret":
        raise HTTPException(
            status_code=401, detail="Invalid client_id or client_secret"
        )

    # Validate username and password
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    # Create token
    access_token = create_access_token(
        {"sub": user["username"]},
        expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES),
    )

    return {"access_token": access_token, "token_type": "bearer"}


@app.get("/secure-data")
async def secure_data(token: str = Depends(oauth2_scheme)):
    # Verify JWT token
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    except JWTError:
        raise HTTPException(status_code=403, detail="Invalid token")

    return {"message": "Welcome! Your token is valid."}
