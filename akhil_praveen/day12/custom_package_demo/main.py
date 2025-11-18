
from customer_package import (validation_customer_id,
                              validation_customer_age,
                              InvalidCustomerAgeException,
                              InvalidCustomerIDException)

try:
    print(validation_customer_id(-1))
except Exception as e:
    print(e)
    
try:
   print(validation_customer_id(101))
except Exception as e:
    print(e)
    
try:
    print(validation_customer_age(15))
except Exception as e:
    print(e)
    
try:
    print(validation_customer_age(34))
except Exception as e:
    print(e)