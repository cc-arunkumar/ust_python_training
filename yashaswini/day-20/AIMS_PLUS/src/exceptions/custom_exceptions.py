def message(exception,msg):
    # Build a consistent error payload used by all custom exceptions.
    info = {
         "status": "Error",
         "error_code": exception,
         "message": msg
    }
    return info


class InvalidInputException(Exception):
    # Raised when input validation fails or required fields are missing/invalid.
    def __init__(self, msg):
        super().__init__(message("InvalidInputException",msg))

class DuplicateRecordException(Exception):
    # Raised when attempting to create a record that already exists (uniqueness violation).
    def __init__(self, msg):
        super().__init__(message("InvalidInputException",msg))

class RecordNotFoundExcpetion(Exception):
    # Raised when a requested record cannot be found in the database.
    def __init__(self, msg):
        super().__init__(message("InvalidInputException",msg))

class ValidationErrorException(Exception):
    # Raised for business rule or data validation errors beyond simple type checks.
    def __init__(self, msg):
        super().__init__(message("InvalidInputException",msg))

class DatabaseConnectionException(Exception):
    # Raised when the application cannot establish or use the database connection.
    def __init__(self, msg):
        super().__init__(message("InvalidInputException",msg))