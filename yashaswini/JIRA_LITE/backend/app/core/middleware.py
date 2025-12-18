from fastapi import Request, status
from fastapi.responses import JSONResponse
from datetime import datetime
import logging
import traceback
from app.db.mongodb import logs_collection
import uuid

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

async def log_to_mongodb(request: Request, log_data: dict):
    """Log to MongoDB logs collection"""
    try:
        log_entry = {
            "log_id": f"LOG-{uuid.uuid4().hex[:8].upper()}",
            "task_id": log_data.get("task_id", "N/A"),
            "user_id": log_data.get("user_id", 0),
            "action": log_data.get("action", "unknown"),
            "old_value": log_data.get("old_value"),
            "new_value": log_data.get("new_value"),
            "remarks": log_data.get("remarks"),
            "created_at": datetime.utcnow()
        }
        await logs_collection.insert_one(log_entry)
    except Exception as e:
        logger.error(f"Failed to log to MongoDB: {str(e)}")

async def error_handling_middleware(request: Request, call_next):
    """Centralized error handling middleware"""
    try:
        response = await call_next(request)
        return response
    except Exception as exc:
        logger.error(f"Unhandled exception: {str(exc)}")
        logger.error(traceback.format_exc())
        
        # Log error to MongoDB
        try:
            error_log = {
                "log_id": f"ERROR-{uuid.uuid4().hex[:8].upper()}",
                "task_id": "SYSTEM",
                "user_id": 0,
                "action": "system_error",
                "old_value": None,
                "new_value": str(exc),
                "remarks": f"Path: {request.url.path}, Method: {request.method}",
                "created_at": datetime.utcnow()
            }
            await logs_collection.insert_one(error_log)
        except:
            pass
        
        return JSONResponse(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            content={
                "detail": "Internal server error",
                "error": str(exc) if request.app.debug else "An unexpected error occurred"
            }
        )

async def request_logging_middleware(request: Request, call_next):
    """Log all incoming requests"""
    start_time = datetime.utcnow()
    
    # Log request
    logger.info(f"Request: {request.method} {request.url.path}")
    
    response = await call_next(request)
    
    # Calculate processing time
    process_time = (datetime.utcnow() - start_time).total_seconds()
    
    # Log response
    logger.info(
        f"Response: {request.method} {request.url.path} "
        f"Status: {response.status_code} Time: {process_time:.4f}s"
    )
    
    # Add custom header
    response.headers["X-Process-Time"] = str(process_time)
    
    return response