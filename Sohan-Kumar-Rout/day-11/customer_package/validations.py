from .exceptions import InvalidCustomerID, InvalidCustomerAge

def validate_customer_id(cid):
    if cid <= 0:
        raise InvalidCustomerID(cid)
    return True

def validate_customer_age(age):
    if age < 18 or age > 60:
        raise InvalidCustomerAge(age)
    return True