from .exceptions import InvalidCustomerAgeException,InvalidCustomerIDException

def validate_age(age):
    if age<18 or age>60:
        raise InvalidCustomerAgeException(age)
    return True

def validate_cid(cid):
    if cid<=0:
        raise InvalidCustomerIDException(cid)
    return True
