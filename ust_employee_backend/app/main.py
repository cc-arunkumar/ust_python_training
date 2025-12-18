from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# Use package-relative imports so the module can be imported as `app.main`
from middleware.logging_middleware import LoggingMiddleware

from database.connection import engine, Base
from routers.employee_router import router as employee_router
from routers.task_router import router as task_router
from routers.users_router import router as users_router
from routers.auth_router import auth_router

from fastapi import WebSocket, WebSocketDisconnect
from utils.notifications import get_manager
# -------------------------------------------------
# Create DB tables
# -------------------------------------------------
Base.metadata.create_all(bind=engine)

# -------------------------------------------------
# FastAPI App
# -------------------------------------------------
app = FastAPI(
    title="UST Employee Task Management API",
    version="2.0",
    description="Phase 2 Backend – Employees, Users, Tasks"
)

# -------------------------------------------------
# Request logging middleware (best-effort)
# -------------------------------------------------
app.add_middleware(LoggingMiddleware)

# -------------------------------------------------
# CORS (Frontend ready)
# -------------------------------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------------------------------------
# Routers
# -------------------------------------------------

app.include_router(auth_router)
app.include_router(employee_router)
app.include_router(users_router)
app.include_router(task_router)


# WebSocket endpoint for notifications
manager = get_manager()

@app.websocket("/ws/notifications")
async def websocket_notifications(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            # Keep connection open; clients may optionally send pings
            await websocket.receive_text()
    except WebSocketDisconnect:
        manager.disconnect(websocket)


