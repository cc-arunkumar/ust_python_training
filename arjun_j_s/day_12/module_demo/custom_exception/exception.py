
class InvalidAgeError(Exception):
    def __init__(self, age):
        super().__init__(f"Invalid Age: {age}")

class InvalidNameError(Exception):
    def __init__(self, name):
        super().__init__(f"Invalid Name : {name}")
