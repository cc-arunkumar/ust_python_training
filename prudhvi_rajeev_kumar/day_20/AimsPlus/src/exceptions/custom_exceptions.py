class InvalidInputException(Exception):
    """
    Raised when the input does not meet expected criteria.
    Used for catching invalid or malformed user inputs.
    """
    pass


class DuplicateRecordException(Exception):
    """
    Raised when a record already exists in the system (e.g., duplicate email or ID).
    Used to enforce uniqueness constraints.
    """
    pass


class RecordNotFoundException(Exception):
    """
    Raised when a requested record is not found in the database.
    Useful for handling cases where data is missing or deleted.
    """
    pass


class ValidationErrorException(Exception):
    """
    Raised when there is an issue with CSV file validation or format.
    Triggered by issues like incorrect data types or missing columns.
    """
    pass


class DatabaseConnectionException(Exception):
    """
    Raised when a connection to the database cannot be established.
    Can be used to handle connectivity issues or configuration errors.
    """
    pass
