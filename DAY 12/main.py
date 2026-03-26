from custom_exceptions import (
    InvalidCustomerAgeException,
    InvalidCustomerIDException,
    validate_age,
    validate_cid
)

try:
    age=5
    validate_age(age)
except InvalidCustomerAgeException as e:
    print(f"Error occured : {e}\n")

try:
    cid=1
    validate_cid(cid)
except InvalidCustomerIDException as e:
    print(f"Error occured : {e}")

print("DOne!")
