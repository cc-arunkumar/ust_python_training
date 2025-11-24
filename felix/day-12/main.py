# Import validation functions and custom exceptions from the customer package
from customer_package import (
    validate_customer_id,
    validate_customer_age,
    InvalidCustomerIDException,
    InvalidCustomerAgeException
)

# Test validate_customer_id with an invalid ID
try:
    validate_customer_id(-5)  # Invalid ID (negative number)
except InvalidCustomerIDException as e:
    # Catch the custom exception and print the error message
    print("error: ", e)

# Test validate_customer_age with an invalid age
try:
    validate_customer_age(75)  # Invalid age (above allowed range)
except InvalidCustomerAgeException as e:
    # Catch the custom exception and print the error message
    print("error: ", e)

# Indicate that the script has finished running
print("Done!")
