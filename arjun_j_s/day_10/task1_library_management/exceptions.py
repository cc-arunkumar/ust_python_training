# exceptions.py
class LMSException(Exception):
    """Base class for LMS exceptions."""
    pass

class InvalidBookError(LMSException):
    pass

class InvalidUserError(LMSException):
    pass

class BookNotAvailableError(LMSException):
    pass

class UserNotAllowedError(LMSException):
    pass

class TransactionError(LMSException):
    pass

class ValidationError(LMSException):
    pass
