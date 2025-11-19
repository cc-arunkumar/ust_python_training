class InvalidCustomerIDException(Exception):
    def __init__(self,c_id):
        super().__init__(f"Invalid Customer Id: {c_id}")
        
class InvalidCustomerAgeException(Exception):
    def __init__(self,age):
        super().__init__(f"Invalid Customer age: {age}")
        
