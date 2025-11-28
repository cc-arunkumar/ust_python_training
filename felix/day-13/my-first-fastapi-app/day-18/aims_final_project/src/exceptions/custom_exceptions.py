# Custom exception classes for application-specific error handling

class InvalidInputException(Exception):
    """
    Raised when the input provided to a function or API
    does not meet the required format or validation rules.
    """
    pass


class DuplicateRecordException(Exception):
    """
    Raised when attempting to insert a record that already exists
    in the database or violates unique constraints.
    """
    pass


class RecordNotFoundException(Exception):
    """
    Raised when a requested record cannot be found in the database.
    Useful for handling 404-like scenarios in APIs.
    """
    pass


class ValidationErrorException(Exception):
    """
    Raised when data validation fails, such as incorrect field values
    or missing required attributes.
    """
    pass


class DatabaseConnectionException(Exception):
    """
    Raised when a database connection cannot be established
    or is unexpectedly lost during an operation.
    """
    pass