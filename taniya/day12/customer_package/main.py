# Import validation functions and custom exceptions from customer_package
from customer_package import(
    validate_customer_id,            # Function to validate customer ID
    validate_customer_age,           # Function to validate customer age
    InvalidCustomerAgeException,     # Exception raised for invalid age
    InvalidCustomerIDException       # Exception raised for invalid ID
)

# -------------------------------
# Validate customer ID
# -------------------------------
try:
    validate_customer_id(-5)         # Attempt to validate an invalid customer ID (-5)
except InvalidCustomerIDException as e:
    # Catch exception if ID is invalid and print error message
    print("Error: ", e)

# -------------------------------
# Validate customer age
# -------------------------------
try:
    validate_customer_age(75)        # Attempt to validate an invalid age (75)
except InvalidCustomerAgeException as e:
    # Catch exception if age is invalid and print error message
    print("Error: ", e)

# -------------------------------
# End of program
# -------------------------------
print("Done")                        # Print confirmation that program finished