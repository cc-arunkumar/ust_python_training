class InvalidCustomerID(Exception):
    def __init__(self, cid):
        super().__init__(f"Invalid Customer id : {cid}")

class InvalidCustomerAge(Exception):
    def __init__(self, age):
        super().__init__(f"Invalid age : age cannot be negative or 0 : {age}")
        