class AIMSException(Exception):
    """Base class for all custom exceptions in AIMS."""
    pass


class ValidationError(AIMSException):
    """Raised when data validation fails (e.g., invalid date, email)."""
    pass


class DatabaseError(AIMSException):
    """Raised when a database connection or operation fails."""
    pass


class CSVError(AIMSException):
    """Raised when there is an issue with CSV file handling."""
    pass