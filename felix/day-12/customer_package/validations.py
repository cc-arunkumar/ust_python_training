from .exceptions import InvalidCustomerIDException, InvalidCustomerAgeException

def validate_customer_id(cid: int) -> bool:
    """
    Validates a customer ID.

    Args:
        cid (int): Customer ID to validate.

    Raises:
        InvalidCustomerIDException: If the customer ID is less than or equal to zero.

    Returns:
        bool: True if the customer ID is valid.
    """
    if cid <= 0:
        raise InvalidCustomerIDException(cid)
    return True


def validate_customer_age(age: int) -> bool:
    """
    Validates a customer's age.

    Args:
        age (int): Age of the customer.

    Raises:
        InvalidCustomerAgeException: If age is below 18 or above 60.

    Returns:
        bool: True if the age is valid.
    """
    if age < 18 or age > 60:
        raise InvalidCustomerAgeException(age)
    return True
