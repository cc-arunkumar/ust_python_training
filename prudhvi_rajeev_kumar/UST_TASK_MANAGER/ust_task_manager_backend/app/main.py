import uvicorn
from fastapi import FastAPI
from app.core.config import settings
from app.core.logging import get_logger
from app.db.sql import Base, engine
from app.routers import users, employees, tasks, utils

logger = get_logger()

def create_app() -> FastAPI:
    app = FastAPI(title=settings.app_name, debug=settings.debug)
    # Ensure SQL tables exist (for production use Alembic)
    Base.metadata.create_all(bind=engine)

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
