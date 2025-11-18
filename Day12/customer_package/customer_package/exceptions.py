# exceptions.py
class InvalidCustomerIDException(Exception):
    def __init__(self, cid):
        super().__init__(f"Invalid Customer ID: {cid}")

class InvalidCustomerAgeException(Exception):
    def __init__(self, age):
        super().__init__(f"Invalid Customer Age: {age}")
