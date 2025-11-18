# main.py

from customer_package import (
    validate_customer_id,
    validate_customer_age,
    InvalidCustomerIDException,
    InvalidCustomerAgeException
)

try:
    validate_customer_id(-5)
except InvalidCustomerIDException as e:
    print("Error:", e)

try:
    validate_customer_age(75)
except InvalidCustomerAgeException as e:
    print("Error:", e)

print("Done!")

#Sample Execution
# Error: Invalid Customer ID: -5
# Error: Invalid Customer Age: 75
# Done!