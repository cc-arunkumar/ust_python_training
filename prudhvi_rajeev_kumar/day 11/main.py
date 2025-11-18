from customer_package import (
    validate_customer_id,
    validate_customer_age,
    InvalidCustomerAgeException,
    InvalidCustomerIdException
)

try:
    validate_customer_id(-5)
except InvalidCustomerIdException as e:
    print("Error : ", e)


try:
    validate_customer_age(75)
except InvalidCustomerAgeException as e:
    print("Error:", e)

print("Done!")

#Output:
# Error :  Tnvaild Customer Id for -5
# Error: Invalid Customer age for 75
# Done!
