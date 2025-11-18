from .exceptions import InvalidCustomerIDException, InvalidCustomerAgeException

def validate_customer_id(cid):
    if cid<=0:
        raise InvalidCustomerIDException(cid)
    return True

def validate_customer_age(age):
    if age<18 or age>60:
        raise InvalidCustomerAgeException(age)
    return True