from fastapi import FastAPI

# Import routers from different modules
# Each router contains endpoints for a specific feature
from src.api.asset_api import asset_router          # Asset management endpoints
from src.api.maintenance_api import maintenance_router  # Maintenance log endpoints
from src.api.vendor import vendor_router            # Vendor management endpoints
from src.api.employee_api import employee_router    # Employee directory endpoints
from src.api.login_api import login_router          # Login/authentication endpoints
from src.auth.jwt_auth import jwt_router            # JWT authentication endpoints

# -----------------------------
# Initialize FastAPI application
# -----------------------------
# Title will appear in Swagger UI (/docs) and OpenAPI schema
app = FastAPI(title="AIMS PLUS")

# -----------------------------
# Register routers with the app
# -----------------------------
# Each router groups related endpoints under a common prefix
app.include_router(login_router)        # /login → login endpoints
app.include_router(jwt_router)          # /auth → JWT verification endpoints
app.include_router(asset_router)        # /assets → asset inventory endpoints
app.include_router(maintenance_router)  # /maintenance → maintenance log endpoints
app.include_router(vendor_router)       # /vendors → vendor endpoints
app.include_router(employee_router)     # /employees → employee directory endpoints
