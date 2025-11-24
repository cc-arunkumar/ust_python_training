from customer_package import (validation_customer_id,
                              validation_customer_age,
                              InvalidCustomerAgeException,
                              InvalidCustomerIDException)   # Import validation functions and custom exceptions

# Test invalid customer ID
try:
    print(validation_customer_id(-1))   # Should raise InvalidCustomerIDException
except Exception as e:
    print(e)   # Print exception message
    
# Test valid customer ID
try:
   print(validation_customer_id(101))   # Should return valid result
except Exception as e:
    print(e)   # Print exception message
    
# Test invalid customer age
try:
    print(validation_customer_age(15))   # Should raise InvalidCustomerAgeException
except Exception as e:
    print(e)   # Print exception message
    
# Test valid customer age
try:
    print(validation_customer_age(34))   # Should return valid result
except Exception as e:
    print(e)   # Print exception message

# ===========================
# Expected Output (example):
# ===========================
# InvalidCustomerIDException: Customer ID cannot be negative
# Valid Customer ID: 101
# InvalidCustomerAgeException: Age must be between 18 and 65
# Valid Customer Age: 34
