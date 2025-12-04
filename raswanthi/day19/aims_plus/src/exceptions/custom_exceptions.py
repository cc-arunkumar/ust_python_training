import json
 
class CustomException(Exception):
    """Base class for custom exceptions with JSON response."""
    error_code: str = "CustomException"
 
    def __init__(self, message: str):
        self.message = message
        super().__init__(message)
 
    def to_json(self):
        return {
            "status": "error",
            "error_code": self.error_code,
            "message": self.message
        }
 
    def __str__(self):
        return json.dumps(self.to_json())
 
 
class InvalidInputException(CustomException):
    error_code = "InvalidInputException"
 
 
class DuplicateRecordException(CustomException):
    error_code = "DuplicateRecordException"
 
 
class RecordNotFoundException(CustomException):
    error_code = "RecordNotFoundException"
 
 
class ValidationErrorException(CustomException):
    error_code = "ValidationErrorException"
 
 
class DatabaseConnectionException(CustomException):
    error_code = "DatabaseConnectionException"
 
 