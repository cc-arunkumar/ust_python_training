from customer_package import (
    validate_customer_id,
    validate_customer_age,
    InvalidCustomerIDException,
    InvalidCustomerAgeException
)

try:
    validate_customer_id(-5)
except InvalidCustomerIDException as e:
    print("error: ",e)
    
try:
    validate_customer_age(75)
except InvalidCustomerAgeException as e:
    print("error: ",e)
    
print("Done!")