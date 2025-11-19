from customer_package import(
    validate_customer_id,
    validate_customer_age,
    InvalidCustomerID,
    InvalidCustomerAge,
)

try:
    validate_customer_id(-5)
except InvalidCustomerID as e:
    print("Error:",e)
    
try:
    validate_customer_age(75)
except InvalidCustomerAge as e:
    print("Error:",e)

print("Done!")
