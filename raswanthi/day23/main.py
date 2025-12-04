# main.py
import os
from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from starlette.middleware.sessions import SessionMiddleware
from authlib.integrations.starlette_client import OAuth
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="OAwth Demo")
app.add_middleware(SessionMiddleware, secret_key="your-secret-key")

# Configure OAuth
oauth = OAuth()
oauth.register(
    name="google",
    client_id=os.getenv("GOOGLE_CLIENT_ID"),
    client_secret=os.getenv("GOOGLE_CLIENT_SECRET"),
    server_metadata_url="https://accounts.google.com/.well-known/openid-configuration",
    client_kwargs={"scope": "openid email profile"},
)

@app.get("/")
async def index(request: Request):
    user = request.session.get("user")
    if user:
        return {"message": f"Logged in as {user['name']} ({user['email']})"}
    return {"message": "Not logged in", "login_url": "/login"}

@app.get("/login")
async def login(request: Request):
    redirect_uri = request.url_for("auth_callback")
    return await oauth.google.authorize_redirect(request, redirect_uri)

@app.get("/auth/callback")
async def auth_callback(request: Request):
    token = await oauth.google.authorize_access_token(request)
    userinfo = token.get("userinfo")
    request.session["user"] = userinfo
    return RedirectResponse(url="/protected")

@app.get("/protected")
async def protected(request: Request):
    user = request.session.get("user")
    if not user:
        return RedirectResponse(url="/login")
    return {"message": f"Hello {user['name']}"}

@app.get("/logout")
async def logout(request: Request):
    request.session.pop("user", None)
    return RedirectResponse(url="/")
