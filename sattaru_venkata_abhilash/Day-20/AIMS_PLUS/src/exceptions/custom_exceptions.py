def message(exception, msg):
    """
    This function creates a structured error message with the provided exception and message.
    
    :param exception: The exception type or name (e.g., 'InvalidInputException')
    :param msg: The error message or details associated with the exception
    :return: A dictionary containing the status, error code, and message
    """
    info = {
         "status": "Error",  # The status of the response (in this case, always "Error")
         "error_code": exception,  # The exception type or error code (e.g., InvalidInputException)
         "message": msg  # The error message explaining the issue
    }
    return info


# Custom exception class for handling invalid input
class InvalidInputException(Exception):
    """
    Raised when the input provided to the system is invalid.
    """
    def __init__(self, msg):
        # Call the parent Exception class constructor with a structured error message
        super().__init__(message("InvalidInputException", msg))


# Custom exception class for handling duplicate records
class DuplicateRecordException(Exception):
    """
    Raised when there is an attempt to insert a duplicate record.
    """
    def __init__(self, msg):
        # Call the parent Exception class constructor with a structured error message
        super().__init__(message("DuplicateRecordException", msg))


# Custom exception class for handling record not found errors
class RecordNotFoundExcpetion(Exception):
    """
    Raised when a requested record is not found in the system.
    """
    def __init__(self, msg):
        # Call the parent Exception class constructor with a structured error message
        super().__init__(message("RecordNotFoundException", msg))


# Custom exception class for handling validation errors
class ValidationErrorException(Exception):
    """
    Raised when there is an error during the validation process.
    """
    def __init__(self, msg):
        # Call the parent Exception class constructor with a structured error message
        super().__init__(message("ValidationErrorException", msg))


# Custom exception class for handling database connection errors
class DatabaseConnectionException(Exception):
    """
    Raised when there is a failure to connect to the database.
    """
    def __init__(self, msg):
        # Call the parent Exception class constructor with a structured error message
        super().__init__(message("DatabaseConnectionException", msg))
