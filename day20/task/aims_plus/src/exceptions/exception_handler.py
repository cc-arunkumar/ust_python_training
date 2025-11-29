from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from exceptions.custom_exception import (
    RecordNotFoundException,
    DuplicateRecordException,
    ValidationErrorException,
    DatabaseConnectionException,
)

def add_exception_handlers(app: FastAPI):

    @app.exception_handler(RecordNotFoundException)
    async def not_found(request: Request, exc: RecordNotFoundException):
        return JSONResponse(status_code=404, content={"status": "error", "message": str(exc)})

    @app.exception_handler(DuplicateRecordException)
    async def duplicate(request: Request, exc: DuplicateRecordException):
        return JSONResponse(status_code=409, content={"status": "error", "message": str(exc)})

    @app.exception_handler(ValidationErrorException)
    async def validation(request: Request, exc: ValidationErrorException):
        return JSONResponse(status_code=422, content={"status": "error", "message": str(exc)})

    @app.exception_handler(DatabaseConnectionException)
    async def db_error(request: Request, exc: DatabaseConnectionException):
        return JSONResponse(status_code=500, content={"status": "error", "message": str(exc)})
