# Function to generate a structured error message
def message(exception, msg):
    info = {
        "status": "Error",  # Status indicating an error
        "error_code": exception,  # Exception type or error code
        "message": msg  # Detailed error message
    }
    return info  # Return the structured error message


# Custom exception class for invalid input errors
class InvalidInputException(Exception):
    def __init__(self, msg):
        # Initialize the exception with a structured error message
        super().__init__(message("InvalidInputException", msg))


# Custom exception class for duplicate record errors
class DuplicateRecordException(Exception):
    def __init__(self, msg):
        # Initialize the exception with a structured error message
        super().__init__(message("DuplicateRecordException", msg))


# Custom exception class for record not found errors
class RecordNotFoundException(Exception):
    def __init__(self, msg):
        # Initialize the exception with a structured error message
        super().__init__(message("RecordNotFoundException", msg))


# Custom exception class for validation errors
class ValidationErrorException(Exception):
    def __init__(self, msg):
        # Initialize the exception with a structured error message
        super().__init__(message("ValidationErrorException", msg))


# Custom exception class for database connection errors
class DatabaseConnectionException(Exception):
    def __init__(self, msg):
        # Initialize the exception with a structured error message
        super().__init__(message("DatabaseConnectionException", msg))
