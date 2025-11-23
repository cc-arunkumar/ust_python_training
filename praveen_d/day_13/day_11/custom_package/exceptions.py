# creating our own exceptions

class InvalidCustomerIdException(Exception):
    def __init__(self, cid):
        super().__init__(cid)
        print(f"Invalid customer ID:{cid}")

class InvalidCustomerAgeException(Exception):
    def __init__(self, age):
        super().__init__(age)
        print("The customer age is below 18 which is not allowed:{age}")