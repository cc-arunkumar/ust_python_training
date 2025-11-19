from .exceptions import InvalidCustomerIDException,InvalidCustomerAgeException

def validate_customer_id(c_id):
    if c_id<=0:
        raise InvalidCustomerIDException(c_id)
    return True

def validate_customer_age(age):
    if age<18 or age>60:
        raise InvalidCustomerAgeException(age)
    return True