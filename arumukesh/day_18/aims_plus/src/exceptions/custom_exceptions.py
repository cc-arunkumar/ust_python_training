"""
Custom Exception Module
-----------------------
This module defines reusable custom exception classes that provide consistent, 
structured error responses across the API. These exceptions help in making error 
messages standardized and meaningful for API consumers.

Each exception automatically structures the message as:

{
    "status": "Error",
    "error_code": "<ExceptionName>",
    "message": "<details>"
}

Author: (Your Name)
"""

# Utility function to structure error messages
def message(exception, msg):
    """
    Generate a formatted error response dictionary.

    Args:
        exception (str): The name/type of the exception.
        msg (str): Human-readable error message.

    Returns:
        dict: Structured error response.
    """
    return {
        "status": "Error",
        "error_code": exception,
        "message": msg
    }


# ------------------------ Custom Exception Classes ------------------------

class InvalidInputException(Exception):
    """Raised when the user submits data that does not meet validation rules."""
    def __init__(self, msg):
        super().__init__(message("InvalidInputException", msg))


class DuplicateRecordException(Exception):
    """Raised when attempting to insert a record that already exists."""
    def __init__(self, msg):
        super().__init__(message("DuplicateRecordException", msg))


class RecordNotFoundException(Exception):
    """Raised when a requested record cannot be found in the database."""
    def __init__(self, msg):
        super().__init__(message("RecordNotFoundException", msg))


class ValidationErrorException(Exception):
    """Raised when field-level validation fails (e.g., regex mismatch)."""
    def __init__(self, msg):
        super().__init__(message("ValidationErrorException", msg))


class DatabaseConnectionException(Exception):
    """Raised when the system cannot connect to or interact with the database."""
    def __init__(self, msg):
        super().__init__(message("DatabaseConnectionException", msg))
