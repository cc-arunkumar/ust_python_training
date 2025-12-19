from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pathlib import Path

from app.database import Base, engine
from app.routers import employees, tasks, users, attachments
from app.routers import auth

# Create tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="UST Employee Task API", version="1.0.0")

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Ensure uploads directory exists and mount it at /uploads so files can be served if needed.
uploads_dir = Path(__file__).resolve().parent.parent / "uploads"
uploads_dir.mkdir(parents=True, exist_ok=True)
app.mount("/uploads", StaticFiles(directory=str(uploads_dir)), name="uploads")



app.include_router(auth.router)
# app/main.py

# app.include_router(employees.router)
# app.include_router(tasks.router)


app.include_router(employees.router)
app.include_router(tasks.router)
app.include_router(users.router)
app.include_router(attachments.router)


@app.get("/")
def root():
    return {"message": "Backend is running"}
