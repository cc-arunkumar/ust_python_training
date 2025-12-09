# exceptions.py

class InvalidCustomerID(Exception):
    def __init__(self, cid):
        super().__init__(f"Invalid Customer ID: {cid}")
        self.cid = cid


class InvalidCustomerAge(Exception):
    def __init__(self, age):
        super().__init__(f"Invalid Customer Age: {age}")
        self.age = age
