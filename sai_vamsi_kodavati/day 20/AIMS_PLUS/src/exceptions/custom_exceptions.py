"""
Custom exception classes for AIMS Plus application.
Each exception returns a standard JSON response format.
"""
 
 
class APIException(Exception):
    """Base exception class for all API exceptions."""
   
    pass
 
 
class InvalidInputException(APIException):
    """Raised when input validation fails."""
   
    pass
 
 
class DuplicateRecordException(APIException):
    """Raised when attempting to create a duplicate record."""
   
    pass
 
 
class RecordNotFoundException(APIException):
    """Raised when a requested record is not found."""
   
    pass
 
class ValidationErrorException(APIException):
    """Raised when data validation fails."""
   
    pass
 
class DatabaseConnectionException(APIException):
    """Raised when database connection fails."""
   
    def __init__(self, message: str):
        super().__init__(
            message=message,
            error_code="DatabaseConnectionException",
            status_code=500
        )
 