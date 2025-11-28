class InvalidInputException(Exception):
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)

class DuplicateRecordException(Exception):
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)

class RecordNotFoundException(Exception):
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)

class ValidationErrorException(Exception):
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)

class DatabaseConnectionException(Exception):
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)
