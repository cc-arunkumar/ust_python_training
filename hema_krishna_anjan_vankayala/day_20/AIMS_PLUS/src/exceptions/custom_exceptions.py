class APIException(Exception):
    pass


class InvalidInputException(APIException):
    pass


class DuplicateRecordException(APIException):
    pass

class RecordNotFoundException(APIException):
    pass


class ValidationErrorException(APIException):
    pass


class DatabaseConnectionException(APIException):
    
    pass