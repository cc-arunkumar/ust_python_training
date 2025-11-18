class InvalidCustomerIdException(Exception):
    def __init__(self, cid):
        super().__init__(f"Tnvaild Customer Id for {cid}")
        
class InvalidCustomerAgeException(Exception):
    def __init__(self, age):
        super().__init__(f"Invalid Customer age for {age}")
        
