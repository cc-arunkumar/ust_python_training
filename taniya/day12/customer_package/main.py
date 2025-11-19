from customer_package import(
    validate_customer_id,
    validate_customer_age,
    InvalidCustomerAgeException,
    InvalidCustomerIDException
)

try:
    validate_customer_id(-5)
except InvalidCustomerIDException as e:
    print("Error: ",e)
try:
    validate_customer_age(75)
except InvalidCustomerAgeException as e:
    print("Error: ",e)
    
print("Done")