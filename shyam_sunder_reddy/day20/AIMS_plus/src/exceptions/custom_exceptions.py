def message(exception,msg):
    info = {
         "status": "Error",
 "error_code": exception,
 "message": msg
    }
    return info
 
class InvalidInputException(Exception):
    def __init__(self, msg):
        super().__init__(message("InvalidInputException",msg))
class DuplicateRecordException(Exception):
    def __init__(self, msg):
        super().__init__(message("InvalidInputException",msg))
class RecordNotFoundExcpetion(Exception):
    def __init__(self, msg):
        super().__init__(message("InvalidInputException",msg))
class ValidationErrorException(Exception):
    def __init__(self, msg):
        super().__init__(message("InvalidInputException",msg))
class DatabaseConnectionException(Exception):
    def __init__(self, msg):
        super().__init__(message("InvalidInputException",msg))
 
 
 