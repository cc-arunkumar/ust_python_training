# main.py
import os
from fastapi import FastAPI, Request, Depends
from fastapi.responses import RedirectResponse, HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from authlib.integrations.starlette_client import OAuth
from starlette.config import Config

from dotenv import load_dotenv
load_dotenv()

GITHUB_CLIENT_ID = os.getenv("GITHUB_CLIENT_ID")
GITHUB_CLIENT_SECRET = os.getenv("GITHUB_CLIENT_SECRET")
if not GITHUB_CLIENT_ID or not GITHUB_CLIENT_SECRET:
    raise RuntimeError("Set GITHUB_CLIENT_ID and GITHUB_CLIENT_SECRET as environment variables")

config = Config(environ={
    "GITHUB_CLIENT_ID": GITHUB_CLIENT_ID,
    "GITHUB_CLIENT_SECRET": GITHUB_CLIENT_SECRET,
})
oauth = OAuth(config)
oauth.register(
    name="github",
    client_id=GITHUB_CLIENT_ID,
    client_secret=GITHUB_CLIENT_SECRET,
    access_token_url="https://github.com/login/oauth/access_token",
    access_token_params=None,
    authorize_url="https://github.com/login/oauth/authorize",
    authorize_params=None,
    api_base_url="https://api.github.com/",
    client_kwargs={"scope": "read:user user:email"},
)

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    """
    Home page with a "Login with GitHub" link
    """
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/login")
async def login(request: Request):
    """
    Redirect user to GitHub's authorization URL
    """
    redirect_uri = request.url_for("auth_callback")
    return await oauth.github.authorize_redirect(request, redirect_uri)


@app.get("/auth/callback")
async def auth_callback(request: Request):

    token = await oauth.github.authorize_access_token(request)  
   
    resp = await oauth.github.get("user", token=token)
    profile = resp.json()
    email = None
    try:
        em_resp = await oauth.github.get("user/emails", token=token)
        emails = em_resp.json()
        for e in emails:
            if e.get("primary") and e.get("verified"):
                email = e.get("email")
                break
        if not email and emails:
            email = emails[0].get("email")
    except Exception:
        email = None

    return templates.TemplateResponse("profile.html", {
        "request": request,
        "profile": profile,
        "email": email,
        "token": token
    })


@app.get("/logout")
async def logout():
    return RedirectResponse("/")
