# validations.py

from .exceptions import InvalidCustomerID, InvalidCustomerAge

def validate_customer_id(cid):
    try:
        cid = int(cid)
    except ValueError:
        raise InvalidCustomerID(cid)

    if cid <= 0:
        raise InvalidCustomerID(cid)

    return True


def validate_customer_age(age):
    try:
        age = int(age)
    except ValueError:
        raise InvalidCustomerAge(age)

    if age < 18 or age > 60:
        raise InvalidCustomerAge(age)

    return True
