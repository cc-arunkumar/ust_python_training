from starlette.middleware.base import BaseHTTPMiddleware
from database.mongodb import log_collection
from datetime import datetime

class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        response = await call_next(request)

        log_collection.insert_one({
            "method": request.method,
            "path": request.url.path,
            "status_code": response.status_code,
            "timestamp": datetime.utcnow()
        })

        return response
