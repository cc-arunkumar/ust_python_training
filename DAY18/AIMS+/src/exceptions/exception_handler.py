from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse
from .custom_exceptions import InvalidInputException, DuplicateRecordException, RecordNotFoundException, ValidationErrorException, DatabaseConnectionException

# General handler for custom exceptions
async def custom_exception_handler(request: Request, exc: Exception):
    if isinstance(exc, InvalidInputException):
        return JSONResponse(
            status_code=400,
            content={
                "status": "error",
                "error_code": "InvalidInputException",
                "message": exc.message
            }
        )
    elif isinstance(exc, DuplicateRecordException):
        return JSONResponse(
            status_code=400,
            content={
                "status": "error",
                "error_code": "DuplicateRecordException",
                "message": exc.message
            }
        )
    elif isinstance(exc, RecordNotFoundException):
        return JSONResponse(
            status_code=404,
            content={
                "status": "error",
                "error_code": "RecordNotFoundException",
                "message": exc.message
            }
        )
    elif isinstance(exc, ValidationErrorException):
        return JSONResponse(
            status_code=422,
            content={
                "status": "error",
                "error_code": "ValidationErrorException",
                "message": exc.message
            }
        )
    elif isinstance(exc, DatabaseConnectionException):
        return JSONResponse(
            status_code=500,
            content={
                "status": "error",
                "error_code": "DatabaseConnectionException",
                "message": exc.message
            }
        )
    else:
        # Handle unexpected exceptions
        return JSONResponse(
            status_code=500,
            content={
                "status": "error",
                "error_code": "InternalServerError",
                "message": "An unexpected error occurred."
            }
        )
