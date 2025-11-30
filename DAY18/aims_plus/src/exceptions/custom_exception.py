class RecordNotFoundException(Exception):
    pass

class DuplicateRecordException(Exception):
    pass

class ValidationErrorException(Exception):
    pass

class DatabaseConnectionException(Exception):
    pass
