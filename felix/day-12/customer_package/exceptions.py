class InvalidCustomerIDException(Exception):
    """
    Exception raised when a provided customer ID is invalid.

    Attributes:
        cid (Any): The invalid customer ID that triggered the exception.
    """
    def __init__(self, cid):
        # Call the base Exception class with a meaningful error message
        super().__init__(f"Invalid Customer ID: {cid}")
        


class InvalidCustomerAgeException(Exception):
    """
    Exception raised when a customer's age is invalid.

    Attributes:
        age (Any): The invalid age value that triggered the exception.
    """
    def __init__(self, age):
        # Call the base Exception class with a descriptive message
        super().__init__(f"Invalid Customer age: {age}")
