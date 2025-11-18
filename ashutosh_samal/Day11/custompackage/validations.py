from exceptions import InvalidCustomerAgeException,InvalidCustomerIDException

def validate_customerID(cid):
    if cid<=0:
        raise InvalidCustomerIDException(cid)
    return True

def validate_customer_age(age):
    if age<18 or age>60:
        raise InvalidCustomerAgeException
    return True