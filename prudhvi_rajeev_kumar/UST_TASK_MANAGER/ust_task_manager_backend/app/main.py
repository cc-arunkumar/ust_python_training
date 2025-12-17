import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware   # ✅ import CORS middleware
from app.core.config import settings
from app.core.logging import get_logger
from app.db.sql import Base, engine
from app.routers import users, employees, tasks, utils

logger = get_logger()

def create_app() -> FastAPI:
    app = FastAPI(title=settings.app_name, debug=settings.debug)
    # Ensure SQL tables exist (for production use Alembic)
    Base.metadata.create_all(bind=engine)

    # ✅ Add CORS middleware here
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost:5173"],  # frontend dev server
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # Routers
    app.include_router(users.router)
    app.include_router(employees.router)
    app.include_router(tasks.router)
    app.include_router(utils.router)

    @app.get("/health")
    def health():
        return {"status": "ok"}

    return app

app = create_app()

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)
